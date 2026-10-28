import pytest

from namebridge.schema import forbidden_keys

REFUSED = [
    "ethnicity", "Ethnie", "ethnic_group", "sub_ethnicity_1", "tribe", "tribu", "clan", "religion",
    "Religion", "caste", "race", "racialCategory",
    "ubwoko", "Ubwooko", "idini", "amadini", "kabila", "dini", "relative_dini",
]
ALLOWED = ["trace_id", "tracing_request", "ordinal", "gardinia", "name", "relation_name"]


@pytest.mark.parametrize("key", REFUSED)
def test_refused_in_every_record_language(key):
    assert forbidden_keys({key: "x"}) == [key]


@pytest.mark.parametrize("key", ALLOWED)
def test_ordinary_fields_pass(key):
    assert forbidden_keys({key: "x"}) == []


def test_nested():
    assert forbidden_keys({"a": [{"b": {"Ethnie": 1}}]}) == ["a[0].b.Ethnie"]
