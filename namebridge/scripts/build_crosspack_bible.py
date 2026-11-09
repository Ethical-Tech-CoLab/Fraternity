"""Extend the cross-pack Christian-names dataset from openly licensed Bible translations.

Each Bible book named after a person has a fixed book id (JHN, MAT, RUT ...); the book's
running header (USFM \\h) in a translation therefore gives that person's name in that
language, without guessing. Translations (ebible.org USFM zips, run in the folder holding them):
  fraLSG  French Louis Segond 1910 (public domain)
  engwebp World English Bible (public domain)
  swhulb  Swahili Unlocked Literal Bible (Door43, CC BY-SA 4.0)
  lin     Lingala Bible (Biblica, CC BY-SA 4.0)
  nya     Chichewa Bible (Biblica, CC BY-SA 4.0)
Kinyarwanda forms are the first-chapter headings of Bibiliya Yera (PDF already cited as
rw-bibiliya-yera); Timoteyo, whose book heading is missing from that PDF, is taken from
Ibyakozwe 16:1 ("umwigishwa witwaga Timoteyo"). Only individual names (facts) are taken,
not text, so the dataset stays CC BY 4.0 with attribution.

Run: python scripts/build_crosspack_bible.py <folder-with-zips> data/crosspack/christian-names-2026.1.json
"""
import json, re, sys, zipfile
from pathlib import Path

folder, dataset_path = Path(sys.argv[1]), Path(sys.argv[2])
TRANSLATIONS = {
    "fraLSG": ("fr", "ebible-fr-lsg", "Louis Segond 1910 (public domain), USFM edition from ebible.org", "https://ebible.org/details.php?id=fraLSG"),
    "engwebp": ("en", "ebible-en-web", "World English Bible (public domain), USFM edition from ebible.org", "https://ebible.org/details.php?id=engwebp"),
    "swhulb": ("sw", "ebible-sw-ulb", "Swahili Unlocked Literal Bible (Door43 World Missions Community, CC BY-SA 4.0), ebible.org", "https://ebible.org/details.php?id=swhulb"),
    "lin": ("ln", "ebible-ln-biblica", "Lingala Bible (Biblica, Inc., 2020, CC BY-SA 4.0), ebible.org", "https://ebible.org/details.php?id=lin"),
    "nya": ("ny", "ebible-ny-biblica", "Chichewa Bible (Biblica, Inc., 2002/2016, CC BY-SA 4.0), ebible.org", "https://ebible.org/details.php?id=nya"),
}
# book id -> (concept id, label); concepts that already exist are extended, not duplicated
BOOKS = {
    "MAT": ("matthaios", None), "MRK": ("markos", None), "LUK": ("loukas", None), "JHN": ("iohannes", None),
    "1PE": ("petros", None), "JAS": ("iakobos", None), "JUD": ("ioudas", None),
    "JOS": ("yehoshua", "Joshua (Hebrew Yehoshua)"), "RUT": ("rut", "Ruth"), "1SA": ("shemuel", "Samuel"),
    "EZR": ("ezra", "Ezra"), "NEH": ("nehemyah", "Nehemiah"), "EST": ("ester", "Esther"), "JOB": ("iyyov", "Job"),
    "ISA": ("yeshayahu", "Isaiah"), "JER": ("yirmeyahu", "Jeremiah"), "EZK": ("yehezkel", "Ezekiel"), "DAN": ("daniel", "Daniel"),
    "HOS": ("hoshea", "Hosea"), "JOL": ("yoel", "Joel"), "AMO": ("amos", "Amos"), "OBA": ("ovadyah", "Obadiah"),
    "JON": ("yonah", "Jonah"), "MIC": ("mikhah", "Micah"), "NAM": ("nahum", "Nahum"), "HAB": ("habaqquq", "Habakkuk"),
    "ZEP": ("tsefanyah", "Zephaniah"), "HAG": ("haggai", "Haggai"), "ZEC": ("zekharyah", "Zechariah"), "MAL": ("malakhi", "Malachi"),
    "1TI": ("timotheos", "Timothy"), "TIT": ("titos", "Titus"), "PHM": ("philemon", "Philemon"),
}
RW = {"JOS": "Yosuwa", "RUT": "Rusi", "1SA": "Samweli", "EZR": "Ezira", "NEH": "Nehemiya", "EST": "Esiteri", "JOB": "Yobu",
      "ISA": "Yesaya", "JER": "Yeremiya", "EZK": "Ezekiyeli", "DAN": "Daniyeli", "HOS": "Hoseya", "JOL": "Yoweli", "AMO": "Amosi",
      "OBA": "Obadiya", "JON": "Yona", "MIC": "Mika", "NAM": "Nahumu", "HAB": "Habakuki", "ZEP": "Zefaniya", "HAG": "Hagayi",
      "ZEC": "Zekariya", "MAL": "Malaki", "MAT": "Matayo", "MRK": "Mariko", "LUK": "Luka", "JHN": "Yohana", "TIT": "Tito",
      "PHM": "Filemoni", "JAS": "Yakobo", "1PE": "Petero", "JUD": "Yuda", "1TI": "Timoteyo"}

data = json.loads(dataset_path.read_text(encoding="utf-8"))
concepts = {c["id"]: c for c in data["concepts"]}
added_forms = added_sources = 0


def add(cid, label, text, lang, src):
    global added_forms, added_sources
    if cid not in concepts:
        concepts[cid] = {"id": cid, "label": label, "forms": []}
        data["concepts"].append(concepts[cid])
    for f in concepts[cid]["forms"]:
        if f["text"] == text and f["lang"] == lang:
            if src not in f["sources"]:
                f["sources"].append(src); added_sources += 1
            return
    concepts[cid]["forms"].append({"text": text, "lang": lang, "sources": [src]})
    added_forms += 1


for tid, (lang, src, name, url) in TRANSLATIONS.items():
    data["sources"][src] = {"name": name, "url": url, "locator": "running header (USFM \\h) of each book named after a person", "language": lang,
                            "note": "only individual names are taken (facts), not text"}
    z = zipfile.ZipFile(folder / f"{tid}.zip")
    for member in z.namelist():
        if not member.lower().endswith((".usfm", ".sfm")):
            continue
        head = z.read(member).decode("utf-8", "ignore")[:3000]
        bid, h = re.search(r"\\id\s+(\w{3})", head), re.search(r"\\h\s+(.+)", head)
        if bid and h and bid.group(1) in BOOKS:
            cid, label = BOOKS[bid.group(1)]
            text = re.sub(r"^\d\s*", "", h.group(1).strip())
            # Some headers are book titles, not names ("Waraka wa Yakobo" = Letter of James).
            text = re.sub(r"^(waraka wa|barua ya|kitabu cha|lettre de|épître de|epistle of|book of)\s+", "", text, flags=re.I).title()
            add(cid, label, text, lang, src)
data["sources"]["rw-bibiliya-yera"]["locator"] = (data["sources"]["rw-bibiliya-yera"].get("locator", "") +
    "; first-chapter headings of each book named after a person (read 9 Nov 2026); Timoteyo from Ibyakozwe 16:1").strip("; ")
for bid, text in RW.items():
    cid, label = BOOKS[bid]
    add(cid, label, text, "rw", "rw-bibiliya-yera")
v = data["version"].split("."); v[1] = str(int(v[1]) + 1); v[2] = "0"; data["version"] = ".".join(v)
dataset_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print({"concepts": len(data["concepts"]), "forms_added": added_forms, "sources_added_to_existing_forms": added_sources, "version": data["version"]})
