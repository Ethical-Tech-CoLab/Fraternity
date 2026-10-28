"""CPIMS+ / Primero ingestion allowlist (THREAT_MODEL.md T13; SCOPE.md §4).

Only named fields are read. Everything else is dropped without its value
being copied, and ethnicity, sub-ethnicity, clan and religion fields are
reported as refused. Names arrive as one typed string, so they are kept
exactly as written and never split here (§5.3).

Field names from Primero's source, as recorded in RESEARCH_LOG.md (26 Oct 2026).
"""

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
}
LIST_FIELDS = {"other_names_used", "nicknames"}


def ingest_cpims(record):
    """Return (mapped_fields, dropped_field_names, refused_field_names).

    Values of dropped or refused fields are never copied or returned.
    """
    mapped, dropped, refused = {}, [], []
    for key, value in record.items():
        if forbidden_keys({key: None}):
            refused.append(key)
        elif key in CPIMS_ALLOWLIST:
            target = CPIMS_ALLOWLIST[key]
            if target in LIST_FIELDS:
                value = [] if value in (None, "") else value if isinstance(value, list) else [value]
            mapped[target] = value
        else:
            dropped.append(key)
    return mapped, sorted(dropped), sorted(refused)
