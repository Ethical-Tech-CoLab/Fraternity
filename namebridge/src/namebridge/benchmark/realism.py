"""Synthetic world, step 4: realism checks before the freeze (week 6; BENCHMARK_PROTOCOL.md §2.4).

1. Fidelity test: synthetic names vs the naming profiles, by Jensen-Shannon divergence, against
   limits fixed and committed BEFORE the first comparison (params realism_limits, commit 4614adc).
   Checks against independent evidence (DRC corpus-wide n-grams and lengths, which the generator
   never saw) are separated from checks that hold by construction (they only test the code).
2. Copy test (protocol, changed 9 Nov 2026): the share of synthetic full names built ONLY from
   listed (top-frequency) elements, reported with the invention rate. No real full name is held,
   so no synthetic name can be compared with one; common-element combinations will coincide with
   real names by chance, which is expected.

Only numbers leave this module. Run: python -m namebridge.benchmark.realism [--people N]
"""

import json
import sys
from collections import Counter
from math import log2

from namebridge.benchmark.world import PARAMS, World, _load, full_name


def jsd(p, q):
    """Jensen-Shannon divergence (base 2) between two count dicts, over the union of keys."""
    keys = set(p) | set(q)
    sp, sq = sum(p.values()) or 1, sum(q.values()) or 1
    P = {k: p.get(k, 0) / sp for k in keys}
    Q = {k: q.get(k, 0) / sq for k in keys}
    M = {k: (P[k] + Q[k]) / 2 for k in keys}
    kl = lambda A: sum(A[k] * log2(A[k] / M[k]) for k in keys if A[k] > 0)
    return (kl(P) + kl(Q)) / 2


def ngrams(words, n, only=None):
    c = Counter()
    for w in words:
        for i in range(len(w) - n + 1):
            g = w[i:i + n]
            if only is None or g in only:
                c[g] += 1
    return c


def _restrict(counts, keys):
    return {k: counts.get(k, 0) for k in keys}


def fidelity(world, limits):
    base = [p for p in world.people if "lookalike_of" not in p]
    cd = _load("cd-congonames-2026.1.json")
    res = {}

    def put(key, value, limit, kind, detail=None):
        res[key] = {"value": round(value, 4), "limit": limit, "kind": kind, "pass": value <= limit, **(detail or {})}

    cd_people = [p for p in base if p["origin"] == "CD"]
    native = [e["text"] for p in cd_people for e in p["name"] if e["slot"] in ("nom", "postnom")]
    given = [e["text"] for p in cd_people for e in p["name"] if e["slot"] == "christian"]
    for key, words, table, n in (("F1_cd_native_trigrams", native, "probable_native_ngrams_3", 3),
                                 ("F2_cd_native_bigrams", native, "probable_native_ngrams_2", 2),
                                 ("F3_cd_given_trigrams", given, "probable_surname_ngrams_3", 3)):
        ref = {r["ngram"]: r["count"] for r in cd["ngrams"][table]}
        syn = ngrams(words, n, set(ref))
        put(key, jsd(syn, ref), limits[key]["limit"], limits[key]["kind"],
            {"largest_gaps": [g for g in sorted(ref, key=lambda g: -abs(syn.get(g, 0) / max(1, sum(syn.values()))
                                                                         - ref[g] / sum(ref.values())))[:5]]})
    lengths = sorted(len(full_name(p)) for p in cd_people)
    mean = sum(lengths) / len(lengths)
    p90 = lengths[int(0.9 * (len(lengths) - 1))]
    gap = max(abs(mean - cd["structure"]["chars"]["mean_chars"]), abs(p90 - cd["structure"]["chars"]["p90_chars"]))
    put("F4_cd_length", gap, limits["F4_cd_length"]["limit_chars"], "independent",
        {"synthetic_mean": round(mean, 2), "synthetic_p90": p90, "corpus_mean": cd["structure"]["chars"]["mean_chars"],
         "corpus_p90": cd["structure"]["chars"]["p90_chars"]})
    tok = Counter(min(4, len(p["name"])) for p in cd_people)
    ref_tok = Counter()
    for k, v in cd["structure"]["token_count_distribution"].items():
        if k.isdigit() and int(k) >= 2:
            ref_tok[min(4, int(k))] += v
    put("F5_cd_token_count", jsd(tok, ref_tok), limits["F5_cd_token_count"]["limit"], "by_construction")

    worst, details = 0.0, {}
    for (origin, slot, sex), pool in world.pools.items():
        if origin == "ALL" or sex is None:
            continue
        drawn = Counter(e["text"] for p in base if p["origin"] == origin and p["sex"] == sex
                        for e in p["name"] if e["basis"] == "profile" and e.get("source") == pool.source
                        and e["slot"] == slot.replace("_young", ""))
        if (slot == "christian") or sum(drawn.values()) < 200:
            continue  # Christian slots mix profile and corridor pool; small pools are noise
        ref = Counter()
        for e, w in pool.items:  # the newborn lists repeat names (two years; INEZA twice in 2024): sum them
            ref[e] += w
        value = jsd(_restrict(drawn, ref), ref)
        details[f"{origin}/{slot}/{sex}"] = round(value, 4)
        worst = max(worst, value)
    put("F6_listed_element_frequencies", worst, limits["F6_listed_element_frequencies"]["limit"], "by_construction",
        {"per_pool": details})

    worst, details = 0.0, {}
    for origin, ref in world.provinces.items():
        fams = Counter(f["province_of_origin"] for f in world.families if f["origin"] == origin and not f.get("lookalike_of"))
        details[origin] = round(jsd(fams, ref), 4)
        worst = max(worst, details[origin])
    put("F7_provinces", worst, limits["F7_provinces"]["limit"], "by_construction", {"per_origin": details})

    bi = Counter(sum(e["slot"] == "christian" for e in p["name"]) for p in base if p["origin"] == "BI")
    bi_ref = {int(k): v for k, v in world.p["bi_prenom_tokens"]["value"].items()}
    rw = Counter(len(p["name"]) for p in base if p["origin"] == "RW")
    rw_ref = Counter()
    for k, v in world.p["rw_names_per_person"]["value"].items():
        rw_ref[min(3, int(k))] += v
    value = max(jsd(bi, bi_ref), jsd(rw, rw_ref))
    put("F8_structure", value, limits["F8_structure"]["limit"], "by_construction",
        {"bi_prenom_tokens": round(jsd(bi, bi_ref), 4), "rw_names_per_person": round(jsd(rw, rw_ref), 4)})

    worst, details = 0.0, {}
    for origin, slot in (("RW", "kinyarwanda"), ("BI", "kirundi")):
        inv = [e["text"] for p in base if p["origin"] == origin for e in p["name"]
               if e["basis"] == "invented" and e["slot"] == slot]
        listed = Counter()
        for (o, s, _), pool in world.pools.items():
            if o == origin and s.replace("_young", "") == slot:
                for e, w in pool.items:
                    for i in range(len(e) - 2):
                        listed[e[i:i + 3]] += w
        value = jsd(ngrams(inv, 3), listed)
        details[f"{origin}/{slot}"] = round(value, 4)
        worst = max(worst, value)
    put("F9_invented_trigrams", worst, limits["F9_invented_trigrams"]["limit"], "partly_circular", {"per_slot": details})
    return res


def copy_test(world):
    """Share of synthetic full names made only of listed elements, and the invention rate (per origin)."""
    out = {}
    base = [p for p in world.people if "lookalike_of" not in p]
    for origin in ("RW", "BI", "CD"):
        ps = [p for p in base if p["origin"] == origin]
        only_listed = sum(all(e["basis"] in ("profile", "corridor_pool", "inherited") and e["basis"] != "invented"
                              for e in p["name"]) for p in ps)
        elems = [e for p in ps for e in p["name"]]
        names = Counter(full_name(p) for p in ps)
        out[origin] = {
            "people": len(ps),
            "full_names_only_listed_elements": round(only_listed / len(ps), 3),
            "invented_element_rate": round(sum(e["basis"] == "invented" for e in elems) / len(elems), 3),
            "synthetic_full_names_shared_by_2plus": round(sum(c for c in names.values() if c > 1) / len(ps), 3),
        }
    return out


def run(params, people=None):
    world = World(params, people=people).generate()
    limits = params["realism_limits"]["checks"]
    fid = fidelity(world, limits)
    return {"limits_fixed_on": params["realism_limits"]["fixed_on"], "fidelity": fid,
            "all_pass": all(v["pass"] for v in fid.values()), "copy_test": copy_test(world)}


def main(argv):
    opt = lambda flag, default=None: argv[argv.index(flag) + 1] if flag in argv else default
    params = json.loads(PARAMS.read_text(encoding="utf-8"))
    people = opt("--people")
    result = run(params, int(people) if people else None)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if not result["all_pass"]:
        sys.exit("fidelity test failed: correct the generator (BENCHMARK_PROTOCOL.md §2.4), do not move the limits")


if __name__ == "__main__":
    main(sys.argv[1:])
