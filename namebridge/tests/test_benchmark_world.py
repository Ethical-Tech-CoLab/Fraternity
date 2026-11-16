import json

import pytest

from namebridge.benchmark.world import PARAMS, World, build_pools, full_name, write
from namebridge.schema import forbidden_keys


@pytest.fixture(scope="module")
def world():
    return World(json.loads(PARAMS.read_text(encoding="utf-8")), people=3000).generate()


def test_same_seed_same_world():
    p = json.loads(PARAMS.read_text(encoding="utf-8"))
    a = World(p, people=300).generate().people
    b = World(p, people=300).generate().people
    c = World(p, seed=1, people=300).generate().people
    assert a == b and a != c


def test_size_is_a_parameter(world):
    assert 3000 <= len(world.people) < 3010  # stops after the family that crosses the target


def test_every_parameter_has_a_source_and_confidence():
    params = json.loads(PARAMS.read_text(encoding="utf-8"))["params"]
    for name, p in params.items():
        assert p.get("source") and p.get("confidence"), name
        if p.get("varied"):
            assert len(p["range"]) == 2, name


def test_invented_elements_are_never_listed_profile_elements(world):
    listed = {}
    for (o, s, _), pool in build_pools().items():
        listed.setdefault((o, s.replace("_young", "")), set()).update(e for e, _ in pool.items)
    for p in world.people:
        for e in p["name"]:
            if e["basis"] == "invented":
                slot = "nom" if e["slot"] == "postnom" else e["slot"]
                assert e["text"] not in listed[p["origin"], slot]
                assert e["slot"] in ("kirundi", "kinyarwanda", "nom", "postnom")  # Christian names never invented


def test_naming_rules(world):
    people = {p["id"]: p for p in world.people}
    for fam in world.families:
        father = people.get(fam["father"]) if fam["father"] else None
        for pid in fam["members"]:
            p = people[pid]
            slots = [e["slot"] for e in p["name"]]
            if p["origin"] == "CD":
                assert slots[0] == "nom" and slots[-1] == "christian" or slots[-2] == "christian"
                if "postnom" in slots:
                    assert p["name"][0]["text"] != p["name"][1]["text"]
            else:
                assert slots[0] == ("kinyarwanda" if p["origin"] == "RW" else "kirundi")
            if father and p["role"] == "child":
                # a child may share one element with the father, never all of them
                assert [e["text"] for e in p["name"]] != [e["text"] for e in father["name"]]
            if any(e["basis"] == "inherited" for e in p["name"]) and p["origin"] == "BI":
                assert p["sex"] == "M"  # Burundi: a son may receive his father's name


def test_cd_siblings_sharing_a_nom_have_different_postnoms(world):
    by_family = {}
    for p in world.people:
        if p["origin"] == "CD" and p["role"] == "child" and len(p["name"]) >= 3 and p["name"][1]["slot"] == "postnom":
            by_family.setdefault((p["family"], p["name"][0]["text"]), []).append(p["name"][1]["text"])
    for posts in by_family.values():
        assert len(posts) == len(set(posts))


def test_no_forbidden_fields_and_written_output(world, tmp_path):
    assert all(not forbidden_keys(p) for p in world.people)
    manifest = write(world, tmp_path)
    assert manifest["summary"]["people"] == len(world.people)
    assert (tmp_path / "people.jsonl").read_text(encoding="utf-8").count("\n") == len(world.people)


def test_full_name_order():
    rw = {"origin": "RW", "name": [{"text": "uwase", "slot": "kinyarwanda"}, {"text": "marie", "slot": "christian"}]}
    cd = {"origin": "CD", "name": [{"text": "kasongo", "slot": "nom"}, {"text": "ilunga", "slot": "postnom"},
                                   {"text": "jean", "slot": "christian"}]}
    assert full_name(rw) == "UWASE Marie"
    assert full_name(cd) == "KASONGO ILUNGA Jean"


def test_rw_middle_name_follows_sex(world):
    for p in world.people:
        if p["origin"] == "RW" and len(p["name"]) == 3:
            assert p["name"][1]["text"] in ({"marie", "jeanne"} if p["sex"] == "F" else {"jean"})


def test_default_world_passes_its_own_size_check():
    w = World(json.loads(PARAMS.read_text(encoding="utf-8"))).generate()
    check = w.size_check()
    assert check["ok"], check
