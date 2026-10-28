"""Protected case graph: schema and validator only (CONCEPT-IDEA.md §5.1B).

This semester it stays empty: no real case data (SCOPE.md §4; DATA_RULES.md
DR-0 class C). The validator is used on synthetic records and in tests.
"""

from datetime import date

from namebridge.schema import forbidden_keys

NODE_TYPES = {
    "PersonHypothesis", "ObservedName", "CaseRecord", "Document", "Location", "Event",
    "Organization", "ContactPoint", "FamilyOrHouseholdGroup", "MediaObject", "BiometricReference",
}
EDGE_TYPES = {
    "same_person_candidate",
    "reported_parent_of", "reported_sibling_of", "reported_spouse_of",
    "member_of_household",
    "seen_at", "registered_at", "travelled_with",
    "attended_school", "associated_with_organization",
    "name_observed_in_document",
    "corroborated_by", "contradicted_by",
}
RELATIONSHIP_EDGES = {"reported_parent_of", "reported_sibling_of", "reported_spouse_of", "member_of_household"}

# Who asserted a fact, when, under what authority, how sensitive, how sure,
# and with whom it may be shared (§5.1B; §8 control 4).
FACT_METADATA = ("asserted_by", "asserted_at", "authority", "sensitivity", "confidence", "sharing")
SENSITIVITY = {"low", "medium", "high"}

# §5.3: preserve first, normalise into parallel fields.
OBSERVED_NAME_REQUIRED = ("observed_full_name", "observed_script", "source_type", "source_field_label", "source_order")
SOURCE_TYPES = {"oral_report", "form", "passport_viz", "passport_mrz", "registry", "flyer", "other"}

# Malawi Data Protection Act 2024 s. 8 bases used in tracing (DPIA.md (c)).
LAWFUL_BASES = {"vital_interest", "public_interest", "consent", "legal_obligation"}
# §8 control 7; NAME_CHANGE.md rule 2.
PROTECTED_FLAGS = {
    "minor", "trafficking", "domestic_violence", "asylum", "witness_protection",
    "may_not_wish_to_be_found", "possible_name_change",
}
ROUTES = {"ordinary", "protected"}
MATCH_DECISIONS = {"candidate", "confirmed", "rejected", "unresolved", "insufficient_evidence"}
RAW_BIOMETRIC_KEYS = {"fingerprint", "iris", "template", "face_image", "biometric_data"}
# Evidence kinds for a match. A confirmation needs at least one that is not a
# name: a name-only score never reaches confirmation (BENCHMARK_PROTOCOL.md §7;
# CONCEPT-IDEA.md §5.6).
NAME_EVIDENCE = {"name", "other_name", "nickname", "name_sound"}
OTHER_EVIDENCE = {"age", "date_of_birth", "sex", "family", "place", "event", "document", "photo_check", "question_only_family_knows"}


def _fact_errors(item, label):
    errors = [f"{label}: missing fact metadata {f!r}" for f in FACT_METADATA if f not in item]
    if item.get("sensitivity") not in SENSITIVITY | {None}:
        errors.append(f"{label}: unknown sensitivity {item['sensitivity']!r}")
    return errors


def validate_observed_name(name):
    label = f"ObservedName {name.get('id', '?')}"
    errors = [f"{label}: missing {f!r}" for f in OBSERVED_NAME_REQUIRED if f not in name]
    # A name heard and written down by someone else depends on how that person
    # spells sounds (§5.4A): record the writing convention they used.
    if name.get("source_type") == "oral_report" and not name.get("recorded_by_convention"):
        errors.append(f"{label}: an oral report needs 'recorded_by_convention' (e.g. fr, en, rn)")
    if name.get("source_type") not in SOURCE_TYPES | {None}:
        errors.append(f"{label}: unknown source_type {name['source_type']!r}")
    if name.get("source_order", "as_observed") != "as_observed":
        errors.append(f"{label}: source_order must be 'as_observed'; names are never reordered (§5.3)")
    return errors


def validate_case_record(record):
    label = f"CaseRecord {record.get('id', '?')}"
    errors = []
    for f in (
        "id", "lawful_basis", "sharing", "protected_flags", "route", "other_names_used", "possible_name_change",
        "created_at", "retain_until",
    ):
        if f not in record:
            errors.append(f"{label}: missing {f!r}")
    if errors:
        return errors

    # Retention and deletion (§8 control 9; DATA_RULES.md): every record says when it must go.
    try:
        if date.fromisoformat(record["retain_until"]) <= date.fromisoformat(record["created_at"]):
            errors.append(f"{label}: retain_until must be after created_at")
    except (TypeError, ValueError):
        errors.append(f"{label}: created_at and retain_until must be ISO dates (YYYY-MM-DD)")
    if record["lawful_basis"] not in LAWFUL_BASES:
        errors.append(f"{label}: unknown lawful_basis {record['lawful_basis']!r}")
    flags = set(record["protected_flags"])
    for flag in flags - PROTECTED_FLAGS:
        errors.append(f"{label}: unknown protected flag {flag!r}")
    if record["route"] not in ROUTES:
        errors.append(f"{label}: unknown route {record['route']!r}")
    if not isinstance(record["other_names_used"], list):
        errors.append(f"{label}: other_names_used must be a list (NAME_CHANGE.md rule 6)")

    # Every case involving a minor is a protected-person case (§8 control 7).
    if record.get("subject_is_minor") and "minor" not in flags:
        errors.append(f"{label}: a minor's case must carry the 'minor' flag")
    if record["lawful_basis"] == "consent" and record.get("subject_is_minor") and not record.get("guardian_consent"):
        errors.append(f"{label}: consent for a minor must come from a parent or guardian (Malawi DPA s. 17)")
    # A possible name change is a protected-person case (NAME_CHANGE.md rule 2).
    if record["possible_name_change"] and "possible_name_change" not in flags:
        errors.append(f"{label}: possible_name_change needs the 'possible_name_change' flag")
    if flags and record["route"] != "protected":
        errors.append(f"{label}: a flagged case must use route 'protected'")

    for key in forbidden_keys(record):
        errors.append(f"{label}: forbidden field {key!r} (no ethnicity, clan or religion; T13)")
    return errors


def validate_node(node):
    label = f"{node.get('type', '?')} {node.get('id', '?')}"
    if node.get("type") not in NODE_TYPES:
        return [f"{label}: unknown node type"]
    errors = []
    if node["type"] == "ObservedName":
        errors.extend(validate_observed_name(node))
    elif node["type"] == "CaseRecord":
        errors.extend(validate_case_record(node))
    elif node["type"] == "BiometricReference":
        # A pointer to an authorised system, never raw biometrics (§5.1B; SCOPE.md §4).
        if not node.get("external_ref"):
            errors.append(f"{label}: needs 'external_ref' to an authorised system")
        for key in RAW_BIOMETRIC_KEYS & set(node):
            errors.append(f"{label}: raw biometric field {key!r} is not allowed")
    if node["type"] in {"ContactPoint", "Location"} and node.get("sensitivity") != "high":
        errors.append(f"{label}: contact and location data are always 'high' sensitivity (§8 control 6)")
    if node["type"] != "CaseRecord":
        for key in forbidden_keys(node):
            errors.append(f"{label}: forbidden field {key!r}")
    return errors


def validate_edge(edge):
    label = f"edge {edge.get('id', '?')}"
    rel = edge.get("relation_type")
    if rel not in EDGE_TYPES:
        return [f"{label}: unknown relation_type {rel!r}"]
    errors = _fact_errors(edge, label)
    # Relationships are reported, never inferred (§12 "should not have").
    if rel in RELATIONSHIP_EDGES and edge.get("inferred"):
        errors.append(f"{label}: relationships are only reported, never inferred automatically")
    if rel == "same_person_candidate":
        decision = edge.get("decision", "candidate")
        if decision not in MATCH_DECISIONS:
            errors.append(f"{label}: unknown decision {decision!r}")
        # No automatic identity confirmation (SCOPE.md §4; GDPP para. 41; Malawi DPA s. 25).
        if decision == "confirmed" and (not edge.get("decided_by") or edge.get("decided_by") == "automatic"):
            errors.append(f"{label}: only a human reviewer can confirm a match")
        evidence = set(edge.get("evidence", []))
        for kind in evidence - NAME_EVIDENCE - OTHER_EVIDENCE:
            errors.append(f"{label}: unknown evidence kind {kind!r}")
        if decision == "confirmed" and not evidence & OTHER_EVIDENCE:
            errors.append(f"{label}: a name alone never confirms a match; add non-name evidence")
    for key in forbidden_keys(edge):
        errors.append(f"{label}: forbidden field {key!r}")
    return errors
