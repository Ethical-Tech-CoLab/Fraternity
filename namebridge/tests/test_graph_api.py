import json
from pathlib import Path

from namebridge.graph_api import NameGraph

REPO_GRAPH = Path(__file__).resolve().parents[1] / "data" / "graph"


def _edge(eid, a, b, rel, conf=0.6, status="proposed", reversible=True):
    return {"id": eid, "from": a, "to": b, "relation_type": rel, "confidence": conf, "confidence_basis": "attested",
            "review_status": status, "reversible": reversible, "source_name": "s", "source_url": "u", "source_excerpt_or_locator": "l"}


def _graph(tmp_path, forms, edges):
    nodes = [{"id": f"nf:{t.lower()}", "type": "NameForm", "text": t, "languages": ["und"]} for t in forms]
    (tmp_path / "nodes.jsonl").write_text("\n".join(json.dumps(n) for n in nodes), encoding="utf-8")
    (tmp_path / "edges.jsonl").write_text("\n".join(json.dumps(e) for e in edges), encoding="utf-8")
    return NameGraph(tmp_path)


def test_repo_graph_yohana_reaches_other_languages_through_the_concept():
    r = NameGraph(REPO_GRAPH).variants("yohana")
    forms = {v["form"] for v in r["variants"]}
    assert {"Jean", "John", "Yoane", "Yohane"} <= forms
    jean = next(v for v in r["variants"] if v["form"] == "Jean")
    assert len(jean["path"]) == 2 and all(s["source_name"] for s in jean["path"])
    assert jean["path_confidence"] == round(jean["path"][0]["confidence"] * jean["path"][1]["confidence"], 4)


def test_repo_graph_negative_constraint_reported():
    r = NameGraph(REPO_GRAPH).variants("ISHIMWE")
    assert {"Ashimwe", "Nishimwe"} <= {n["form"] for n in r["not_equivalent"]}
    assert not {"Ashimwe", "Nishimwe"} & {v["form"] for v in r["variants"]}


def test_negative_constraint_blocks_a_reachable_variant(tmp_path):
    g = _graph(tmp_path, ["Aaa", "Bbb", "Ccc"], [
        _edge("e1", "nf:aaa", "nf:bbb", "orthographic_variant_of"),
        _edge("e2", "nf:bbb", "nf:ccc", "orthographic_variant_of"),
        _edge("e3", "nf:aaa", "nf:ccc", "not_equivalent_to")])
    r = g.variants("Aaa")
    assert [v["form"] for v in r["variants"]] == ["Bbb"]
    assert [n["form"] for n in r["not_equivalent"]] == ["Ccc"]


def test_deprecated_edges_are_ignored(tmp_path):
    g = _graph(tmp_path, ["Aaa", "Bbb"], [_edge("e1", "nf:aaa", "nf:bbb", "orthographic_variant_of", status="deprecated")])
    assert g.variants("Aaa")["variants"] == []


def test_one_way_edges_are_followed_one_way(tmp_path):
    g = _graph(tmp_path, ["Aaa", "Bbb"], [_edge("e1", "nf:aaa", "nf:bbb", "nickname_of", reversible=False)])
    assert [v["form"] for v in g.variants("Aaa")["variants"]] == ["Bbb"]
    assert g.variants("Bbb")["variants"] == []


def test_confused_names_are_never_variants(tmp_path):
    g = _graph(tmp_path, ["Aaa", "Bbb"], [_edge("e1", "nf:aaa", "nf:bbb", "commonly_confused_with")])
    r = g.variants("Aaa")
    assert r["variants"] == [] and [c["form"] for c in r["commonly_confused_with"]] == ["Bbb"]


def test_min_confidence_prunes_long_paths(tmp_path):
    g = _graph(tmp_path, ["Aaa", "Bbb", "Ccc"], [
        _edge("e1", "nf:aaa", "nf:bbb", "orthographic_variant_of", conf=0.5),
        _edge("e2", "nf:bbb", "nf:ccc", "orthographic_variant_of", conf=0.5)])
    assert [v["form"] for v in g.variants("Aaa", min_confidence=0.3)["variants"]] == ["Bbb"]


def test_unknown_name_returns_empty_with_note():
    r = NameGraph(REPO_GRAPH).variants("Zzzqx")
    assert r["matched_forms"] == [] and r["variants"] == [] and "never confirmation" in r["note"]


def test_repo_graph_ambiguous_form_is_flagged_with_concepts():
    r = NameGraph(REPO_GRAPH).variants("Yakobo")
    assert len(r["ambiguous_between"]) == 2
    via = {v["form"]: v["via_concept"] for v in r["variants"]}
    assert via.get("Jacques") and via.get("Jacob") and via["Jacques"] != via["Jacob"]


def test_unambiguous_query_has_no_flag():
    assert NameGraph(REPO_GRAPH).variants("Yohana")["ambiguous_between"] == []
