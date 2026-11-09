"""Attested relationships between personal-name forms (week 5).

A dataset (data/variants/*.json) lists name forms and relations between them, each with a
source: spelling variants that co-occur as frequent forms in real aggregate data, and
negative constraints (not_equivalent_to) between names registered as distinct. Nothing is
invented here; generated variants belong to the matcher, not the graph. Every edge enters
as `proposed`.

Run: python -m namebridge.variants data/variants/<dataset>.json ... [--graph data/graph]
"""

import json
import sys

from namebridge.packs import merge

LICENSE = "CC-BY-4.0"


def validate_dataset(data):
    did = data.get("dataset_id", "?")
    errors = [f"dataset {did}: missing {f!r}" for f in ("dataset_id", "version", "sources", "forms", "relations") if f not in data]
    if errors:
        return errors
    ids = {f["id"] for f in data["forms"]}
    for i, r in enumerate(data["relations"]):
        where = f"dataset {did}: relation {i} ({r.get('from')}->{r.get('to')})"
        if r.get("from") not in ids or r.get("to") not in ids:
            errors.append(f"{where}: unknown form")
        if r.get("source") not in data["sources"]:
            errors.append(f"{where}: every relation needs a known source")
        if not r.get("regions"):
            errors.append(f"{where}: regions required")
    return errors


def dataset_to_graph(data):
    did, src = data["dataset_id"], data["sources"]
    forms = {f["id"]: f for f in data["forms"]}
    def nid(fid):
        return f"{'mo' if forms[fid].get('type') == 'Morpheme' else 'nf'}:{did}:{fid}"

    nodes = []
    for f in data["forms"]:
        node = {"id": nid(f["id"]), "type": f.get("type", "NameForm"), "text": f["text"], "languages": [f["lang"]], "dataset_id": did}
        if node["type"] == "NameForm":
            node["script"] = "Latn"
        if f.get("meaning"):
            node["meaning"] = f["meaning"]
        nodes.append(node)
    edges = []
    for r in data["relations"]:
        s = src[r["source"]]
        edge = {"id": f"e:{did}:{r['from']}:{r['relation_type']}:{r['to']}",
                "from": nid(r["from"]), "to": nid(r["to"]), "relation_type": r["relation_type"],
                "source_name": s["name"], "source_url": s["url"], "source_excerpt_or_locator": s["locator"],
                "source_language": s["language"],
                "applicable_languages": sorted({forms[r["from"]]["lang"], forms[r["to"]]["lang"]}),
                "applicable_regions": r["regions"], "confidence": r["confidence"], "confidence_basis": r["confidence_basis"],
                "reversible": r.get("reversible", True), "review_status": "proposed", "license": LICENSE, "dataset_id": did}
        if r.get("note"):
            edge["note"] = r["note"]
        edges.append(edge)
    return nodes, edges


def load(datasets, graph_dir):
    errors = [e for d in datasets for e in validate_dataset(d)]
    if errors:
        return errors
    nodes, edges = [], []
    for data in datasets:
        n, e = dataset_to_graph(data)
        nodes.extend(n)
        edges.extend(e)
    return merge(graph_dir, "dataset_id", {d["dataset_id"] for d in datasets}, nodes, edges)


if __name__ == "__main__":
    args = sys.argv[1:]
    graph = "data/graph"
    if "--graph" in args:
        i = args.index("--graph")
        graph = args[i + 1]
        del args[i:i + 2]
    datasets = [json.load(open(p, encoding="utf-8")) for p in args]
    problems = load(datasets, graph)
    print("\n".join(problems) or f"{len(datasets)} dataset(s) loaded into {graph}")
    sys.exit(1 if problems else 0)
