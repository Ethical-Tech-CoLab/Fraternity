"""CPIMS+ / Primero ingestion allowlist (THREAT_MODEL.md T13; SCOPE.md §4).

Only named fields are read. Everything else is dropped without its value
being copied, and ethnicity, sub-ethnicity, clan and religion fields are
reported as refused, at any depth. Names arrive as one typed string, so they
are kept exactly as written and never split here (§5.3).

Field names from Primero's source (RESEARCH_LOG.md, 26 and 28 Oct 2026). In a
case, relatives are a nested list, `family_details_section`; in a trace, the
relative's name is a top-level field.
"""

import unicodedata

from namebridge.schema import forbidden_keys

# Primero field -> NameBridge field
CPIMS_ALLOWLIST = {
    "name": "observed_full_name",
    "name_other": "other_names_used",
    "name_nickname": "nicknames",
    "date_of_birth": "date_of_birth",
    "age": "age",
    "sex": "sex",
    "relation": "relation",
    "relation_name": "relative_observed_name",
    "relation_nickname": "relative_nickname",
    "relation_other_family": "relative_other_family",
    "relation_age": "relative_age",
    "consent_for_tracing": "consent_for_tracing",
}
FAMILY_SECTION = "family_details_section"
RELATIVE_ALLOWLIST = {
    "relation_name": "observed_full_name",
    "relation_nickname": "nicknames",
    "relation": "relation",
    "relation_age": "age",
}
LIST_FIELDS = {"other_names_used", "nicknames"}


class Refused(Exception):
    """The whole record may not be ingested."""


def _scalar(value):
    if isinstance(value, list):
        return all(isinstance(v, (str, int, float, bool)) or v is None for v in value)
    return isinstance(value, (str, int, float, bool)) or value is None


def _take(record, allowlist, prefix, mapped, dropped, refused):
    for key, value in record.items():
        where = f"{prefix}{key}"
        if forbidden_keys({key: None}):
            refused.append(where)
        elif key in allowlist and _scalar(value):
            target = allowlist[key]
            if target in LIST_FIELDS:
                value = [] if value in (None, "") else value if isinstance(value, list) else [value]
            mapped[target] = value
        else:
            # Unknown field, or an allowed field holding a nested object: drop
            # it whole, and report any forbidden keys hidden inside by name.
            dropped.append(where)
            refused.extend(f"{where}.{k}" for k in forbidden_keys(value))


def ingest_cpims(record, kind="case"):
    """Return (mapped_fields, dropped_field_names, refused_field_names).

    Values of dropped or refused fields are never copied or returned. A case
    is refused whole unless `consent_for_tracing` is true, as in Primero's own
    matching, which only searches cases with consent.
    """
    if kind == "case" and record.get("consent_for_tracing") is not True:
        raise Refused("case without consent_for_tracing = true")
    mapped, dropped, refused = {}, [], []
    rest = {k: v for k, v in record.items() if k != FAMILY_SECTION}
    _take(rest, CPIMS_ALLOWLIST, "", mapped, dropped, refused)
    relatives = record.get(FAMILY_SECTION) or []
    if relatives:
        mapped["relatives"] = []
        for i, relative in enumerate(relatives if isinstance(relatives, list) else []):
            if not isinstance(relative, dict):
                dropped.append(f"{FAMILY_SECTION}[{i}]")
                continue
            out = {}
            _take(relative, RELATIVE_ALLOWLIST, f"{FAMILY_SECTION}[{i}].", out, dropped, refused)
            mapped["relatives"].append(out)
    return mapped, sorted(dropped), sorted(refused)


def guess_script(text):
    """ISO 15924 code: Latn if every letter is Latin, otherwise Zzzz (unknown)."""
    letters = [c for c in text if c.isalpha()]
    if letters and all("LATIN" in unicodedata.name(c, "") for c in letters):
        return "Latn"
    return "Zzzz"


def observed_names(mapped, record_id, recorded_by_convention):
    """ObservedName nodes for the case schema (case_graph.validate_node), one per name."""

    def node(suffix, text, label):
        return {
            "id": f"{record_id}:{suffix}",
            "type": "ObservedName",
            "observed_full_name": text,
            "observed_script": guess_script(text),
            "source_type": "form",  # typed into CPIMS+ by a caseworker
            "source_field_label": label,
            "source_order": "as_observed",
            "written_by": "other",
            "recorded_by_convention": recorded_by_convention,
        }

    nodes = []
    if mapped.get("observed_full_name"):
        nodes.append(node("name", mapped["observed_full_name"], "name"))
    for i, text in enumerate(mapped.get("other_names_used", [])):
        nodes.append(node(f"other{i}", text, "name_other"))
    for i, text in enumerate(mapped.get("nicknames", [])):
        nodes.append(node(f"nick{i}", text, "name_nickname"))
    if mapped.get("relative_observed_name"):
        nodes.append(node("relative", mapped["relative_observed_name"], "relation_name"))
    for i, relative in enumerate(mapped.get("relatives", [])):
        if relative.get("observed_full_name"):
            nodes.append(node(f"rel{i}", relative["observed_full_name"], f"{FAMILY_SECTION}.relation_name"))
    return nodes
