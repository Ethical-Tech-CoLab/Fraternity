"""Load language packs into the public Name Knowledge Graph (week 4).

Each pack becomes a Language node per language and a Rule node per rule
entry (structure, order, transliteration, sound layer ...), carrying the
entry's source and confidence. Name-to-name edges are not made here: they
come from attested sources (naming profiles, cross-pack given names), never
from applying a rule to generate variants (DATA_RULES.md DR-1.5).

Loading replaces the nodes a pack loaded before, so it can be re-run.

Run: python -m namebridge.packs data/packs/<pack>.json ... [--graph data/graph]
"""

import json
import sys
from pathlib import Path

from namebridge.schema.name_graph import read_jsonl, validate_graph
from namebridge.schema.pack import RULE_FIELDS, validate_pack

TEMPLATE_ID = "xx-template-2026.1"


def pack_to_nodes(pack):
    pid = pack["pack_id"]
    nodes = [
        {"id": f"lang:{lang}", "type": "Language", "code": lang}
        for lang in pack["languages"]
    ]
    for field in RULE_FIELDS:
        for i, entry in enumerate(pack[field]):
            nodes.append({
                "id": f"rule:{pid}:{field}:{entry.get('id', i)}",
                "type": "Rule",
                "pack_id": pid,
                "pack_version": pack["version"],
                "field": field,
                "source": entry["source"],
                "confidence": entry["confidence"],
                "rule": entry,
            })
    return nodes


def merge(graph_dir, owner_field, owners, new_nodes, new_edges=()):
    """Replace what `owners` loaded before (nodes and edges whose owner_field is
    in owners) with new_nodes and new_edges. Nodes with an id already in the
    graph from another owner (Language nodes) are shared, not duplicated.
    Returns a list of errors; nothing is written if there are any."""
    graph_dir = Path(graph_dir)
    nodes = [n for n in read_jsonl(graph_dir / "nodes.jsonl") if n.get(owner_field) not in owners]
    edges = [e for e in read_jsonl(graph_dir / "edges.jsonl") if e.get(owner_field) not in owners]
    known = {n["id"] for n in nodes}
    for node in new_nodes:
        if node["id"] not in known:
            nodes.append(node)
            known.add(node["id"])
    edges.extend(new_edges)

    errors = validate_graph(nodes, edges)
    if errors:
        return errors
    for name, items in (("nodes.jsonl", nodes), ("edges.jsonl", edges)):
        items.sort(key=lambda item: item["id"])
        with (graph_dir / name).open("w", encoding="utf-8") as f:
            for item in items:
                f.write(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n")
    return []


def load(packs, graph_dir):
    """Merge packs into graph_dir; return a list of errors (nothing is written if any)."""
    errors = [e for pack in packs for e in validate_pack(pack)]
    if errors:
        return errors
    nodes = [node for pack in packs for node in pack_to_nodes(pack)]
    return merge(graph_dir, "pack_id", {pack["pack_id"] for pack in packs}, nodes)


if __name__ == "__main__":
    args = sys.argv[1:]
    graph = "data/graph"
    if "--graph" in args:
        i = args.index("--graph")
        graph = args[i + 1]
        del args[i:i + 2]
    packs = []
    for path in args:
        with open(path, encoding="utf-8") as f:
            pack = json.load(f)
        if pack.get("pack_id") != TEMPLATE_ID:
            packs.append(pack)
    problems = load(packs, graph)
    print("\n".join(problems) or f"{len(packs)} pack(s) loaded into {graph}")
    sys.exit(1 if problems else 0)
