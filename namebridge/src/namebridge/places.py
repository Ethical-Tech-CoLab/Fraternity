"""Place-name changes: provinces and towns renamed, merged or split (week 4).

A dataset (data/places/*.json) lists units (a name in a country at a level,
over a period) and changes between them, each with its sources. Each unit
becomes a Region node, with its other names (Kinyarwanda names, colonial
names, old spellings) and their sources, and each change a proposed edge,
old to new: renamed_to, merged_into (partial when only part of the unit went
there) or split_into. located_in records containment, not a change (Byumba
is in Gicumbi District). A child who says "Kayanza" and a record that says
"Butanyerera" can then be compared.

Run: python -m namebridge.places data/places/<dataset>.json ... [--graph data/graph]
"""

import json
import sys

from namebridge.packs import merge
from namebridge.schema.name_graph import PLACE_RELATIONS

LICENSE = "CC-BY-4.0"


def validate_dataset(data):
    did = data.get("dataset_id", "?")
    errors = [f"dataset {did}: missing {f!r}" for f in ("dataset_id", "version", "sources", "units", "changes", "confidence") if f not in data]
    if errors:
        return errors
    keys = {unit["key"] for unit in data["units"]}
    for unit in data["units"]:
        for other in unit.get("other_names", []):
            for sid in [other.get("source")] + other.get("also_in", []):
                if sid not in data["sources"]:
                    errors.append(f"dataset {did}: {unit['key']}: other name {other.get('name')!r} needs a known source")
    for i, change in enumerate(data["changes"]):
        where = f"dataset {did}: change {i} ({change.get('from')} -> {change.get('to')})"
        if change.get("relation") not in PLACE_RELATIONS:
            errors.append(f"{where}: relation must be one of {sorted(PLACE_RELATIONS)}")
        for end in ("from", "to"):
            if change.get(end) not in keys:
                errors.append(f"{where}: unknown unit {change.get(end)!r}")
        if not change.get("sources"):
            errors.append(f"{where}: every change needs a source")
        for sid in change.get("sources", []):
            if sid not in data["sources"]:
                errors.append(f"{where}: unknown source {sid!r}")
    return errors


def dataset_to_graph(data):
    did = data["dataset_id"]
    sources = data["sources"]
    nodes = [
        {"id": f"region:{unit['key']}", "type": "Region", "name": unit["name"], "country": unit["country"],
         "level": unit["level"], "period": unit["period"], "dataset_id": did,
         **({"other_names": unit["other_names"]} if unit.get("other_names") else {})}
        for unit in data["units"]
    ]
    edges = []
    for change in data["changes"]:
        refs = [sources[s] for s in change["sources"]]
        country = change["from"].split(":")[0]
        edge = {
            "id": f"e:{did}:{change['from']}>{change['to']}",
            "from": f"region:{change['from']}", "to": f"region:{change['to']}",
            "relation_type": change["relation"],
            "year": change["year"],
            "source_name": "; ".join(r["name"] for r in refs),
            "source_url": "; ".join(r["url"] for r in refs),
            "source_excerpt_or_locator": "; ".join(r["locator"] for r in refs),
            "source_language": refs[0]["language"],
            "applicable_languages": [],
            "applicable_regions": [country],
            "confidence": data["confidence"],
            "confidence_basis": "attested",
            "reversible": True,
            "review_status": "proposed",
            "license": LICENSE,
            "dataset_id": did,
        }
        if change.get("partial"):
            edge["partial"] = True
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
    datasets = []
    for path in args:
        with open(path, encoding="utf-8") as f:
            datasets.append(json.load(f))
    problems = load(datasets, graph)
    print("\n".join(problems) or f"{len(datasets)} dataset(s) loaded into {graph}")
    sys.exit(1 if problems else 0)
