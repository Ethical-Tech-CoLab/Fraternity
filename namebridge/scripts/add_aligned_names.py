"""Add pre-screened alignment proposals (scripts/align_bible_names.py) to the cross-pack dataset.

Forms enter with basis 'statistical' and confidence 0.4, proposed. Proposals rejected in the
author's pre-screen (9 Nov 2026) are listed in REJECTED with the reason; the pre-screen is not
a review in the sense of namebridge.review (no reviewer role is claimed).

Run: python scripts/add_aligned_names.py <align.json> data/crosspack/christian-names-2026.1.json
"""
import json, sys
from pathlib import Path

REJECTED = {
    ("eliyahu", "ln"): "'Elize' may be Elijah or Elisha, both in the passage",
    ("elisha", "fr"): "'Il' is a pronoun", ("elisha", "sw"): "'Israeli' is a people", ("elisha", "ny"): "'Israeli' is a people",
    ("stephanos", "fr"): "'Joseph' is another person", ("stephanos", "ln"): "'Isalaele' is a people",
    ("barnabas", "ln"): "'Bayuda' means 'the Jews'", ("silas", "fr"): "'Juifs' means 'Jews'", ("kornelios", "ln"): "'Molimo' means 'spirit'",
}
SRC = {"fr": ("ebible-fr-lsg-align", "https://ebible.org/details.php?id=fraLSG", "Louis Segond 1910 (public domain), ebible.org"),
       "sw": ("ebible-sw-ulb-align", "https://ebible.org/details.php?id=swhulb", "Swahili Unlocked Literal Bible (Door43, CC BY-SA 4.0), ebible.org"),
       "ln": ("ebible-ln-biblica-align", "https://ebible.org/details.php?id=lin", "Lingala Bible (Biblica, CC BY-SA 4.0), ebible.org"),
       "ny": ("ebible-ny-biblica-align", "https://ebible.org/details.php?id=nya", "Chichewa Bible (Biblica, CC BY-SA 4.0), ebible.org"),
       "rw": ("rw-bibiliya-yera-align", "https://abisezerano.com/wp-content/uploads/2018/06/bibiliya.pdf", "Bibiliya Yera (Kinyarwanda Bible), PDF")}
EN = ("ebible-en-web", "https://ebible.org/details.php?id=engwebp")

align = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
path = Path(sys.argv[2]); data = json.loads(path.read_text(encoding="utf-8"))
concepts = {c["id"]: c for c in data["concepts"]}
for lang, (sid, url, name) in SRC.items():
    data["sources"][sid] = {"name": name, "url": url, "language": lang,
                            "locator": "count alignment with the World English Bible in passages where the person is the main character (scripts/align_bible_names.py): similar count (+-40%) and similar spelling (Jaro-Winkler >= 0.6); statistical, pre-screened, not reviewed"}
added, skipped = 0, []
seeds = {}
for p in align["proposals"]:
    key = (p["concept"], p["lang"])
    if key in REJECTED:
        skipped.append((key, REJECTED[key])); continue
    c = concepts.get(p["concept"])
    if c is None:
        c = concepts[p["concept"]] = {"id": p["concept"], "label": p["label"], "forms": []}
        data["concepts"].append(c)
    seeds[p["concept"]] = p["seed"]
    if any(f["text"] == p["text"] and f["lang"] == p["lang"] for f in c["forms"]):
        continue
    c["forms"].append({"text": p["text"], "lang": p["lang"], "sources": [SRC[p["lang"]][0]], "basis": "statistical", "confidence": 0.4,
                       "evidence": f"{p['count']} occurrences vs {p['seed_count']} for '{p['seed']}' in {p['passages']}; similarity {p['similarity']}"})
    added += 1
for cid, seed in seeds.items():  # the English seed itself is the reference form
    c = concepts[cid]
    if not any(f["lang"] == "en" for f in c["forms"]):
        c["forms"].append({"text": seed, "lang": "en", "sources": [EN[0]], "basis": "statistical", "confidence": 0.4,
                           "evidence": "English reference form used for the alignment"})
        added += 1
v = data["version"].split("."); v[1] = str(int(v[1]) + 1); v[2] = "0"; data["version"] = ".".join(v)
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print({"forms_added": added, "rejected": len(skipped), "concepts": len(data["concepts"]), "version": data["version"]})
