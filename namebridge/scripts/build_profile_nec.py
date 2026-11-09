"""Build an adult Rwanda naming profile from NEC district-council candidate lists (raw list, DR-1.2).

Final candidate lists published by Rwanda's National Electoral Commission (31 Oct 2026), one PDF
per province. Columns: district, seat category, names, sex, approval mark; no ethnicity and no
date of birth. Text is read in memory, no row is printed, only elements seen 5+ times are kept,
and the PDFs are deleted after running (same session).

Inputs (in the working folder): <PROVINCE>.pdf from
  https://www.nec.gov.rw/fileadmin/user_upload/NEC/News_Images/URUTONDE_NDAKUKA_RW_ABAKANDIDA_<PROVINCE>.pdf
Run: python scripts/build_profile_nec.py data/profiles/rw-nec-2026.1.json AMAJYARUGURU AMAJYEPFO IBURASIRAZUBA IBURENGERAZUBA
"""
import collections, hashlib, json, re, subprocess, sys

MIN = 5
TOKEN = re.compile(r"^[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ'’\-]*$")
CATEGORIES = {"Rusange", "30%"}
out_path, provinces = sys.argv[1], sys.argv[2:]
pos = {k: collections.Counter() for k in ("first", "middle", "last")}
pos_sex = {k: collections.Counter() for k in ("first", "last")}
ntok = collections.Counter(); sexes = collections.Counter(); prov_n = collections.Counter(); stats = collections.Counter(); checks = {}

for prov in provinces:
    pdf = f"{prov}.pdf"
    checks[prov] = hashlib.sha256(open(pdf, "rb").read()).hexdigest()[:16]
    text = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True).stdout
    for line in text.splitlines():
        t = line.split()
        if len(t) < 5 or t[-1] != "YEGO":
            continue
        if t[1] not in CATEGORIES or t[-2] not in ("M", "F"):
            stats["rows_rejected_layout"] += 1
            continue
        names, sex = t[2:-2], t[-2]
        if len(names) < 1 or not all(TOKEN.match(n) and len(n) >= 2 for n in names):
            stats["rows_rejected_malformed"] += 1
            continue
        stats["rows_parsed"] += 1
        names = [n.lower().replace("’", "'") for n in names]
        pos["first"][names[0]] += 1; pos_sex["first"][(names[0], sex)] += 1
        if len(names) > 1:
            pos["last"][names[-1]] += 1; pos_sex["last"][(names[-1], sex)] += 1
        for n in names[1:-1]:
            pos["middle"][n] += 1
        ntok[len(names)] += 1; sexes[sex] += 1; prov_n[prov.lower()] += 1

top = lambda c: [{"element": e, "count": n} for e, n in c.most_common() if n >= MIN]
profile = {
    "profile_id": "rw-nec-2026.1", "version": "0.1.0", "origin": "RW", "confidence": "high",
    "method": ("Built from NEC final district-council candidate lists (31 Oct 2026) under DATA_RULES DR-1.2: text read in memory, no row printed, "
               "district and seat category not kept per person, only elements seen 5+ times; raw PDFs deleted in the same session (9 Nov 2026). Script: scripts/build_profile_nec.py"),
    "sources": [{"name": f"National Electoral Commission (NEC) Rwanda, Urutonde ndakuka rw'abakandida ku mwanya w'umujyanama mu nama njyanama y'Akarere, {p.title()}",
                 "url": f"https://www.nec.gov.rw/fileadmin/user_upload/NEC/News_Images/URUTONDE_NDAKUKA_RW_ABAKANDIDA_{p}.pdf", "sha256_16": checks[p]} for p in provinces],
    "population_note": "Adult candidates for district councils in four provinces (Kigali not included); no birth dates in the source, so no cohort breakdown. Candidates are more schooled and engaged than average; 30% seats are reserved for women",
    "structure": {"rows_parsed": stats["rows_parsed"], "rows_rejected_layout": stats["rows_rejected_layout"], "rows_rejected_malformed": stats["rows_rejected_malformed"],
                  "sex": dict(sexes), "names_per_person": dict(sorted(ntok.items())), "by_province": dict(prov_n)},
    "elements": {f"{k}_position": top(c) for k, c in pos.items()},
    "elements_by_sex": {f"{k}_position": [{"element": e, "sex": s, "count": n} for (e, s), n in c.most_common() if n >= MIN] for k, c in pos_sex.items()},
    "never": "No ethnicity, clan or religion field or pattern (the source has none; C12)",
}
json.dump(profile, open(out_path, "w"), ensure_ascii=False, indent=2)
open(out_path, "a").write("\n")
print({"parsed": stats["rows_parsed"], "rej_layout": stats["rows_rejected_layout"], "rej_malformed": stats["rows_rejected_malformed"],
       "kept": {k: len(v) for k, v in profile["elements"].items()}, "names_per_person": profile["structure"]["names_per_person"], "sex": dict(sexes)})
