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


def test_rwandan_towns_kept_their_names():
    # Byumba the town was not renamed in 2006: it is the capital of Gicumbi
    # District. Byumba the former province was merged; both share the name.
    nodes, edges = dataset_to_graph(places())
    names = {n["id"]: n["name"] for n in nodes}
    town = next(n["id"] for n in nodes if n["name"] == "Byumba" and n["level"] == "town")
    byumba = [e for e in edges if e["from"] == town]
    assert byumba and all(e["relation_type"] == "located_in" for e in byumba)
    assert any(names[e["to"]] == "Gicumbi" for e in byumba)


def test_kinyarwanda_province_names_are_sourced():
    nodes, _ = dataset_to_graph(places())
    north = next(n for n in nodes if n["name"] == "Northern Province")
    north_rw = [o for o in north["other_names"] if o["name"] == "Intara y'Amajyaruguru"]
    assert north_rw and north_rw[0]["source"] == "rw-north" and "rw-law-04-2010" in north_rw[0]["also_in"]
    assert any(o["name"] == "Province du Nord" and o["lang"] == "fr" for o in north["other_names"])


def test_other_name_needs_source():
    data = places()
    unit = next(u for u in data["units"] if u.get("other_names"))
    unit["other_names"][0]["source"] = "nowhere"
    assert any("needs a known source" in e for e in validate_dataset(data))


def _by_name(nodes):
    return {n["id"]: n for n in nodes}


def test_burundi_crosswalk_keeps_the_two_butaganzwas_apart():
    nodes, edges = dataset_to_graph(places())
    by = _by_name(nodes)
    targets = {}
    for e in edges:
        src = by[e["from"]]
        if src["name"] == "Butaganzwa" and src["period"] == "pre2025" and e["relation_type"] == "merged_into":
            targets.setdefault(e["from"], set()).add(by[e["to"]]["name"])
    assert len(targets) == 2
    assert {"Matongo"} in targets.values()  # the Kayanza one
    assert any("Butaganzwa" in t for t in targets.values())  # the Ruyigi one


def test_burundi_crosswalk_is_derived_and_proposed():
    nodes, edges = dataset_to_graph(places())
    by = _by_name(nodes)
    isale = [e for e in edges if by[e["from"]]["name"] == "Isale" and e["relation_type"] == "merged_into"]
    assert {by[e["to"]]["name"] for e in isale} == {"Isare", "Ntahangwa"}
    assert all(e["confidence_basis"] == "generated" and e["review_status"] == "proposed" and e["partial"] for e in isale)


def test_every_new_burundi_commune_is_in_a_province():
    # Guards against losing the 42 commune -> province links (lost once on 5 Nov 2026).
    nodes, edges = dataset_to_graph(places())
    new_communes = {n["id"] for n in nodes if n["country"] == "BI" and n["level"] == "commune" and n["period"] == "2025-"}
    placed = {e["from"] for e in edges if e["relation_type"] == "located_in"}
    assert len(new_communes) == 42 and new_communes <= placed
