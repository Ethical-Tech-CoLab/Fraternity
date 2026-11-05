import json
from pathlib import Path

from namebridge.packs import load, pack_to_nodes
from namebridge.schema.name_graph import read_jsonl

PACKS = Path(__file__).resolve().parents[1] / "data" / "packs"
GRAPH = Path(__file__).resolve().parents[1] / "data" / "graph"


def pack(name):
    return json.loads((PACKS / name).read_text(encoding="utf-8"))


def test_every_rule_becomes_a_sourced_rule_node():
    nodes = pack_to_nodes(pack("bi-kirundi-2026.1.json"))
    rules = [n for n in nodes if n["type"] == "Rule"]
    assert rules and all(n["source"] and n["confidence"] for n in rules)
    assert "rule:bi-kirundi-2026.1:transliteration_rules:rw-to-rn-by" in {n["id"] for n in rules}


def test_load_is_repeatable(tmp_path):
    packs = [pack("rw-kiny-2026.1.json"), pack("bi-kirundi-2026.1.json")]
    assert load(packs, tmp_path) == []
    first = (tmp_path / "nodes.jsonl").read_text(encoding="utf-8")
    assert load(packs, tmp_path) == []
    assert (tmp_path / "nodes.jsonl").read_text(encoding="utf-8") == first


def test_invalid_pack_writes_nothing(tmp_path):
    bad = pack("rw-kiny-2026.1.json")
    bad["name_structures"][0]["source"] = ""
    assert any("needs a source" in e for e in load([bad], tmp_path))
    assert not (tmp_path / "nodes.jsonl").exists()


def test_reload_replaces_old_rules(tmp_path):
    p = pack("rw-kiny-2026.1.json")
    load([p], tmp_path)
    p["phonetic_rules"] = p["phonetic_rules"][:1]
    load([p], tmp_path)
    ids = {n["id"] for n in read_jsonl(tmp_path / "nodes.jsonl")}
    assert "rule:rw-kiny-2026.1:phonetic_rules:mp-is-mh" not in ids


def test_repo_graph_holds_every_pack():
    ids = {n.get("pack_id") for n in read_jsonl(GRAPH / "nodes.jsonl")}
    for path in PACKS.glob("*.json"):
        pid = json.loads(path.read_text(encoding="utf-8"))["pack_id"]
        if pid != "xx-template-2026.1":
            assert pid in ids, f"{path.name} not loaded: run python -m namebridge.packs data/packs/*.json"
