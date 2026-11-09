"""Review workflow for graph edges: proposed -> reviewed / deprecated (CONCEPT-IDEA.md §5.1A, §10 phase 1).

Loaders rebuild data/graph from the datasets, so review decisions cannot live in the graph
files. They are kept in an append-only log, data/reviews/reviews.jsonl, one decision per line:

  {"edge": <edge id>, "decision": "reviewed" | "deprecated" | "proposed",
   "reviewer": <name>, "reviewer_role": linguist | community_expert | investigator | data_steward,
   "date": "YYYY-MM-DD", "note": <reason>}

`apply_reviews` replays the log (the last decision per edge wins) and is called by the shared
loader merge, so every reload keeps the decisions. Decisions are made by people with a role,
never by a script or an AI assistant (DATA_RULES.md DR-1.5); a generated edge can never be
reviewed (the schema refuses it). A deprecated edge stays in the graph for the record and is
ignored by the graph API.

Run:
  python -m namebridge.review queue [--dataset <id>] [--limit 20]
  python -m namebridge.review record <edge-id> reviewed|deprecated --by <name> --role <role> --note "<reason>"
"""

import datetime
import json
import sys
from pathlib import Path

from namebridge.schema.name_graph import REVIEWER_ROLES, read_jsonl, validate_graph

DECISIONS = {"reviewed", "deprecated", "proposed"}


def reviews_path(graph_dir):
    return Path(graph_dir).resolve().parent / "reviews" / "reviews.jsonl"


def read_reviews(graph_dir):
    path = reviews_path(graph_dir)
    return read_jsonl(path) if path.exists() else []


def apply_reviews(edges, reviews):
    """Replay decisions onto edges in place (last decision per edge wins). Returns unknown edge ids."""
    latest = {}
    for r in reviews:
        latest[r["edge"]] = r
    by_id = {e["id"]: e for e in edges}
    for eid, r in latest.items():
        e = by_id.get(eid)
        if e is None:
            continue
        e["review_status"] = r["decision"]
        for k in ("reviewer_role", "reviewed_by", "reviewed_on", "review_note"):
            e.pop(k, None)
        if r["decision"] != "proposed":
            e.update({"reviewer_role": r["reviewer_role"], "reviewed_by": r["reviewer"],
                      "reviewed_on": r["date"], "review_note": r.get("note", "")})
    return sorted(set(latest) - set(by_id))


def check_decision(r):
    errors = []
    if r.get("decision") not in DECISIONS:
        errors.append(f"decision must be one of {sorted(DECISIONS)}")
    if r.get("decision") != "proposed":
        if r.get("reviewer_role") not in REVIEWER_ROLES:
            errors.append(f"reviewer_role must be one of {sorted(REVIEWER_ROLES)}")
        if not r.get("reviewer"):
            errors.append("a reviewer name is required")
        if not r.get("note"):
            errors.append("a note giving the reason is required")
    return errors


def record(graph_dir, decision):
    """Validate a decision against the current graph, then append it to the log and rewrite the graph."""
    errors = check_decision(decision)
    graph_dir = Path(graph_dir)
    nodes = read_jsonl(graph_dir / "nodes.jsonl")
    edges = read_jsonl(graph_dir / "edges.jsonl")
    if decision.get("edge") not in {e["id"] for e in edges}:
        errors.append(f"unknown edge {decision.get('edge')!r}")
    if errors:
        return errors
    log = read_reviews(graph_dir) + [decision]
    apply_reviews(edges, log)
    errors = validate_graph(nodes, edges)
    if errors:
        return errors
    path = reviews_path(graph_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(decision, ensure_ascii=False, sort_keys=True) + "\n")
    with (graph_dir / "edges.jsonl").open("w", encoding="utf-8") as f:
        for e in sorted(edges, key=lambda e: e["id"]):
            f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
    return []


def queue(graph_dir, dataset=None, limit=20):
    edges = [e for e in read_jsonl(Path(graph_dir) / "edges.jsonl")
             if e["review_status"] == "proposed" and (dataset is None or e.get("dataset_id") == dataset)]
    edges.sort(key=lambda e: (e["confidence_basis"] == "generated", -float(e["confidence"]), e["id"]))
    return [{"edge": e["id"], "relation": e["relation_type"], "from": e["from"], "to": e["to"], "confidence": e["confidence"],
             "basis": e["confidence_basis"], "source": e["source_name"][:120]} for e in edges[:limit]], len(edges)


if __name__ == "__main__":
    args, graph = sys.argv[1:], "data/graph"
    opt = lambda flag, default=None: args[args.index(flag) + 1] if flag in args else default
    if args[:1] == ["queue"]:
        items, total = queue(graph, opt("--dataset"), int(opt("--limit", 20)))
        print(json.dumps({"proposed_total": total, "shown": items}, ensure_ascii=False, indent=2))
    elif args[:1] == ["record"] and len(args) >= 3:
        d = {"edge": args[1], "decision": args[2], "reviewer": opt("--by"), "reviewer_role": opt("--role"),
             "date": datetime.date.today().isoformat(), "note": opt("--note", "")}
        problems = record(graph, d)
        print("\n".join(problems) or f"recorded: {args[2]} {args[1]}")
        sys.exit(1 if problems else 0)
    else:
        sys.exit(__doc__)
