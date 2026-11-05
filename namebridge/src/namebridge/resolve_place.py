"""Resolve a place name as a person or a record gives it (week 4).

A child may say "Kamenge" (a commune of Bujumbura until the 2010s, a zone
today); a record may say "Butanyerera" (a province since 2025, made of the
old Kayanza, Kirundo and Ngozi). resolve() finds every place the name can
mean, then follows the place links of the graph both ways in time:

- later: renamed_to, merged_into, split_into, continues_as (old -> new);
- earlier: the same links backwards (new -> old);
- within: located_in, upwards, to give the larger units it lies in.

Each candidate comes with the path that explains it and a score: the
product of the step weights (the area share when the link records one, 0.5
for a partial link without a share, 1 otherwise). Names are compared folded:
case, accents, hyphens, spaces and prefixes such as "Quartier" or
"Province de" are ignored, so "Nyanza Lac" finds "Nyanza-Lac". A name that
means several places (Cibitoke, Byumba, Gihosha) returns all of them: the
caller, not this function, decides between them.

Run: python -m namebridge.resolve_place <name> [--country BI] [--graph data/graph]
"""

import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

from namebridge.schema.name_graph import PLACE_RELATIONS, read_jsonl

TEMPORAL = PLACE_RELATIONS - {"located_in"}
# On equal scores, a change over time explains more than containment.
_RANK = {"later": 0, "earlier": 1, "within": 2}
_PREFIX = re.compile(
    r"^(quartier|zone|commune|colline|province( d[eu]s?| de la| de l)?|ville de|city of|district of|"
    r"intara y|umujyi wa|akarere ka)\s+",
)


def fold(name):
    text = unicodedata.normalize("NFKD", str(name)).encode("ascii", "ignore").decode().lower()
    text = re.sub(r"[’'`]", " ", text).strip()
    text = _PREFIX.sub("", text)
    return re.sub(r"[^a-z0-9]", "", text)


class PlaceIndex:
    def __init__(self, graph_dir):
        graph_dir = Path(graph_dir)
        self.nodes = {n["id"]: n for n in read_jsonl(graph_dir / "nodes.jsonl") if n.get("type") == "Region"}
        self.by_name = defaultdict(set)
        for nid, node in self.nodes.items():
            for name in [node["name"]] + [o["name"] for o in node.get("other_names", [])]:
                self.by_name[fold(name)].add(nid)
        self.out, self.into = defaultdict(list), defaultdict(list)
        for edge in read_jsonl(graph_dir / "edges.jsonl"):
            if edge.get("relation_type") in PLACE_RELATIONS and edge["from"] in self.nodes and edge["to"] in self.nodes:
                self.out[edge["from"]].append(edge)
                self.into[edge["to"]].append(edge)

    def matches(self, name, country=None):
        found = self.by_name.get(fold(name), set())
        return sorted(n for n in found if country is None or self.nodes[n]["country"] == country)

    @staticmethod
    def _weight(edge):
        if edge.get("share") is not None:
            return float(edge["share"])
        return 0.5 if edge.get("partial") else 1.0

    def resolve(self, name, country=None, max_steps=4):
        """Every place the name can refer to, with the path and a score."""
        results = {}
        frontier = [(nid, 1.0, []) for nid in self.matches(name, country)]
        for nid, score, path in frontier:
            results[nid] = (score, path)
        for _ in range(max_steps):
            nxt = []
            for nid, score, path in frontier:
                steps = [(e, e["to"], "later") for e in self.out[nid] if e["relation_type"] in TEMPORAL]
                steps += [(e, e["from"], "earlier") for e in self.into[nid] if e["relation_type"] in TEMPORAL]
                steps += [(e, e["to"], "within") for e in self.out[nid] if e["relation_type"] == "located_in"]
                for edge, other, direction in steps:
                    # Do not reverse direction in time: "earlier" then "later" would
                    # jump to siblings (Kayanza -> Butanyerera -> Kirundo).
                    if path and {path[-1][1], direction} == {"earlier", "later"}:
                        continue
                    # After going up ("within"), only keep going up; and do not go up
                    # from a place reached backwards in time (Kayanza -> old Busiga
                    # -> Ngozi province is a chain of valid steps, but noise).
                    if path and path[-1][1] == "within" and direction != "within":
                        continue
                    if direction == "within" and any(s[1] == "earlier" for s in path):
                        continue
                    new_score = score * self._weight(edge)
                    old = results.get(other)
                    better = old is None or new_score > old[0] or (
                        new_score == old[0] and old[1] and _RANK[direction] < _RANK[old[1][-1][1]]
                    )
                    if better:
                        step = (edge["relation_type"], direction, other, edge.get("confidence_basis"))
                        results[other] = (new_score, path + [step])
                        nxt.append((other, new_score, path + [step]))
            frontier = nxt
        out = []
        for nid, (score, path) in results.items():
            node = self.nodes[nid]
            kind = "match" if not path else path[-1][1] if all(s[1] == path[-1][1] for s in path) else "mixed"
            out.append({
                "id": nid, "name": node["name"], "country": node["country"], "level": node["level"],
                "period": node["period"], "score": round(score, 3), "kind": kind,
                "derived": any(s[3] == "generated" for s in path),
                "path": [
                    f"{rel} ({direction}) -> {self.nodes[other]['name']} [{self.nodes[other]['level']}, {self.nodes[other]['period']}]"
                    for rel, direction, other, _ in path
                ],
            })
        order = {"match": 0, "later": 1, "earlier": 2, "mixed": 3, "within": 4}
        return sorted(out, key=lambda r: (order[r["kind"]], -r["score"], r["name"]))


if __name__ == "__main__":
    args = sys.argv[1:]
    graph, country = "data/graph", None
    for flag in ("--graph", "--country"):
        if flag in args:
            i = args.index(flag)
            value = args[i + 1]
            del args[i:i + 2]
            if flag == "--graph":
                graph = value
            else:
                country = value
    index = PlaceIndex(graph)
    for row in index.resolve(" ".join(args), country):
        derived = " [derived]" if row["derived"] else ""
        print(f"{row['kind']:8s} {row['score']:.2f} {row['country']} {row['level']:8s} {row['name']} ({row['period']}){derived}")
        for step in row["path"]:
            print(f"           {step}")
