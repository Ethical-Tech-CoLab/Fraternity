# Research Log

Running log of research sessions. Append one entry per session, newest at
the bottom. Keep it short: what was looked at, what was found, what is
still open. Findings themselves belong in the case files or the situation
research — this log records the trail (sources, decisions, dead ends) so
the work can be picked up and audited later.

Same sourcing discipline as the rest of the project: every figure keeps
its source, date, and reporting period; conflicting figures stay side by
side; single-sourced claims are flagged as unverified.

## Entry template

```markdown
## YYYY-MM-DD — <short topic>

**Focus:** what this session set out to deepen (case / pathway / question).

**Sources consulted:**
- <title> — <publisher>, <date> — <URL> — <what it gave / didn't give>

**Findings:**
- <finding> — <source, date, reporting period>. Flag `[unverified]` if
  single-sourced.

**Files touched:** `docs/...`

**Open questions / next steps:**
- ...
```

---

## 2026-10-05 — Start of the deepening phase

**Focus:** Resuming Fraternity work. Starting to go deeper on the
research beyond the initial breadth pass (Dzaleka situation research +
four comparative case files: Kakuma, Cox's Bazar, Za'atari, Bidibidi).

**Starting state:**
- `docs/DZALEKA_SITUATION_RESEARCH.md` and `docs/cases/*.md` refreshed
  after the Tavily API-key fix (commits `cf35861`..`fa454d2`).
- Artifacts: Dzaleka Refugee Camp — Situation Research
  (https://claude.ai/artifact/SdRRKd3sigDaWZJVVT4YUZ — same doc as the
  compiled-synthesis link in `RESEARCH_BACKGROUND_DOCUMENT.md`) and
  Dzaleka Theory of Change — Situation Analysis
  (https://claude.ai/artifact/WVVKJFRKdsxvAHnqfxuker).

**Open questions / next steps:**
- Decide which case(s) / pathway(s) to deepen first.

## 2026-10-05 — First cross-case comparison

**Focus:** Build `docs/comparison.md` (called for in `CONCEPT.md` once
≥3 cases exist; it didn't exist yet) to see where to deepen.

**Sources consulted:** the five case files only (as refreshed
2026-09-22). No new external research — the Tavily pass was blocked in
this session (the Tavily MCP server isn't configured for this project, and
reading the API key from config was not permitted).

**Findings:**
- Funding collapse is a pivot node in 5/5 cases → high leverage but not
  neglected; treated as context, not a narrowing candidate.
- Undocumented national-DRM ↔ camp-management emergency interface in 4/5
  cases; Cox's Bazar has a named protocol (not yet extracted) → candidate
  lever L1.
- Protection/child protection is first to collapse in most cases;
  protection is the worst-funded sector where measured (Cox's Bazar 24%)
  → candidate lever L2.
- Law ≠ practice gap recurs (Kakuma, Bidibidi, Dzaleka) → L3.

**Files touched:** `docs/comparison.md` (new), `docs/RESEARCH_LOG.md`.

**Open questions / next steps:**
- Run the Tavily pass on gaps G1–G4 in `docs/comparison.md` §6 first
  (they decide between L1 and L2).

## 2026-10-05 — Comparison pass 2: Tavily on gaps G1–G4

**Focus:** Close the gaps that decide between L1 and L2
(`docs/comparison.md` §6). Tavily MCP was available this session.

**Sources consulted:**
- Multi-Hazard Emergency (Lifesaving) Relocation Protocol — Rohingya
  Response/ISCG, uploaded Aug 2026 —
  https://rohingyaresponse.org/wp-content/uploads/2026/08/MULTI-HAZARD-EMERGENCY-LIFESAVING-RELOCATION-PROTOCOL-OF-ROHINGYA-CAMPS-IN-BANGLADESH_FINAL.pdf
  — full triggers, phases, roles, EVI annex (as of Oct 2024).
- Mongabay via PreventionWeb, Sep 2026 — July 2026 landslides; DRM
  programme 40% funded.
- Daily Star, 6 Jul 2026 — UNHCR landslide death tally 2021–2026.
- UNHCR Uganda RRP Funding Dashboard Q1 2026 (PDF, published 12 Jun 2026)
  — sector and protection sub-sector funding.
- UCRRP 2026 Prioritization — tier budgets.
- JRP 2025 funding update (31 Dec 2025) — confirms Cox's protection 24%.
- 3RP RSO 2026; FTS Jordan/Malawi/Uganda 2026 — Jordan sector funding
  **not** obtainable (FTS 3RP Jordan coverage 2.3%, clearly incomplete);
  FTS Kenya 2026 URL returned 404.
- Africa Brief summary of Malawi NMHCP 2025–26 — plan exists; refugee
  coverage not stated `[secondary]`.
- Draft Turkana County DRM Policy (2017) — names Kakuma fire risk; no
  camp activation SOP.

**Findings:**
- G1 closed: Cox's Bazar protocol extracted. It is a usable benchmark, but
  deaths continued in Jul 2026 because physical mitigation was
  underfunded, so L1's leverage was downgraded to M.
- G4 partial: Uganda protection ~20% funded in Q1 2026, the best-funded
  sector in proportional terms. That contradicts the "worst-funded
  everywhere" premise of L2, so L2's neglectedness was downgraded.
  Kenya/Malawi have no sector-level visibility at all, so a new lever L2b
  was added.
- Emerging case signal: Dzaleka looks most neglected across both L1 and
  L2/L2b. Not a narrowing decision.

**Files touched:** `docs/cases/coxs-bazar.md`, `docs/cases/bidibidi.md`,
`docs/cases/dzaleka.md`, `docs/comparison.md` (§7 added),
`docs/RESEARCH_LOG.md`.

**Open questions / next steps:**
- Read the Malawi NMHCP 2025–26 PDF itself; search for "Dzaleka" and
  "refugee" (G3).
- Za'atari JCD/SRAD emergency plan (G2); Jordan 3RP 2026 protection
  funding from a 3RP Jordan dashboard (G4).
- Cox's "Landslide Risk Prevention… Strategy & Action Plan" (G1 residual).
- Check whether "Dzaleka as most neglected case" survives G2/G3.

## 2026-10-05 — Pass 3: fill protection-funding gaps (official sources only)

**Focus:** Fill the "?" cells in `docs/comparison.md` §7.2 (Jordan, Kenya,
Malawi), using only official sources (OCHA FTS, UNHCR).

**Sources consulted:**
- OCHA FTS API — `/v1/public/plan/year/2026` (plan list) and
  `/v1/public/fts/flow?planId=…&groupby=cluster` for plans 1524 (JRP),
  1526 (Uganda RRP), 1528 (3RP). JRP has cluster data; 3RP and Uganda
  RRP are entirely "not specified" by sector. No Kenya or Malawi plan
  exists for 2026.
- UNHCR Annual Results Reports 2025 (Malawi, Kenya, Uganda, Jordan,
  Bangladesh), §3.1 Financial Data — budget vs. funds available by
  outcome area.
- UNHCR Funding Updates 2026 as of 30 Sep 2026: Kenya (52%), Jordan
  (29%), South Africa MCO (18%; confirmed it does **not** cover Malawi).
- UNHCR Malawi country page — 2026 budget $12.64M; no 2026 funding
  update listed.
- Dead ends: ReliefWeb pages/API blocked from curl; unhcr.org blocked
  from curl (403), so Tavily extract was used instead. Guessed PDF URLs
  for a Malawi 2026 update returned 404.

**Findings:** see the new Tables A–C in `docs/comparison.md` §7.2. Key
points:
- Kenya: UNHCR GBV and CP lines were well funded in 2025.
- Jordan has the lowest GBV coverage of the five.
- Malawi has no separate CP outcome area and no 2026 funding update.
- Cox's Bazar protection is 45.4% funded in 2026, against a smaller
  requirement.

**Open questions / next steps:**
- The §7.3 lever scoring has not been re-scored against Tables A–C yet.
- Uganda's 2026 sector figures are still Q1 only; look for the Q2
  dashboard.

## 2026-10-05 — Dzaleka update since 22 Sept + watch list

**Focus:** Refresh `docs/DZALEKA_SITUATION_RESEARCH.md` ahead of
presenting the preliminary research to the professor.

**Sources consulted:** Nation Online and MBC (mid-Sept 2026, quoting
UNHCR Malawi and the Commissioner for Refugees); The New Humanitarian
(30 Sept); SOS Médias Burundi (18 Sept); Malawi24 (5 Oct, HRDC); Inua
Advocacy / Dzaleka Online (Refugee Bill date); UNHCR ARR 2025 Malawi;
UNHCR Malawi country page; OCHA FTS API.

**Findings:** WFP blanket rations ended Sept 2026; draft Refugee Bill
due 9 Oct; UNHCR Malawi 22.8% funded in 2025, no 2026 funding update;
Chitipa relocation stalled (145 vs. 439 ha discrepancy); serious
security allegations, all unverified.

**Files touched:** `docs/DZALEKA_SITUATION_RESEARCH.md` (updates merged into §1–12,
§14 watch list), `docs/RESEARCH_LOG.md`.

**Open questions / next steps:** work through the §14 watch list,
starting with the Refugee Bill on 9 Oct.

## 2026-10-05 — Length of stay and the three durable solutions

**Focus:** How long people stay in Dzaleka, and the current status of
UNHCR's three durable solutions (voluntary repatriation, resettlement,
local integration) for Malawi.

**Sources consulted:** UNHCR Annual Results Report 2025 – Malawi
(Outcome Areas 13, 14, 15); UNHCR submission to the UPR, 50th session
(Apr 2025); Congressional Research Service IF12813 (US admissions
suspension); Malawi Refugee Law Reader (AfricanLII); Refugee Studies
Centre (2010); Journal of Folklore and Education (2024); Maravi Post
(2017); Inua Advocacy (Jun 2026); Border Monitor (Oct 2026).

**Findings:**
- No official average-length-of-stay figure exists. Proxies: camp is 32
  years old; residents have been refugees up to 28 years; 39% of the
  registered population is still awaiting refugee status determination.
- 2025 exits from all solutions combined: 775 people (~1.2%) vs. ~3,600
  arrivals.
- Repatriation: 135. Resettlement: 634 departures, but submissions fell
  79% (2,430 → 499); complementary pathways fell from 43 to 6.
- Local integration is legally blocked (Art. 34 reservation;
  naturalisation applications refused).

**Files touched:** `docs/DZALEKA_SITUATION_RESEARCH.md` (new §8;
sections renumbered — the watch list is now §14).

**Open questions / next steps:** request the distribution of residents
by year of arrival from UNHCR or the Department of Refugees; confirm the
global 2025 resettlement figure against UNHCR's own publication.

## 2026-10-05 — Durable solutions history since 1994

**Focus:** Historical series (1994–2025) for voluntary repatriation,
resettlement (including destinations such as Australia) and local
integration from Malawi.

**Sources consulted:** UNHCR Refugee Data Finder API (`/solutions` and
`/population`, coa=MLW — note that UNHCR uses MLW, not MWI); UNHCR
Annual Results Reports 2024 and 2025 – Malawi; UNHCR Regional Bureau
for Southern Africa resettlement dashboard (Mar 2025); UN Malawi
Country Results Report 2022; ICMC/Xinhua (2010); Malawi Refugee Law
Reader. Dead ends: the UNHCR Resettlement Data Portal is restricted;
global resettlement statistical reports (2008, 2011) don't break out
Malawi.

**Findings:**
- Repatriation of Dzaleka-profile nationalities totals 1,520 in
  1994–2025.
- Resettlement data points: 227 (2009), 915 (2022), 1,770 (2024), 634
  (2025). Destinations include the US, Australia, Canada, New Zealand,
  Norway, Sweden, Finland and the Netherlands.
- No naturalisations recorded in any year.

**Files touched:** `docs/DZALEKA_SITUATION_RESEARCH.md` (§8.6).

**Open questions / next steps (deferred — not contacting UNHCR for now):** request the year-by-year resettlement
series by destination from UNHCR Malawi or the Regional Bureau for
Southern Africa (rsarbdima@unhcr.org is the dashboard contact); the
exact 2023 departure figure is still missing.

## 2026-10-05 — Full refresh of the Dzaleka document and cluster re-scoring

**Focus:** Bring `docs/DZALEKA_SITUATION_RESEARCH.md` fully up to date,
then check whether the cluster recommendations (§13, formerly §12) still
hold.

**Changes:**
- Fixed stale statements:
  - over-capacity now ~525% at ~63,000 (derived);
  - the $8M→$1M "spending authority" cut is now distinguished from the
    $12.64M 2026 budget;
  - the government is now on record via the Commissioner for Refugees;
  - the "UNHCR stopped registering" claim is partly explained
    (registration moved to the Department of Refugees);
  - evidence gaps expanded.
- §9 theory of change: problem statement and levers revised to include
  durable-solutions closure, the end of blanket rations, and the
  cross-case nuance (funding visibility, not funding in general, is what
  is neglected in Malawi).
- §13 re-scored. A → leverage Very high, tractability Low–moderate
  (time-bound); B and D → neglect Very high; C → tractability higher
  (Cox's Bazar template); E broadened to a "data blackout". New awareness
  angle "No way out".
- `docs/comparison.md` Dzaleka baseline row updated; pointer note added
  to `docs/cases/dzaleka.md`.

**Conclusion:** the Sept 2026 recommendation (B, C, E, G score best)
still holds, with three shifts: A moves up (time-bound bill window), D
becomes more urgent, and Dzaleka's case for focus is stronger. Still not
narrowing to a single lever before the 9 Oct bill and the October
targeted distribution.

## 2026-10-05 — Funding table rewritten for clarity; 90% cut removed

**Focus:** The §3 funding table mixed a global figure (UNHCR worldwide
spend) with a Malawi figure (requirement), and needs with spending.

**Changes:**
- Split into a one-line global context and a Malawi year-by-year table
  (budget / money available / % covered / spent) for 2024–2026, from the
  UNHCR Annual Results Reports 2024 and 2025.
- **Correction:** the "$8M → $1M (−90%)" UNHCR Malawi cut had no linked
  source and could not be verified, so it was removed everywhere (§3,
  §10, §13, awareness angle 1).
- Replaced with verified figures: funds available $8.4M (2024) → $6.0M
  (2025); 2026 budget halved to $12.6M; a 40% spending-authority
  reduction in 2025 per the UN Resident Coordinator (via FairPlanet,
  secondary).

## 2026-10-05 — Source audit of the Dzaleka document

**Focus:** Apply the same check that caught the funding table problem
(mixed scope, unsourced numbers, arithmetic) to the whole Dzaleka
document, then the comparison.

**Corrected:**
- GHO $23B mislabelled as "the UN's" ask.
- IDA refugee window: 21 eligible countries (Dec 2025), not 14.
- UPR votes: 228 + 65 + 1 split = 294.
- Election: held 16 Sept, declared 24 Sept 2025, 56.8% vs 33.0%.
- Unsourced "117 children" removed (505 detained, per SALC; 902 by
  26 May, per HRW).
- Burundi share of the non-DRC population: ~63%, not 91%.
- "UNHCR has not declared Burundi safe" was wrong: returns have been
  deemed safe since 2017 and are promoted since late 2025, amid
  coercion concerns.
- 109 Burundians repatriated from Dzaleka in Oct 2023, not 2025–26.
- The "government is pursuing a 2026 back-to-camp policy" overstatement
  (only the 2023 directive remains in force).
- Parametric insurance: ~$408k, $33/household/month for 3 months.
- Tumaini 11th edition was 2025.
- Mental-health study: peer-reviewed screening, two of five authors
  affiliated with FSF.

**Added:**
- Homeland Security Minister Mukhito (Nation, 26 Jul 2026): the
  government is considering citizenship for some long-staying refugees.
  This was propagated to §8.4, §8.5, §9 levers, cluster A, the "No way
  out" angle and the watch list.
- WFP $12/person = 60% of a $20 ration (Jul 2026).
- Links for crime, INSPIRE-O, Plan exit and Ockenden.

**Not re-verified:** listed explicitly in §9 ("Audit of 5 Oct 2026").

**Comparison:** Kayilizi cost figure fixed; note added that the
baseline funding row is not like-for-like.

**Not yet audited:** the four other case files (Kakuma, Bidibidi,
Za'atari, Cox's Bazar).

## 2026-10-05 — Pathway B restructured with explicit units

Every figure in §3 now states its unit, and the section was split
accordingly:
- 3.1 Global (per year)
- 3.2 UNHCR Malawi (per year, whole operation)
- 3.3 WFP rations (per person, per month, by date)
- 3.4 Funding gaps (total for a stated period)
- 3.5 Context

Derived scale figures were added and labelled as derived: ~$100 per
refugee per year from UNHCR in 2025; ~$1.26M/month for full rations.

## 2026-10-05 — Focus proposal: cluster G (plan B: C)

**Decision (for discussion with the professor):** focus on cluster G
(local/faith-based response). The intervention is an open tool, free for
anyone, with FSF as its first user.

**Two levels:**
- Research level: continuity of essential services when they come to
  depend on local, volunteer-based actors.
- Case level: the FSF clinic (asynchronous telemedicine, caravan-borne
  donated medicines, spreadsheet stock), as illustration and possible
  pilot.

**Facts from the team (not public):**
- caravans roughly every 3 months, 8–30 volunteers, up to 3 kg each, so
  24–90 kg per caravan at most;
- no local stock to buy (site visit).

**Corrections during the discussion:**
- Initial tool ideas (case referral, clinic records) sat in D/E, not G.
- G must start from the refugee's entry point.
- Local purchase was dropped.

**Next:** ethical field mapping of how refugees seek help; clinic
baseline. Plan B: cluster C.

**Files touched:** `docs/DZALEKA_SITUATION_RESEARCH.md` (§13).
