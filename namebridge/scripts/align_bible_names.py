"""Propose forms of biblical names that are not book titles, by count alignment across translations.

For each person, a passage where they are the main character is chosen (Joseph: Genesis 37-50).
The English seed name is counted there; in each other translation a candidate must pass TWO
tests: (1) its count in the same passage is within +-40% of the seed's, and (2) it looks like
the seed (Jaro-Winkler >= 0.6 after mapping j->y, ph->f, c->k, th->t, which these languages
use for the same sounds), since the names are cognates. Count alone picked wrong words
(Gideon -> "Madian", Rebekah -> "Tango"; review of 9 Nov 2026). Among passing candidates the
most similar wins. The result is statistical, not attested: forms enter as
'statistical', lower confidence, proposed, for human review. Ambiguous results (runner-up
within 10% of the winner's count) are reported and NOT written.

Inputs: ebible USFM zips (fraLSG engwebp swhulb lin nya) in <ebible-folder>; the Kinyarwanda
Bible PDF (rw-bibiliya-yera) as <rw-pdf>. Output: a proposals JSON for review.
Run: python scripts/align_bible_names.py <ebible-folder> <rw-pdf> <out.json>
"""
import collections, json, re, subprocess, sys, zipfile
from pathlib import Path

from namebridge.normalize import fold
from namebridge.similarity import jaro_winkler


def _shape(name):
    t = fold(name)
    for a, b in (("ph", "f"), ("th", "t"), ("j", "y"), ("c", "k"), ("q", "k")):
        t = t.replace(a, b)
    return t

TARGETS = [  # concept id, label, seed (English WEB), passages [(book, first, last)]
    ("ioseph", None, "Joseph", [("GEN", 37, 50)]),
    ("moshe", "Moses", "Moses", [("EXO", 3, 40)]),
    ("dawid", "David", "David", [("1SA", 16, 31)]),
    ("avraham", "Abraham", "Abraham", [("GEN", 17, 25)]),
    ("sarah", "Sarah", "Sarah", [("GEN", 17, 23)]),
    ("yitshaq", "Isaac", "Isaac", [("GEN", 24, 28)]),
    ("rivqah", "Rebekah", "Rebekah", [("GEN", 24, 27)]),
    ("yaakov", "Jacob (Hebrew Ya'aqov; distinct from the concept iakobos/James)", "Jacob", [("GEN", 28, 35)]),
    ("rahel", "Rachel", "Rachel", [("GEN", 29, 31)]),
    ("binyamin", "Benjamin", "Benjamin", [("GEN", 42, 45)]),
    ("noah", "Noah", "Noah", [("GEN", 6, 9)]),
    ("gidon", "Gideon", "Gideon", [("JDG", 6, 8)]),
    ("devorah", "Deborah", "Deborah", [("JDG", 4, 5)]),
    ("shimshon", "Samson", "Samson", [("JDG", 13, 16)]),
    ("eliyahu", "Elijah", "Elijah", [("1KI", 17, 19), ("2KI", 1, 2)]),
    ("elisha", "Elisha", "Elisha", [("2KI", 2, 8)]),
    ("shlomo", "Solomon", "Solomon", [("1KI", 1, 11)]),
    ("yehonatan", "Jonathan", "Jonathan", [("1SA", 14, 14), ("1SA", 18, 20)]),
    ("naomi", "Naomi", "Naomi", [("RUT", 1, 4)]),
    ("aharon", "Aaron", "Aaron", [("LEV", 8, 10)]),
    ("stephanos", "Stephen", "Stephen", [("ACT", 6, 7)]),
    ("barnabas", "Barnabas", "Barnabas", [("ACT", 11, 15)]),
    ("silas", "Silas", "Silas", [("ACT", 15, 17)]),
    ("lazaros", "Lazarus", "Lazarus", [("JHN", 11, 12)]),
    ("martha", "Martha", "Martha", [("LUK", 10, 10), ("JHN", 11, 12)]),
    ("kornelios", "Cornelius", "Cornelius", [("ACT", 10, 10)]),
]
STOP = {"God", "Yahweh", "Lord", "LORD", "Israel", "Egypt", "Dieu", "Éternel", "Seigneur", "Mungu", "Bwana", "Yahwe", "Nzambe", "Yawe", "Nkolo",
        "Mulungu", "Yehova", "Ambuye", "Chauta", "Imana", "Uwiteka", "Yesu", "Jésus", "Jesus", "Yezu", "Israël", "Isiraeli", "Egypte", "Égypte", "Misri"}
TRANS = {"fraLSG": "fr", "swhulb": "sw", "lin": "ln", "nya": "ny"}
RW_BOOKS = {"GEN": "Itangiriro", "EXO": "Kuva", "LEV": "Abalewi", "JDG": "ABACAMANZA", "RUT": "Rusi", "1SA": "1 Samweli",
            "1KI": "1 Abami", "2KI": "2 Abami", "LUK": "Luka", "JHN": "Yohana", "ACT": "Ibyakozwe n’intumwa"}
CAP = re.compile(r"\b([A-ZÀ-ÝŴ][a-zà-ÿŵ'’]+)")


def usfm_chapters(text):
    text = re.sub(r"\\w\s+([^|\\]+)\|[^\\]*\\w\*", r"\1", text)
    chapters, cur = {}, None
    for part in re.split(r"(\\c\s+\d+)", text):
        m = re.match(r"\\c\s+(\d+)", part)
        if m:
            cur = int(m.group(1)); chapters[cur] = ""
        elif cur is not None:
            chapters[cur] += re.sub(r"\\[a-z0-9]+\*?", " ", part)
    return chapters


def load_usfm(zpath):
    z, books = zipfile.ZipFile(zpath), {}
    for n in z.namelist():
        if n.lower().endswith((".usfm", ".sfm")):
            t = z.read(n).decode("utf-8", "ignore")
            m = re.search(r"\\id\s+(\w{3})", t)
            if m:
                books[m.group(1)] = usfm_chapters(t)
    return books


def load_rw(pdf):
    text = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True).stdout
    books, cur = collections.defaultdict(dict), None
    heads = {v: k for k, v in RW_BOOKS.items()}
    for line in text.splitlines():
        m = re.match(r"^\s*((?:[123] )?[A-ZÀ-Ý][\w’'\- ]{1,30}?) (\d{1,3})\s*$", line)
        if m and m.group(1).strip() in heads:
            cur = (heads[m.group(1).strip()], int(m.group(2))); books[cur[0]][cur[1]] = ""
        elif cur:
            books[cur[0]][cur[1]] += line + " "
    return books


def passage(books, spans):
    return " ".join(books.get(b, {}).get(c, "") for b, a, z in spans for c in range(a, z + 1))


folder, rw_pdf, out = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
en = load_usfm(folder / "engwebp.zip")
others = {lang: load_usfm(folder / f"{tid}.zip") for tid, lang in TRANS.items()}
others["rw"] = load_rw(rw_pdf)
proposals, report = [], []
for cid, label, seed, spans in TARGETS:
    seed_n = len(re.findall(rf"\b{seed}\b", passage(en, spans)))
    row = {"concept": cid, "seed": seed, "seed_count": seed_n, "forms": {}}
    for lang, books in others.items():
        counts = collections.Counter(w for w in CAP.findall(passage(books, spans)) if w not in STOP)
        cands = sorted(((-jaro_winkler(_shape(w), _shape(seed)), w, c) for w, c in counts.items()
                        if seed_n and 0.6 * seed_n <= c <= 1.4 * seed_n and jaro_winkler(_shape(w), _shape(seed)) >= 0.6))
        if not cands:
            row["forms"][lang] = {"status": "no candidate"}; continue
        sim, w, c = cands[0]
        rivals = [(w2, c2) for s2, w2, c2 in cands[1:] if abs(s2 - sim) <= 0.05]
        row["forms"][lang] = {"form": w, "count": c, "similarity": round(-sim, 3), "status": "ambiguous" if rivals else "ok", "rivals": rivals[:3]}
        if not rivals:
            proposals.append({"concept": cid, "label": label, "text": w, "lang": lang, "seed": seed, "seed_count": seed_n, "count": c, "similarity": round(-sim, 3),
                              "passages": spans})
    report.append(row)
Path(out).write_text(json.dumps({"report": report, "proposals": proposals}, ensure_ascii=False, indent=1), encoding="utf-8")
for r in report:
    print(f"{r['seed']:<10}{r['seed_count']:>4} | " + " | ".join(f"{l}:{v.get('form','-')}({v.get('count','')}){'?' if v['status']!='ok' else ''}" for l, v in r["forms"].items()))
