import json
import random
import re

import pytest

from namebridge.benchmark.records import (CONFUSIONS, CONVENTIONS, FOREIGN_RULES, PACKS, Recorder, load_packs,
                                          pack_entry, write)
from namebridge.benchmark.world import PARAMS, World
from namebridge.schema import forbidden_keys


@pytest.fixture(scope="module")
def params():
    return json.loads(PARAMS.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def rec(params):
    return Recorder(World(params, people=4000).generate(), params).generate()


def test_every_transform_is_a_pack_entry():
    packs = load_packs()
    for origins, section, sound, writer, _, _ in CONVENTIONS:
        for o in origins:
            assert pack_entry(packs[o], section, sound, writer), (o, sound, writer)
    for o in origins:
        assert pack_entry(packs[o], "spelling_conventions", "/ɾ/", "ny")  # Chichewa r/l rule
    for origins, sounds, _, _, _ in CONFUSIONS:
        for o in origins:
            assert pack_entry(packs[o], "listener_confusions", sounds), (o, sounds)
    # foreign-name rules apply only where the pack holds the entry (the DRC pack has no i -> y entry)
    params = json.loads(PARAMS.read_text(encoding="utf-8"))
    r = Recorder(World(params, people=20).generate(), params)
    for o in PACKS:
        for rule in r.foreign[o]:
            section, key, writer = FOREIGN_RULES[rule]
            assert pack_entry(packs[o], section, key, writer)
    assert "i_to_y" not in r.foreign["CD"] and "i_to_y" in r.foreign["RW"]


def test_no_unsourced_foreign_rule_in_records(rec):
    for r in rec.records:
        if rec.people[r["gold_person"]]["origin"] == "CD":
            assert not any(e.endswith("/i/~y") for e in r["errors"])


def test_every_record_parameter_has_a_source(params):
    for name, p in params["params"].items():
        if name.startswith("rec_"):
            assert p.get("source") and p.get("confidence"), name


def test_same_seed_same_records(params):
    a = Recorder(World(params, people=200).generate(), params).generate().records
    b = Recorder(World(params, people=200).generate(), params).generate().records
    assert a == b


def test_calibration_near_22_percent(rec):
    assert 0.18 <= rec.summary()["name_values_differ_between_linked_records"] <= 0.26


def test_records_are_consistent(rec):
    people = rec.people
    for r in rec.records:
        p = people[r["gold_person"]]
        assert r["record_year"] >= p["birth_year"]
        if r["source"] == "school_list":
            assert 6 <= rec.year - p["birth_year"] <= 24
        if r["source"] == "passport_mrz":
            assert not p["minor"] and re.fullmatch(r"[A-Z<]{1,39}", r["name"]) and r["written_by"] != "ear"
        if any(e.startswith("name_change") for e in r["errors"]):
            assert not p["minor"] and r["source"] in ("registration", "distribution_list", "school_list")
        assert not forbidden_keys(r)


def test_chichewa_writer_rule():
    params = json.loads(PARAMS.read_text(encoding="utf-8"))
    params["params"]["rec_convention_rate"]["value"] = 1.0
    r = Recorder(World(params, people=50).generate(), params)
    r.rng = random.Random(0)
    log = []
    # l at the start, l after a/o/u, r after i/e
    assert r._chichewa_rl("rukundo", log, "BI") == "lukundo"
    assert r._chichewa_rl("barore", log, "BI") == "balole"
    assert r._chichewa_rl("kirena", log, "BI") == "kirena"
    assert log and all(e.endswith(":/ɾ/:ny") for e in log)


def test_errors_are_logged_by_kind(rec):
    kinds = {e.split(":")[0] for r in rec.records for e in r["errors"]}
    assert {"order", "typo", "crosspack", PACKS["RW"], PACKS["BI"], PACKS["CD"]} <= kinds


def test_written_output_has_no_private_fields(rec, tmp_path):
    write(rec, tmp_path)
    first = json.loads((tmp_path / "records.jsonl").read_text(encoding="utf-8").splitlines()[0])
    assert not any(k.startswith("_") for k in first)


def test_french_writer_conventions_only_for_french_writers(rec):
    for r in rec.records:
        for e in r["errors"]:
            if e.endswith(":fr") and ":spelling_conventions:" in e:
                assert r["writer_language"] == "fr", (r["record_id"], e)
