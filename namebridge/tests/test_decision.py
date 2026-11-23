import pytest

from namebridge.decision import Candidate, Thresholds, decide

T = Thresholds(possible=0.5, strong=0.9, margin=0.1)


def one(score, **kw):
    kw.setdefault("minor", False)
    return decide([Candidate("r", score, **kw)], T)[0]


def test_thresholds_are_required():
    with pytest.raises(TypeError):
        decide([Candidate("r", 0.99, minor=False)], None)


def test_bad_thresholds_rejected():
    with pytest.raises(ValueError):
        Thresholds(possible=0.9, strong=0.5, margin=0.1)


def test_low_score_stops_as_insufficient():
    assert one(0.2).status == "insufficient_evidence"


def test_middle_score_stays_possible_not_strong():
    assert one(0.7).status == "possible"


def test_verified_conflict_stops_even_with_high_score():
    v = one(0.99, minor=False, conflicts=("birth_year",))
    assert v.status == "conflict" and v.stopped


def test_close_second_candidate_is_ambiguous_for_both():
    vs = {v.record_id: v for v in decide([Candidate("a", 0.95, minor=False), Candidate("b", 0.90, minor=False)], T)}
    assert vs["a"].status == "ambiguous" and vs["a"].stopped  # gap 0.05 < margin 0.1
    assert vs["b"].status == "ambiguous" and vs["b"].stopped  # a better candidate exists: never strong


def test_clear_adult_match_is_strong_but_only_a_person_confirms():
    v = one(0.95, minor=False)
    assert v.status == "strong_evidence" and not v.stopped


def test_child_on_names_alone_never_strong():
    v = one(0.99, minor=True)
    assert v.status == "needs_independent_check" and v.stopped


def test_child_with_independent_check_can_be_strong():
    v = one(0.99, minor=True, independent_check=True)
    assert v.status == "strong_evidence"


def test_statuses_never_say_confirmed():
    from namebridge.decision import STATUSES
    assert "confirmed" not in STATUSES  # a person confirms; the function only recommends


def test_every_candidate_gets_a_verdict_in_score_order():
    vs = decide([Candidate("x", 0.3, minor=False), Candidate("y", 0.95, minor=False)], T)
    assert [v.record_id for v in vs] == ["y", "x"]
