import json
import shutil
from pathlib import Path

from namebridge.graph_api import NameGraph
from namebridge.review import queue, read_reviews, record
from namebridge.variants import load as load_variants

REPO = Path(__file__).resolve().parents[1]
DS = REPO / "data" / "variants" / "attested-variants-2026.1.json"
EDGE = "e:attested-variants-2026.1:muamba:orthographic_variant_of:mwamba"


def _graph(tmp_path):
    g = tmp_path / "data" / "graph"
    g.mkdir(parents=True)
    (g / "nodes.jsonl").write_text("", encoding="utf-8")
    (g / "edges.jsonl").write_text("", encoding="utf-8")
    assert load_variants([json.loads(DS.read_text(encoding="utf-8"))], g) == []
    return g


def _d(decision="deprecated", role="linguist", edge=EDGE):
    return {"edge": edge, "decision": decision, "reviewer": "Test Reviewer", "reviewer_role": role, "date": "2026-11-09", "note": "test"}


def test_invalid_role_or_missing_note_refused(tmp_path):
    g = _graph(tmp_path)
    assert any("reviewer_role" in e for e in record(g, _d(role="intern")))
    bad = _d(); bad["note"] = ""
    assert any("note" in e for e in record(g, bad))
    assert read_reviews(g) == []


def test_unknown_edge_refused(tmp_path):
    g = _graph(tmp_path)
    assert any("unknown edge" in e for e in record(g, _d(edge="e:nope")))


def test_decision_survives_reload_and_deprecated_is_hidden_from_api(tmp_path):
    g = _graph(tmp_path)
    assert NameGraph(g).variants("Muamba")["variants"]
    assert record(g, _d()) == []
    assert load_variants([json.loads(DS.read_text(encoding="utf-8"))], g) == []   # rebuild from the dataset
    edge = next(json.loads(l) for l in (g / "edges.jsonl").read_text(encoding="utf-8").splitlines() if EDGE in l)
    assert edge["review_status"] == "deprecated" and edge["reviewer_role"] == "linguist"
    assert NameGraph(g).variants("Muamba")["variants"] == []


def test_reviewed_edge_leaves_the_queue(tmp_path):
    g = _graph(tmp_path)
    _, before = queue(g)
    assert record(g, _d(decision="reviewed")) == []
    _, after = queue(g)
    assert after == before - 1


def test_generated_edge_cannot_be_reviewed(tmp_path):
    g = _graph(tmp_path)
    edges = [json.loads(l) for l in (g / "edges.jsonl").read_text(encoding="utf-8").splitlines()]
    edges[0]["confidence_basis"] = "generated"
    (g / "edges.jsonl").write_text("\n".join(json.dumps(e) for e in edges), encoding="utf-8")
    assert any("generated" in e for e in record(g, _d(decision="reviewed", edge=edges[0]["id"])))
