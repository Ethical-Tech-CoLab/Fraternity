"""Build contains_morpheme edges from frequent real names (profiles) to sourced name parts.

Only parts with a sourced meaning are used; names are elements seen 5+ times in the naming
profiles already in the repository. Segmentation is mechanical (substring at the stated
position), so edges have basis 'generated' and can never be reviewed (schema rule); they
explain shared parts, they are not variants.

Run: python scripts/build_morphemes.py data/variants/morphemes-2026.1.json
"""
import json, sys
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data"
MORPHEMES = [  # id, text, position, lang, meaning, source id
    ("imana", "imana", "end", "rw", "God (Imana)", "simbananiye"),
    ("imana-rn", "imana", "end", "rn", "God (Imana)", "simbananiye"),
    ("nyira", "nyira", "start", "rw", "feminine name-forming element", "kimenyi"),
    ("muka", "muka", "start", "rw", "feminine name-forming element", "kimenyi"),
    ("munya", "munya", "start", "rw", "masculine name-forming element", "kimenyi"),
    ("hungu", "hungu", "end", "rn", "boy (umuhungu)", "cox"),
]
SOURCES = {
    "simbananiye": {"name": "Simbananiye, L. (2005), 'Les noms de personnes au Burundi', Anthropologie et Sociétés 29(1): 167-181 (names addressed to Imana); Cox, Kirundi-English dictionary (Imana: God)", "url": "https://www.erudit.org/fr/revues/as/2005-v29-n1-as993/011745ar.pdf", "locator": "pp. 171-176", "language": "fr"},
    "kimenyi": {"name": "Kimenyi, A. (1978), 'Aspects of Naming in Kinyarwanda', Anthropological Linguistics 20(6): 258-271", "url": "https://www.jstor.org/stable/30027411", "locator": "pp. 261-262 (nyira-, mukaa-, munya-)", "language": "en"},
    "cox": {"name": "Cox, E. E. (1969, rev. M. Philipps 2023), Kirundi-English dictionary", "url": "https://www.matana.de/kirundi.pdf", "locator": "umuhūngu 'boy, son'", "language": "en"},
}
PROFILES = {"rn": [("bi-ceni-2026.1", ("nom",))], "rw": [("rw-nec-2026.1", ("first_position", "last_position", "middle_position")), ("rw-nisr-2026.1", None)]}

names = {"rn": set(), "rw": set()}
for lang, plist in PROFILES.items():
    for pid, keys in plist:
        p = json.loads((DATA / "profiles" / f"{pid}.json").read_text(encoding="utf-8"))
        for k, lst in p["elements"].items():
            if keys is None or k in keys:
                names[lang] |= {e["element"] for e in lst}
forms, relations, seen = [], [], set()
for mid, text, pos, lang, meaning, sid in MORPHEMES:
    forms.append({"id": mid, "text": text, "lang": lang, "type": "Morpheme", "meaning": meaning})
    for n in sorted(names[lang]):
        hit = n.endswith(text) if pos == "end" else n.startswith(text)
        if hit and n != text and len(n) > len(text) + 1:
            fid = f"{lang}-{n}"
            if fid not in seen:
                forms.append({"id": fid, "text": n.title(), "lang": lang}); seen.add(fid)
            relations.append({"from": fid, "to": mid, "relation_type": "contains_morpheme", "source": sid, "confidence": 0.7,
                              "confidence_basis": "generated", "regions": ["BI"] if lang == "rn" else ["RW"], "reversible": False})
out = {"dataset_id": "morphemes-2026.1", "version": "0.1.0",
       "description": "Frequent real names (elements seen 5+ times in the naming profiles) linked to name parts with a sourced meaning. Mechanical segmentation: basis 'generated', never reviewable; these edges explain shared parts and are not variants.",
       "sources": SOURCES, "forms": forms, "relations": relations}
Path(sys.argv[1]).write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print({"morphemes": len(MORPHEMES), "names": len(seen), "edges": len(relations)})
