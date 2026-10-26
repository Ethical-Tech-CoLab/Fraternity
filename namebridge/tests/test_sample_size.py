from namebridge.benchmark import sample_size as ss


def test_minor_precision_needs_4742_pairs():
    assert ss.pairs_for_error_bound(0.001, errors=1) == 4742


def test_zero_errors_follows_rule_of_three():
    assert ss.pairs_for_error_bound(0.01, errors=0) == 299


def test_minimum_people_is_driven_by_minor_precision():
    size = ss.minimum_people()
    assert size["binding"] == "minor precision"
    assert 25_000 <= size["total"] <= 26_000
