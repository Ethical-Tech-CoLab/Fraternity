"""Cross-pack name data: names shared across the corridor's languages (week 4).

A dataset (data/crosspack/*.json) lists name concepts, each with the form
it takes in each language and the sources that attest it. Each concept
becomes a NameConcept node, each form a NameForm node, and each form is
linked to its concept by a proposed `historical_cognate_of` edge carrying
its sources. Cognates are for low-weight query expansion, never automatic
equivalence (CONCEPT-IDEA.md §3).

Run: python -m namebridge.crosspack data/crosspack/<dataset>.json ... [--graph data/graph]
"""

import json
import re
import sys
import unicodedata

from namebridge.packs import merge

LICENSE = "CC-BY-4.0"


def _slug(text):
    folded = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", folded.lower()).strip("-")


def validate_dataset(data):
    did = data.get("dataset_id", "?")
    errors = [f"dataset {did}: missing {f!r}" for f in ("dataset_id", "version", "sources", "concepts", "regions", "confidence") if f not in data]
    if errors:
        return errors
    for cid, concept in ((c.get("id", "?"), c) for c in data["concepts"]):
        if not concept.get("forms"):
            errors.append(f"dataset {did}: concept {cid} has no forms")
        for form in concept.get("forms", []):
            if not form.get("text") or not form.get("lang"):
                errors.append(f"dataset {did}: concept {cid}: every form needs text and lang")
            if not form.get("sources"):
                errors.append(f"dataset {did}: {cid}/{form.get('text')}: every form needs a source")
            for sid in form.get("sources", []):
                if sid not in data["sources"]:
                    errors.append(f"dataset {did}: {cid}/{form.get('text')}: unknown source {sid!r}")
    return errors


def dataset_to_graph(data):
    did = data["dataset_id"]
    sources = data["sources"]
    nodes, edges = [], []
    for concept in data["concepts"]:
        cid = f"nc:{did}:{concept['id']}"
        nodes.append({"id": cid, "type": "NameConcept", "label": concept["label"], "dataset_id": did})
        # One NameForm per written form; its languages and sources are merged
        # (Yohana is the Swahili, Kinyarwanda and Kirundi form of John).
        by_text = {}
        for form in concept["forms"]:
            entry = by_text.setdefault(form["text"], {"langs": [], "sources": []})
            entry["langs"].append(form["lang"])
            entry["sources"].extend(s for s in form["sources"] if s not in entry["sources"])
        for text, entry in by_text.items():
            fid = f"nf:{did}:{concept['id']}:{_slug(text)}"
            nodes.append({
                "id": fid, "type": "NameForm", "text": unicodedata.normalize("NFC", text),
                "script": "Latn", "languages": entry["langs"], "dataset_id": did,
            })
            refs = [sources[s] for s in entry["sources"]]
            edges.append({
                "id": f"e:{did}:{concept['id']}:{_slug(text)}",
                "from": fid, "to": cid, "relation_type": "historical_cognate_of",
                "source_name": "; ".join(r["name"] for r in refs),
                "source_url": "; ".join(r["url"] for r in refs),
                "source_excerpt_or_locator": "; ".join(r["locator"] for r in refs),
                "source_language": refs[0]["language"],
                "applicable_languages": entry["langs"],
                "applicable_regions": data["regions"],
                "confidence": data["confidence"],
                "confidence_basis": "attested",
                "reversible": True,
                "review_status": "proposed",
                "license": LICENSE,
                "dataset_id": did,
            })
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
