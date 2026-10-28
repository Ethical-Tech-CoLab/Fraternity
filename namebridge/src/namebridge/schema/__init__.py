"""Schemas and validators (week 3).

- name_graph: the public Name Knowledge Graph (CONCEPT-IDEA.md §5.1A)
- case_graph: the protected case graph, schema only (§5.1B)
- ingest: CPIMS+/Primero field allowlist (THREAT_MODEL.md T13)
- pack: language-pack template (§11)

Validators return a list of error strings; an empty list means valid.
"""

import re

# Attribute and field names NameBridge never holds: ethnicity, clan, tribe,
# religion and related (CONCEPT-IDEA.md §8 control 12; SCOPE.md §4; T8, T13),
# in the corridor's record languages too: French (Burundi's CENI lists head the
# column "Ethnie"), Kirundi/Kinyarwanda and Swahili (RESEARCH_LOG.md, 28 Oct).
# Long stems match anywhere in a field name; short words only as whole words,
# so "trace" and "ordinal" pass.
_STEMS = re.compile(r"ethni|tribe|tribal|tribu|clan|religio|caste", re.IGNORECASE)
_WORDS = {
    "race", "racial",
    "ubwoko", "ubwooko", "amoko",  # Kirundi/Kinyarwanda: race, tribe, clan, kind
    "idini", "amadini", "madini",  # Kinyarwanda/Kirundi: religion
    "kabila", "makabila", "ukabila",  # Swahili: tribe, clan
    "dini",  # Swahili: religion
}


def _is_forbidden(key):
    key = str(key)
    if _STEMS.search(key):
        return True
    words = re.sub(r"([a-z])([A-Z])", r"\1 \2", key).lower()
    return any(w in _WORDS for w in re.split(r"[^a-z]+", words))


def forbidden_keys(mapping, path=""):
    """Names of forbidden keys anywhere in a nested dict or list."""
    found = []
    if isinstance(mapping, dict):
        for key, value in mapping.items():
            here = f"{path}.{key}" if path else str(key)
            if _is_forbidden(key):
                found.append(here)
            found.extend(forbidden_keys(value, here))
    elif isinstance(mapping, list):
        for i, value in enumerate(mapping):
            found.extend(forbidden_keys(value, f"{path}[{i}]"))
    return found
