"""Week 6 "done when": a sample of 300 pairs gets a human check (BENCHMARK_PROTOCOL.md §8).

Draws a reproducible, stratified sample of pairs from the DEV split of a built benchmark
(never test or holdout) and writes two files:
- pairs.json: what the reviewer sees, as a caseworker would (no answers; no internal fields
  such as who wrote a name or how, which would give the answer away);
- key.jsonl: the gold answer and the stratum of each pair, kept locally for the comparison;
- pair-check.html: the review page (human_check_page.html with pairs.json embedded), published as
  a private claude.ai artifact whose answers are read back for the comparison.

Strata: 110 same-person record pairs, 30 tracing request vs the sought person's record,
50 relatives (different people, same family), 60 look-alikes (hard negatives), 50 different
families of the same origin sharing a name element. Pair order is shuffled.

Run: python -m namebridge.benchmark.human_check [--build build/benchmark] [--out build/benchmark/human_check]
     python -m namebridge.benchmark.human_check --compare <dir with answers/*.json from ArtifactData>
"""

import json
import random
import sys
from collections import defaultdict
from pathlib import Path

from namebridge.benchmark.world import ROOT

STRATA = {"same_person": 110, "request_vs_record": 30, "relatives": 50, "lookalike": 60, "shared_element": 50}
SEED = 20261117
SHOWN = ("source", "record_year", "name", "sex", "age_or_birth", "province_of_origin", "claimed_origin")


def _read(path):
    return [json.loads(line) for line in Path(path).read_text(encoding="utf-8").splitlines()]


def shown_record(r):
    return {"kind": "record", **{k: r.get(k) for k in SHOWN}}


def shown_query(q):
    s = q["sought"]
    return {"kind": "request", "record_year": q["record_year"], "relationship_said": q["relationship_said"],
            "requester_is_child": q["requester"]["is_child"], "name": s["name"], "sex": s["sex"],
            "age_or_birth": {"age_about": s["age_about"], "at_year": q["record_year"]} if s["age_about"] is not None else None,
            "province_of_origin": s["province_of_origin"]}


def sample(build, seed=SEED):
    build = Path(build)
    rng = random.Random(seed)
    people = {p["id"]: p for p in _read(build / "gold" / "people.jsonl")}
    public = {r["record_id"]: r for r in _read(build / "public" / "records.jsonl")}
    gold_rec = [g for g in _read(build / "gold" / "records.jsonl") if g["split"] == "dev" and g["searchable"]]
    by_person = defaultdict(list)
    for g in gold_rec:
        by_person[g["person"]].append(g["record_id"])
    one = {pid: recs[0] for pid, recs in by_person.items()}
    pairs = []

    def add(stratum, a, b, answer, extra=None):
        pairs.append({"stratum": stratum, "a": a, "b": b, "answer": answer, **(extra or {})})

    multi = sorted(pid for pid, recs in by_person.items() if len(recs) >= 2)
    for pid in rng.sample(multi, STRATA["same_person"]):
        a, b = rng.sample(by_person[pid], 2)
        add("same_person", shown_record(public[a]), shown_record(public[b]), "same", {"records": [a, b], "person": pid})

    queries = {q["query_id"]: q for q in _read(build / "public" / "queries.jsonl")}
    found = [g for g in _read(build / "gold" / "queries.jsonl")
             if g.get("split") == "dev" and g["expected"] == "found" and g["sought_person"] in by_person]
    for g in rng.sample(sorted(found, key=lambda x: x["query_id"]), STRATA["request_vs_record"]):
        r = rng.choice(by_person[g["sought_person"]])
        add("request_vs_record", shown_query(queries[g["query_id"]]), shown_record(public[r]), "same",
            {"query": g["query_id"], "record": r, "person": g["sought_person"]})

    rel = [x for x in _read(build / "gold" / "relations.jsonl") if x["a"] in one and x["b"] in one]
    for x in rng.sample(sorted(rel, key=lambda x: (x["a"], x["b"])), STRATA["relatives"]):
        add("relatives", shown_record(public[one[x["a"]]]), shown_record(public[one[x["b"]]]), "different",
            {"relation": x["relation"], "people": [x["a"], x["b"]]})

    looks = [h for h in _read(build / "gold" / "hard_negatives.jsonl") if h["a"] in one and h["b"] in one]
    for h in rng.sample(sorted(looks, key=lambda x: x["a"]), min(STRATA["lookalike"], len(looks))):
        add("lookalike", shown_record(public[one[h["a"]]]), shown_record(public[one[h["b"]]]), "different",
            {"same_name": h["same_name"], "people": [h["a"], h["b"]]})

    by_token = defaultdict(list)
    for pid, rid in one.items():
        for tok in public[rid]["name"].lower().split():
            if len(tok) > 3:
                by_token[(people[pid]["origin"], tok)].append(pid)
    keys = sorted(k for k, v in by_token.items() if len({people[p]["family"] for p in v}) >= 2)
    got, seen = 0, set()
    while got < STRATA["shared_element"]:
        a, b = rng.sample(by_token[rng.choice(keys)], 2)
        if people[a]["family"] == people[b]["family"] or (a, b) in seen or "lookalike_of" in people[a]:
            continue
        seen.add((a, b))
        add("shared_element", shown_record(public[one[a]]), shown_record(public[one[b]]), "different", {"people": [a, b]})
        got += 1

    rng.shuffle(pairs)
    for i, p in enumerate(pairs, 1):
        p["pair_id"] = f"h{i:03d}"
    return pairs


def write(pairs, out):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    shown = [{"pair_id": p["pair_id"], "a": p["a"], "b": p["b"]} for p in pairs]
    (out / "pairs.json").write_text(json.dumps(shown, ensure_ascii=False), encoding="utf-8")
    template = (Path(__file__).with_name("human_check_page.html")).read_text(encoding="utf-8")
    embedded = json.dumps(shown, ensure_ascii=False).replace("</", "<\\/")
    (out / "pair-check.html").write_text(template.replace("__PAIRS__", embedded), encoding="utf-8")
    with open(out / "key.jsonl", "w", encoding="utf-8") as f:
        for p in pairs:
            f.write(json.dumps({k: v for k, v in p.items() if k not in ("a", "b")}, ensure_ascii=False) + "\n")
    return len(shown)


def compare(key_path, answers_dir):
    """Agreement between the reviewer's answers (one JSON file per pair, as ArtifactData saves
    them under <answers_dir>/answers/) and the gold key, overall and per stratum."""
    key = {k["pair_id"]: k for k in _read(key_path)}
    answers = {}
    for f in sorted((Path(answers_dir) / "answers").glob("*.json")):
        body = json.loads(f.read_text(encoding="utf-8"))
        answers[f.stem] = body.get("data", body)
    rows = defaultdict(lambda: {"answered": 0, "agree": 0, "disagree": 0, "unsure": 0, "unrealistic": 0})
    disagreements = []
    for pid, a in answers.items():
        if pid not in key or not a.get("answer"):
            continue
        k = key[pid]
        for s in (k["stratum"], "all"):
            r = rows[s]
            r["answered"] += 1
            r["unrealistic"] += bool(a.get("unrealistic"))
            if a["answer"] == "unsure":
                r["unsure"] += 1
            elif a["answer"] == k["answer"]:
                r["agree"] += 1
            else:
                r["disagree"] += 1
        if a["answer"] not in ("unsure", k["answer"]) or a.get("unrealistic"):
            disagreements.append({"pair_id": pid, "stratum": k["stratum"], "gold": k["answer"], "reviewer": a["answer"],
                                  "unrealistic": bool(a.get("unrealistic")), "note": a.get("note", "")})
    for r in rows.values():
        decided = r["agree"] + r["disagree"]
        r["agreement_when_decided"] = round(r["agree"] / decided, 3) if decided else None
    return {"per_stratum": dict(rows), "to_review": disagreements}


def main(argv):
    opt = lambda flag, default=None: argv[argv.index(flag) + 1] if flag in argv else default
    build = opt("--build", ROOT / "build" / "benchmark")
    if "--compare" in argv:
        print(json.dumps(compare(Path(build) / "human_check" / "key.jsonl", opt("--compare")), ensure_ascii=False, indent=2))
        return
    n = write(sample(build), opt("--out", Path(build) / "human_check"))
    print(f"{n} pairs written")


if __name__ == "__main__":
    main(sys.argv[1:])
