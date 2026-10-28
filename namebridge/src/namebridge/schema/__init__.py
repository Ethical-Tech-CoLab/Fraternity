"""Schemas and validators (week 3).

- name_graph: the public Name Knowledge Graph (CONCEPT-IDEA.md §5.1A)
- case_graph: the protected case graph, schema only (§5.1B)
- ingest: CPIMS+/Primero field allowlist (THREAT_MODEL.md T13)
- pack: language-pack template (§11)

Validators return a list of error strings; an empty list means valid.
"""

import re

# Attribute and field names NameBridge never holds: ethnicity, clan, tribe,
# religion and related (CONCEPT-IDEA.md §8 control 12; SCOPE.md §4; T8, T13).
# "race" only as a whole word part, so "trace" and "tracing" pass.
_FORBIDDEN = re.compile(r"ethnic|tribe|tribal|clan|religio|caste|(^|[_\W])rac(e|ial)([_\W]|$)", re.IGNORECASE)


def forbidden_keys(mapping, path=""):
    """Names of forbidden keys anywhere in a nested dict or list."""
    found = []
    if isinstance(mapping, dict):
        for key, value in mapping.items():
            here = f"{path}.{key}" if path else str(key)
            if _FORBIDDEN.search(str(key)):
                found.append(here)
            found.extend(forbidden_keys(value, here))
    elif isinstance(mapping, list):
        for i, value in enumerate(mapping):
            found.extend(forbidden_keys(value, f"{path}[{i}]"))
    return found
