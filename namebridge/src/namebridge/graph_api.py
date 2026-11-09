"""Graph API: given a name, the typed paths to its variants, with confidence and sources (CONCEPT-IDEA.md §12).

This queries NAMES, never people: the public graph holds general naming knowledge only
(§5.1A), and a public reverse lookup of people is excluded (§12, "should not have").

- The query is normalised with namebridge.normalize (original kept, transform path returned).
- Variants are reached over equivalence-type edges (EQUIVALENCE_TYPES of the schema),
  through NameConcept nodes where forms share a concept (Jean -> John: Greek Iōannēs -> Yohana).
- Each variant comes with its best path: every step's relation type, confidence, basis,
  review status and source. Path confidence is the product of step confidences (conservative).
- not_equivalent_to edges are negative constraints: a variant they touch is removed and the
  constraint is reported. commonly_confused_with is reported separately, never as a variant.
- Ambiguous paths: when the query matches forms of more than one concept (Yakobo: James or
  Jacob), `ambiguous_between` lists the concepts and each variant names the concept it came
  through, so alternatives are not read as variants of each other.
- Deprecated edges are ignored. Nothing here confirms an identity (§5.6).

Run: python -m namebridge.graph_api "Yohana" [--graph data/graph] [--min-confidence 0.2]
"""

import heapq
import json
import sys
from collections import defaultdict
from pathlib import Path

from namebridge.normalize import forms as name_forms
from namebridge.schema.name_graph import EQUIVALENCE_TYPES, read_jsonl


class NameGraph:
    def __init__(self, graph_dir="data/graph"):
        graph_dir = Path(graph_dir)
        self.nodes = {n["id"]: n for n in read_jsonl(graph_dir / "nodes.jsonl") if n.get("type") in ("NameForm", "NameConcept")}
        self.adj = defaultdict(list)           # node -> [(neighbour, edge)] over equivalence edges
        self.negative = defaultdict(list)      # node -> [(other, edge)] not_equivalent_to
        self.confused = defaultdict(list)      # node -> [(other, edge)] commonly_confused_with
        for e in read_jsonl(graph_dir / "edges.jsonl"):
            if e.get("review_status") == "deprecated" or e["from"] not in self.nodes or e["to"] not in self.nodes:
                continue
            rel = e["relation_type"]
            if rel == "not_equivalent_to":
                self.negative[e["from"]].append((e["to"], e)); self.negative[e["to"]].append((e["from"], e))
            elif rel == "commonly_confused_with":
                self.confused[e["from"]].append((e["to"], e)); self.confused[e["to"]].append((e["from"], e))
            elif rel in EQUIVALENCE_TYPES:
                self.adj[e["from"]].append((e["to"], e))
                if e.get("reversible") is True:
                    self.adj[e["to"]].append((e["from"], e))
        self.by_folded = defaultdict(set)
        for nid, n in self.nodes.items():
            if n["type"] == "NameForm":
                f = name_forms(n["text"])
                for key in [f["folded"]] + f["variants"]:
                    self.by_folded[key].add(nid)

    def lookup(self, name):
        f = name_forms(name)
        found = set()
        for key in [f["folded"]] + f["variants"]:
            found |= self.by_folded.get(key, set())
        return f, sorted(found)

    @staticmethod
    def _step(node_from, node_to, e):
        return {"from": node_from, "to": node_to, "relation_type": e["relation_type"], "confidence": e["confidence"],
                "confidence_basis": e["confidence_basis"], "review_status": e["review_status"],
                "source_name": e["source_name"], "source_url": e["source_url"], "locator": e["source_excerpt_or_locator"], "edge": e["id"]}

    def variants(self, name, min_confidence=0.0, max_steps=4):
        query, starts = self.lookup(name)
        best = {s: (1.0, []) for s in starts}
        heap = [(-1.0, s) for s in starts]
        while heap:
            neg, node = heapq.heappop(heap)
            conf, path = best[node]
            if -neg < conf or len(path) >= max_steps:
                continue
            for nxt, e in self.adj[node]:
                c = conf * float(e["confidence"])
                if c < min_confidence or (nxt in best and best[nxt][0] >= c):
                    continue
                best[nxt] = (c, path + [self._step(node, nxt, e)])
                heapq.heappush(heap, (-c, nxt))

        blocked = {}
        for s in starts:
            for other, e in self.negative[s]:
                blocked[other] = e
        # Ambiguous paths: the query matches forms of more than one concept (Swahili "Yakobo" is
        # both James/Jacques and Jacob). Each variant then says which concept it came through.
        concept_of = {}
        for s in starts:
            for nxt, e in self.adj[s]:
                if self.nodes[nxt]["type"] == "NameConcept":
                    concept_of[s] = self.nodes[nxt]["label"]
        ambiguous = sorted(set(concept_of.values())) if len(set(concept_of.values())) > 1 else []
        results = []
        for nid, (conf, path) in best.items():
            n = self.nodes[nid]
            if nid in starts or n["type"] != "NameForm" or nid in blocked:
                continue
            item = {"form": n["text"], "languages": n.get("languages", []), "node": nid, "path_confidence": round(conf, 4), "path": path}
            if ambiguous:
                via = [self.nodes[st["to"]]["label"] for st in path if self.nodes[st["to"]]["type"] == "NameConcept"]
                item["via_concept"] = via[0] if via else None
            results.append(item)
        results.sort(key=lambda r: (-r["path_confidence"], r["form"]))
        return {
            "query": {"original": query["original"], "folded": query["folded"], "transform_path": query["path"]},
            "matched_forms": [{"node": s, "form": self.nodes[s]["text"], "languages": self.nodes[s].get("languages", [])} for s in starts],
            "ambiguous_between": ambiguous,
            "variants": results,
            "not_equivalent": [{"form": self.nodes[o]["text"], "node": o, **self._step(s, o, e)} for s in starts for o, e in self.negative[s]],
            "commonly_confused_with": [{"form": self.nodes[o]["text"], "node": o, **self._step(s, o, e)} for s in starts for o, e in self.confused[s]],
            "note": "Name knowledge only: variants are hypotheses for search, never confirmation of an identity (CONCEPT-IDEA.md §5.6)",
        }


if __name__ == "__main__":
    args = sys.argv[1:]
    graph, min_conf = "data/graph", 0.0
    if "--graph" in args:
        i = args.index("--graph"); graph = args[i + 1]; del args[i:i + 2]
    if "--min-confidence" in args:
        i = args.index("--min-confidence"); min_conf = float(args[i + 1]); del args[i:i + 2]
    if len(args) != 1:
        sys.exit(__doc__)
    print(json.dumps(NameGraph(graph).variants(args[0], min_confidence=min_conf), ensure_ascii=False, indent=2))
