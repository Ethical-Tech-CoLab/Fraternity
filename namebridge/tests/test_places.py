import json
from pathlib import Path

from namebridge.places import dataset_to_graph, validate_dataset
from namebridge.schema import name_graph as ng

ROOT = Path(__file__).resolve().parents[1] / "data"
PLACES = ROOT / "places" / "places-2026.1.json"


def places():
    return json.loads(PLACES.read_text(encoding="utf-8"))


def test_dataset_is_valid():
    assert validate_dataset(places()) == []


def test_change_without_source_is_refused():
    data = places()
    data["changes"][0]["sources"] = []
    assert any("needs a source" in e for e in validate_dataset(data))


def test_kayanza_is_now_in_butanyerera():
    nodes, edges = dataset_to_graph(places())
    names = {n["id"]: n["name"] for n in nodes}
    assert any(
        names[e["from"]] == "Kayanza" and names[e["to"]] == "Butanyerera" and e["relation_type"] == "merged_into"
        for e in edges
    )


def test_place_relations_join_regions_only():
    nodes = [
        {"id": "nf:a", "type": "NameForm", "text": "Kitega", "script": "Latn"},
        {"id": "region:b", "type": "Region", "name": "Gitega", "country": "BI"},
    ]
    _, edges = dataset_to_graph(places())
    edge = dict(edges[0], **{"from": "nf:a", "to": "region:b", "id": "x"})
    assert any("cannot join NameForm to Region" in e for e in ng.validate_graph(nodes, [edge]))


def test_region_needs_country():
    assert any("ISO 3166" in e for e in ng.validate_node({"id": "r", "type": "Region", "name": "Gitega"}))


def test_repo_graph_holds_the_places():
    ids = {n.get("dataset_id") for n in ng.read_jsonl(ROOT / "graph" / "nodes.jsonl")}
    assert "places-2026.1" in ids
