import pytest

from namebridge.schema import case_graph
from namebridge.schema.ingest import Refused, guess_script, ingest_cpims, observed_names

CONSENT = {"consent_for_tracing": True}


def test_allowlisted_fields_are_mapped_and_names_kept_whole():
    record = {**CONSENT, "name": "Synthetic  Name Two", "name_other": "Other Name", "sex": "f"}
    mapped, dropped, refused = ingest_cpims(record)
    assert mapped["observed_full_name"] == "Synthetic  Name Two"
    assert mapped["other_names_used"] == ["Other Name"]
    assert dropped == refused == []


def test_ethnicity_and_religion_refused_without_values():
    record = {**CONSENT, "name": "A", "ethnicity": ["secret-1"], "sub_ethnicity_1": "secret-2", "religion": ["secret-3"]}
    mapped, dropped, refused = ingest_cpims(record)
    assert refused == ["ethnicity", "religion", "sub_ethnicity_1"]
    assert "secret" not in repr((mapped, dropped, refused))


def test_unknown_fields_dropped():
    mapped, dropped, _ = ingest_cpims({**CONSENT, "name": "A", "location_current": "somewhere"})
    assert dropped == ["location_current"] and "somewhere" not in repr(mapped)


def test_case_without_consent_is_refused_whole():
    with pytest.raises(Refused):
        ingest_cpims({"name": "A"})
    with pytest.raises(Refused):
        ingest_cpims({"name": "A", "consent_for_tracing": False})
    ingest_cpims({"name": "A"}, kind="trace")  # traces carry the inquirer's request


def test_relatives_in_nested_family_section_are_kept():
    # Shape from Primero's db/dev_fixtures/cases.rb (checked 28 Oct 2026).
    record = {**CONSENT, "name": "A", "family_details_section": [
        {"relation_name": "Synthetic Father", "relation": "father"},
        {"relation_name": "Synthetic Mother", "relation": "mother", "relation_ethnicity": "secret"},
    ]}
    mapped, _, refused = ingest_cpims(record)
    assert [r["observed_full_name"] for r in mapped["relatives"]] == ["Synthetic Father", "Synthetic Mother"]
    assert refused == ["family_details_section[1].relation_ethnicity"]
    assert "secret" not in repr(mapped)


def test_forbidden_keys_hidden_in_nested_values_are_not_copied():
    record = {**CONSENT, "name": {"text": "A", "ethnicity": "secret"}}
    mapped, dropped, refused = ingest_cpims(record)
    assert "observed_full_name" not in mapped and dropped == ["name"]
    assert refused == ["name.ethnicity"]


def test_ingested_names_pass_the_case_schema():
    record = {**CONSENT, "name": "Synthetic Name", "name_nickname": "Nick",
              "family_details_section": [{"relation_name": "Synthetic Father", "relation": "father"}]}
    mapped, _, _ = ingest_cpims(record)
    nodes = observed_names(mapped, "case-9", recorded_by_convention="en")
    assert len(nodes) == 3
    for node in nodes:
        assert case_graph.validate_node(node) == []


def test_guess_script():
    assert guess_script("Ndayishimiye") == "Latn"
    assert guess_script("Ndáyishimíye") == "Latn"
    assert guess_script("恩达伊") == "Zzzz"
