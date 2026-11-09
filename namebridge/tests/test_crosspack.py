import json
from pathlib import Path

from namebridge.crosspack import dataset_to_graph, load, validate_dataset
from namebridge.packs import load as load_packs
from namebridge.schema.name_graph import read_jsonl

ROOT = Path(__file__).resolve().parents[1] / "data"
NAMES = ROOT / "crosspack" / "christian-names-2026.1.json"


def names():
    return json.loads(NAMES.read_text(encoding="utf-8"))


def test_dataset_is_valid():
    assert validate_dataset(names()) == []


def test_form_without_source_is_refused():
    data = names()
    data["concepts"][0]["forms"][0]["sources"] = []
    assert any("needs a source" in e for e in validate_dataset(data))


def test_shared_form_is_one_node_with_its_languages():
    nodes, edges = dataset_to_graph(names())
    yohana = [n for n in nodes if n.get("text") == "Yohana"]
    assert len(yohana) == 1 and sorted(yohana[0]["languages"]) == ["rn", "rw", "sw"]


def test_cognate_edges_are_proposed_and_sourced():
    _, edges = dataset_to_graph(names())
    assert edges and all(e["review_status"] == "proposed" and e["source_url"] for e in edges)
    assert {e["relation_type"] for e in edges} == {"historical_cognate_of"}


def test_packs_and_crosspack_coexist(tmp_path):
    packs = [json.loads(p.read_text(encoding="utf-8")) for p in (ROOT / "packs").glob("*.json")]
    packs = [p for p in packs if p["pack_id"] != "xx-template-2026.1"]
    assert load_packs(packs, tmp_path) == []
    assert load([names()], tmp_path) == []
    assert load_packs(packs, tmp_path) == []  # reloading packs keeps the cross-pack data
    assert any(e.get("dataset_id") for e in read_jsonl(tmp_path / "edges.jsonl"))


def test_repo_graph_holds_the_christian_names():
    ids = {n.get("dataset_id") for n in read_jsonl(ROOT / "graph" / "nodes.jsonl")}
    assert "christian-names-2026.1" in ids


def test_slug_keeps_letters_without_decomposition():
    # Regression (9 Nov 2026): ɛ/ɔ were dropped, so distinct forms could share an id.
    from namebridge.crosspack import _slug
    assert _slug("Pɛtɛlɔ") == "petelo"
    assert _slug("Pɛtɛlɔ") != _slug("Ptl")


def test_forms_differing_only_by_accents_stay_separate():
    # Joël (fr) and Joel (en) fold to the same slug; both forms must survive with distinct ids.
    from namebridge.crosspack import dataset_to_graph
    data = {"dataset_id": "t-2026.1", "regions": ["CD"], "confidence": 0.6,
            "sources": {"s": {"name": "n", "url": "u", "locator": "l", "language": "fr"}},
            "concepts": [{"id": "yoel", "label": "Joel", "forms": [
                {"text": "Joël", "lang": "fr", "sources": ["s"]}, {"text": "Joel", "lang": "en", "sources": ["s"]}]}]}
    nodes, edges = dataset_to_graph(data)
    forms = [n for n in nodes if n["type"] == "NameForm"]
    assert sorted(n["text"] for n in forms) == ["Joel", "Joël"]
    assert len({n["id"] for n in forms}) == 2 and len({e["id"] for e in edges}) == 2
