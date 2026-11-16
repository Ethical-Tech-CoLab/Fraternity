import json
from collections import Counter, defaultdict

import pytest

from namebridge.benchmark.queries import build
from namebridge.benchmark.records import PACKS, load_packs, pack_entry
from namebridge.benchmark.world import PARAMS


def _read(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


@pytest.fixture(scope="module")
def built(tmp_path_factory):
    out = tmp_path_factory.mktemp("bench")
    manifest = build(json.loads(PARAMS.read_text(encoding="utf-8")), out, people=3000)
    return out, manifest


def test_public_files_hold_no_answers(built):
    out, _ = built
    for r in _read(out / "public" / "records.jsonl"):
        assert "gold_person" not in r and "person" not in r
    for q in _read(out / "public" / "queries.jsonl"):
        assert "expected" not in q and "sought_person" not in q and "kind" not in q
        assert "id" not in q.get("sought", {})


def test_absent_people_have_no_public_record_and_are_never_found(built):
    out, _ = built
    gold_records = _read(out / "gold" / "records.jsonl")
    public_ids = {r["record_id"] for r in _read(out / "public" / "records.jsonl")}
    absent = {r["person"] for r in gold_records if not r["searchable"]}
    assert absent
    for r in gold_records:
        assert (r["record_id"] in public_ids) == r["searchable"]
    for g in _read(out / "gold" / "queries.jsonl"):
        if g.get("sought_person") in absent:
            assert g["expected"] == "not_present"
        elif g.get("sought_person"):
            assert g["expected"] != "not_present"


def test_reciprocal_pairs_link_both_ways(built):
    out, _ = built
    gold = {g["query_id"]: g for g in _read(out / "gold" / "queries.jsonl")}
    public = {q["query_id"]: q for q in _read(out / "public" / "queries.jsonl")}
    pairs = [g for g in gold.values() if g.get("reciprocal_with")]
    assert pairs
    for g in pairs:
        other = gold[g["reciprocal_with"]]
        assert other["reciprocal_with"] == g["query_id"]
        assert (g["sought_person"], g["searcher_person"]) == (other["searcher_person"], other["sought_person"])
        if g["same_clerk"]:
            assert public[g["query_id"]]["writer_id"] == public[other["query_id"]]["writer_id"]


def test_splits_are_by_family_and_lookalikes_share_the_split(built):
    out, _ = built
    split = {s["family"]: s["split"] for s in _read(out / "gold" / "splits.jsonl")}
    people = {p["id"]: p for p in _read(out / "gold" / "people.jsonl")}
    for p in people.values():
        assert p["split"] == split[p["family"]]
    for h in _read(out / "gold" / "hard_negatives.jsonl"):
        assert people[h["a"]]["split"] == people[h["b"]]["split"]
    shares = Counter(split.values())
    total = sum(shares.values())
    assert 0.55 < shares["train"] / total < 0.65 and 0.15 < shares["test"] / total < 0.25


def test_adversarial_searches_must_be_refused(built):
    out, manifest = built
    adv = [g for g in _read(out / "gold" / "queries.jsonl") if g["kind"].startswith("adversarial")]
    assert len(adv) == 400 and all(g["expected"] == "refuse" and g["rule"] for g in adv)
    assert len({g["kind"] for g in adv}) == 4


def test_child_speech_only_where_the_pack_has_it(built):
    out, _ = built
    packs = load_packs()
    people = {p["id"]: p for p in _read(out / "gold" / "people.jsonl")}
    seen = False
    for g in _read(out / "gold" / "queries.jsonl"):
        for e in g.get("errors", []):
            if ":child-" in e:
                seen = True
                origin = people[g["sought_person"]]["origin"]
                assert e.startswith(PACKS[origin]) and pack_entry(packs[origin], "phonetic_rules", e.split(":")[-1])
    assert seen


def test_holdout_is_separate(built):
    out, manifest = built
    main_ids = {p["id"] for p in _read(out / "gold" / "people.jsonl")}
    hold = _read(out / "holdout" / "gold" / "people.jsonl")
    assert hold and all(p["id"].startswith("h") and p["id"] not in main_ids for p in hold)
    years = {r["record_year"] for r in _read(out / "holdout" / "public" / "records.jsonl")}
    assert min(years) >= 2025
    assert manifest["frozen"] is False and all(len(v) == 64 for v in manifest["sha256"].values())


def test_same_seed_same_files(built, tmp_path):
    out, manifest = built
    again = build(json.loads(PARAMS.read_text(encoding="utf-8")), tmp_path, people=3000)
    assert again["sha256"] == manifest["sha256"]
