"""Build a DERIVED Burundi naming profile (gate G6 basis, option (i) of 9 Nov 2026).

No Burundian list is read. The Rwanda profile (NISR published top-20 tables) is converted to
Kirundi spelling with the deterministic rw->rn rules of the bi-kirundi pack (Comparative
Grammar 2007, Table 1). The result is a hypothesis about Burundian names, marked as such;
an aggregator (Geneanet/Forebears) may be used only as a cross-check (G6).

Run: python scripts/build_profile_bi_derived.py data/profiles/bi-derived-2026.1.json
"""
import json, re, sys
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data"
rw = json.loads((DATA / "profiles" / "rw-nisr-2026.1.json").read_text(encoding="utf-8"))
pack = json.loads((DATA / "packs" / "bi-kirundi-2026.1.json").read_text(encoding="utf-8"))
rules = [(r["from"], r["to"], r["id"]) for r in pack["transliteration_rules"] if r.get("direction") == "rw->rn"]
# longest first, so "shy" is handled before any shorter overlap
rules.sort(key=lambda r: -len(r[0]))


def to_kirundi(name):
    applied = []
    for src, dst, rid in rules:
        if src in name:
            name = name.replace(src, dst)
            applied.append(rid)
    return name, applied


out = {"profile_id": "bi-derived-2026.1", "version": "0.1.0", "origin": "BI", "confidence": "medium",
       "method": ("DERIVED, not observed: the Kinyarwanda names of profile rw-nisr-2026.1 converted to Kirundi spelling with the bi-kirundi rw->rn rules "
                  f"({', '.join(r[2] for r in rules)}). Counts are the Rwandan counts, kept only as relative weights. Built 9 Nov 2026 by scripts/build_profile_bi_derived.py"),
       "sources": [{"name": "rw-nisr-2026.1 (NISR, Rwanda Vital Statistics Reports 2024 and 2025)"},
                   {"name": "Kinyarwanda and Kirundi Comparative Grammar (Zorc & Nibagwire, Dunwoody Press, 2007), §1.1.1, Table 1, via the bi-kirundi pack transliteration rules"}],
       "known_bias": ("Kirundi and Kinyarwanda share most name stock but not all; names specific to Burundi are missing, and Rwandan popularity is not Burundian popularity. "
                      "Newborns of 2024-2025, not the refugees' generation. To be checked against real Burundian frequencies (option (ii): CENI lists under DR-1)"),
       "elements": {}, "never": rw["never"]}
for key, lst in rw["elements"].items():
    conv = []
    for e in lst:
        k, applied = to_kirundi(e["element"])
        conv.append({"element": k, "count": e["count"], "from_kinyarwanda": e["element"], "rules": applied})
    out["elements"][key.replace("kinyarwanda_name", "derived_kirundi_name")] = conv
changed = sorted({(e["from_kinyarwanda"], e["element"]) for l in out["elements"].values() for e in l if e["rules"]})
out["converted_forms"] = [{"kinyarwanda": a, "kirundi": b} for a, b in changed]
json.dump(out, open(sys.argv[1], "w"), ensure_ascii=False, indent=2)
open(sys.argv[1], "a").write("\n")
print("converted:", changed)
