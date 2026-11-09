"""Build the register of sources and licences for every source cited by graph edges.

Collected from the datasets' own source lists (places, cross-pack names, variants), not by
splitting edge text (some source names contain the separator). A licence is recorded only
where it was verified; otherwise "not stated", meaning only facts (names, dates, relations)
are used and no text is reproduced. Third-party copies of copyrighted works are flagged.

Run: python scripts/build_source_register.py data/register/sources.json
"""
import json, sys
from collections import defaultdict
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data"
VERIFIED = {  # url prefix -> (licence as stated by the source, how verified)
    "https://ebible.org/details.php?id=fraLSG": ("public domain", "copr.htm in the ebible.org USFM package, read 9 Nov 2026"),
    "https://ebible.org/details.php?id=engwebp": ("public domain", "copr.htm in the ebible.org USFM package, read 9 Nov 2026"),
    "https://ebible.org/details.php?id=swhulb": ("CC BY-SA 4.0", "copr.htm in the ebible.org USFM package, read 9 Nov 2026"),
    "https://ebible.org/details.php?id=lin": ("CC BY-SA 4.0", "copr.htm in the ebible.org USFM package, read 9 Nov 2026"),
    "https://ebible.org/details.php?id=nya": ("CC BY-SA 4.0", "copr.htm in the ebible.org USFM package, read 9 Nov 2026"),
    "https://data.humdata.org/dataset/cod-ab": ("CC BY-IGO", "HDX dataset page, recorded when the boundaries were loaded (5 Nov 2026)"),
    "https://doi.org/10.3390/data11070169": ("CC BY 4.0", "MDPI Data article licence; the authors' repository declares no licence (RESEARCH_LOG 9 Nov 2026)"),
    "https://worldfactbookarchive.org": ("public domain", "CIA World Factbook, a US government work"),
    "https://www.biblegateway.com/passage/?search=Matthieu": ("public domain", "Louis Segond 1910 text"),
    "https://www.bible.com/bible/1/": ("public domain", "King James Version text"),
    "https://www.bible.com/versions/1-kjv": ("public domain", "King James Version text"),
}
CONCERNS = {
    "https://dokumen.pub/": "third-party host of a copyrighted book; used only for a book-list snippet (Matayo, Mariko, Luka, Yohana). Not replaceable online (checked 9 Nov 2026: Cox's dictionary lacks them; bible.com blocks scripts); the same four spellings are attested for Kinyarwanda and Swahili by other sources, so no edge depends on this one. Official source to use when someone can read it: Société Biblique du Burundi, Bibiliya Yera (2015), also in its mobile app",
    "https://abisezerano.com/": "digital edition of Bibiliya Yera prepared by the volunteer group Grace Geeks (stated on its first page), hosted by a third party; whether the Bible Society of Rwanda authorised it is not verified; used only for names (facts)",
}
KIND = [("ebible.org", "religious text"), ("bible", "religious text"), ("biblafrique", "religious text"), ("open.bible", "religious text"),
        ("shepherdsglobal", "religious text"), ("harvestime", "religious text"), ("bibleproject", "religious text"),
        ("humdata", "UN / humanitarian data"), ("unocha", "UN / humanitarian report"), ("unicef", "UN / humanitarian report"),
        (".gov.", "government"), ("rwandalii", "government (legislation)"), ("ceniburundi", "government (electoral commission)"),
        ("statistics.gov.rw", "government (statistics)"), ("doi.org", "peer-reviewed publication"), ("kulib.kyoto", "peer-reviewed publication"),
        ("newtimes", "press"), ("breakingburundi", "press"), ("crisisgroup", "NGO report"), ("geoboundaries", "open geodata"),
        ("statoids", "reference site"), ("rulers.org", "reference site"), ("worldstatesmen", "reference site"), ("nationsonline", "reference site"),
        ("worldfactbook", "government (US)"), ("github.com/Ethical-Tech-CoLab", "NameBridge derived data"), ("dokumen.pub", "third-party copy")]

entries = defaultdict(lambda: {"datasets": set()})
for folder in ("places", "crosspack", "variants"):
    for path in sorted((DATA / folder).glob("*.json")):
        d = json.loads(path.read_text(encoding="utf-8"))
        for sid, s in d["sources"].items():
            e = entries[s["url"]]
            e.update({"url": s["url"], "name": s["name"], "language": s.get("language")})
            e["datasets"].add(d["dataset_id"])
out = []
for url, e in sorted(entries.items()):
    lic = next((v for k, v in VERIFIED.items() if url.startswith(k)), None)
    rec = {"url": url, "name": e["name"], "language": e["language"], "datasets": sorted(e["datasets"]),
           "kind": next((k for frag, k in KIND if frag in url), "other"),
           "licence": lic[0] if lic else "not stated", "licence_verified": bool(lic),
           "how_verified": lic[1] if lic else None,
           "use": "facts only (names, dates, relations and short locators); no text reproduced"}
    concern = next((v for k, v in CONCERNS.items() if url.startswith(k)), None)
    if concern:
        rec["concern"] = concern
    out.append(rec)
reg = {"register": "NameBridge source and licence register", "built": "by scripts/build_source_register.py", "sources": out,
       "summary": {"sources": len(out), "licence_verified": sum(r["licence_verified"] for r in out), "with_concern": sum("concern" in r for r in out)}}
Path(sys.argv[1]).write_text(json.dumps(reg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(reg["summary"])
