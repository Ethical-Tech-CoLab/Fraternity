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
# Second batch (9 Nov 2026): more common biblical names; run with "extra" as 4th argument.
EXTRA = [
    ("adam", "Adam", "Adam", [("GEN", 2, 5)]), ("hevel", "Abel", "Abel", [("GEN", 4, 4)]), ("qayin", "Cain", "Cain", [("GEN", 4, 4)]),
    ("lot", "Lot", "Lot", [("GEN", 13, 14), ("GEN", 19, 19)]), ("yishmael", "Ishmael", "Ishmael", [("GEN", 16, 17), ("GEN", 21, 21), ("GEN", 25, 25)]),
    ("esav", "Esau", "Esau", [("GEN", 25, 28), ("GEN", 32, 33), ("GEN", 36, 36)]), ("lavan", "Laban", "Laban", [("GEN", 29, 31)]),
    ("leah", "Leah", "Leah", [("GEN", 29, 30)]), ("dinah", "Dinah", "Dinah", [("GEN", 34, 34)]), ("yehudah", "Judah", "Judah", [("GEN", 38, 38), ("GEN", 43, 44)]),
    ("reuven", "Reuben", "Reuben", [("GEN", 37, 37), ("GEN", 42, 42)]), ("efrayim", "Ephraim", "Ephraim", [("GEN", 48, 48)]),
    ("menashe", "Manasseh", "Manasseh", [("GEN", 48, 48)]), ("miryam", "Miriam", "Miriam", [("NUM", 12, 12)]),
    ("kalev", "Caleb", "Caleb", [("JOS", 14, 15)]), ("rahav", "Rahab", "Rahab", [("JOS", 2, 2), ("JOS", 6, 6)]),
    ("boaz", "Boaz", "Boaz", [("RUT", 2, 4)]), ("hannah", "Hannah", "Hannah", [("1SA", 1, 2)]), ("eli", "Eli", "Eli", [("1SA", 1, 4)]),
    ("shaul", "Saul (king)", "Saul", [("1SA", 9, 15)]), ("yishai", "Jesse", "Jesse", [("1SA", 16, 17)]),
    ("golyat", "Goliath", "Goliath", [("1SA", 17, 17)]), ("avigayil", "Abigail", "Abigail", [("1SA", 25, 25)]),
    ("avshalom", "Absalom", "Absalom", [("2SA", 13, 18)]), ("natan", "Nathan", "Nathan", [("2SA", 7, 7), ("2SA", 12, 12)]),
    ("yoav", "Joab", "Joab", [("2SA", 2, 3), ("2SA", 18, 20)]), ("avner", "Abner", "Abner", [("2SA", 2, 3)]),
    ("rehavam", "Rehoboam", "Rehoboam", [("1KI", 12, 14)]), ("yarovam", "Jeroboam", "Jeroboam", [("1KI", 11, 14)]),
    ("ahav", "Ahab", "Ahab", [("1KI", 16, 22)]), ("izevel", "Jezebel", "Jezebel", [("1KI", 18, 21)]), ("naaman", "Naaman", "Naaman", [("2KI", 5, 5)]),
    ("hizqiyahu", "Hezekiah", "Hezekiah", [("2KI", 18, 20)]), ("yoshiyahu", "Josiah", "Josiah", [("2KI", 22, 23)]),
    ("mordekhai", "Mordecai", "Mordecai", [("EST", 2, 10)]), ("haman", "Haman", "Haman", [("EST", 3, 9)]),
    ("zerubbavel", "Zerubbabel", "Zerubbabel", [("EZR", 3, 5), ("HAG", 1, 2)]), ("nevukhadnetsar", "Nebuchadnezzar", "Nebuchadnezzar", [("DAN", 1, 4)]),
    ("elisheva", "Elizabeth", "Elizabeth", [("LUK", 1, 1)]), ("nikodemos", "Nicodemus", "Nicodemus", [("JHN", 3, 3), ("JHN", 7, 7), ("JHN", 19, 19)]),
    ("thomas", "Thomas", "Thomas", [("JHN", 11, 11), ("JHN", 14, 14), ("JHN", 20, 21)]), ("philippos", "Philip", "Philip", [("ACT", 8, 8), ("JHN", 1, 1), ("JHN", 6, 6), ("JHN", 12, 12), ("JHN", 14, 14)]),
    ("andreas", "Andrew", "Andrew", [("JHN", 1, 1), ("JHN", 6, 6), ("JHN", 12, 12)]), ("nathanael", "Nathanael", "Nathanael", [("JHN", 1, 1), ("JHN", 21, 21)]),
    ("ananias", "Ananias", "Ananias", [("ACT", 5, 5), ("ACT", 9, 9), ("ACT", 22, 23)]), ("apollos", "Apollos", "Apollos", [("ACT", 18, 19), ("1CO", 1, 4)]),
    ("priskilla", "Priscilla", "Priscilla", [("ACT", 18, 18)]), ("akylas", "Aquila", "Aquila", [("ACT", 18, 18)]),
    ("felix", "Felix", "Felix", [("ACT", 23, 25)]), ("festos", "Festus", "Festus", [("ACT", 24, 26)]), ("zakchaios", "Zacchaeus", "Zacchaeus", [("LUK", 19, 19)]),
    ("tabitha", "Tabitha / Dorcas", "Dorcas", [("ACT", 9, 9)]),
]
STOP = {"God", "Yahweh", "Lord", "LORD", "Israel", "Egypt", "Dieu", "Éternel", "Seigneur", "Mungu", "Bwana", "Yahwe", "Nzambe", "Yawe", "Nkolo",
        "Mulungu", "Yehova", "Ambuye", "Chauta", "Imana", "Uwiteka", "Yesu", "Jésus", "Jesus", "Yezu", "Israël", "Isiraeli", "Egypte", "Égypte", "Misri"}
TRANS = {"fraLSG": "fr", "swhulb": "sw", "lin": "ln", "nya": "ny"}
RW_BOOKS = {"GEN": "Itangiriro", "EXO": "Kuva", "LEV": "Abalewi", "NUM": "Kubara", "JOS": "Yosuwa", "JDG": "ABACAMANZA", "RUT": "Rusi",
            "1SA": "1 Samweli", "2SA": "2 Samweli", "1KI": "1 Abami", "2KI": "2 Abami", "EZR": "Ezira", "EST": "Esiteri", "DAN": "Daniyeli",
            "HAG": "Hagayi", "LUK": "Luka", "JHN": "Yohana", "ACT": "Ibyakozwe n’intumwa", "1CO": "1 Abakorinto"}
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
if len(sys.argv) > 4 and sys.argv[4] == "extra":
    TARGETS = EXTRA
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
