import json
from pathlib import Path

from namebridge.variants import dataset_to_graph, validate_dataset

DATA = Path(__file__).resolve().parents[1] / "data" / "variants"


def _repo():
    return [json.loads(p.read_text(encoding="utf-8")) for p in DATA.glob("*.json")]


def test_repo_datasets_are_valid():
    for d in _repo():
        assert validate_dataset(d) == [], d["dataset_id"]


def test_every_edge_is_proposed_and_sourced():
    for d in _repo():
        _, edges = dataset_to_graph(d)
        assert edges and all(e["review_status"] == "proposed" and e["source_name"] for e in edges)


def test_relation_needs_known_source_and_form():
    d = {"dataset_id": "t-2026.1", "version": "0.1.0", "sources": {"s": {}}, "forms": [{"id": "a", "text": "A", "lang": "rw"}],
         "relations": [{"from": "a", "to": "b", "relation_type": "not_equivalent_to", "source": "x", "regions": ["RW"]}]}
    errs = validate_dataset(d)
    assert any("unknown form" in e for e in errs) and any("known source" in e for e in errs)
