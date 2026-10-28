from namebridge.schema import case_graph as cg


def case(**overrides):
    c = {
        "id": "case-1", "type": "CaseRecord", "lawful_basis": "vital_interest", "sharing": ["tracing_service"],
        "protected_flags": [], "route": "ordinary", "other_names_used": [], "possible_name_change": False,
    }
    c.update(overrides)
    return c


def test_ordinary_case_is_valid():
    assert cg.validate_node(case()) == []


def test_minor_must_be_flagged_and_protected():
    errors = cg.validate_case_record(case(subject_is_minor=True))
    assert any("'minor' flag" in e for e in errors)
    assert cg.validate_case_record(case(subject_is_minor=True, protected_flags=["minor"], route="protected")) == []


def test_possible_name_change_is_protected():
    errors = cg.validate_case_record(case(possible_name_change=True))
    assert any("possible_name_change" in e for e in errors)
    ok = case(possible_name_change=True, protected_flags=["possible_name_change"], route="protected")
    assert cg.validate_case_record(ok) == []


def test_flagged_case_cannot_use_ordinary_route():
    errors = cg.validate_case_record(case(protected_flags=["trafficking"]))
    assert any("route 'protected'" in e for e in errors)


def test_minor_consent_needs_guardian():
    c = case(lawful_basis="consent", subject_is_minor=True, protected_flags=["minor"], route="protected")
    assert any("s. 17" in e for e in cg.validate_case_record(c))


def test_religion_and_ethnicity_fields_refused():
    errors = cg.validate_case_record(case(religion="any", subject={"sub_ethnicity_1": "any"}))
    assert len([e for e in errors if "forbidden field" in e]) == 2


def test_trace_fields_are_not_mistaken_for_race():
    assert cg.validate_case_record(case(tracing_request_id="tr-1")) == []


def test_observed_name_keeps_order():
    name = {
        "id": "on-1", "type": "ObservedName", "observed_full_name": "Synthetic Name", "observed_script": "Latn",
        "source_type": "form", "source_field_label": "Nom", "source_order": "as_observed",
    }
    assert cg.validate_node(name) == []
    assert any("never reordered" in e for e in cg.validate_node({**name, "source_order": "given_first"}))


def test_biometrics_only_as_pointer():
    assert cg.validate_node({"id": "b1", "type": "BiometricReference"})
    errors = cg.validate_node({"id": "b1", "type": "BiometricReference", "external_ref": "sys:1", "fingerprint": "x"})
    assert any("raw biometric" in e for e in errors)


def test_location_is_high_sensitivity():
    assert cg.validate_node({"id": "l1", "type": "Location", "sensitivity": "medium"})


def fact(**overrides):
    e = {
        "id": "m1", "relation_type": "same_person_candidate", "asserted_by": "matcher", "asserted_at": "2026-11-02",
        "authority": "tracing_service", "sensitivity": "high", "confidence": 0.8, "sharing": [],
    }
    e.update(overrides)
    return e


def test_no_automatic_confirmation():
    assert any("human reviewer" in e for e in cg.validate_edge(fact(decision="confirmed")))
    assert any("human reviewer" in e for e in cg.validate_edge(fact(decision="confirmed", decided_by="automatic")))
    assert cg.validate_edge(fact(decision="confirmed", decided_by="reviewer:senior-caseworker")) == []


def test_relationships_are_reported_not_inferred():
    errors = cg.validate_edge(fact(relation_type="reported_parent_of", inferred=True))
    assert any("never inferred" in e for e in errors)


def test_facts_need_metadata():
    assert any("asserted_by" in e for e in cg.validate_edge({"id": "x", "relation_type": "seen_at"}))
