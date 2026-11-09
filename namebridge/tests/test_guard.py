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


def test_ordinary_words_containing_a_stem_pass():
    # "dis-tribu-tion", "at-tribu-te": false positives fixed 9 Nov 2026.
    from namebridge.schema import forbidden_keys
    ok = {"token_count_distribution": 1, "name_attributes": 1, "contribution": 1, "attributeName": 1}
    assert forbidden_keys(ok) == []


def test_real_tribe_fields_still_caught_next_to_benign_words():
    from namebridge.schema import forbidden_keys
    bad = {"tribu": 1, "Tribu_origine": 1, "tribe_distribution": 1, "ethnie": 1, "distribution_by_clan": 1}
    assert sorted(forbidden_keys(bad)) == sorted(bad)
