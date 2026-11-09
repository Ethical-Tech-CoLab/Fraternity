"""Build the Rwanda naming profile from NISR's PUBLISHED aggregate tables (no raw data).

Source: National Institute of Statistics of Rwanda, Rwanda Vital Statistics Reports, annex
"Top 20 most preferred babies' surnames ... by sex" (CRVS system). Run in a folder holding the
report PDFs:
  vsr2025.pdf  https://statistics.gov.rw/sites/default/files/documents/2026-04/Rwanda%20Civil%20Registration%20Vital%20Statistics%202025_0.pdf
  vsr2024.pdf  https://statistics.gov.rw/sites/default/files/documents/2025-04/Rwanda%20Vital%20Statistics%20Report%202024_N.pdf

Run: python scripts/build_profile_nisr.py data/profiles/rw-nisr-2026.1.json
"""
import hashlib, json, re, subprocess, sys

REPORTS = {
    2025: ("vsr2025.pdf", "https://statistics.gov.rw/sites/default/files/documents/2026-04/Rwanda%20Civil%20Registration%20Vital%20Statistics%202025_0.pdf", 356838),
    2024: ("vsr2024.pdf", "https://statistics.gov.rw/sites/default/files/documents/2025-04/Rwanda%20Vital%20Statistics%20Report%202024_N.pdf", 341029),
}
ROW = re.compile(r"^\s*(\d{1,2})\s+([A-Z]+)\s+([\d,]+)\s+([A-Z]+)\s+([\d,]+)\s*$")


def annex(pdf):
    text = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True).stdout
    start = text.rfind("most preferred babies")
    rows = []
    for line in text[start:].splitlines()[1:40]:
        m = ROW.match(line)
        if m:
            rows.append(m.groups())
        if line.strip().startswith("Source"):
            break
    assert len(rows) == 20, (pdf, len(rows))
    return rows


out = {"profile_id": "rw-nisr-2026.1", "version": "0.1.0", "origin": "RW", "confidence": "high",
       "method": "Built only from NISR's published annex tables (top 20 Kinyarwanda names of newborns by sex); no individual record was read. Built 9 Nov 2026 by scripts/build_profile_nisr.py",
       "sources": [], "population_note": "Babies born and registered in 2024 and 2025. Refugees in Dzaleka from Rwanda are older: this shows current naming, not their generation's. Only the Kinyarwanda name (called 'surname' by NISR) is covered, not Christian given names",
       "data_quality_note": "In both years the same name appears twice in one column (female: INEZA ranks 1 and 11 in 2024; ISHIMWE ranks 2 and 16 in 2025, 3 and 19 in 2024); kept as published, not merged. An earlier copy of the 2025 report (alpha.statistics.gov.rw) printed the 2024 figures under the 2025 title; the final 2025 report is used",
       "elements": {}, "births_registered_in_year": {},
       "observations": [
           "Most top names are given to both sexes (e.g. ISHIMWE, IRAKOZE, IGIRANEZA, IRADUKUNDA, IRASUBIZA, INEZA, IZIBYOSE, NIYOGISUBIZO, IGANZE): sex cannot be inferred from a Kinyarwanda name",
           "Names sharing a root are distinct names, not spelling variants: ISHIMWE / ASHIMWE / NISHIMWE; IGANZE / AGANZE; MPANO / IMPANO; INEZA / INEZAYIMANA / UWINEZA"],
       "never": "No ethnicity, clan or religion pattern (BENCHMARK_PROTOCOL.md §2.4; C12)"}
for year, (pdf, url, births) in sorted(REPORTS.items()):
    rows = annex(pdf)
    out["sources"].append({"name": f"National Institute of Statistics of Rwanda (NISR), Rwanda Vital Statistics Report {year}, annex 'Top 20 most preferred babies' surnames in {year} by sex' (source: CRVS system)",
                           "url": url, "sha256_16": hashlib.sha256(open(pdf, "rb").read()).hexdigest()[:16]})
    out["births_registered_in_year"][str(year)] = births
    out["elements"][f"kinyarwanda_name_top20_female_{year}"] = [{"element": r[1].lower(), "count": int(r[2].replace(",", "")), "rank": int(r[0])} for r in rows]
    out["elements"][f"kinyarwanda_name_top20_male_{year}"] = [{"element": r[3].lower(), "count": int(r[4].replace(",", "")), "rank": int(r[0])} for r in rows]
json.dump(out, open(sys.argv[1], "w"), ensure_ascii=False, indent=2)
open(sys.argv[1], "a").write("\n")
print("written", {k: len(v) for k, v in out["elements"].items()})
