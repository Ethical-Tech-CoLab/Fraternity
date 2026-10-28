from namebridge.schema.ingest import ingest_cpims


def test_allowlisted_fields_are_mapped_and_names_kept_whole():
    mapped, dropped, refused = ingest_cpims({"name": "Synthetic  Name Two", "name_other": "Other Name", "sex": "f"})
    assert mapped == {"observed_full_name": "Synthetic  Name Two", "other_names_used": ["Other Name"], "sex": "f"}
    assert dropped == refused == []


def test_ethnicity_and_religion_refused_without_values():
    record = {"name": "A", "ethnicity": "secret-1", "sub_ethnicity_1": "secret-2", "religion": "secret-3"}
    mapped, dropped, refused = ingest_cpims(record)
    assert refused == ["ethnicity", "religion", "sub_ethnicity_1"]
    assert "secret" not in repr((mapped, dropped, refused))


def test_unknown_fields_dropped():
    mapped, dropped, _ = ingest_cpims({"name": "A", "location_current": "somewhere"})
    assert dropped == ["location_current"] and "somewhere" not in repr(mapped)
