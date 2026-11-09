"""Build the Burundi naming profile from CENI 2025 candidate lists (raw list, DR-1.2 + DR-1.7).

The lists contain an ethnicity column. This parser matches that column as an anonymous
token and NEVER stores, counts or prints it; residence is not kept either. Text is
extracted in memory (no text files on disk), no row is ever printed, and only aggregates
of elements seen 5 or more times are written. Delete the PDFs after running (same session).

Inputs (in the working folder): <PROVINCE>.pdf from
  https://www.ceniburundi.bi/wp-content/uploads/2025/02/<PROVINCE>-CANDIDATS-DEPUTES-2025.pdf
Run: python scripts/build_profile_ceni.py data/profiles/bi-ceni-2026.1.json BUJUMBURA BUTANYERERA ...
"""
import collections, hashlib, json, re, subprocess, sys

MIN = 5
TOKEN = re.compile(r"^[A-ZÀ-Ý][A-ZÀ-Ý'\-]*$")
# No · Nom · Prénom(s) · year (OCR may insert a space) · sex · <ethnicity: anonymous> · residence
ROW = re.compile(r"^\s*\d{1,3}\s+(?P<nom>\S+)\s+(?P<prenoms>.+?)\s+(?P<year>\d(?:\s?\d){3})\s+(?P<sex>[MF])\s+\S+\s+\S.*$")

out_path, provinces = sys.argv[1], sys.argv[2:]
nom = collections.Counter(); prenom = collections.Counter()
nom_by_sex = collections.Counter(); prenom_by_sex = collections.Counter()
nom_by_decade = collections.Counter()
n_prenoms = collections.Counter(); decades = collections.Counter(); sexes = collections.Counter()
by_province = collections.Counter(); stats = collections.Counter(); checks = {}

for prov in provinces:
    pdf = f"{prov}.pdf"
    checks[prov] = hashlib.sha256(open(pdf, "rb").read()).hexdigest()[:16]
    text = subprocess.run(["pdftotext", "-raw", pdf, "-"], capture_output=True, text=True).stdout
    for line in text.splitlines():
        m = ROW.match(line)
        if not m:
            continue
        year = int(m["year"].replace(" ", ""))
        toks = m["prenoms"].split()
        # Elements of 1-2 letters are dropped unseen: a shifted row could otherwise carry the
        # ethnicity code (one or two letters) into a name field (DR-1.7).
        short = [t for t in [m["nom"]] + toks if len(t) <= 2]
        if short:
            stats["rows_dropped_short_token"] += 1
            continue
        if not (1930 <= year <= 2007) or not TOKEN.match(m["nom"]) or not toks or not all(TOKEN.match(t) for t in toks):
            stats["rows_rejected_malformed"] += 1
            continue
        stats["rows_parsed"] += 1
        sex, dec = m["sex"], f"{year // 10 * 10}s"
        k = m["nom"].lower()
        nom[k] += 1; nom_by_sex[(k, sex)] += 1; nom_by_decade[(k, dec)] += 1
        for t in toks:
            prenom[t.lower()] += 1; prenom_by_sex[(t.lower(), sex)] += 1
        n_prenoms[len(toks)] += 1; decades[dec] += 1; sexes[sex] += 1; by_province[prov.lower()] += 1


def top(counter):
    return [{"element": e, "count": c} for e, c in counter.most_common() if c >= MIN]


profile = {
    "profile_id": "bi-ceni-2026.1", "version": "0.1.0", "origin": "BI", "confidence": "high",
    "method": ("Built from CENI 2025 deputy-candidate lists under DATA_RULES DR-1.2/DR-1.7: text read in memory, ethnicity and residence columns never stored, "
               "no row printed, only elements seen 5+ times kept; raw PDFs deleted in the same session (9 Nov 2026). Script: scripts/build_profile_ceni.py"),
    "sources": [{"name": f"CENI Burundi, Élection des Députés 2025, liste nominative définitive des candidats, province {p.title()}",
                 "url": f"https://www.ceniburundi.bi/wp-content/uploads/2025/02/{p}-CANDIDATS-DEPUTES-2025.pdf", "sha256_16": checks[p]} for p in provinces],
    "population_note": "Adult election candidates born mostly 1950s-2000s (political party members: more urban, more schooled, more male than the population); the closest available proxy for the refugees' generation",
    "structure": {"rows_parsed": stats["rows_parsed"], "rows_rejected_malformed": stats["rows_rejected_malformed"], "rows_dropped_short_token": stats["rows_dropped_short_token"],
                  "sex": dict(sexes), "birth_decade": dict(sorted(decades.items())),
                  "number_of_prenom_tokens": dict(sorted(n_prenoms.items())), "by_province": dict(by_province),
                  "order_observed": "Nom (Kirundi name) column first, Prénoms (mostly Christian/French or Muslim given names) second; both in capitals"},
    "elements": {"nom": top(nom), "prenom": top(prenom)},
    "elements_by_sex": {"nom": [{"element": e, "sex": s, "count": c} for (e, s), c in nom_by_sex.most_common() if c >= MIN],
                        "prenom": [{"element": e, "sex": s, "count": c} for (e, s), c in prenom_by_sex.most_common() if c >= MIN]},
    "nom_by_birth_decade": [{"element": e, "decade": d, "count": c} for (e, d), c in nom_by_decade.most_common() if c >= MIN],
    "never": "No ethnicity, clan or religion field or pattern; the source's ethnicity column is never read into any variable (DR-1.7; C12)",
}
json.dump(profile, open(out_path, "w"), ensure_ascii=False, indent=2)
open(out_path, "a").write("\n")
print({"parsed": stats["rows_parsed"], "rejected": stats["rows_rejected_malformed"], "dropped_short": stats["rows_dropped_short_token"], "noms_kept": len(profile["elements"]["nom"]),
       "prenoms_kept": len(profile["elements"]["prenom"]), "decades": profile["structure"]["birth_decade"], "sex": dict(sexes)})
