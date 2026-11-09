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

## 2026-10-05 — Dzaleka document restructured into ToC format

Reorganised `docs/DZALEKA_SITUATION_RESEARCH.md` to follow the case-file
format in `CONCEPT.md`, then clusters, then the rest.

- **Part I:**
  - Baseline.
  - Pathways A–D. Political context, length of stay/durable solutions
    and origins moved under A; family and health moved under D.
  - New cross-pathway causal skeleton (mermaid diagram).
  - Evidence gaps/audit.
  - Draft ToC skeleton, now complete: problem statement, long-term
    outcome, one intermediate outcome per pathway, assumptions, levers.
- **Part II:** actors, clusters, proposed focus, awareness angles.
- **Part III:** watch list and sources.

All cross-references were renumbered and acronym first-use was
re-checked. No content was added beyond the skeleton, outcomes and
assumptions.

## 2026-10-07 — Shift from diagnosis to solutions

The professor's feedback on the ToC: the research must start from what we
can do that actually changes something in the camp. The situation research
is kept unchanged as context.

**Constraints clarified the same day:** no funding; output is free and open
source; small impact is fine; the aim is to start a line of technology
development. A first draft built on funded pilots (remote work, cash) was
replaced accordingly. Its livelihood evidence is kept as context.

- **New:** `docs/SOLUTIONS.md`. One or more open-source tools per cluster
  (A1 law comparator, B1 funding tracker, C1 risk/evacuation map,
  D1 help directory, E1 open dataset, G1 caravan and stock planner, G2
  help-seeking entry point), scored on real user, small change, zero
  budget, data safety, duplication, research value and replicability.
- **Recommendation:** G1 first (FSF is a guaranteed user), C1 as the
  research track (mid-Dec rains), E1 as a by-product.
- **Open point:** whether G1 counts as cluster G, given the 5 Oct
  correction that clinic records sat in D/E.
- **Tooling:** the Tavily API key failed (unauthorised); the built-in web
  search was used instead.

**Next:** discuss with the professor; ask FSF for the stock spreadsheet
structure and next caravan date; check MapMalawi's OSM data for Dzaleka.

**Later the same day:** asked to think outside the box (apps for refugees,
awareness, practical ideas). Added §3 to `SOLUTIONS.md` with 12 ideas
(X1–X12) in three groups: apps for refugees, moving money without
funding, and awareness. Favourites: X10 "Live on $8" (awareness game), X1
"Is this offer real?" (scam/trafficking checker), X7 "Reverse caravan"
(crafts out on returning FSF caravans). Revised recommendation: one
awareness piece (X10) plus one practical tool (G1 + X7, or X1), with C1
as the research track. RICS removed from the document at the user's
request.

**Rewrite with a reality filter (same day).** Builders are the user (with
Claude) and the professor; FSF gives context only; no funding; no field
presence. `SOLUTIONS.md` was rewritten. Key findings:
- Most refugee apps die ("digital litter": most of 169 apps from 2015–16
  were defunct by 2018), so build into something already used.
- Dzaleka already has a refugee-led platform, Dzaleka Online Services
  (Dzaleka Connect; public API; 149 services; alerts; Met Malawi weather;
  last commit 5 Oct 2026). It is English-only and web-only, mostly built
  by one developer, and the `dos` repository has no licence file.
- Radio Yetu broadcasts in six languages (2026 status unconfirmed).
  TakenoLAB is a refugee-led tech school.

Recommendation: Option 1, contribute languages, a low-data version and a
weekly radio bulletin to DOS; Option 2, rain/heat alert thresholds as the
research track (the flood hazard at Dzaleka is not evidenced
yet). Next: contact Dzaleka Connect before writing code.

**Re-researched with Tavily (same day).** Fixed the Tavily key: the
project-level config held an old key that overrode the valid global one.
Corrections and new findings in `SOLUTIONS.md`:
- DOS is richer than first stated: "Get help now" hotlines, Rights
  Navigator, essentials in EN/FR/SW/Chichewa, Easy Read, open data
  platform. There is no Kirundi or Kinyarwanda version.
- DOS 2025 report: 17,952 users but only 3,705 in Malawi and 1,697
  returning. The gap is reach inside the camp, not features.
- Population by origin (DOS): DRC 65%, Burundi 22%, Rwanda 13%.
- Yetu Radio is active in 2026; sources disagree on its languages (5 vs 6)
  and frequency (107.6 vs 99.1 MHz).
- Flooding is documented: Friedman (2021, Virginia Tech) modelled Dzaleka
  from 3.5 cm drone imagery; erosion patterns predict collapsed houses.
- Recommendation now: Option 1 "last-mile kit" (DOS API → weekly radio
  script, WhatsApp cards and a printable sheet in Swahili/French); Option
  2 rain warnings by zone (research track) building on Friedman 2021.


## 2026-10-07 — Online microwork and paid surveys for refugees

Question from the user: could Dzaleka refugees earn from online
microtask or survey sites, and actually receive the money? New file:
`docs/ONLINE_MICROWORK.md` (Tavily).

- PayPal does not work in Malawi, which blocks PayPal-only platforms
  (e.g. Prolific).
- Payoneer works in Malawi (Toloka, Clickworker and Upwork pay through
  it), but its ID check does not list refugee documents.
- Centenary Bank has an agency in Dzaleka (17,420 accounts).
- The biggest catch is the official rate (~MWK 1,750/$) against the
  parallel market (3,500–4,500), so money earned online loses about half
  its real value.
- Realistic pay is ~$1.40–5.50 an hour, and the work is irregular.
- Proposal: a verified "online work that really pays" guide (Option 1
  content), built from residents' real payout experience. Ask TakenoLAB
  and Dzaleka Connect first.

## 2026-10-07 — SOLUTIONS.md restructured as "Dzaleka Info Bridge"

The user found SOLUTIONS.md confusing and asked to learn from examples like
refugeeconnectivity.org. Reviewed with Tavily: Connectivity for Refugees
(UNHCR/ITU/GSMA; 11 countries, not Malawi), GSMA "Digital Lives of
Refugees" (2026: only ~1/3 in Kiziba and Bidi Bidi have used mobile
internet), GSMA "Digital Worlds" (58% fear phone scams), ConnectRefugee
(Nakivale: verified NGO announcements in 5 languages, built by
refugees), Internews rumour tracking, Hello Hubs (Rhino Camp: community
governance).

SOLUTIONS.md now frames one product with a core (weekly digest: DOS →
radio script, WhatsApp cards, A4 sheet, in Swahili/French) and three parts:
A, a questions and rumours loop; B, heavy-rain warnings by zone (shadow mode
in the 2026–27 season); C, a verified online-work guide. Added a lessons
table, risks and a roadmap.

**Critical review and revision (same day).** The user asked whether the
proposal is real. Verdict: buildable, but the need is an untested
hypothesis (no resident consulted; DOS's Facebook, WhatsApp groups or the
radio may already carry the information; weekly content may be thin; it
would add unpaid weekly work for reviewers). SOLUTIONS.md revised:
- Step 0 is now validation: three questions to DOS, Yetu Radio and
  TakenoLAB, plus university ethics approval.
- Step 1 is now fixed essentials (urgent help, hotlines, scam warnings)
  translated once into Kirundi/Kinyarwanda, as radio spots, A4 sheets and
  WhatsApp cards. This is the only documented gap.
- The weekly digest becomes Step 2, conditional and monthly by default.
- The rumour loop is removed (needs paid staff).
- The rain warnings are described honestly (area forecast plus a fixed
  risk map) and need ground truth; shadow mode Dec 2026 – Apr 2027.

## 2026-10-14 — Seven options documented for discussion (SOLUTIONS.md §9)

For the 15 Oct meeting with Professor Yorke Rhodes, added section 9 to
SOLUTIONS.md: seven candidate interventions (community reporting,
multilingual information, weather alerts, open map data, climate risk,
needs assessment, existing systems), a comparison table, a synthetic-data
MVP for the reporting option and questions for local partners. No option
selected; reporting is the user's current preference. Sections 1–8 left
unchanged.

Checked 14 Oct 2026:
- Met Malawi (DCCMS) publishes a public CAP RSS feed; latest item 12 Oct
  2026; alerts are district or national, not camp zones.
- Sahana Eden (MIT), Ushahidi platform (AGPL) and FixMyStreet (AGPL) are
  all actively maintained on GitHub.
- HOT Tasking Manager API: no project matching "Dzaleka".
- HDX: five Dzaleka datasets, all UNHCR surveys (nutrition 2012/2016,
  socio-economic 2017, cash PDM 2020, RMS 2023); no map layers.
- OSM has the site, hospital, health centre and market as features.
  Building and path completeness not measured: Overpass returned
  504/406 errors. Still open.
- Defesa Civil Alerta: operator-run cell broadcast (MIDR + Anatel, since
  Dec 2024); ITU technical contribution is restricted access.

## 2026-10-15 — Refugee Bill presented (diagnosis update)

Tavily search on the draft Refugee Bill announced for 9 Oct, plus Dzaleka
news since 5 Oct.

- **Held as announced.** On 9 Oct the Special Law Commission (chair
  Justice Prof. Redson Kapindu) presented its report and a draft
  Refugees (Protection and Management) Bill. Confirmed by MBC, the
  public broadcaster.
- Key proposals: asylum seekers stay in camps; recognised refugees "with
  valid reasons" may **apply** to live outside; right to work and to run
  small and medium businesses in "designated areas"; equal access to
  education; Eligibility Committee, Appeals Board and appeal to the
  courts; Department of Refugee Services; stateless persons; a separate
  Disaster Risk Management Amendment Bill.
- **Not law yet:** next steps are the Minister of Justice → Cabinet →
  Parliament. No Cabinet date has been found. MHRC urged fast-tracking (13 Oct).
- Conflict kept: Streamline (a Kenyan aggregator) says the bill
  "dismantles" encampment. MBC describes only a permission-based exception.
- Full bill text not found online. Citizenship provisions not reported.
- Malawi at UNHCR ExCom (Oct 2026): 939 RSD decisions in 2026; Chitipa
  settlement site reaffirmed.
- Dead end: "relocate refugee centres to the border in December" is a
  South African story, not Malawi.
- Also seen, not added to the case file: SOS Médias Burundi (single
  source) reports a Burundian trader's death after a collision with a
  police vehicle near Dzaleka (6 Oct); the Tumaini Festival cancelled its
  2026 edition (Dzaleka Online).

**Files touched:** `DZALEKA_SITUATION_RESEARCH.md` (§2.1 table and
update, durable-solutions openings, watch list), `SOLUTIONS.md` (15 Oct
note).

**Next:** get the full report/bill text (Law Commission, Inua Advocacy);
score it against Inua's 7-point checklist; watch for Cabinet adoption.

**Later the same day — legislative path.** Tavily: Constitution ss. 73–74
(21-day assent, veto override, entry into force by Gazette), Law
Commission Act (report → Minister → Parliament), Standing Order 114 (two
Gazette notices ≥21 days apart before the first reading; from a 2018
guideline, current text not checked), Ministry of Justice stages. Next
sitting: 9 Nov – 11 Dec 2026 (mid-year budget review); the bill is not
listed and the timing makes it very unlikely. Earliest realistic window:
2027. Precedent: law-reform bills stuck for years at the Ministry of
Justice (Nyasa Times, Jan 2026). Added to `DZALEKA_SITUATION_RESEARCH.md`
§2.1. The user proposed a project to consolidate eligibility information
for refugees; it was discussed, not yet added to `SOLUTIONS.md`.

**Later the same day — section 10 added to SOLUTIONS.md.** At the user's
request, the eligibility-information idea was developed as a proposal,
"Know your status": three layers (rules today / tracker and explainer /
eligibility guide), so most of the work stays useful if the bill is never
passed; phases with decision gates and stop/pivot rules; and a list of
knowledge to collect (law, politics, audience, ecosystem, translation,
safety and liability, technical). Not selected; for discussion with the
professor.

**Later the same day — existing work check (chatbot idea).** Tavily plus
direct fetches. No chatbot for Dzaleka/Malawi refugees found (absence of
evidence; ask DOS, Inua and TakenoLAB). The DOS Rights Navigator already
covers most of the planned "rules today" layer (English, web; 1989 Act,
1990 Regulations, gate pass, legal aid directory, incident tracker). The
Inua Advocacy guide (Dec 2024) targets the public and advocates. UNHCR
HELP Malawi returned 403, so it is still to check by hand. Elsewhere:
Signpost (AI pilot needs a human in the loop; not in Malawi), IRC ALMA,
IRAP Mona, UNHCR La Chama, Rafiki AI in Kakuma (single source). WhatsApp
Business has banned general-purpose AI bots since 15 Jan 2026. Design
consequence recorded in SOLUTIONS.md §10: build on the Rights Navigator,
as a guided (menu) bot.

**Later the same day — risk table and partner decision.** Added to
SOLUTIONS.md §10: the risks of a keyword-search bot (main one: "proposed"
read as "in force"; mitigations: status label and date on every answer,
expiry dates, multiple-choice results, per-answer disclaimer and referral,
no stored queries, one official number). The user has no Malawian
partner, so publishing under a partner's name was dropped. Decision: a
local partner (DOS or Inua) is a launch condition, not a start condition.
Without one, the bot stays a research prototype.

**Later the same day — SOLUTIONS.md reorganised.** At the user's request,
rewritten around three paths: (1) change a constraint (partners and
residents first; funding; no advertising); (2) the structural lever:
evidence for the Refugee Bill (proposed focus), tracker, later
monitoring and eligibility guide; (3) small, real and research (rain
shadow mode, OSM, translated essentials, guided chatbot, live map). One
overview table gives feasibility and how each option changes reality.
Set aside: reporting to organisations, needs assessment, live-map alerts
about people, advertising, standalone app, digest, rumour loop. The
pre-reorganisation version (with the 15 Oct sections 10–11 detail) was
backed up outside the repo; it is not in git.

**Later the same day — Path 1 removed.** The user does not want funding,
partner contact or conversations with residents in the plan. SOLUTIONS.md
now has two paths: (1) the Refugee Bill (ideas 1A–1D) and (2) small, real
and research (2A–2E). Without anyone in the camp, the information tools
(2C–2E) stay research prototypes. Advertising and the ethics and partner
items were removed with Path 1.

## 2026-10-15 — Family tracing: REFUNITE review and idea 2F

The user proposed a "Tinder-style" mutual-match platform to find missing
relatives. Tavily plus direct fetches:
- REFUNITE (Refugees United) already does this: anonymous profiles,
  search by name and markers, private messages. It claims 1M+
  registrations and 75k+ families reconnected, and lists Malawi, the
  DRC, Burundi and Rwanda. m.refunite.org is live with 12 languages,
  none of them Kirundi, Kinyarwanda, Lingala or Chichewa. The public
  profile is visible except contact details; all usage data is logged.
  Signs that the platform is idle: the site shows "© 2024", the news is
  old and the figures are unchanged; the organisation has moved to
  Relay, RelayID (2025) and Relay Funder (Dec 2025). The EUAA 2025 guide
  still recommends it.
- The Red Cross RFL works inside Dzaleka (Malawi Red Cross and ICRC).
  ICRC Trace the Face has a southern Africa version.
- Decision: no new platform (splits users; persecution risk; no
  verification). Added idea 2F to SOLUTIONS.md: an open-source module
  for matching Great Lakes names (spelling, order, Christian-name and
  place-name variants), evaluated on synthetic data only. Added to the
  proposed focus at the user's request.

**Later the same day — 2F expanded as "Open Great Lakes Names".** At the
user's request: the open dictionary becomes the core (usable without
anyone adopting the module), plus an intake guide for tracing services
(all names in any order, parents' names, colline, the province name at
the time; never ethnicity or clan), language packs in phases (Kirundi,
Kinyarwanda and Congolese Swahili first; non-Latin scripts out for now),
and the evaluation. Sending the guide to the Red Cross would be a one-off
contact with an organisation; that decision is left to the user.

**Later the same day — delivery deferred.** Offering 2F to REFUNITE, the
Red Cross or UNHCR is now the final phase, decided after the evaluation.
Steps 1–4 do not depend on anyone agreeing, because the open outputs
stand on their own.

**Later the same day — family-separation data.** At the user's request
(to show why 2F matters), Tavily search for how many families separate in
displacement. No direct count exists; proxies were added to
`DZALEKA_SITUATION_RESEARCH.md` §5.2:
- ICRC missing persons: ~169k (2019, derived), 195k+ (2022), 284,400
  (end 2024, +68%), "227,000+" (end 2025) vs 409,855 open cases (end
  2025). The divergence is kept: likely different measures and caseload
  reviews.
- ICRC Africa: 40,708 → 71,000+ (2019 → Jun 2024, +75%).
- UNHCR unaccompanied and separated children: 25k asylum applications
  (2019), 51.7k (2022), 218k registered (2024); these are not one series.
- Great Lakes: Kenani 2017 (60% unaccompanied or separated), Kivu 2025
  separations, Burundi 2025; Dzaleka 67 (Dec 2025).
- No share of separated refugees for the Great Lakes (gap); Syrians in
  Jordan 36.5% as a comparator.
Summary added to SOLUTIONS.md 2F ("Why it matters").

## 2026-10-19 — NameBridge concept, timetable, 2F scope

- Added `docs/CONCEPT-IDEA.md` ("NameBridge", supplied by the user): option
  analysis for a cross-border name-intelligence system for missing-person
  search. Its §14 wrongly said `SOLUTIONS.md` returned a 404 (the repo is
  public and the file was on `main`); corrected.
- Added `docs/TIMETABLE.md`: weekly scope from 19 Oct to 18 Dec 2026, with
  2F as the main track, 1A second, 1B and 2A as small fixed tasks.
- Week 1, first task: `SOLUTIONS.md` 2F now has "What 2F takes from
  NameBridge". Adopted: sourced, typed dictionary entries with confidence
  and review status; generated entries stay `proposed`; negative ("not the
  same name") entries; etymology as low-weight expansion only; original
  names never overwritten; the §11 language-pack format; Burundi sibling
  naming kept as an evidence gap; recall@10, precision and false-match
  rate per language; Splink as an optional comparison. Not adopted: the
  protected case graph, human review interface, shadow pilot, deployment,
  real-data benchmark, federation and biometrics (they need partners or
  real records).
- Next: Kinyarwanda literature; 1B tracker page; search for the full bill
  text.

**Later the same day — direction changed to NameBridge.** The user
clarified that the project's work is NameBridge itself (`CONCEPT-IDEA.md`),
not 2F with parts of NameBridge. The rest of `SOLUTIONS.md` is kept but not
used. `TIMETABLE.md` rewritten around NameBridge §10 phases 0–2 compressed
into 9 weeks (19 Oct–18 Dec 2026), with a proposed Great Lakes → Malawi
pilot corridor (Kinyarwanda, Kirundi, Congolese Swahili) and synthetic data
only; phases 3–4 after the semester and only with a tracing partner. The
"What 2F takes from NameBridge" subsection was replaced by a short pointer;
README, `SOLUTIONS.md` header and `CONCEPT-IDEA.md` §14 updated to match.

**Later the same day — FSF in the final phase; no sale.** The user decided
NameBridge will not be sold. The final phase in `TIMETABLE.md` now offers it
free of charge to the tracing organisations and to Fraternidade Sem
Fronteiras, whose work with children in care (foster children, the Órfãos
do Congo project) could use it to trace relatives; minors follow the
protected-person rules (§8, control 7). The user plans to present the
project to FSF and hear their view.

**Later the same day — timetable aligned with CONCEPT-IDEA.** Audit found
gaps; fixed: phase 0 data rules (sharing, retention, disclosure, incident
response); §9.3 temporal holdout, name-only vs full-evidence results and
fairness slices; §12 must-haves (regression suite, graph API, role-based
access, access log, retention/deletion); option 4 (commercial) tested only
with a free licence and no data leaving our machine. New table of
deliberate differences (9 weeks, synthetic data, no advisory group,
Latin-script corridor, ~2,000 relationships, phases 3–4 conditional) and
deferred should-haves. `CONCEPT-IDEA.md` §10 gains "Final phase — free
offer": not sold; FSF uses an intake guide derived from the packs and
refers cases to an authorised tracing service, without running the system.

**Later the same day — §8 controls added.** A second check found §8
controls missing from the timetable. Added on synthetic data: consent and
lawful basis (4) and protected-person flags (7) in week 7; progressive
disclosure (8) and challenge and correction (9) in week 9. Controls 10 and
11, the non-corridor naming systems of §3 and most §13 questions are listed
under "Differences" as later work. What 18 Dec delivers: NameBridge phases
0–2 for the Great Lakes corridor, with the safeguards that can be tested
offline.

## 2026-10-26 — NameBridge week 1 (phase 0): scope and repo skeleton

**Focus:** `TIMETABLE.md` week 1, done a week late (planned 19–23 Oct).

**Sources consulted:**
- `DZALEKA_SITUATION_RESEARCH.md` §1, §2.4 — population by origin (services.dzaleka.com/data, Mar 2025) and new-arrival mix (UNHCR).
- `CONCEPT-IDEA.md` §2.3, §8, §10 phase 0, §12.

**Findings / decisions:**
- Pilot corridor confirmed: Great Lakes → Malawi. DRC 37,245 (65%), Burundi 12,604 (22%), Rwanda 7,135 (12%) of 57,438 in Dzaleka, Mar 2025; together about 99%.
- Users: tracing caseworkers in authorised services (phase 3 onward, with a partner); linguists and community experts for the public graph; FSF only through the intake guide; the researchers this semester. Not users: the public, families searching directly, law enforcement and governments (proposed; to confirm with the professor).
- Allowed purposes and prohibited uses written from §8 control 1 and the §12 "should not have" list, plus no locating people for enforcement or surveillance.
- Licences: code Apache-2.0 (patent grant); graph and packs CC BY 4.0.
- Burundi sibling-surname question (§2.3): the Kirundi pack will record surname agreement as `unknown` until sourced.

**Files touched:** `docs/SCOPE.md` (new), `namebridge/` (new skeleton), `docs/TIMETABLE.md`, `README.md`, `docs/RESEARCH_LOG.md`.

**Open questions / next steps:**
- Professor to see `SCOPE.md` (week 1 "done when").
- Week 2: threat model, desk data-protection assessment, data rules, benchmark protocol; start Kinyarwanda naming research.

## 2026-10-26 — Evidence check of the week 1 scope (Tavily)

**Focus:** the user felt phase 0 went too fast; second desk-research pass to test every claim in `SCOPE.md`.

**Sources consulted:** listed as [S1]–[S16] in `SCOPE.md`. Main ones: UNHCR figures via FairPlanet (Oct 2024); USCRI on Dzaleka UASC (2026); Rwanda Law 71/2024; Burundi Code des personnes et de la famille 1993; Université du Burundi onomastics paper (Bigangara 1982); DRC Family Code via FamilySearch and an ICC annex; Malawi Data Protection Act 2024; HRW on Rohingya data (2021); RFL Code of Conduct; CongoNames corpus (*Data*, Jul 2026).

**Findings:**
- Confirmed: corridor shares (UNHCR 36,469 / 12,291 / 7,019 at 31 Oct 2024; DOS 65 / 22 / 12% Mar 2025). Need: the Red Cross in Dzaleka "can only cross-reference lists of other refugee camps" (USCRI) — the NameBridge task. Rwanda: law forbids a child bearing only all of a parent's or sibling's names (Law 71/2024 arts 38–39).
- Changed: Burundi is `disputed / context-dependent`, not `unknown` — free choice of name in law, no family names before Christianity, missionary patronymics, sons sometimes named after fathers. DRC packs organised by naming system; Swahili is the camp lingua franca, Lingala also spoken. Malawi Red Cross Society (with ICRC) named as the tracing actor. Governments: users vs data sources separated; repatriation screening added to prohibited uses (Rohingya precedent). Malawi DPA 2024 and RFL Code of Conduct added. UNHCR's 2015 policy allows law-enforcement transfers; our rule is stricter.
- New candidate source: CongoNames, 8.05 M real names, CC BY 4.0 — aggregate statistics only, after week 5 review.
- `[unverified]`: no 2026 nationality breakdown for Dzaleka found; UNHCR 2022 policy not checked on law-enforcement transfers; Duchaj & Ntihirageza full text not fetched; DRC Family Code read only through secondary sources.

**Files touched:** `docs/SCOPE.md`, `docs/TIMETABLE.md` (weeks 2 and 5), `docs/RESEARCH_LOG.md`.

**Open questions / next steps:** professor review of `SCOPE.md`; the unverified items above go into week 2.

## 2026-10-26 — NameBridge week 2 (phase 0): threats, DPIA, data rules, benchmark

**Focus:** `TIMETABLE.md` week 2, researched with Tavily; four separate documents, as the user chose. The user approved the proposed cost-of-errors default (missed candidate worse at retrieval; false match worse at confirmation).

**Sources consulted:** cited per document ([T*], [D*], [R*], [B*]). New since the scope check: ICRC 2022 RFL breach (515,000 people); RFL guide §7.3.2 (no contact details without the located person's consent) and §7.4.3 (closure); IFRC PrepareCenter ("sometimes traffickers are parents/relatives"; consent impossible for sought persons, so vital or public interest is used); Malawi DPA 2024 s. 17 (children), s. 30 (DPIA contents, submitted to MACRA before processing), ss. 19–26 (rights incl. against solely automated decisions); UNHCR 2015 policy §6.3.2 (law-enforcement transfers only for serious crime etc.); LINDDUN; IASC data-responsibility guidance 2023; GeCo (Christen); entity-centric ER evaluation (Binette 2024); Splink evaluation docs; DRC Family Code primary text (2017 consolidation, arts 56–64); UNHCR DRC situation (Malawi 41,071 DRC, 30 Apr 2026).

**Findings:**
- DRC Family Code (primary text): art. 56 order and spelling of name elements immutable; art. 57 same-family members with the same nom must add different complementary elements; art. 59 parents choose the name; art. 61 a parent who transmits a name must add at least one different element; art. 62 a married woman keeps her name and may add her husband's; art. 64 changes only by court. So DRC siblings can share a partial name — partial agreement is evidence.
- **Kinyarwanda (start of research):** HRW 1999 — written only since the early 20th century; official orthography often not followed (e.g. *burugumestri* / *burugumesteri*); most Rwandans do not share a family name. Records write the surname first, often in capitals; the ID card has one field, *Amazina*. **Conflict:** The New Times, 6 May 2026, says children "traditionally take the father's surname" and that some urban families now reconsider it. Law 71/2024 art. 39 forbids only bearing *all* of a parent's names. Next: find onomastic or statistical evidence (week 4).
- An unaccompanied child may have no parent or guardian to consent (s. 17), so the lawful basis must be vital interest with a best-interest assessment, not consent.
- Phase 0 exit: complete except the stewards and advisory group (gaps); phase 1 can start.
- `[unverified]`: Malawi DPA section numbers come from summaries (check against the Act); the HRW chapter on ID-card ethnicity still to cite precisely; Duchaj & Ntihirageza full text still not fetched.

**Files touched:** `docs/THREAT_MODEL.md`, `docs/DPIA.md`, `docs/DATA_RULES.md`, `docs/BENCHMARK_PROTOCOL.md` (new); `docs/SCOPE.md` (§8 exit check, Rwanda conflict, 2026 figure); `docs/TIMETABLE.md`; `README.md`.

**Open questions / next steps:** professor review of the five phase 0 documents, especially the cost ratios and targets (`BENCHMARK_PROTOCOL.md` §7) and the not-a-user rule; week 3: schema and validator, including the ethnicity guard (`THREAT_MODEL.md` §4.2).

## 2026-10-26 — UNICEF sources on child tracing, data protection and AI

**Focus:** the user asked whether UNICEF has reports related to the laws and procedures in the phase 0 documents.

**Sources consulted:**
- Primero / CPIMS+ — [primero.org](https://www.primero.org), [cpims.org](https://www.cpims.org), [UNICEF Digital Impact](https://www.unicef.org/digitalimpact/primero-information-management-system), [Admin Guide](https://support.primero.org/pdfs/primeroIMS/PrimeroAdminGuide/master/book.pdf), [User Guide](https://support.primero.org/pdfs/primeroIMS/PrimeroCPIMSUserGuide/master/book.pdf), [API doc](https://github.com/primeroIMS/primero/blob/main/doc/api.md), [community forum](https://support.primero.org/forum/t/family-tracing-and-reunification/318), [CPIMS+ review 2024](https://socialserviceworkforce.org/wp-content/uploads/2024/03/CPIMS_Review_Report.pdf).
- UNICEF, [Policy on Personal Data Protection](https://www.unicef.org/documents/policy-personal-data-protection) (effective 15 Jul 2020).
- UNICEF Innocenti, [Guidance on AI and Children 3.0](https://www.unicef.org/innocenti/media/11991/file/UNICEF-Innocenti-Guidance-on-AI-and-Children-3-2025.pdf), Dec 2025.
- UNICEF + The GovLab (NYU), [Responsible Data for Children (RD4C)](https://rd4c.org) and its [22-question audit tool](https://files.rd4c.org/22-Questions-to-Assess-RD4C-tool.pdf).
- Government of Malawi / UNICEF Malawi, [Reference Manual for Child Protection Workers](https://www.unicef.org/malawi/media/6011/file/Government%20of%20Malawi%20-%20Reference%20Manual%20for%20Child%20Protection%20Workers.pdf).
- Malawi, [Child Care, Protection and Justice Act 2010](https://justice.gov.mw/sites/default/files/2021-06/Child%20Care%2C%20Protection%20and%20Justice%20Act.pdf).
- ICRC/IRC/SCUK/UNICEF/UNHCR/WVI, [Inter-Agency Guiding Principles on UASC](https://www.icrc.org/en/publication/1101-inter-agency-guiding-principles-unaccompanied-and-separated-children) (2004).
- UNICEF, [Programmatic Guidance on Cross-Border Case Management](https://clearinghouse.unicef.org/download-ch-media/c2e55ade-f072-4e23-927e-dc7ebbbbe43c) — snippet only; full text could not be fetched.
- UNICEF MENA, [Children on the Move in North Africa](https://www.unicef.org/mena/media/28791/file/pub2025-003-l-children-on-the-move-in-north-africa-and-along-key-routes%20(1).pdf.pdf), 2025.
- UNICEF/DLA Piper, [Birth Registration – Phase Two](http://citizenshiprightsafrica.org/wp-content/uploads/2016/08/UNICEF-Comp-laws-Birth-Registration2_2016.pdf), 2016 (Malawi section).

**Findings:**
- **Primero / CPIMS+ is the closest existing system.** It is UNICEF-led inter-agency, open source, a certified digital public good, and has more than 10,000 users in more than 60 countries.
  - Its family-tracing module matches caregivers' tracing requests against registered children. Matching is configured by choosing which *fields* to compare (Solr-based). Results are labelled only "Possible" or "Likely".
  - It descends from RapidFTR, built for **Congolese refugees in Uganda** (2012–14).
  - It has a tracing-consent field and proGres / ICRC reference fields, and an API with `potential_matches` endpoints.
  - Interface locales listed (v1.7) are en, fr, ar, so, es, bd, id, ku: no Swahili, Kinyarwanda or Kirundi.
  - No evidence found of culturally aware name-variant handling. That is the gap NameBridge addresses.
  - Licence: "please carefully read our LICENSE" (not yet read). Malawi deployment: not found.
  - **Implication:** NameBridge could be offered as a name-variant layer for CPIMS+, via its API or as search synonyms, rather than a separate system. This is a decision for the user and the professor.
- **RD4C is UNICEF + The GovLab at NYU.** It has 7 principles and a 22-question audit tool; NameBridge can be checked against it. It is an NYU link for the professor.
- **UNICEF Guidance on AI and Children 3.0** has 10 requirements: safety, data and privacy, non-discrimination and fairness, transparency and explainability, best interests, and others. It says data processing for children on the move or without identification "should not entail large-scale, indiscriminate and wide-ranging collection" — matches DR-1 and the DPIA's minimisation.
- **UNICEF Policy on Personal Data Protection (2020)** has sections on automated decision-making, transfers, breach, and emergency contexts. It applies if UNICEF is a partner.
- **Malawi child law:**
  - The Child Care, Protection and Justice Act 2010 defines a child as under 16. The Constitution (amended 2017) says under 18 and prevails (UNICEF Malawi manual). NameBridge uses under 18 — consistent.
  - A guardian must be resident in Malawi (s. 38). This matters for consent and representation of unaccompanied children (`DPIA.md` (c)).
  - The manual's best-interest determination is a four-question test, citing the UNHCR BID guidelines (2008).
- **Scale:** Dzaleka registered **756 unaccompanied minors in 2016** (academia.edu study, `[unverified]`), against 67 registered unaccompanied or separated children with the Red Cross in Dec 2025 (USCRI). This is not the same measure; keep both.
- **Cross-border tracing:** UNICEF guidance recommends regional digital platforms, with tracing started within 72 hours of identifying a child (MENA 2025).

**Files touched:** `docs/RESEARCH_LOG.md`.

**Open questions / next steps:**
- Decide whether NameBridge targets CPIMS+ integration (affects week 3 schema and the API).
- Read Primero's LICENSE and matching code.
- Run the RD4C 22 questions on NameBridge.
- Try the cross-border case management guidance again.

## 2026-10-26 — How Primero / CPIMS+ matches (code read)

**Focus:** the user considers CPIMS+ relevant to NameBridge and decided this without consulting the professor. This entry records what it actually does, from its source code.

**Sources consulted:** [primeroIMS/primero](https://github.com/primeroIMS/primero), `main` branch, last push 19 Oct 2026, 76 stars: `LICENSE`, `app/services/matching_service.rb`, `app/services/language_service.rb`, `app/models/concerns/phonetic_searchable.rb`, `solr/configsets/primero/conf/schema.xml`; [CPIMS+ review (2024)](https://socialserviceworkforce.org/wp-content/uploads/2024/03/CPIMS_Review_Report.pdf); Primero [Admin](https://support.primero.org/pdfs/primeroIMS/PrimeroAdminGuide/master/book.pdf) and [User](https://support.primero.org/pdfs/primeroIMS/PrimeroCPIMSUserGuide/master/book.pdf) guides.

**Findings:**
- **Licence:** AGPL-3.0-or-later. The CPIMS+ and GBVIMS+ configurations (JSON bundles) are available on request from UNICEF. NameBridge stays Apache-2.0 as a *separate service* called over Primero's API. If code were merged into Primero, that code would have to be AGPL.
- **Matching (`MatchingService`):**
  - A Solr full-text "any of" query over boosted fields: names, other names and nicknames ×15; sex and age ×10; relatives' names ×10; date of birth ×5; relationship ×5; nationality, language and religion ×3; **ethnicity and sub-ethnicity** with no boost but still used as match fields.
  - Only children with `consent_for_tracing = true` are searched.
  - Top 20 results.
  - Scores are **divided by the best score in the same result list**. The top hit is always 1.0, however weak, so scores are **relative, not calibrated**.
  - "Likely" if there is only one result, or if score − mean > 0.7; otherwise "Possible".
  - There is **no "not found" or "insufficient evidence" outcome**; the weakest results are cut below 0.1 of the best.
- **Name handling (`LanguageService`, Solr schema):**
  - Names are split on spaces and stripped of diacritics.
  - Latin tokens are encoded with **Double Metaphone**, a phonetic algorithm designed for English and European names. Plus edge n-grams for prefix search.
  - No knowledge of name variants (Jean / John / Yohana), no handling of name structure (nom / postnom / prénom; Kinyarwanda surname-first), no transliteration paths, and no explanation of *why* names matched beyond which fields matched.
  - Name order is ignored (bag of tokens). That helps with reordering, but loses structure.
- **The CPIMS+ review (2024)** says data protection is one of the tool's strengths. Configurable FTR matching on chosen fields was added in v1.6.

**What this means for NameBridge:**
1. **The gap is confirmed.** The most widely used inter-agency tracing tool matches names with an English-oriented phonetic code and relative scores. NameBridge's sourced variant graph, calibrated scores and abstention address exactly that.
2. **Integration path:**
   - NameBridge as a separate service (Apache-2.0).
   - It reads a tracing request and candidate cases through Primero's API (`/api/v2/traces/:id/potential_matches`, cases, tracing requests).
   - It returns ranked candidates with explanations to the caseworker.
   - It writes nothing back automatically.
   - Lighter option: export graph variants as **Solr synonym lists** that a Primero deployment can load.
3. **Benchmark:** add a **"CPIMS+-style baseline"** (Double Metaphone + boosted field match + score/max normalisation) to `BENCHMARK_PROTOCOL.md`, so the comparison is against what caseworkers actually use.
4. **Ethnicity:** CPIMS+ uses ethnicity and sub-ethnicity as match fields; NameBridge does not (C12). Any integration must not read those fields. Document this, without judging the CPIMS+ design: in its setting, with consent and case management, it may be justified.

**Files touched:** `docs/RESEARCH_LOG.md`.

**Open questions / next steps:** confirm the integration direction with the user; if confirmed, update `SCOPE.md` (users and deliverables), `BENCHMARK_PROTOCOL.md` (new baseline), and the week 3 schema (a record shape compatible with Primero's case and trace fields).

## 2026-10-26 — Decision: CPIMS+ as integration target and baseline

**Decision (user):** adopt Primero / CPIMS+ as NameBridge's main integration target and comparison baseline, **without making it a dependency**. The core stays generic, so it remains usable with the Red Cross, REFUNITE and FSF.

**Changes:**
- `SCOPE.md`: CPIMS+ caseworkers added as future users; synonym export (week 9) and companion service (after the semester) added as deliverables; ban on reading ethnicity, sub-ethnicity, clan or religion fields from connected systems.
- `BENCHMARK_PROTOCOL.md`: CPIMS+-style baseline; new child-report error type.
- `TIMETABLE.md`: weeks 3, 6, 7 and 9, and the post-semester table.
- `THREAT_MODEL.md`: T13, unwanted fields via the API; design change 6, ingestion allowlist.

**Why:** CPIMS+ has no name-variant knowledge, an English-oriented phonetic code and relative scores (previous entry). It is the most direct route for NameBridge's variants to reach caseworkers.

**Limits accepted:**
- Synonym export carries only high-confidence variants; the calibrated scores, abstention and explanations need the companion service.
- CPIMS+ data is less structured than ours.
- The focus shifts towards children, so the 0.999 confirmation rule applies.
- AGPL means NameBridge stays a separate service.
- No CPIMS+ deployment found in Malawi, so it is a route to scale in the region, not evidence for Dzaleka.

## 2026-10-26 — Benchmark size and realism: naming profiles

**Focus:** the user questioned the 3,000-person benchmark, which Claude had chosen without a derivation, and asked how to bring reality into synthetic data without exposing real people.

**Decisions (user):**
- **Size from the targets.** `namebridge/src/namebridge/benchmark/sample_size.py` (with tests) derives the minimum from `BENCHMARK_PROTOCOL.md` §7: **25,300** people. Set to **26,000** (about 8,700 families, about 78,000 records), with equal thirds by origin (re-weighted to Dzaleka's real mix) and about half minors.
  - The binding constraint is minors' precision ≥ 0.999: 4,742 pairs with one false match allowed, × a design effect of 1.6.
  - The fairness slices need 1,471 pairs each.
- **"Patterns with sources, never people."** Five layers of reality: names, structure, variation, error rates and demography. Each parameter is sourced.
- **Naming profiles** (the user's idea): study the real list, keep only the findings, delete the raw data. Generate by recombining common elements and inventing rare ones (minimum 5 occurrences). No patterns of ethnicity, clan, tribe or religion.
- **Realism checks:** fidelity test (Jensen–Shannon divergence, local, only numbers leave), copy test (percentage only), a real-pattern test set from public variants, and a sensitivity analysis over error rates.
- **Security vs ethics:** FileVault is on and there is no Time Machine destination; iCloud Drive is active, so reference data lives in `~/namebridge-ref/`, outside synced folders. Encryption addresses leaks; minimisation (deleting the raw data) addresses the ethics.
- **For the professor:** whether NYU's IRB must confirm the aggregate use of public name lists.

**New sources:**
- NESA Rwanda exam result lists (2024/25).
- UN Security Council 1533 (DRC) sanctions-list aliases (`KAKOLELE`/`KAKORERE`, `MPAMO`/`MPANO`, `LUMISA`/`LUMINSA`/`LUMWINSA`).
- Kinyarwanda spelling reform, 13 Oct 2014 (met pushback, so old and new forms coexist).
- IJPDS 2023, South African health records: about 22% of name values differ between records of the same person; algorithms built on anglicised names fail on local names.
- Uganda EMR deduplication preprint, 2025.
- IJPDS: name errors are more frequent when the name is unfamiliar to whoever records it.

**Files touched:** `docs/BENCHMARK_PROTOCOL.md` (§2.1, §2.2, new §2.4, §8, §9, sources B11–B16), `docs/DATA_RULES.md` (DR-1), `docs/TIMETABLE.md` (weeks 4–6, progress, questions for the professor), `namebridge/src/namebridge/benchmark/`, `namebridge/tests/test_sample_size.py`.

**Open:** a Burundi name source; fidelity limits are to be set before the comparison in week 6.

## 2026-10-26 — Week 2 completion: verification and Kinyarwanda groundwork

**Focus:** close the items week 2 left unverified, and finish the Kinyarwanda groundwork (Tavily).

**Sources consulted:**
- Malawi, Data Protection Act 2024, primary text (PDF at mca.ac.mw).
- HRW, *Leave None to Tell the Story*: [Geno1-3-10](https://www.hrw.org/reports/1999/rwanda/Geno1-3-10.htm) and [Geno1-3-09](https://www.hrw.org/reports/1999/rwanda/Geno1-3-09.htm).
- Duchaj & Ntihirageza (2009), York University; Daley (2018), Oxford.
- Kimenyi (1978), "Aspects of Naming in Kinyarwanda", *Anthropological Linguistics* 20(6).
- Blog and press accounts of Rwandan naming (low confidence).
- UNHCR 2015 data protection policy §6.3.2, full conditions.
- Offensive X guide and the Act's definitions (registration threshold).

**Findings:**
- **Malawi Act, checked against its text:**
  - s. 17 (children); ss. 19–24 (rights); **s. 25 (automated decision-making)**; s. 26 (derogations); s. 29 (records); s. 30 (DPIA); s. 33 (DPO: public authority, large-scale monitoring, or large-scale sensitive data).
  - **s. 41: registration before processing for "controllers of significant importance"** (more than 10,000 data subjects resident in Malawi). A Dzaleka tracing partner likely qualifies.
  - `DPIA.md` and `THREAT_MODEL.md` corrected.
- **HRW 1999:** "Tutsi attempting to pass the barriers were usually identified by their identity cards and then slain" (Geno1-3-10). Now cited precisely for M9 / T8.
- **Burundi names (Duchaj & Ntihirageza 2009):** the Kirundi name is given first, and a French Christian name is added later, when "the original name becomes the surname". **Burundian refugees in Tanzanian towns changed to Swahili names** as a strategy of invisibility, and some kept pseudonyms after naturalisation (Daley 2018). Consequences:
  - new error type, "adopted name in exile" (`BENCHMARK_PROTOCOL.md` §2.3);
  - new threat **T14**: matching across a deliberate name change, routed as a protected-person case;
  - `SCOPE.md` §1 updated.
- **Kinyarwanda (Kimenyi 1978):** gender-marked prefixes — `nyira-`, `mukaa-`, `kaa-` feminine; `nya-`, `munya-`, `see-`, `nyiri-`, `rwaa-`, `ki-` masculine. Used only to keep generated names consistent with generated sex; never to infer sex (C12).
- **Rwanda fathers'-surname conflict:** accounts describe an optional third name from the father's side, and sibling names sharing a root as a "familial theme" (blogs, 2011; New Times, 2026), against HRW / Wikipedia, which say surnames are not inherited. Modelled as a varied parameter *q*, like Burundi's *p*. Low confidence until a statistical source exists (the NESA lists may show it in week 4).
- **UNHCR 2015 policy §6.3.2:** law-enforcement transfers only for a serious criminal offence, to a competent authority, if the transfer substantially assists and the data cannot otherwise be obtained, if it is proportionate, and **with consent for victims and witnesses**.
- **Still open:** the text of the 2022 GDPP on this point could not be fetched (Refworld blocked the extract).

**Files touched:** `docs/DPIA.md`, `docs/THREAT_MODEL.md` (T14, sources), `docs/SCOPE.md` (§1, S18), `docs/BENCHMARK_PROTOCOL.md` (§2.2, §2.3, B17–B18), `docs/TIMETABLE.md`.

**Week 2 status:** complete, except the GDPP 2022 text and the professor's review.

## 2026-10-26 — Deliberate name change in exile: patterns and rules

**Focus:** the user asked for name change in exile to be "taken into account in every context", and asked whether there is a pattern.

**Sources consulted:**
- Duchaj & Ntihirageza (2009), abstract via YorkSpace (full text could not be fetched).
- Malkki (1995) via *African Studies Quarterly*.
- Daley (2018), *Migration and Society*.
- IRRI, *A Dangerous Impasse* (2010).
- *American Ethnologist*, "Names are Problems".
- TRT Afrika and VOA (Jun 2023).

**Findings:**
- **The change is ordered (Burundians in Tanzania).** The Christian given name is replaced first, often by a Muslim name, and the Kirundi surname is kept. The surname is changed only if "too noticeable", to a Burundian name that passes as Tanzanian (Ha). It happens in towns and minority settings, not in settlements, and continues after naturalisation.
- **Rwandans in Uganda** change names *and* claim another nationality (Congolese) or a local ethnicity (Banyankole).
- **Congolese refugees** keep open names and close names by design, use interchangeable spellings (`Rashindi`/`Kashindi`) and use kinship terms loosely. UNHCR staff treated discrepancies with suspicion, which can harm protection cases.
- **Malawi, 2023:** the government said 55 genocide suspects sought by Rwanda may be hiding under Malawian names, and began revoking citizenships and passports; critics warned it could ensnare legitimate refugees. In 2020, a former Minister of Homeland Security was jailed for selling citizenship to Burundians and Rwandans.

**Decisions:**
- New cross-cutting document `docs/NAME_CHANGE.md` with seven rules: no edges between unrelated names; "possible name change" routed as a protected-person case; nationality is weak evidence; names never used as credibility evidence; no support for verification or revocation campaigns; intake takes the names a person chooses; name-change rate depends on setting.
- `SCOPE.md` §4: two new prohibited uses.
- `THREAT_MODEL.md`: T14 refined; new **T15** (output used against a refugee's credibility).
- `BENCHMARK_PROTOCOL.md`: ordered error type (*s1* > *s2*, both varied).
- `DATA_RULES.md`: intake rule.
- `TIMETABLE.md`: weeks 3 and 7.

**Open:** no study of name change among refugees in Malawi; rates of step 1 and step 2 unknown.

## 2026-10-26 — NYU IRB and public name lists (gate G3)

**Focus:** the user asked for research on whether NYU's IRB must review the aggregate use of public name lists.

**Sources consulted:**
- 45 CFR 46.102(e) and 46.104(d)(4) (Cornell LII, eCFR).
- NYU HRPP: How to Apply, Forms & Guidance, the Human Subjects Research Decision Tree (PDF), and the NHSR checklist.
- UAB on exempt category 4.
- NIH IRBO on NHSR (for comparison).

**Findings:**
- A human subject requires interaction **or identifiable *private* information**. Information is private only if a person can reasonably expect it will not be made public. Published exam results and the UN list are public.
- NYU's decision tree: publicly available existing data → "Not human subjects research. No application to the IRB office is needed."
- NYU HRPP: investigators need no formal determination **if sure**; if unsure, contact the HRPP. Formal NHSR is an abridged Cayuse application, usually for an external party (funder, data provider, journal).
- **Likely result: NHSR.** Reasons to still ask: the names are identifiable, some of minors; the topic is sensitive; publication is possible.
- **Not covered:** contact with people (native-speaker review in 2027) and phase 3 case data **will** be human subjects research.

**Output:** `docs/IRB_DETERMINATION.md` with three options (A self-determine; B email the HRPP, recommended; C formal NHSR via Cayuse) and a draft email. G3 updated in `TIMETABLE.md`; future IRB need noted under "not gates for the semester".

**Gate status:** G3 stays **open (hard)**. The professor chooses A, B or C; it closes when a written answer is recorded.

## 2026-10-28 — Unblocked work during the professor meeting: G6, UNHCR 2022, Malawi, G4/G5 examples

**Focus:** while G1–G3 wait for today's meeting, the user asked to advance everything not blocked by a gate (Tavily).

**Gate check:** G1 is open, so phase 1 work was not started. The items below are phase 0 gaps (UNHCR policy, Malawi name change), our own soft gate G6 (choosing a source; nothing downloaded) and decision support for G4/G5.

### G6: a source for Burundian names

| Candidate | What it is | Verdict |
| --- | --- | --- |
| **CENI 2025 candidate lists** ([e.g. Bujumbura province, National Assembly](https://www.ceniburundi.bi/wp-content/uploads/2025/02/BUJUMBURA-CANDIDATS-DEPUTES-2025.pdf); also communal lists, per [U. Antwerp archive](https://www.uantwerpen.be/en/projects/centre-des-grands-lacs-afrique/droit-pouvoir-paix-burundi/elections/elections-2025)) | Official "liste nominative définitive des candidats": surname in capitals, given names, birth year, sex, **ethnicity (Hutu/Tutsi/Twa)**, residence. Public by law; published Jan–Feb 2025 | **Proposed** as the Burundi profile source, on conditions (below) |
| National exam lists (concours national, 9th year) | Results announced publicly, but the orientation lists go to provincial offices (RTNB on X, 27 Aug 2026); no public name list found | Not available |
| `names-dataset` (PyPI, philipperemy) | 730k first names, 983k last names, Burundi included | **Rejected:** built from the 2021 Facebook leak of 533M accounts (its own README). Breach data; incompatible with `DATA_RULES.md` |
| Kimenyi 1989, *Kinyarwanda and Kirundi Names* (appendix: most popular names) | Book (Edwin Mellen) | Use for meanings and structure only; copyrighted, no frequencies |
| IJTPD 2016, "A Context-Based Approach to the Study of Names" (University of Burundi) | 70 student respondents; Kirundi surnames of Christian origin dominate; 54% named by the father | Structure only; sample too small for frequencies |

**Conditions on CENI** (proposed; user to confirm, since G6 is ours):

1. The parser **drops the ethnicity column on read**; it is never written to disk, counted or joined. This is stricter than DR-1.2, and is the ethnicity guard (T13) applied at ingestion.
2. The source is **named in the G3 email** to the HRPP (done in `IRB_DETERMINATION.md`), because the raw files contain ethnicity.
3. **Known bias:** adults only (born about 1955–2000), political candidates, more men. Recorded as a fidelity limit; Burundian children's names in the benchmark lean on the given-name trend sources instead.
4. Nothing downloaded until G3 closes. *What was read today:* only an extract of one PDF, to check its columns. No names were saved.

### UNHCR's 2022 General Policy (GDPP) on law-enforcement transfers

- Refworld (two URLs) and the UNHCR blog still fail to extract. Dzaleka Online Services lists the PDF (720 KB, 15 Oct 2022) without a working link in the extract.
- Indirect evidence: UNHCR's 2025 complementary-pathways guidance cites **GDPP para. 35** (inform the data subject before disclosing fraud-related data, with a right to object) and **para. 44** (assess the third party's protection before sharing).
- **Still open.** The 2015 policy §6.3 (serious crime, competent authority, etc.) remains our reference. *Next step:* download the PDF by hand in a browser and read it.

### Malawi name change

- Still no study of refugees changing names in Malawi.
- New: a documented chain of aliases for one genocide suspect (Rwandan → three Burundian aliases → a Malawian identity; Malawian passport 2007). Single source chain (The New Times via Nyasa Times, Jun 2023). Added to `NAME_CHANGE.md` §4 [N9] **without the names** (DR-1.1).
- New: 396 foreigners' papers revoked in 2023; a critic called it "indiscriminate" [N10].
- **Consequence:** the only Malawi evidence concerns alleged perpetrators, which rule 5 excludes, so it does not set benchmark rates.

### G4/G5 examples

- New `docs/GATE_EXAMPLES.md`: three invented cases for G4 (retrieval miss, minor false match, adult false match) and four for G5 (C1–C4), with options A/B/C for rule 5 (recommended: A).
- Possible new rule raised for G4: a minor never reaches "strong evidence" without a non-name check.

**Open:** user to confirm the CENI source for G6; GDPP text; professor's decisions on G1–G5.

## 2026-10-28 (later) — G6 closed: how the Burundi profile is built

**Question from the user:** how many names do the CENI lists hold, is there another safe source, and could social-media data be used with our filter?

**Findings:**
- **CENI size:** the 5 provincial National Assembly PDFs (e.g. Gitega 28 pages, Butanyerera 34 pages; party lists of up to about 46). Estimate **about 3,000–6,000 names**, not counted, because downloading waits for G3. After the ≥ 5 filter, only common elements survive. Commune and hill-council candidate lists (e.g. 486 candidates in one commune, *Le Renouveau*) were not found online.
- **Forebears.io:** already aggregated (8,340 Burundian surnames and 6,435 given names, with incidence). Its sources and terms pages could not be fetched; it is commercial; noise ("Jean" as a surname, "Mama" as a given name) suggests social-media-like inputs. Usable only as a cross-check, citing the figures, never copying the tables.
- **Kirundi and Kinyarwanda** are dialects of one language and share most of their name stock (Kimenyi 1989, *Kinyarwanda and Kirundi Names*, abstract via AfricaBib). The NESA lists, which are large and include minors, therefore cover most Burundian name elements.

**Social-media data refused**, with the filter or without it:
1. The people the rules protect are in it: refugees who changed their names (`NAME_CHANGE.md` rules 1 and 5).
2. Social-media profiles are probably not "public" in the IRB sense, so using them would likely be human subjects research and would undo the G3 analysis.
3. Platform terms of service forbid scraping; the only ready-made Burundi set is breach data (`names-dataset`).
4. Quality is poor: nicknames, "Mama X", pseudonyms.

**Decision (user, 28 Oct 2026), G6 closed:** the Burundi profile is built from **NESA name elements weighted by CENI 2025 frequencies** (ethnicity column dropped on read), plus the sourced Kirundi spelling differences; **Forebears aggregates as a cross-check only**.

**Risk:** the Burundi third of the benchmark may look too Rwandan. The week 6 fidelity test measures it per origin.
**Still gated:** downloading NESA and CENI waits for G3.

## 2026-10-28 (later) — UNHCR's 2022 General Policy (GDPP) read

**Source:** UNHCR, *General Policy on Personal Data Protection and Privacy*, approved 20 Dec 2022, in force 31 Dec 2022, review by 31 Dec 2027 ([Refworld](https://www.refworld.org/policy/strategy/unhcr/2022/en/124207)). PDF downloaded by hand by the user (Refworld blocks automated tools). The PDF has 16 pages; **the annexes, including Annex 1 on transition, are not in it**.

**Findings:**
- **No law-enforcement section.** The GDPP has no equivalent of the 2015 policy's §6.3 (transfer to national law-enforcement agencies and courts). Sharing with any third party falls under **para. 44**: only "based on arrangements that afford an adequate level of protection", in line with the principles and the rights of data subjects.
- **The 2015 policy stays in force.** Para. 75(a): for persons of concern, the 2015 policy "will be deemed an implementing instrument" under para. 16. So the 2015 §6.3.2 conditions (serious criminal offence, competent authority, and so on) still apply. Our references [S12] and [T11] are therefore correct, not outdated.
- **Limitations (paras 62–63):** data-subject rights may be limited for safety and security, "investigatory and disciplinary proceedings", overriding operational needs, or the overriding rights of others. Each limitation must be issued by senior management or the data controller, documented, necessary and proportionate.
- **Automated decisions (para. 41):** no automated decision with significant adverse effects, except with consent, for a contract, or when explicitly authorised. **Para. 42:** assess and mitigate the risks of automated decision-making. This matches our rule that confirmation is always a human decision (`BENCHMARK_PROTOCOL.md` §7) and the Malawi Act s. 25.
- **Objection (para. 35):** a right to object at any time on grounds relating to the person's particular situation. Cited in UNHCR's 2025 complementary-pathways guidance for fraud disclosures.
- **Sensitive data (footnote 3):** "Given the particularly vulnerable position of persons of concern to UNHCR, the nature of their personal data is generally sensitive"; data on offences and criminal proceedings is listed as sensitive.

**Consequences:**
- NameBridge's rule (no government or police users; no law-enforcement transfers) stays **stricter** than UNHCR's, which permits transfers under the 2015 §6.3 conditions. This is a deliberate difference to explain to partners that use UNHCR's standard.
- If a tracing partner works under UNHCR, its data-sharing arrangement must meet para. 44, and our DPIA must answer para. 42 (risks of automated decisions).
- `SCOPE.md` [S12] and `THREAT_MODEL.md` [T11] updated; the open item is closed in `TIMETABLE.md`.

**Not verified:** Annex 1 (the transition activities), which may say when the 2015 policy is to be replaced.

## 2026-10-28 (later) — Commercial use reopened; gate G7

**Decision (user, 28 Oct 2026):** the 19 Oct rule "NameBridge is not sold" is withdrawn. Selling or licensing later is an open option; the free offer to tracing services and FSF stays. Nothing else is decided.

**Facts checked:**
- NYU [Statement of Policy on Intellectual Property](https://www.nyu.edu/about/policies-guidelines-compliance/policies-and-guidelines/policy-intellectual-property.html) §4.7 (accessed 28 Oct 2026): "Students generally own copyright in coursework they create", except where rights are assigned for particular courses or the work falls under NYU-ownership provisions (§4.1), e.g. research projects or sponsored programs "under the auspices of NYU". Faculty supervising students "should inform Students in advance if participation may result in NYU ownership". Not yet read: §4.1 itself.
- The repo `Ethical-Tech-CoLab/Fraternity` is **public**: code already published under Apache-2.0 may be used and sold by anyone, irrevocably. Only future versions can change licence, and only if all copyright holders agree.

**Changes:** `CONCEPT-IDEA.md` final phase; `TIMETABLE.md` final-phase row and new gate **G7** (ownership, licence, deal terms).

## 2026-10-28 (later) — Rule 5 reworded: trace people who changed names, safely

**User's point (28 Oct 2026):** a person may change name to protect themselves, or after trafficking, and still want to be found by relatives, safely. Rule 5 as written ("no support … for searches for people who changed their names") weakened the main purpose of NameBridge.

**Decision (user):** rule 5 reworded. Tracing people who changed their names is **supported**; searches whose purpose is to expose or verify an identity against the person's will (campaigns, alleged perpetrators) are not. This only clarifies what case C1 already allowed. `SCOPE.md` §4 now uses the same wording; it is still under the professor's G1 review.

**Added:**
- `NAME_CHANGE.md`: "safety layers" table (9 layers, mapped to the existing controls and threats: C1–C2, C6–C9, M2, T1, T3, T4, T6, T8, T14). The public dictionary holds spelling variants only, so it reveals no name changes.
- `GATE_EXAMPLES.md`: case C5 (trafficking survivor, found by her sister with checks); a second G5 question: a **restricted name-change layer** (substitution patterns, never published or exported, used only in protected cases).
- `TIMETABLE.md` G5 row updated.

## 2026-10-28 (evening) — Professor meeting: G1, G2, G3, G7 closed; G5 partly

**Decisions (professor, reported by the user):**
- **G1:** `SCOPE.md` approved.
- **G2:** governments and law enforcement are not users.
- **G3:** option **A**: NYU IRB review is not needed (recorded in `IRB_DETERMINATION.md`, Decision).
- **G5:** alleged perpetrators, option **A** (never searched for). Restricted name-change layer: **yes, with conditions** (sourced patterns, week 7 access controls, legal check). *Corrected the same evening: first recorded as not discussed.*
- **G7:** NameBridge stays open source; no intention to sell, because the work is humanitarian; licences may be offered where useful. No owner needs to be named, because it is open source. *Corrected the same evening: first recorded as not discussed.* This replaces the afternoon note "commercial use reopened".
- **G4:** not discussed; the 26 Oct defaults stay in use.

**Consequences:** week 3 (schema and validator) may start. In week 4, the public lists (CongoNames, NESA, CENI, the UN list) may be downloaded and processed under `DATA_RULES.md` DR-1 (study, keep aggregates, delete). Agenda with answers: `MEETING_2026-10-28.md`.

## 2026-10-28 (evening) — Week 3 started: schema and validators

**Built** (`namebridge/src/namebridge/schema/`, 38 tests passing):
- `name_graph`: the public Name Knowledge Graph (§5.1A). It rejects unknown relation types, with a pointer to `NAME_CHANGE.md` rule 1, so adopted names cannot enter. It also rejects any `layer` other than public (the restricted layer is separate; G5), generated edges that are not `proposed`, reviewed edges without a reviewer or source, edges without any source, `married_or_previous_form_of` unless attached to a Rule, and ethnicity, clan or religion attributes anywhere.
- `case_graph`: the protected case graph, schema only (§5.1B). Fact metadata; lawful basis (Malawi DPA s. 8); a minor or a `possible_name_change` forces a flag and the protected route; guardian consent for minors (s. 17); only a human can confirm a match (GDPP para. 41; s. 25); relationships reported, never inferred; biometrics only as pointers; contact and location always high sensitivity.
- `ingest`: CPIMS+/Primero allowlist. Names are kept whole; unknown fields are dropped; ethnicity, sub-ethnicity and religion fields are refused by name, and their values are never copied (T13).
- `pack`: the language-pack template (§11) and validator; `data/packs/TEMPLATE.json`.

**Decision (Claude, user may change):** storage is JSON / JSON Lines, so the package needs only the standard library (no YAML dependency).
**Remaining in week 3:** Kirundi spelling rules (research).

## 2026-10-28 (evening) — Kirundi spelling rules (week 3 research)

**Sources:**
- [K1] *Kinyarwanda and Kirundi Comparative Grammar*, Dunwoody Press, 2007, ISBN 978-1-931546-32-4 (ISBN as given on the [dokumen.pub record](https://dokumen.pub/kinyarwanda-and-kirundi-comparative-grammar-9781931546324.html); [PDF extract](https://www.matana.de/kirundi_kinyarwanda.pdf), §1.1.1, Table 1). Authors are not shown in the extract; *to confirm* (believed to be Zorc & Nibagwire).
- [K2] Wikipedia, [Rwanda-Rundi](https://en.wikipedia.org/wiki/Rwanda-Rundi), "Spelling" table (same four rules; consistent with [K1]).
- [K3] Forebears, [Burundi surnames](https://forebears.io/burundi/surnames) (accessed 28 Oct 2026): *Havyarimana* is ranked 25th in Burundi.
- [K4] Omniglot snippet: a standardised Kirundi spelling since the 1940s, with "slightly different" Catholic and Protestant mission spellings. *Single source; page not fetched.*

**Findings:**
- **Four spelling differences are automatic** [K1][K2]: Kinyarwanda «cy» → Kirundi «c», «jy» → «j», «shy» → «sh», «by» → «vy». Examples: *cyane* / *cane*, *-jya* / *-ja*, *nshya* / *nsha*, *umubyeyi* / *umuvyeyi*.
- **They work one way only.** Kinyarwanda → Kirundi is deterministic. Kirundi → Kinyarwanda is not, because both languages also have plain «sh» (*ishami*, *igishanga*) [K1]. So the matcher must generate *both* options when going from Kirundi: sh → {sh, shy}, c → {c, cy}, j → {j, jy}, vy → {vy, by}.
- **The rule shows up in names:** *Habyarimana* (Rwandan spelling) and *Havyarimana* (Burundian spelling, [K3]) are the same name.
- **Other differences are sporadic** (e.g. Rundi «-anka» / Rwanda «-anga»), so they need sourced word-by-word edges, not rules [K1].
- **Tone and length marks** (circumflex, macron, caron) appear in linguistic writing [K2]. Registries and lists normally use plain letters, so search forms fold them; the original form is still kept (§5.3).

**Consequences:**
- **G6 profile:** the Kinyarwanda → Kirundi direction is deterministic, so NESA name elements can be converted to Burundian spelling before the CENI weighting.
- **Week 4 `bi-kirundi` pack:** the four rules go in as `transliteration_rules` (practice: cultural/orthographic, confidence: high, source [K1]). The graph gets a Rule node plus sourced `orthographic_variant_of` edges.
- **Open:** the Catholic vs Protestant mission spellings [K4]; to check in week 4.

## 2026-10-28 (evening) — Sound layer: names told aloud

**User's idea (28 Oct 2026):** a child who cannot read knows names only as sounds. The person who writes them down may mishear because of accent, and spells them with their own habits. The model must cover sounds, digraphs that are one sound, and the possible spellings.

**Sources:**
- [P1] *Kinyarwanda and Kirundi Comparative Grammar* (Dunwoody Press, 2007; [extract](https://www.matana.de/kirundi_kinyarwanda.pdf)), ch. 2, Tables 25–27: the consonant inventory (prenasalised stops, *cy*, *jy*, *shy*, *pf*, *ts*), and the linguists' disagreement over which consonants exist (Kirundi 19–26 consonants, also per [Wikipedia](https://en.wikipedia.org/wiki/Kirundi)).
- [P2] "Phonological Aspects of Loanword Adaptation in Kinyarwanda", *IJLRHSS* 3(3) ([PDF](http://www.ijlrhss.com/paper/volume-3-issue-3/3-HSS-598.pdf)): [r] and [l] are allophones of one phoneme. Ministry of Education spelling rules keep «l» only in proper nouns that already used it and in unintegrated loanwords (e.g. *Kamali*, *Kigali*). Note: the same name can be heard and written with r or l.
- [P3] Wikipedia, [French orthography](https://en.wikipedia.org/wiki/French_orthography): /w/ usually written «ou»; «ch» = /ʃ/; «dj» = /dʒ/; «tch» = /tʃ/. English «ch» = /tʃ/ ([Collins](https://grammar.collinsdictionary.com/us/pronunciation-guide-fr/different-sounds-of-letters)).
- [P4] UNESCO, [*The Standardization of the spelling of African names*](https://unesdoc.unesco.org/ark:/48223/pf0000059805): French and English writers spelled the same African names differently ("Ouoloffes" vs "Jolof").
- [P5] Mani, Yeh & Condon, ["Learning to Match Names Across Languages"](https://aclanthology.org/W08-1402.pdf), MITRE, Coling 2008 workshop: matching by pronunciation, using per-language grapheme-to-phoneme rules or cross-language rules.
- [P6] Apache Solr guide, [Phonetic matching](https://solr.apache.org/guide/solr/latest/indexing-guide/phonetic-matching.html): Beider-Morse applies language-specific rules; Soundex and Metaphone families are English-centred.

**Design:** `CONCEPT-IDEA.md` §5.4A. Three pack lists (sound inventory; writing conventions by writer language; listener confusions), plus `recorded_by_convention` on oral-report names. Sound is one more comparison field, never sufficient on its own.

**Code (42 tests):** the pack schema and template gain `phoneme_inventory`, `spelling_conventions` and `listener_confusions` (each entry needs a source; confidence may be `hypothesis`); an `oral_report` ObservedName must record `recorded_by_convention`.

**Gaps:**
- No source yet on how children mispronounce or simplify Kirundi or Kinyarwanda names.
- No source yet on Chichewa spelling habits (Malawian caseworkers).
- Listener confusions beyond r/l are hypotheses.
- Checking these with native speakers is planned for Jan–Mar 2027 and needs IRB review if it involves people (`IRB_DETERMINATION.md`).

## 2026-10-28 (night) — Week 3 review: diagnosis and fixes

**Why:** the user asked for a diagnosis of week 3, which had been marked ✔ too early. Two bugs and seven half-enforced rules were found and fixed (63 tests, from 42).

**Bugs fixed:**
- **B1, relatives lost:** in a Primero *case*, relatives are nested in `family_details_section` (checked in Primero's `db/dev_fixtures/cases.rb`, 28 Oct 2026); only *traces* have a flat `relation_name` (`doc/api/traces/id/get.md`). Ingestion now reads the nested list with its own allowlist.
- **B2, ethnicity inside an allowed field:** an allowed field holding a nested object is now dropped whole, and forbidden keys inside it are reported by name at any depth.

**Rules completed:**
- **R1** spelling, sound and romanisation variants must reach Jaro-Winkler ≥ 0.8 on folded forms (threshold from Grannis et al. 2004, PMID 15360771: highest linkage sensitivity at 0.8). Below that, the edge must be reviewed, attested or expert, and give a reason. Checked on real pairs: Kakolele/Kakorere 0.90, Habyarimana/Havyarimana 0.95, Ciza/Tchiza 0.89, Rwanda/Ruanda 0.90 pass; Jean/Hamisi 0.47 fails. This enforces `NAME_CHANGE.md` rule 1 even when a variant type is misused.
- **R2** a confirmation needs at least one piece of non-name evidence.
- **R3** a CPIMS+ case without `consent_for_tracing = true` is refused whole (Primero's matching only searches such cases).
- **R4** case records need `created_at` and `retain_until`.
- **R5** every entry in every pack rule list needs a source and a confidence.
- **R6** link types join only the right node types; transliteration needs two scripts.
- **R7** ingested names become ObservedName nodes that pass the case schema.
- **M1** GitHub Actions runs the tests and validators on Python 3.10 and 3.12 (3.9, the local Python, is not offered on the runner; it is tested locally) (`.github/workflows/namebridge-tests.yml`).
- **M2** `docs/SCHEMA.md`, the schema in plain language for reviewers.
- **M3** duplicate links and contradictions (variant + not equivalent) are rejected.
- **M4** name text must be Unicode NFC (W3C Character Model, "Content authors SHOULD use … NFC"); full ICU set-up stays in week 4.

**Research (Tavily):**
- **[K1] authors confirmed:** R. David Zorc and Louise Nibagwire, Dunwoody Press, 2007 ([Stanford SearchWorks](https://searchworks.stanford.edu/view/7513422); [WorldCat](https://search.worldcat.org/title/Kinyarwanda-and-Kirundi-comparative-grammar/oclc/182537195)).
- **Kirundi spelling variation, second and third sources:**
  - Mioni (1975), ["The standardization of the orthography in Rundi"](https://www.africabib.org/rec.php?RID=188045899): "in Burundi, it is more a question of orthographic habits than of an orthographic code".
  - Nassenstein, ["Kinyarwanda and Kirundi: On Colonial Divisions…"](https://journals.uhk.cz/modernafrica/article/download/184/180/361), *Modern Africa*: missionary orthographies, and the *by*/*vy* divergence.
  - So spelling habits varied, as the Omniglot snippet said. The specific Catholic vs Protestant differences are **still not documented**; Mioni's full text is the next place to look.

## 2026-10-28 (night) — Catholic vs Protestant Kirundi spelling; how written clusters sound

**Question:** the open item from the week 3 review: what are the Catholic vs Protestant spelling differences in Kirundi?

**Sources:**
- [O1] Mioni, A. (1975), "The standardization of the orthography in Rundi", *Journal of the Language Association of Eastern Africa* 3(1): 21–26 ([AfricaBib](https://www.africabib.org/rec.php?RID=188045899)); a 1968 Dar es Salaam conference paper. **Abstract only; the full text is not online.** A related book: Mioni (1970), *Problèmes de linguistique, d'orthographe et de coordination culturelle au Burundi* ([HathiTrust record](https://catalog.hathitrust.org/Record/003153779)).
- [O2] Cox, E. E. (1969), Kirundi-English dictionary, Marston Memorial Historical Center; revised edition by M. Philipps, Feb 2023 ([PDF](https://www.matana.de/kirundi.pdf)). It contains "Orthography rules … drawn up by an orthography committee of the Alliance" (the Protestant missions' alliance).
- [O3] Wikipedia (fr), [Église catholique au Burundi](https://fr.wikipedia.org/wiki/%C3%89glise_catholique_au_Burundi): the White Fathers (Catholic) introduced the Latin alphabet and spelling for Kirundi and Kinyarwanda; over 70% of Burundians were Catholic by 1930.
- [O4] Foreign Service Institute, *Kirundi Basic Course* (US government; based on Meeussen 1959, *Essai de grammaire rundi*) ([PDF](https://fsi-languages.yojik.eu/languages/FSI/Kirundi/Basic/FSI%20-%20Kirundi%20Basic%20Course%20-%20Student%20Text.pdf)), pronunciation synopsis.
- [O5] Nassenstein, *Modern Africa* (already cited, 28 Oct): missionaries chose «mw» for [mg], «rw» for [rgw], «tw» for [tkw].

**Findings:**
- **Catholic vs Protestant: the letter-by-letter differences are still not documented.** Mioni's abstract says only that "most of these habits were fixed in the first years of this century", which suggests habits, not a code [O1]. The Protestant committee's rules that we can read [O2] are about **apostrophes, elision and word division** (*n'uko* vs *nuko*; *Harih' ibitabo*). They also say "in some areas, people make the o a w before a and i, but we do not write it that way". Inference, not confirmed: the mission differences may lie more in word division and apostrophes than in letters. For names, that means joined vs split forms and apostrophes should be treated as variants (`hypothesis`). The Catholic spelling comes from the White Fathers [O3].
- **Useful for the sound layer (two consistent sources):** written clusters are pronounced quite differently from their letters. «sw» often sounds like [skw]; «mw» like [my] or [mg]; «rw» like [rgw]; «vy» may contain a [z] sound; «tw» like [tkw] [O4][O5]. A listener who does not know Kirundi spelling may write what they hear, e.g. *rgw*, *skw* or *tkw* for «rw», «sw», «tw». These pairs go into the Kirundi and Kinyarwanda `listener_confusions` in week 4, with confidence `medium` (sourced pronunciation, but not a study of how listeners write it).

**Next:** the full text of Mioni (1975) or (1970) would need library access (NYU Libraries / interlibrary loan). Not blocking; week 4 records the mission question as `disputed` / `hypothesis`.

## 2026-10-28 (night) — Literacy in the corridor: the sound layer is core

**User's point (28 Oct 2026):** it is not only children; illiteracy is high in the region, so the phonetic part is very important.

**Data** (adult literacy, ages 15+, "read and write a short, simple statement"; UNESCO UIS series via [countryeconomy](https://countryeconomy.com/demography/literacy-rate/burundi), [FRED/World Bank](https://fred.stlouisfed.org/series/SEADTLITRZSMWI) and [TheGlobalEconomy](https://www.theglobaleconomy.com/Democratic-Republic-of-the-Congo/Literacy_rate); accessed 28 Oct 2026):

| Country | Adults | Women | Men | Youth 15–24 | Notes |
| --- | --- | --- | --- | --- | --- |
| Burundi | 75.5% (2022) | 69.4% | 81.8% | 93.6% | 37% in 1990, so older adults are far less literate. *Conflict:* RegionWeek (secondary) reports 85.6% for 2021 |
| DRC | 80.5% (2022) | 71.7% | 89.6% | 88.1% | *Conflict:* another UNESCO-sourced series gives 68.5% (2023) |
| Malawi | 68.1% (2022) | 65.1% | 71.4% | 76.8% | *Conflict:* the MIP-1 plan quotes men 83%, women 68.8% |
| Rwanda | ~70–73% | 68% | 73% | — | Secondary sources only (RegionWeek; versus.com); to confirm |
| Refugees (global) | ~60% | — | — | — | Attributed to UNESCO by RefuSHE (Facebook post); **unverified, single source** |

No literacy figure for Dzaleka itself was found. The 2023 Dzaleka Education Assessment ([DOS](https://services.dzaleka.com/resources/dzaleka-education-assessment-2023)) points to microdata in UNHCR's Microdata Library; not yet checked.

**Reading:**
- About one adult in four to one in three cannot read or write in the corridor countries.
- Women and older adults, the parents and grandparents who search for children, are the least literate.
- Literacy does not settle the problem anyway: at registration a clerk or caseworker usually types the name, often in another language.

**Decisions:**
- `CONCEPT-IDEA.md` §5.4A: the sound layer covers children, adults who cannot read, and names typed by others; sound becomes a **core comparison**.
- `BENCHMARK_PROTOCOL.md`: a new source, "name written by ear", with the writer's convention. Its share is a varied parameter, higher for older adults and women. A new error type, "written by ear", and a new fairness slice, "who wrote the name".
- `TIMETABLE.md` week 7: sound comparison is a core field, reported per slice.

**Next:** check the Dzaleka 2023 education microdata for adult literacy (UNHCR Microdata Library).

## 2026-10-28 (night) — Literacy in Dzaleka itself: what the surveys hold

**Question:** is there a literacy figure for Dzaleka?

**Sources checked (metadata and reports only; no microdata downloaded):**
- **Dzaleka Education Assessment 2023** ([DOS entry](https://services.dzaleka.com/resources/dzaleka-education-assessment-2023)): a pointer to UNHCR's Microdata Library; no figures published on the page.
- **UNHCR Results Monitoring Survey (RMS) Malawi 2023** ([catalog 1119](https://microdata.unhcr.org/index.php/catalog/1119)): Dzaleka, Oct 2022–Mar 2023, 333 households, 1,323 individuals. Its individual data dictionary has school attendance and level (EDU01–EDU04) but **no literacy question**.
- **UNHCR Socio-economic assessment, Dzaleka and Luwani, 2017** ([catalog 185](https://microdata.unhcr.org/index.php/catalog/185)): 802 Dzaleka households, March 2017. Its scope lists "education/literacy" for household members, released as an "edited, anonymous dataset for public distribution" (538 household-level variables). From the [report](https://microdata.unhcr.org/index.php/catalog/185/download/410), read in extracts only (the direct download returns a login page):
  - Dzaleka household heads by origin: DRC 42%, Burundi 28%, Rwanda 26%, other 4%.
  - The report's only statement on literacy is qualitative: "Many in the host communities cannot read and write … In the refugee community … many of them have some level of education."

**Findings:**
- **No published literacy figure for Dzaleka was found.**
- Qualitatively, refugees in Dzaleka were *more* educated than the surrounding Malawian communities in 2017 [SEA 2017]. So the national figures (`RESEARCH_LOG.md`, literacy entry) may overstate illiteracy among camp adults.
- The case for a core sound layer still holds:
  - names are mostly typed by clerks and caseworkers in another language;
  - children, women and older adults are the least literate;
  - the 2017 data is old, and arrivals since then have changed the population.

**Option, not taken (needs the user's decision):** register on the UNHCR Microdata Library, accept its terms, and compute the literacy share from the 2017 anonymised file. It is de-identified data about real refugees: not names, but outside what G3 covered (public name lists only). It would need its own short check under `DATA_RULES.md` and `IRB_DETERMINATION.md` before use. **Not needed for the semester:** the benchmark already treats the "written by ear" share as a varied parameter.

## 2026-10-28 (night) — Full review: blind spots found and fixed

**Why:** the user asked for a review of everything done, looking for anything that should be complete but is not.

**Blind spots found and fixed:**
1. **The ethnicity guard was English-only.** It missed "Ethnie", the CENI column name and exactly the source chosen for G6, as well as *tribu*, *ubwoko*, *idini*, *kabila* and *dini*. Meanings checked:
   - *ubwoko* = "race, nation, tribe, kind" ([matana Kirundi dictionary](https://www.matana.de/index1.php?deep=&q=ubwoko)); Rwandan *ubwooko* = social group, clan ([Schoenbrun, Northwestern](https://history.northwestern.edu/documents/people/faculty/schoenbrun/schoenbrun-rwanda-dictionary.pdf));
   - *idini* = religion (Kinyarwanda; Muzungu, *Idini gakondo y'Abanyarwanda*);
   - Swahili *kabila* = tribe, clan and *dini* = religion ([Swahili-English dictionary](https://archive.org/download/swahilienglishdi00madauoft/swahilienglishdi00madauoft.pdf)).

   The guard now matches stems anywhere and short words as whole words (`test_guard.py`); new threat **T18**; new rule **DATA_RULES DR-1.7** (drop on read). Lingala words are not covered yet.
2. **"Who wrote the name" was designed, but not in the schema.** The benchmark slice existed, yet ObservedName had no field for it. Added `written_by` (self / other / unknown); a name written by someone else needs `recorded_by_convention`; an oral report can never be self-written; CPIMS+ names are marked `other`.
3. **`CONCEPT-IDEA.md` §8 control 2** still described a law-enforcement access role, contradicting G2; annotated.
4. **`BENCHMARK_PROTOCOL.md` §2.4** still said the Burundi source was a "gap"; updated with the G6 decision.
5. **`CONCEPT-IDEA.md` §5.3 and §11** lacked the new fields (`written_by`, `recorded_by_convention`, the three sound-layer lists); added.
6. **The threat model** had nothing for the decisions taken today: **T16** (restricted name-change layer leaks), **T17** (sound layer widens candidate lists), **T18** (multilingual ethnicity fields).
7. **The restricted-layer conditions** (G5) were not tracked as a task; week 7 now says it is not built there, and lists its three preconditions.
8. **`SCOPE.md`** named only CongoNames as a source; it now lists the decided profile sources.
9. **`NAME_CHANGE.md` rule 1** did not say how it is enforced; it now points to the validator.
10. `.DS_Store` is now in `.gitignore`.

**Known open items (not blind spots; recorded elsewhere):**
- G4: error costs, and whether "minor" means under 18 at the search or at separation. `subject_is_minor` stays a declared flag until then.
- Lingala and eastern-DRC field names in the guard.
- Mioni (1975) full text.
- Children's pronunciation and Chichewa spelling sources.
- Dzaleka literacy microdata (user's decision).

**Tests:** 91, from 63.

## 2026-11-05 — Week 4 started: the `rw-kiny` pack

**Gates checked:** no open ⛔ gate blocks week 4 (G3 and G6 closed 28 Oct). G4 (⚠) concerns weeks 6 and 8 only.

**Sources (re-read 5 Nov 2026, Tavily):**
- *Kinyarwanda and Kirundi Comparative Grammar* (2007), Tables 25–26 ([extract](https://www.matana.de/kirundi_kinyarwanda.pdf)): consonant inventory, and which linguists accept *c*, *cy*, *jy*, *pf*, *ts*, *shy*, *ng* as phonemes (Coupez 1980 and Jacob 1985 reject *cy*, *jy*, *c*, *pf*, *ts*; only Kimenyi 2001 accepts *ng*).
- Wikipedia, [Kinyarwanda](https://en.wikipedia.org/wiki/Kinyarwanda): the Cw/Cy pronunciation table (*rw* [ɾɡw], *sw* [skw], *tw* [tkw], *bw* [bɡ], *mw* [mŋ], *by* [bɟ], *ry* [ɾɟ]); the 2014 orthography reform met pushback (Niyomugabo & Uwizeyimana 2017, *Language Policy* 17(3)). Consistent with FSI and Nassenstein (28 Oct).
- Wikibooks, [Kinyarwanda/Orthography](https://en.wikibooks.org/wiki/Kinyarwanda/Orthography): length and tone not written; *l* only in loanwords; *mp* = [mh]. Secondary source.
- Wikipedia, [Rwandan names](https://en.wikipedia.org/wiki/Rwandan_names): ID card field *Amazina*; surname first, often in capitals (ALCASA cataloguing guidelines); people addressed by the given name in speech.
- Wikipedia, [Swahili language](https://en.wikipedia.org/wiki/Swahili_language): *ch* = /tʃ/, *sh* = /ʃ/, *ny* = /ɲ/, *j* = [dʒ]; no /ʒ/.
- The New Times, 29 Oct and 17 Nov 2014: the reform's existence and two-year transition. **The article bodies did not load; the letter-level changes are still undocumented.**

**Pack:** `namebridge/data/packs/rw-kiny-2026.1.json`, v0.1.0. Every entry has a source and a confidence; disputed phonemes are `disputed`; listener confusions beyond the sourced pronunciations are `hypothesis`. Gender-marked prefixes are marked `generation_only` (C12). `relationship_implications`: agreement `disputed`, disagreement `neutral`.

**Gaps:**
- The 2014 orthography order's text (ministerial order, Official Gazette, Oct 2014): no rule applied until read (`orthography-2014`, confidence `unknown`).
- Law 71/2024 arts 38–39: taken from `BENCHMARK_PROTOCOL.md` [B1]; re-read the article text before the graph release (week 5).
- How French-, English- or Swahili-speaking writers spell *cy* and *jy*: no source; not entered.
- Prenasal dropping (mb/b): no source; `hypothesis`.

**Tests:** 91 pass; the pack passes `namebridge.schema.pack` (covered by `test_every_pack_in_repo_is_valid`).

**Next:** `bi-kirundi` pack (four automatic Kinyarwanda → Kirundi rules), then the DRC pack and the loader that turns pack rules into Rule and Source nodes in the graph.

## 2026-11-05 — Decision: IPA for the sound layer, in week 7

**Question (user):** should names use the International Phonetic Alphabet?

**Decision (user, 5 Nov 2026):** yes, as the sound layer's internal comparison format, done in week 7 with the sound comparison. Until then, packs keep their current sound notation (`rw-kiny` 0.1.0 mixes spelling and IPA); week 7 converts them to strict IPA and adds a validator check.

**Limits agreed:** a spelling yields a set of possible IPA readings, not one transcription (length and tone are unwritten; names written by ear are already filtered through the writer); IPA is never shown to or typed by caseworkers; sound never decides a match alone (T17).

**Files touched:** `docs/TIMETABLE.md` (week 7).

## 2026-11-05 — Reciprocal search: both sides looking (user's proposal)

**User's idea (5 Nov 2026), reading `GATE_EXAMPLES.md` example 1:** if a girl remembers her mother as "Mama Belyse", look for a Belyse who is herself searching for a daughter like the girl. The girl's name is never shown to the mother; the mother must supply it. If it is right, the case is solved; if not, search more widely.

**Sources:**
- [V1] Alliance CPHA, *Child Protection Minimum Standards*, Standard 13 (UASC), draft 2 for consultation, §13.9 ([PDF](https://alliancecpha.org/sites/default/files/news/attachments/st-13-uasc_draft-2-for-consultation.pdf)): verification "is usually done by matching information from both parties without bringing them into contact, and asking verifying questions"; it also confirms both sides want reunification and that "the child is not handed over to the wrong person". *Draft text, read from a search extract; final wording not checked.*
- [V2] Better Care Network, [Verification and Family Reunification](https://bettercarenetwork.org/library/childrens-care-in-emergencies/verification-and-family-reunification): "adults may identify the wrong child"; a claimed relationship "should be verified before reunification".
- Primero/CPIMS+ already matches caregivers' tracing requests against registered children (26 Oct entry).

**Assessment:** the idea is sound and matches the standard [V1]. Three changes, agreed in discussion:
1. A reciprocal match is a **strong candidate, not a closed case**: knowing a child's name is not proof (traffickers can be relatives, IFRC); verification and a best-interests check still follow.
2. The **one-sided search runs at the same time**, not after: many sought people never file a request.
3. **Standing searches**: a later request is matched against earlier ones.
Added: no independence credit when the same clerk wrote both requests (shared spelling habits).

**Placed in:** `CONCEPT-IDEA.md` §5.5A (design); `BENCHMARK_PROTOCOL.md` §2.5 (reciprocal pairs, varied share *r*); `TIMETABLE.md` weeks 6 and 7; G4 row (candidate answer to question 2, for the professor). Not in `GATE_EXAMPLES.md`, by the user's choice: that page only illustrates error costs.

**Gap:** no source on how often both sides of a separated family file requests; *r* is varied.

## 2026-11-05 — Week 4: the `bi-kirundi` pack

**Sources read today (Tavily):**
- [B4] Burundi, *Code des personnes et de la famille* (1993), Titre II "Du nom", arts 11–14 ([PDF](http://jafbase.fr/docAfrique/Burundi/Burundi-Code-civil.pdf)), **primary text read**: the name is obligatory and given names form part of it (art. 11); the legal name is the one on the birth record or the one used constantly and publicly in childhood, at least to age 16 (art. 12); "le nom est donné à l'enfant par la personne qui déclare la naissance; le choix du nom est libre" (art. 13); the registrar may object only if the name could harm the child (art. 14). **The law sets no inheritance of the father's name.**
- [B5] University of Burundi repository, onomastics paper, §11.1.3, citing Bigangara (1982: 119): no family names before Christianisation except for kings; "missionaries … imposed the hereditary patronymic system wherein children necessarily bear their fathers' names".

**Conflict, kept side by side:** [B5] describes an imposed patronymic practice; Duchaj & Ntihirageza (2009) describe a Kirundi name chosen first, which later works as the surname; the code leaves the choice free. The pack records inheritance as `disputed`, and the benchmark keeps *p* varied. Art. 12 matters for tracing: a name used throughout childhood can be the legal name even if it differs from the birth record.

**Pack:** `namebridge/data/packs/bi-kirundi-2026.1.json`, v0.1.0: the four Kinyarwanda → Kirundi rules (high) and the ambiguous reverse (generate both options); sporadic differences left to graph edges; mission spellings as word-division/apostrophe variants (`hypothesis`); cluster pronunciations including *vy* ~ [z] (medium); CENI order (surname in capitals); Swahili names adopted in Tanzania routed as name changes, not variants. `relationship_implications`: agreement `context-dependent`, disagreement `disputed`.

**Gaps:** a Kirundi-specific source for r/l (the current one is about Kinyarwanda; the phonology is shared); Mioni (1975) full text; spelling of *c*/*j* by French writers in Burundian records (no source).

## 2026-11-05 — Kirundi r/l outside linguistics; Chichewa clerks; colonial place names

**Question (user):** find Kirundi-specific evidence for r/l, looking in safe sources that are not about linguistics (literature, etc.).

**Sources and findings:**
- [R1] **Cox, *Kirundi-English dictionary*** (1969; rev. M. Philipps, Feb 2023; [PDF](https://www.matana.de/kirundi.pdf)), English-Kirundi part, read 5 Nov: **"school: ishūri, ishūli, ishure, ishule"** (four spellings of one word, r/l and i/e) and **"pencil: ikaramu (Sw.)"** (Swahili *kalamu*, l → r). Also *ivatiri* "car" (French *voiture*). **Kirundi-specific evidence of r/l variation in writing**; the `bi-kirundi` r/l rule moves to `high`.
- [R2] **Kirundi New Testament** (book list via a dokumen.pub record; snippet only, page did not load): *Matayo, Mariko, Luka, Yohana*; *Yerusalemu*. l kept in some foreign names, r in others (*Mariko*). Single source, snippet; consistent with the Kinyarwanda rule (l only in names that already had it).
- [R3] **Chichewa, the language of Malawian clerks:** r and l are one sound; the official spelling (1973) writes **r after i or e, l elsewhere** ([Wikipedia, Chewa language](https://en.wikipedia.org/wiki/Chewa_language); Lyons & Mchombo, *Chichewa Grammar*: "R usually follows the vowels E and I … L follows the vowels A, O, U"; [Wiktionary guidelines](https://en.wiktionary.org/wiki/Wiktionary:Chichewa_entry_guidelines)). Three consistent sources. **Consequence:** a Malawian clerk writing a refugee's name may apply the rule (*Nkurunziza* → *Nkulunziza*, *Rukundo* → *Lukundo*). The rule is sourced; that clerks apply it to foreign names is a hypothesis. Partly closes the Chichewa gap of 28 Oct.
- [R4] **Colonial place names** ([Statoids, Burundi](https://statoids.com/ubi.html); Wikipedia, Gitega, Bujumbura): Kitega → Gitega, Usumbura → Bujumbura (1 Jul 1962), Hinga / Muhinga → Muyinga, Karusi → Karuzi. Older people and old records may use the colonial forms. For the cross-pack place data.
- **Not reachable:** Niyonkuru (1985), "Loan-Words in Kirundi", *African Study Monographs* 7: 81–87 (Kyoto repository PDF failed); Nimbona & Simon (2022), "La prononciation du français au Burundi", *Journal of Language Contact* 15(3–4) (abstract only: 12 speakers, eight features differing from reference French; whether r/l is one of them is unknown). Both need library access.

**Files touched:** both packs to v0.2.0 (Chichewa writer convention `ny` in both; Kirundi r/l to `high`; colonial place spellings as a failure mode; new benchmark cases).

## 2026-11-05 — Week 4: graph loader

**Code:** `namebridge.packs` turns each pack into a Language node per language and a Rule node per rule entry (structures, order, transliteration, sound layer), each with the entry's source, confidence and pack version. Re-running replaces a pack's earlier nodes; an invalid pack writes nothing; the whole graph is validated before writing.

**Design choice:** the loader makes **no name-to-name edges**. Applying a rule (e.g. by → vy) to generate variants would create `generated` edges in bulk; variant edges come only from attested sources (naming profiles, cross-pack given names), per DATA_RULES DR-1.5. Source nodes wait for the source register (week 5); until then each Rule node carries its source text.

**Result:** `rw-kiny` and `bi-kirundi` load as 97 nodes; `data/graph` validates. **Tests:** 96 (5 new), from 91.

## 2026-11-05 — Week 4: the DRC pack (`cd-swc-ln`)

**Sources (Tavily, 5 Nov 2026):**
- [C1] DRC, *Code de la famille* (consolidated 2017), arts 56–64 ([PDF](https://www.leganet.be/Legislation/Code%20de%20la%20famille/CDF.2017.pdf)), **primary text read**: prénom, nom and postnom are the elements of the name, and their declared order and spelling are immutable (56); relatives sharing a nom must add different elements (57); names drawn from Congolese cultural heritage (58); parents choose (59); a parent passing on a name adds a different element (61); a married woman keeps her name and may add her husband's (62); adoption (63); changes only by court (64). Confirms the 26 Oct reading.
- [C2] Immigration and Refugee Board of Canada, RIR doc 449451, quoting **Ndaywel è Nziem (1998)**, *Politique Africaine*, and [C3] **Pauwels & Pintens (1983)**, "La législation zaïroise relative au nom" ([PDF](https://www.droitcongolais.info/files/Hum.Sc.-NS-_T.XLVII,2_PAUWELS-J.-M.et-PINTENS-W._La-legislation-zairoise-relative-au-nom.-Droit-et-authenticite-africaine_1983.pdf)): **authenticité**. Christian given names banned from 1971–72 (nationality law of 5 Jan 1972; "affaire des prénoms"); from 24 Apr 1990 allowed in daily life but **not in registers or official documents**; registrable again from 1997. Ndaywel: "l'identité « écrite » a continué à ignorer les prénoms", while speech used them. **Consequence:** adults registered 1972–1997 may have nom + postnom only on documents and a Christian prénom in speech. New failure mode and benchmark case.
- [C4] Wikipedia, [Lingala](https://en.wikipedia.org/wiki/Lingala), and [APiCS survey 60](https://apics-online.info/surveys/60): no uniform spelling; the 1976 standard writes ɛ/ɔ, everyday writing uses e/o; y as i/y/none, w as w/o/u/none, o as o/u, initial prenasal written or not; French-influenced *ou*, *ss*.
- [C5] Wikipedia, [Congo Swahili](https://en.wikipedia.org/wiki/Congo_Swahili); Bose (2016), Kivu Swahili: regional varieties differ mainly in grammar; spelling differences in names not documented.
- CongoNames article (MDPI) did not load; repository abstract read ("dual linguistic origin: Bantu and Christian/French-origin components"). Order of elements in the exam lists to be read when building the profiles.

**Pack:** `namebridge/data/packs/cd-swc-ln-2026.1.json` v0.1.0 (languages swc, ln, fr). UN 1533 aliases are cited for patterns (r/l, nasal insertion) but **no sanctioned person's name is copied** into the pack (`data/README.md`: no data about real people). No ethnic or group marker; eastern DRC names are never read as group markers.

**Graph:** three packs load as 133 nodes; valid. **Tests:** 96 pass.

**Gaps:** CongoNames full article (token order in exam lists); Kivu Swahili spelling habits in names; Kinshasa vs eastern naming differences; DRC 2015 province names (cross-pack places).

## 2026-11-05 — Name changes in court records: gate G8 and its blind spots

**User's questions (5 Nov 2026):** are court name changes public, and can they be used? Clarified: not to track people, but as a check during one search ("Fulano da Silva" found in a court record as now "Siclano Souza").

**Findings:**
- **DRC:** *Code de la famille* art. 66 (read 5 Nov): court decisions changing a name are written in the margin of the birth (and marriage) certificate and sent by the clerk **for publication in the *Journal officiel***. Whether publication happens in practice, and whether the issues are online, is not checked.
- **Rwanda:** name changes follow a ministerial order (a new one published 1 Jun 2026, replacing the 2025 order; The New Times, via Ground News). Whether individual changes are published by name: not confirmed.
- **Malawi:** deed poll; publication requirement not found. **Burundi:** art. 17 of the Code not read.

**Agreed in discussion:**
- **A check during one search** fits rule 5 but must be **manual, by a caseworker on the protected route**. An automatic check would either send every searched name to an outside site (the search itself leaks) or need a local copy of all notices (bulk tracking). Findings go only into the protected case record; the person found decides on contact. Not written into `NAME_CHANGE.md`, by the user's choice.
- **Aggregate patterns from notices:** opened as gate **G8** (professor), because the notices are personal data outside G3. Default: not used.

**Blind spots of court and gazette notices as a pattern source:**
1. **Only formal changes appear.** The changes that matter most here, Swahili names taken in Tanzania, Malawian names, names taken to escape someone, are mostly informal (Daley 2018; `NAME_CHANGE.md`).
2. **The people most at risk are missing.** Someone hiding from traffickers or persecutors will not publish a new name in a gazette. The source under-represents exactly the protected cases.
3. **Different reasons.** Citizens change names at home for marriage, embarrassing names, religion or a reversal of authenticité names; refugees change names for safety and invisibility. Patterns from one need not hold for the other.
4. **Uneven coverage:** the DRC publishes by law, Rwanda perhaps, Malawi, Burundi and Tanzania unknown.
5. **Sensitive reasons:** religious conversion is a reason for change and is sensitive data (G5 condition 3: legal check).
6. **Patterns are not predictions:** over-trusting them would multiply false "possible name change" candidates (T17).

**Mitigation:** the pattern set combines several sources with different blind spots: published studies of exile name change (Daley 2018; Duchaj & Ntihirageza 2009; further literature to search), the notices if G8 allows, and native-speaker and caseworker input in Jan–Mar 2027 (needs IRB review). The benchmark keeps the share of name changes a varied parameter, so results are reported across the range, not at one guess.

## 2026-11-05 — Week 4: Christian names across languages

**Method:** a Bible translation fixes the form of each biblical name in its language, so book names and apostle lists are attested sources for Jean / John / Yohana-type links.

**Sources (Tavily, 5 Nov 2026):** Biblafrique Lingala pages (book names with French equivalents, two versions); Lingala Wikipedia "Biblíya"; Wikipedia "Biblical canon" (English); *Biblia Takatifu*, Open.Bible edition (Swahili, Mathayo 10:2–4); Shepherds Global Classroom Swahili NT survey; BibleProject Kinyarwanda; *Bibiliya Yera* (Kinyarwanda PDF); Kirundi NT (dokumen.pub snippet only, single source).

**Findings:** 8 names: John (Jean, John, Yohana [sw, rw, rn], Yoane / Yowane [ln]); Matthew (Matthieu, Matthew, Mathayo, Matayo [rw, rn, ln], Matai); Mark (Marc, Mark, Marko [sw, ln], Mariko [rw, rn], Malako); Luke (Luc, Luke, Luka); Peter (Pierre, Peter, Petro, Petero, Petelo); James (Jacques, Yakobo); Paul (Paul, Paulo, Pawulo); Jude (Jude, Yuda). The forms follow each language's sound rules already in the packs: Lingala l for r (Malako, Petelo), Kinyarwanda/Kirundi epenthetic vowels (Mariko, Petero, Pawulo).

**Data and code:** `data/crosspack/christian-names-2026.1.json`; `namebridge.crosspack` turns it into 8 NameConcept and 30 NameForm nodes, with 30 `historical_cognate_of` edges, all `proposed`, confidence 0.6, each citing its sources. A form shared by several languages is one node (Yohana: sw, rw, rn). The graph loader now also writes edges; packs and cross-pack data reload independently. **Tests:** 102 (6 new).

**Limits:** a Bible form shows the name exists in the language, not that a person baptised Jean is recorded as Yohana; the edges stay low-weight and proposed until reviewed. **Gaps:** Chichewa forms (no safe source found; a LinkedIn profile is not one); English James and Jude, French Paul (not in the pages read); common non-biblical given names (Emmanuel, Claude, Eric); Kirundi forms beyond the four gospels.

## 2026-11-05 — Chichewa gap: Bible forms and clerks' spelling habits

**Question (user):** close the Chichewa gap using dictionaries, phonetics, literature, language schools, talk transcripts.

**Sources (Tavily, 5 Nov 2026):**
- *Buku Lopatulika*, Bible Society of Malawi (1922; revised 1966, 2014, 2018), book lists on [bible.com](https://www.bible.com/versions/1068-blp-2018-buku-lopatulika) and [bibliatodo](https://www.bibliatodo.com/ny/baibulo/baibulo/buku-lopatulika): **Mateyu, Marko, Luka, Yohane, Yakobo, Petro, Yuda**.
- Chichewa Wikipedia, [Paulo Mtumwi](https://ny.wikipedia.org/wiki/Paulo_Mtumwi): **Paulo**.
- Harvestime Chichewa Bible-study course ([PDF](http://harvestime.org/translations/chichewa/creative%20bible%20study%20fina%20copy.pdf)): the four gospels, **Yohane Mbatizi** (John the Baptist, cf. Jean-Baptiste), Paulo.
- **Peace Corps Malawi**, *An Introduction to the Chichewa Language* (US government language course; [PDF](https://files.peacecorps.gov/multimedia/audio/languagelessons/malawi/MW_Chichewa_Language_Lessons.pdf)): "The letter C always carries an H"; no Q or X; ng' as a separate sound.
- **UK Government, *Malawi Toponymic Factfile*** (2025; [PDF](https://assets.publishing.service.gov.uk/media/68aee2f02f1856648215588f/Malawi_Toponymic_Factfile.pdf)): Chichewa spelling standardised in 1973 (New Chichewa Orthography Rules); one accented letter, ŵ (also Chitumbuka). Also lists Malawi's 28 districts (for the place data).

**Not usable:** talk or audio sources. The research tools read text only, so audio cannot be analysed; transcripts carry no pronunciation. LinkedIn profiles of people with these names were rejected (real people, not sources).

**Changes:** the Christian-names dataset (v0.2.0) gains the Chichewa forms; only Yohane and Mateyu are new written forms, the rest join existing nodes (Marko, Luka, Petro, Yakobo, Paulo, Yuda now also *ny*). All three packs gain two Chichewa conventions: /tʃ/ written *ch* by a Chichewa writer (a Kirundi *c*-name may arrive as *ch*), and ŵ folded to w in search forms. Graph: 179 nodes, 32 edges, valid. **Tests:** 102 pass.

**Still open on Chichewa:** a Chichewa dictionary of personal names (Scott & Hetherwick 1929 is a candidate, not read); how Malawian registration clerks actually write foreign names (a field question for Jan–Mar 2027).

## 2026-11-05 — Mary, Joseph, Emmanuel; names from other religions' texts (held)

**Sources (Tavily, 5 Nov 2026), read at the verse:** Louis Segond 1910 (public domain), Matthieu 1:18–25 and Luc 1:27: *Marie, Joseph, Emmanuel*; KJV Luke 1:27: *Mary, Joseph*; NIV Matthew 1:23: *Immanuel*; Swahili TKU, Mathayo 1:18–25: *Mariamu, Yusufu, Emanueli*; Swahili SRUV, Mathayo 1:23 (search snippet only): *Imanueli*; *Bibiliya Yera*, Matayo 1:18–23, Luka 1:27: *Mariya, Yosefu, Imanweli*; *Buku Lopatulika*, Luka 1:27: *Maria, Yosefe*. Not found: Kirundi and Lingala forms, Chichewa Emmanuel.

**Data:** Christian-names dataset v0.3.0: 11 names, 46 proposed cognate edges. Note the two Swahili spellings of Emmanuel in two translations (Emanueli, Imanueli), itself evidence of spelling variation.

**User's suggestion (5 Nov 2026):** look beyond the Bible, in other religions' books. **Assessment, not yet acted on:**
- Useful in principle: the Qur'an and its translations fix forms such as Yusuf, Maryam, Ibrahim, Yahya, Isa, which are cognates of Joseph, Mary, Abraham, John and Jesus. Swahili Christian forms already come partly from Arabic (*Yusufu*), so some links exist anyway.
- **Risk:** forms found only in another religion's texts (*Yahya* for John, *Isa* for Jesus) look nothing like the Christian forms; their main use in matching would be to link a person across a **change of religion and name**. That is the name-change case: rule 1 (an adopted name is not a variant, no public edge) and the restricted layer, which G5 allows only after a legal check of religion as sensitive data (condition 3). Labelling a form by its religious source would also encode religion, which the guard forbids.
- **Proposal:** forms that are the ordinary rendering in a corridor language (e.g. Swahili *Yusufu*, *Ibrahimu*) may enter the public graph from neutral sources (dictionaries, Bibles, civil lists), tagged by language only. Forms attested only in another religion's texts wait for G5 condition 3 and the restricted layer.

## 2026-11-05 — Week 4: place names that changed

**Why:** places are one of the main kinds of evidence (§5.6), and records, children and older people use old and new names side by side. The decision (user, 5 Nov): put place changes in the graph.

**Schema:** three relations, Region to Region only, old to new: `renamed_to`, `merged_into` (with `partial` when only part of the old unit went there) and `split_into`. They are not name variants and do not count as name equivalence. A Region node needs a name and an ISO 3166 country. `SCHEMA.md` updated.

**Sources (Tavily, 5 Nov 2026):**
- **Burundi 2025** (law of March 2023; 18 provinces → 5): Wikipedia, *Provinces of Burundi* (table of correspondence with former provinces); Breaking Burundi and Burundi Times on the 2025 governors; CIA World Factbook 2024/2025. Muramvya, Rumonge and Gitega (zone of Mahwa) were split between new provinces (`partial`). *Small conflict:* Breaking Burundi puts all of Muramvya in Gitega; Wikipedia splits it between Bujumbura, Butanyerera and Gitega. Recorded as partial to all three.
- **Burundi 1962:** Usumbura → Bujumbura (1 Jul 1962), Kitega → Gitega, Muhinga → Muyinga (Statoids; Wikipedia).
- **Rwanda 2006** (12 provinces → 5): Nations Online (which former province went where; Kigali-Rural split three ways); Statoids. Town renames confirmed only for Butare → Huye, Gisenyi → Rubavu, Kibuye → Karongi, Cyangugu → Rusizi (Wikivoyage: "expect people to use either name"). **Not confirmed, left out:** Ruhengeri → Musanze, Gitarama → Muhanga, Byumba → Gicumbi, Kibungo → Ngoma, Umutara → Nyagatare.
- **DRC:** 1966 city renames (Léopoldville → Kinshasa, Stanleyville → Kisangani, Élisabethville → Lubumbashi, Costermansville → Bukavu, and four more; Statoids); Katanga → Shaba (1972) → Katanga (1997) (WorldStatesmen); Bas-Zaïre → Bas-Congo → Kongo Central, Haut-Zaïre → Orientale (Wikipedia); the 2015 *découpage*, laws 015/004 and 015/006, six provinces split into 21 (Wikipedia table; Statoids; Crisis Group; Rulers.org).

**Data and code:** `data/places/places-2026.1.json` (100 units, 76 changes, each sourced); `namebridge.places`. Graph: 296 nodes, 122 edges, valid. **Tests:** 108 (6 new).

**Gaps:** the unconfirmed Rwandan town renames; the Kinyarwanda names of the new provinces (records in Kinyarwanda use them); communes and districts (Burundi 119 → 42 communes); HDX boundary files for coordinates (not needed for name matching yet).

## 2026-11-05 — Rwanda place gaps: towns were not renamed, districts were

**Question (user):** close the Rwanda gaps, and explain the difficulty. The difficulty: the renames are widely known, but no page read so far stated them, and the project adds a link only when a read source states it.

**Findings (Tavily, 5 Nov 2026):**
- **Two of the five expected renames were wrong.** Byumba was not renamed: it is "a city and sector … and the capital of Gicumbi District". Kibungo likewise is "the capital of Ngoma District". In 2006 the *towns* mostly kept their names; the *districts* around them got new ones.
- **Ruhengeri:** "today known as Musanze … the capital of Musanze District"; "some sources now refer to the city itself as Musanze". **Butare:** "also known as Huye and formerly known as Astrida" (renamed 1962); capital of Huye District. **Gitarama:** "Muhanga district, then known as Gitarama"; infobox "Muhanga City / Gitarama". **Gisenyi:** still Gisenyi, "historically rendered as Kisenyi", in Rubavu District. **Cyangugu:** still Cyangugu, "formerly Shangugu", capital of Rusizi District. **Kibuye:** a city in Karongi District. (Wikipedia, each town's article.)
- **Umutara** was a province (capital Nyagatare), already in the data as merged into the Eastern Province.
- **Organic Law 29/2005**, art. 4 (English text read): four provinces and the City of Kigali, with head offices.
- **Kinyarwanda names**, from each province's official site: *Intara y'Amajyaruguru* (Northern; "brought together the former Ruhengeri, Byumba and the northern part of the former **Kigali Ngali**", the Kinyarwanda name of Kigali-Rural), *Intara y'Amajyepfo* (Southern; former prefectures Gitarama, Butare, Gikongoro), *Intara y'Iburasirazuba* (Eastern), *Intara y'Iburengerazuba* (Western), *Umujyi wa Kigali*.

**Correction:** the four town renames taken from Wikivoyage on 5 Nov ("Gisenyi → Rubavu" etc.) were imprecise and are removed. Lesson recorded: a travel guide's "X (Y)" does not say whether Y is a new name or the surrounding district.

**Schema and data:** a fourth place relation, `located_in` (containment, not a change); places carry `other_names` with sources. Places dataset v0.2.0: 110 units, 90 links. Graph: 306 nodes, 136 edges, valid. **Tests:** 111 (3 new), incl. one showing that Byumba the town and Byumba the former province share a name.

**Still open:** French names of the provinces (*Province du Nord* …) from the French text of Law 29/2005; Burundi and DRC communes.

## 2026-11-05 — Place gaps: French names (Rwanda), Burundi communes, DRC territories

**Rwanda, French and Kinyarwanda names.** Organic Law n°04/2010/OL modifying Law 29/2005 (Rwanda Law Reform Commission; trilingual, text PDF) lists the provinces in three columns: *Intara y'Amajyaruguru* / Northern Province / *Province du Nord*; *Amajyepfo* / Southern / *du Sud*; *Iburasirazuba* / Eastern / *de l'Est*; *Intara y'**U**burengerazuba* / Western / *de l'Ouest*; *Umujyi wa Kigali* / City of Kigali / *Ville de Kigali*. **Official spelling variant:** the law writes *Uburengerazuba*, the Western Province's website *Iburengerazuba*; both recorded. Other names now carry `also_in` when a second source confirms them.

**Burundi communes.** Primary source: *Loi organique n°1/05 du 16 mars 2023* (78-page scanned PDF on CENI's site). No text layer and no OCR installed, so pages 1–6 were read as images. Art. 3: 5 provinces, 42 communes, 451 zones, 3,044 collines/quartiers; art. 4: provinces and chefs-lieux (Cankuzo, Bujumbura, Makamba, Ngozi, Gitega); **art. 5: the 42 communes by province**, now in the graph as `located_in` their province. Observations:
- The law does **not** map the 119 old communes to the 42 new ones. Several old commune names reappear as **zones** (Giteranyi, Gisanze, Gashoho, old communes of Muyinga, are zones of the new commune Butihinda), the same pattern as Rwanda's towns (name kept, level changed). Not recorded as links: a zone with an old commune's name need not cover the same territory.
- The law writes **Karusi**; the province was **Karuzi**. Recorded as another name.
- **Cross-border homonyms:** Burundi has communes *Muhanga*, *Nyanza* and *Gisagara*, which are also Rwandan districts. Place identity must always include the country (it does: `BI:` / `RW:` keys). Worth a failure mode in the matcher.
- Tavily was rate-limited (HTTP 429) and the local Tavily key is still invalid (401); the PDF was downloaded directly from CENI into the scratchpad.

**DRC territories.** UNGEGN 2021 (Ministry of the Interior data, 2017): 26 provinces, 33 villes, 145 territoires, 137 communes; the national programme is still "PDL 145 territoires" in 2026. Indicates the territories persisted through the 2015 reform. Adding them is coverage (`located_in`), not a name change; deferred. Most useful first: the territories of Nord- and Sud-Kivu, where most DRC refugees in Dzaleka come from (needs a sourced list).

**Data:** places v0.4.0; graph 348 nodes, 178 edges, valid. **Tests:** 111 pass.

## 2026-11-05 — Burundi old → new commune table, built by the project

**User's proposal (5 Nov 2026):** build the conversion table ourselves, since the 2023 law lists only the new units. **User's correction, same day:** Wikipedia is not a good source (now a standing rule: wikis only as pointers to primary sources).

**Sources:**
- **New division:** HDX `cod-ab-bdi` v02, Bureau de Centralisation de Géomatique (BCG), valid from 2026, CC BY-IGO (downloaded by the user; HDX blocks scripted downloads with HTTP 202). 5 provinces, 42 communes, 462 zones, 3,067 collines with areas and coordinates. **Its 42 communes match art. 5 of the 2023 law exactly**, province by province: two independent official sources agree.
- **Old division:** geoBoundaries gbOpen BDI ADM1/ADM2 (2007 boundaries; 18 provinces, 119 communes; NYU Spatial Data Repository, Stanford, Map Maker; public domain). The OCHA/IGEBU 2016 "SHP Admin3 Collines" file on HDX turned out to hold **one record only** (a stub); Wikipedia's colline list covers 30 of 119 communes and is not a source anyway.
- **Full forms of names truncated at 10 characters in geoBoundaries:** Bukinanyana, Bwambarangwe, Nyabitsinda, Kanyosha (2026 official data); Mugongo-Manga, Mpinga-Kayove (Council of Ministers communiqué, 15 Jun 2022). *Nyanrusang* left as in the source, flagged (probably Nyanrusange, unconfirmed).

**Method** (`namebridge/scripts/burundi_crosswalk.py`, reproducible, no external libraries): each new colline's point is located inside the old commune polygons; the collines' areas are summed per (old, new) pair. No name matching, so the duplicate colline names the government itself flagged (communiqué, 2022) do not matter. 43 of 3,067 collines fell outside all old polygons (boundary mismatch at edges and lakeshore) and are not counted.

**Validation against independent sources:** at province level the result reproduces the published correspondence exactly: Gitega 97% → Gitega and 3% → Burunga (the zone of Mahwa), Muramvya split Gitega 82% / Butanyerera 13% / Bujumbura 6%, Rumonge Burunga 60% / Bujumbura 40%, all other provinces 100% to the expected new one.

**Result:** 104 of 119 old communes went ≥ 95% into one new commune; 116 ≥ 60%. Links with share ≥ 5% are kept (134), `partial` below 95%, all `generated` and `proposed` with the share recorded. Findings useful for matching:
- **Isale → Isare** (and partly Ntahangwa): an r/l alternation in an official commune name.
- **Two old communes named Butaganzwa** (Kayanza → Matongo; Ruyigi → Butaganzwa): an old place name alone can be ambiguous within one country.
- **Mwumba** (a commune name in the 2022 draft) was an old commune that went wholly into Ngozi.

**Licences:** CC BY-IGO (BCG) and public domain (geoBoundaries); the derived table is published under CC BY 4.0 with attribution to both.

**Data and code:** places v0.5.0, 271 units, 343 links; graph 467 nodes, 389 edges, valid. Loader accepts derived links (basis, confidence, share). **Tests:** 113 (2 new).

**Next (user's correction):** replace the Wikipedia-only sources in the packs, the Christian names and the places data with primary sources.

## 2026-11-05 — "Nyanrusang": the official name is Nyarusange

**Question (user):** find the truncated commune name in reports of international organisations, given Burundi's wars.

**Findings (Tavily, then the primary PDF):**
- **UN and agency reports write *Nyarusange*:** OCHA Burundi Weekly Information Update, 9–22 Apr 2001 ("Displaced populations from Nyarusange commune / Gitega province"); USAID Field Report, Dec 2005 ("Nyarusange communes in Gitega"); FAO livestock case study, May 2008 (Gitega commune borders "Makebuko, Nyarusange and Itaba communes").
- **The official Burundian source agrees:** CENI, *Rapport général sur le processus électoral de 2010*, registration table by commune: GITEGA … MUTAHO, **NYARUSANGE**, RYANSORO. Downloaded from CENI and read locally; only commune names were used (the report also lists candidates; nothing about people was kept).
- ***Nyanrusange*** appears only in geoBoundaries (truncated "Nyanrusang") and in Wikipedia and its copies: an **extra n before r**. Kept as another name, and added to the `bi-kirundi` pack as an attested listener confusion (/nr/ ~ /r/, medium).
- **A homonym:** OCHA (Jul 2005) also mentions "Nyarusange" as a *sector* of Musigati commune (Bubanza). Same name, different place, a different level.
- **Other official variants found in the same CENI table:** *MUGONGOMANGA* written as one word (the 2022 communiqué writes *Mugongo-Manga*); *ISALE* (2010) vs *Isare* (2023 law), an r/l alternation between two official sources; *BUKINANYANA* and *KANYOSHA* confirmed. The `bi-kirundi` r/l rule now cites these official sources.
- **New gap:** in 2010 Bujumbura Mairie had **13 urban communes** (Buterere, Buyenzi, Bwiza, Cibitoke, Gihosha, Kamenge, Kanyosha, Kinama, Kinindo, Musaga, Ngagara, Nyakabiga, Rohero), later merged into Muha, Mukaza and Ntahangwa. People from the capital will use these names; not yet in the data.
- The OCHA war-period reports (2001–2004) also confirm several other old communes (Nyabitsinda, Kabezi, Nyabiraba, Mutimbuzi, Mubimbi, Mutambu, Buyengero) and write "Nyanza Lac" without the hyphen.

**Data:** places v0.6.0 (Nyarusange, with sources); `bi-kirundi` v0.4.0. **Tests:** 113 pass.

## 2026-11-05 — Place resolver: old names find new ones, and the reverse

**User's requirement (5 Nov 2026):** depending on the person's answer, the model must recognise that a new name can refer to an old one, and the reverse.

**Bujumbura's 13 urban communes of 2010** (CENI 2010 list: Buterere, Buyenzi, Bwiza, Cibitoke, Gihosha, Kamenge, Kanyosha, Kinama, Kinindo, Musaga, Ngagara, Nyakabiga, Rohero): in the official 2026 boundaries (BCG v02), twelve are **zones** of Ntahangwa, Mukaza or Mugere, and **Rohero is a quarter** ("Quartier Rohero", zone and commune Mukaza): a commune dropped two levels. New relation **`continues_as`** (same name at another level; `generated`, confidence 0.7, territory not checked). **Ambiguities found:** *Cibitoke* is an old province, a 2025 commune, a zone of that commune and a zone of Bujumbura city; *Gihosha* is a zone in Bujumbura and in Kirundo.

**Code:** `namebridge.resolve_place`. A name (folded: case, accents, hyphens, spaces and prefixes such as *Quartier*, *Province du*, *Intara y'*, *Umujyi wa* ignored) is matched against every place's name and other names; the graph is then followed **later** (old → new), **earlier** (new → old) and **within** (the larger units it lies in). Each candidate has a score (product of step weights: the area share where recorded, 0.5 for a partial link without one, 1 otherwise), a `derived` flag when a step came from the project's own crosswalk, and the path that explains it. Rules that keep results meaningful: no reversing direction in time (Kayanza → Butanyerera must not continue to Kirundo); no going up after going back in time (Kayanza → old Busiga → Ngozi province is valid step by step but noise); on equal scores, a change over time is preferred to containment. A name that means several places returns all of them; choosing is the caller's job, with the rest of the evidence.

**Error found by the resolver:** the 42 new communes had lost their `located_in` province links when the crosswalk was added (an over-broad filter). Restored, with a guard test.

**Examples:** *Kamenge* → zone of Ntahangwa → Bujumbura (2025), and the old Bujumbura Mairie; *Butanyerera* → earlier Kayanza, Kirundo, Ngozi (and part of Muramvya); *Nyanrusange* → Nyarusange → later Gishubi (derived); *Intara y'Amajyaruguru* and *Province du Nord* → Northern Province; *Élisabethville* → Lubumbashi.

**Tests:** 124 (11 new). **Data:** places v0.7.0.

## 2026-11-05 — Bug audit of the place data (user: no progress until bugs and gaps are closed)

**Rule from the user (5 Nov 2026):** nothing advances while known bugs or gaps are open.

**The bug** (42 commune → province links lost to an over-broad filter) was already fixed with a guard test. To catch the same *class* of error, the place data was audited and the checks made permanent (`tests/test_places_integrity.py`): no orphan units; no duplicate links; every old unit has a successor; every current commune, zone, quarter, district and town is placed in a larger unit; the crosswalk shares of each old commune add up to ≥ 90 %; every source is both defined and used.

**What the audit found:**
- An unused source (`rw-wikivoyage`, left over from the four removed links): removed.
- **Nine current towns placed nowhere** (Bujumbura and eight DRC cities), so the resolver could not say that Lubumbashi is in Haut-Katanga. Placed from Statoids' tables of provinces and capitals (page fetched directly; Tavily rate-limited): Lubumbashi → Haut-Katanga, Mbuji-Mayi → Kasaï-Oriental, Kananga → Kasaï-Central, Kisangani → Tshopo, Mbandaka → Équateur, Bukavu → Sud-Kivu, Kinshasa → Kinshasa; Bujumbura → Bujumbura province (2023 law, art. 4: chef-lieu) and Bujumbura Mairie (CENI 2010).
- **Bandundu city** was the capital of the 1966–2015 province; which of Kwango, Kwilu or Mai-Ndombe it lies in now is not in the source. Placed in the old province only; **open gap**.
- Added from the same source: **Kivu split into Maniema, Nord-Kivu and Sud-Kivu**, the home region of most DRC refugees in Dzaleka; older people may say "Kivu".

**Open gaps (in order):** Bandundu city's current province; Wikipedia-only sources still in the data (packs ~32 entries; Rwandan towns; part of the DRC changes; three Christian-name forms); DRC territories (coverage).

**Tests:** 130 (6 new). **Data:** places v0.8.0.

## 2026-11-05 — Bandundu city is in Kwilu; Kwilu's capital is disputed

**Sources:** UNICEF DRC, *Rapport provincial: Province du Kwilu* (2021), read: Kwilu, from the split of the former Bandundu province, has the territories of Bagata, Bulungu, Gungu, Idiofa and Masimanimba "et la ville de Bandundu qui est le chef-lieu de la province"; OCHA, *DRC: A Year of Survival* ("the city of Bandundu, in Kwilu Province"); ReliefWeb ("Bandundu, the capital of Kwilu Province"); Radio Okapi tags "bandundu ville, kwilu". A tourism site and French Wikipedia point the same way but are not cited.

**Conflict, kept side by side:** Statoids gives **Kikwit** as Kwilu's capital; UNICEF (2021) and ReliefWeb give **Bandundu**. Location is consistent (both cities are in Kwilu), so matching is unaffected; the capital is not recorded as a fact.

**Data:** Bandundu city `located_in` Kwilu (2015–), sources UNICEF and OCHA; also kept in the 1966–2015 province. Places v0.8.1. **Tests:** 130 pass. Gap closed.

**Ranking bug found and fixed (same day):** the resolver gave each part of a split a weight of 1, so "Bandundu" returned Kwilu, Kwango and Mai-Ndombe all at 1.00. A split into n parts now weighs 1/n per part: Bandundu city → Kwilu 1.00 (containment), the old province's parts 0.33 each; Kivu → Maniema, Nord-Kivu, Sud-Kivu 0.33 each. Two tests added. **Tests:** 132.

## 2026-11-05 — Place data without Wikipedia

**Rule (user, 5 Nov):** Wikipedia is not a source. All place links now rest on primary or recognised sources; `rw-wiki-towns`, `bi-wiki` and `cd-wiki` are gone from the dataset.

**Rwandan towns, re-sourced:**
- **Organic Law 29/2005** (RwandaLII, trilingual PDF; the UT Austin copy returns an HTML page): its annex has a **coded list of 30 districts and 416 sectors**, province = first two digits (01 Kigali, 02 South, 03 West, 04 North, 05 East). Sectors named Byumba (Gicumbi), Kibungo (Ngoma) and Gisenyi (Rubavu) confirm those towns; every district → province link now cites the law. Also found: a **Butare sector in Rusizi**, a homonym of Butare town (Huye).
- **Musanze District's official site:** "Akarere ka Musanze gakomoka ku cyahoze ari Umujyi wa Ruhengeri, Akarere ka Mutobo, Akarere ka Kinigi…": the 2002–2006 town of Ruhengeri merged into Musanze with other units.
- **REMA, State of Environment Report 2017:** "Huye City was renamed from Butare in 2006" (so Butare *was* renamed, unlike Byumba or Gisenyi; modelled as Butare (1962–2006) → Huye (2006–), located in Huye District); "the Kibuye area … of the District of Karongi".
- **MINUBUMWE, History of Rwanda,** and **The New Times:** Rusizi District, former Cyangugu.
- **Statoids, citing the UN Conference on the Standardization of Geographical Names (1991):** Butare: Astrida; Cyangugu: Shangugu; Gisenyi: Kisenyi; Kigali-Rural: Kigali Ngali, **Kigali Ngari** (r/l); Umutara: Mutara; 1946 territories with colonial spellings Biumba, Kibungu, Kîsenyi.
- **Gitarama → Muhanga: indirect evidence only** (REMA map "Muhanga and Gitarama"; NESA lists a school "GS Gitarama" in Muhanga District). Kept at confidence 0.6 with a note; **open gap** until a direct source is found.

**DRC, re-sourced and corrected (Statoids change history):** ~1975 Kongo-Central → Bas-Zaïre; 1997 Bas-Zaïre → Bas-Congo, Haut-Zaïre → **Haut-Congo**, Shaba → Katanga; ~1998 Haut-Congo → Orientale. The intermediate *Haut-Congo* was missing, and Kongo Central (2015) is a return to the pre-1975 name. Other names added: Kivou, Kassai, Lower/Upper Zaire.

**Tools:** Tavily was rate-limited repeatedly; official PDFs and pages were fetched directly (RwandaLII, district sites, REMA, MINUBUMWE, Statoids). In zsh, a loop variable named `path` overwrote `PATH`; scripts now use Python.

**Data:** places v0.10.0. **Tests:** 132 pass.

**Open gaps:** Gitarama (direct source); Wikipedia-only entries in the packs (~32) and three Christian-name forms; DRC territories (coverage).

## 2026-11-05 — Packs and Christian names: Wikipedia replaced where a primary source exists

**Starting point:** 33 pack entries rested only on a wiki, plus three wiki sources in the Christian names.

**Sources read (5 Nov 2026):**
- **FSI, Swahili Basic Course** (US Foreign Service Institute, public domain; scanned, read as page images, pp. viii–xii): ch as in "cheese" (strongly affricated); j as in "Joe"; ng' as in "sing", also word-initially; **ny written ny before vowels, n before consonants** (nchi); **sh "an unvoiced palatal grooved fricative (note the lack of a voiced counterpart)"**, so Swahili has no /ʒ/; r (a flap) and l are distinct. Re-sourced 12 entries.
- **FSI, Lingala Basic Course** (pp. xii–xiv): /ɛ/ and /ɔ/ are phonemes, "usually written e … o, but sometimes ɛ … ɔ"; ny = /ɲ/; **/r/ and /v/ only in unassimilated loan words** (why Lingala has Malako, Petelo); z ranges over [z, ʒ, dz, dʒ]. Re-sourced 2 entries.
- **FSI, Introduction to French Phonology** (Salazar; scanned): p. 254 "When the consonant g is immediately followed by e or i it is always pronounced j" (high); p. 253 a section on written *ch* (audio drills only; medium); p. 329 "an s between two vowels is pronounced z", hence *ss* (medium). Re-sourced 6 entries.
- **Zorc & Nibagwire (2007)**: /mp'aamafaraanga/ < /n-h-a…/ (written *mp* = n + h); §2.5.12 velarized consonants (bw, kw, tw). Re-sourced 2 entries.
- **IRB Canada, RIR RWA103584.E (2010)**, quoting the 2008 ID card law: a single field "Amazina/names"; the order within it is not stated (claim narrowed accordingly).
- **ALCASA, Africana Cataloging Guidelines 4c**: surname first "also … in Rwanda – in Kinyarwanda as well as French publications", often in capitals, varying even within one publication; **"Central African names (Congolese etc.) did not traditionally include a surname"** (new order rule in the DRC pack).
- **King James Version** (bible.com book list; Acts 13:9 for Paul): replaces the Wikipedia canon table for the English forms.
- **UK Rwanda Toponymic Factfile (2025)**: "Musanze (Ruhangeri)", another spelling of Ruhengeri (places data).

**Removed:** the Lingala form *Yowane* (only source: Lingala Wikipedia); the Chichewa Wikipedia source (*Paulo* keeps the Harvestime course).

**Still without a primary source, kept at confidence `low` with a note:** French writers' *ou* for /w/, *tch* for /tʃ/, *gn* for /ɲ/ (8 entries across the three packs; the UNESCO study on spelling African names [P4] would cover them but UNESDOC does not load without a browser); "people are addressed by the given name in speech" (rw-kiny). **Open gaps.**

**Tests:** 132 pass. Packs: rw-kiny, bi-kirundi, cd-swc-ln bumped; Christian names v0.4.0.

## 2026-11-05 — French spellings of African names: UNESCO 1984

**Source** (opened in Chrome at the user's request; the user downloaded the PDF, since UNESDOC renders it only in a browser viewer): UNESCO, *African ethnonyms and toponyms* (Meeting of Experts, Paris 1978; General History of Africa: Studies and Documents 6, 1984, 198 pp.).
- **Cornevin, R., "The standardization of the spelling of African names: toponyms and ethnonyms"**, pp. 68–79: French and English renderings of the same names — "Adamaoua or Adamawa", "Haoussa (Hausa or Hawsa)", "Tchouana (Tswana)", "Evhé (Ewe in German and English)"; and "j and c(h) are usually given values close to their English value in 'anglophone' countries, but not normally in 'francophone' countries". Sources French *ou* for /w/ and *tch* for an affricate (medium).
- **Alexandre, P.**, same volume, p. 65: "'Urundi' and 'Warundi' are Swahili for 'Burundi' and 'Barundi/Abarundi'": Swahili changes Kirundi class prefixes (Bu- → U-, Ba- → Wa-). New failure mode in `bi-kirundi`.
- French *gn* = /ɲ/: not in the volume; sourced instead from the **FSI Swahili Basic Course**, p. xi (ny "as in … French *gagner*").

**Result:** all 8 French entries re-sourced (medium). Of the 33 pack entries that rested only on a wiki, **one remains**: "people are addressed by the given name in speech" (rw-kiny), kept at `low` with a note. **Tests:** 132 pass.

## 2026-11-05 — Gitarama sourced; "given name in speech" still open

**Gitarama → Muhanga, now direct and official:** MINEDUC, Muhanga District environmental and social management plan ("The climate is tropical in Muhanga (Gitarama)"); MININFRA, ESIA report for Muhanga City (roads "extend to Gahogo and **Gitarama administrative Cells of the Nyamabuye Sector**": Gitarama is also a cell of the town centre); The New Times ("all roads in Gitarama town, Muhanga district"). Confidence back to the dataset default; the indirect REMA/NESA evidence is no longer needed (NESA source removed).

**"Rwandans are addressed by the given name in speech":** no primary source found (searched official, UN and press sources). A Presbyterian Church (USA) mission letter (2017) describes two names (a Rwandan name and, for Christians, a baptismal name) but not forms of address. Kept at `low`; would be closed by Kimenyi (1978), *Anthropological Linguistics* 20(6) (JSTOR, needs NYU library access). Teknonymy ("Mama Teta"), relevant to children's reports like "Mama Belyse" (`GATE_EXAMPLES.md`), also lacks a non-wiki source: **open**.

**Tests:** 132 pass.

## 2026-11-05 — Territories of Nord-Kivu and Sud-Kivu

**Why these first:** most DRC refugees in Dzaleka come from the Kivus; a person may name the territory (Masisi, Uvira…) rather than the province.

**Sources (OCHA, UN):** *Scale up Response Report, Ituri, North Kivu, South Kivu* (Jul–Nov 2023): North Kivu territories Masisi, Rutshuru, Lubero, Beni, Nyiragongo, Walikale; *Sud-Kivu sitrep #4* (21 Apr 2026): Fizi, Mwenga, Uvira, Kalehe, Shabunda, Walungu, Kabare; *Eastern DRC incidents map* (Dec 2025): adds Idjwi, and spells **"Nyirangongo"** (an extra *n*), the same nasal insertion as Nyarusange/Nyanrusange, now in an official UN document. Goma placed in Nord-Kivu (Statoids, provincial capitals).

**Data:** 14 territories `located_in` their province; places v0.11.0. **Tests:** 132 pass (integrity tests now cover the territory level).

**Not done (coverage):** territories of the other 24 provinces; Beni and Uvira as towns (homonyms of their territories).

## 2026-11-05 — Kimenyi (1978) read in full

**Source:** Kimenyi, A. (1978), "Aspects of Naming in Kinyarwanda", *Anthropological Linguistics* 20(6): 258–271 (JSTOR; copy obtained by the user through NYU Libraries; scanned in two columns, read as page images where the text layer was broken). Copyrighted: summarised, not reproduced.

**Findings used:**
- p. 259: no family names in Rwanda; children, father and mother each have their own name; women keep their names when married. Now the primary source of `structure-kiny-name-plus-given` (confidence high).
- p. 258: the naming ceremony is held on the evening of the seventh day; neighbours' children and the mother propose names, but the father names the child. Added to the (still disputed) father-element entry: the article describes naming by the father, not inheriting his name.
- pp. 261–262: name-forming morphemes *nyira-*, *mukaa-*, *kaa-* (feminine) and *nya-*, *munya-*, *see-*, *nyiri-*, *rwaa-*, *ki-*; read directly, replacing the earlier second-hand citation.

**Not in the article:** forms of address in speech, teknonymy ("Mama X"), Christian names. The gap `order-spoken-given-name` stays open (`low`); next candidate is Kimenyi (1989), *Kinyarwanda and Kirundi Names*. Note: the article mentions ethnic groups when describing the two countries; nothing about ethnicity enters the pack (DR-1.7).

## 2026-11-05 — All DRC level-2 units from the official boundary data

**User's decision (5 Nov):** treat the remaining DRC territories now, not later.

**Source:** HDX `cod-ab-cod`, *Democratic Republic of the Congo – Subnational Administrative Boundaries*, **Référentiel Géographique Commun** (RGC), v01 (valid from 2019), updated on HDX April 2026, CC BY-IGO (downloaded by the user; HDX blocks scripted downloads). Sheet `cod_admin2`: **164 level-2 units, territories and cities together, with no type column.**

**Method:** each unit is placed `located_in` its province (all 26 province names matched after folding: "Equateur"/"Équateur", "Maï-Ndombe"/"Mai-Ndombe"). Where a unit of the same name already existed in that province, the official source was added to it instead of creating a duplicate.

**Result:** 141 new level-2 units (`level: admin2`, with the RGC pcode, noted as "territory or city"); **22 existing units cross-checked**, including all 14 Kivu territories taken from OCHA reports and cities such as Goma and Bukavu: the OCHA lists agree with the official data.

**Ambiguity kept, not guessed:** without a type column, "Beni" may be the city or the territory; the territory's seat, **Oïcha**, is a separate unit, and pcodes CD6106 and CD6108 are absent (merged or retired units). The type of each level-2 unit is not asserted.

**Data:** places v0.12.0. **Tests:** 132 pass.

**Same day, from the same RGC file (gap found by a spot check: "Tshikapa" returned nothing):**
- **Level 3:** 519 units (communes, sectors, chiefdoms; e.g. Kinshasa's communes Bandalungwa, Barumbu…), each `located_in` its level-2 unit; none left without a parent. Tshikapa is a level-3 unit of Kamonia.
- **Provincial capitals** (sheet `cod_admincapitals`, `adm_p_lvl = 1`): all 25 placed. **Two conflicts settled by the official source:** Kwilu's capital is **Bandundu** (as UNICEF 2021 and ReliefWeb; Statoids' Kikwit superseded); Kasaï's capital is **Tshikapa** (Statoids' Luebo superseded). The file writes "Mbuji Mayi" without a hyphen (folding handles it).
- Places v0.13.0. **Tests:** 132 pass.

**Open gap after this:** "given name in speech" and teknonymy (rw-kiny), waiting on Kimenyi (1989).

## 2026-11-05 — Two sources from the user's NYU access (not Kimenyi 1989)

- **Rusanganwa, J. (2006), "Rwanda: Language Situation"**, *Encyclopedia of Language & Linguistics*, 2nd ed., pp. 715–716 (author at the National University of Rwanda). Used: a phonetic transcription rendering written *rya* as [rgya] and *rw'indimi* as [rgwiindimi] (primary support for the rw → [rgw] rule and listener confusion); shy, jy, mf, pf, ts treated as single units by Rwandan linguists; Kinyarwanda is a tone language, tone marked only in linguistic writing; first written by missionaries (Catholic prayer book, 1907). Also lists Swahili's role (commerce, and religious use); nothing about religion enters the pack.
- **van de Vijver, Uwambayinema & Chuang (2024)**, *Linguistics* 62(1): 79–119, §2: five vowels, each short or long (Myers 2005); i/e and u/o become glides before vowels; a full list of prenasalised consonants, adding **mf, mv, ns** to the pack's inventory.

Copyrighted: summarised, not reproduced. Neither covers forms of address or teknonymy: that gap stays open, pending Kimenyi (1989). rw-kiny bumped; **tests:** 132 pass.

## 2026-11-09 — Teknonymy and name avoidance: Fédry (2009)

**Source:** Fédry, J. (2009), "« Le nom, c'est l'homme »", *L'Homme* 191: 77–106 (peer-reviewed; open access on OpenEdition). Summarised, not reproduced.

**Findings used (rw-kiny 0.5.0):**
- **para. 49, teknonymy:** naming the parent after a child ("Père de Untel", "Mère de Untel") is very widespread in Africa and usually replaces the birth name in everyday use. The child named is often the eldest son or daughter, elsewhere the last-born. New rule `order-teknonym`, confidence **low**: the paragraph describes Africa in general and does not name Rwanda.
- **para. 55, name avoidance:** in Africa generally a child does not call a parent by name; in many places, **Rwanda named**, this extends to parents-in-law. New failure mode `child-avoids-parent-name`: a child may not know a parent's own name, and "Mama Belyse" names the child, not the mother (`GATE_EXAMPLES.md`, example 1). Retrieval must not depend on the parent's own name.
- **para. 63, Rwanda:** one does not say one's own name before the end of physical growth, about 15 (*ntaw'igura agikura*), as education in modesty. The article's evidence is personal communication (Ganza 2002; Mbonimpa), so treat it as weak evidence. New failure mode `child-withholds-own-name`: a minor who gives no name or only a nickname is not evidence of a hidden identity (consistent with `NAME_CHANGE.md`: never use names as credibility evidence).

**Still open:** `order-spoken-given-name` (which name Rwandans use in speech) is not covered by Fédry; it stays `low` on the Wikipedia claim, pending Kimenyi (1989). Teknonymy needs a Rwanda-specific source to rise above `low`. Ntahombaye (1983), *Des noms et des hommes* (Karthala), the standard study of Burundian names, is the candidate for bi-kirundi (needs library access).

**Search note:** Tavily returned HTTP 429 on two of five sequential calls; no other open Rwanda-specific source on forms of address was found (an Instagram post and language-learning pages are not sources).

**Tests:** 132 pass; graph valid.

## 2026-11-09 — Correction: "Mama X" has two readings

**User's first-hand observation (they have been in the region):** for Rwandans, *mama* and *papa* are used like *senhora*/*senhor* (madam/sir), i.e. respectful address for any adult, not only for parents.

**Published support (Swahili):** Kraska-Szlenk, I. (2018), "Kinship metaphors in Swahili language and culture" (University of Warsaw; [PDF](https://bibliotekanauki.pl/articles/462487.pdf)), Table 1 lists both **"mama X" = teknonym, "X's mother"** and **"mama X" = honorific, "Mrs. X"**; "any adult woman can be addressed or referred to as mama", also with her own name; *baba* is the mirror term.

**What was wrong:** the earlier entry today read "Mama Belyse" only as "mother of Belyse". In `GATE_EXAMPLES.md` example 1, Belyse is the mother's **own** name, i.e. the honorific reading.

**Changes:** rw-kiny 0.5.1: new failure mode `mama-x-two-readings` (search X both as the adult's own given name and as a child's name; "Mama" alone does not show parenthood), `order-teknonym` and `child-avoids-parent-name` reworded; source = the user's field observation plus the Swahili paper. cd-swc-ln 0.4.0: new rule `order-mama-x` (medium; Swahili in general, not Congo Swahili specifically) and the same failure mode. **Tests:** 132 pass; graph valid.

**Benchmark implication (week 6):** generated oral reports should include "Mama/Papa + own given name" and "Mama/Papa + child's name", so recall is measured on both readings.

## 2026-11-09 — Niyonkuru (1987) read in full

**Source:** Niyonkuru, L., "Loan-words in Kirundi: a preliminary study", *African Study Monographs* 7: 81–87, **March 1987** (earlier entries in this log cite it as 1985; the printed date is 1987, received 3 Feb 1986). Copy obtained by the user; kept in `~/namebridge-ref`. Summarised, not reproduced.

**What it is:** a historical and sociolinguistic sketch of the contacts that shaped Kirundi (Swahili trade, German and Belgian rule, missions, migrant labour to Buganda). **It contains no list of loan-words and no sound-adaptation rules**, so it does not serve the sound layer, despite its title.

**Used:**
- p. 82: "Usumbura" is the Swahili rendering of Bujumbura; p. 83: "Urundi" is Kiswahili for Burundi, and the region of Bujumbura is "Uzige, or Buzige in Kirundi". A scholarly second source for the Usumbura → Bujumbura rename (places 0.13.1; until now Statoids only) and more examples for the bi-kirundi Swahili-prefix failure mode (Bu- → U-).
- pp. 81–82, 84: Kinyarwanda-speaking refugees settled in Burundi in 1959–64 and 1972–73 (Bujumbura, Bubanza, Muyinga, Ruyigi); people from eastern Congo were 57.3% of Usumbura's urban population in the 1950s and spoke Kingwana (Congo Swahili). New bi-kirundi failure mode `origin-country-not-naming-language` (bi-kirundi 0.6.0): a person from Burundi may carry Kinyarwanda- or Swahili-spelled names, so all three packs should be tried.

**Not used:** the article's description of ethnic groups and of a Muslim community (DR-1.7; packs hold no ethnicity or religion); the Kirundi names for neighbouring groups (ethnonyms).

**Correction made during this work:** a DOI was first written for this source from memory without checking; it was replaced before commit by the repository's home page, with a note that the exact record URL was not recorded.

**Tests:** 132 pass; graph valid.

## 2026-11-09 — Nimbona & Simon (2022) read in full: how Burundians say French names

**Source:** Nimbona, G. & Simon, A. C. (2022), "La prononciation du français au Burundi : influence du français de Belgique et du kirundi", *Journal of Language Contact* 15: 481–511, doi:10.1163/19552629-15030002. Copy obtained by the user; kept in `~/namebridge-ref`. Summarised, not reproduced.

**Why it matters:** most Burundian given names are Christian names in French form. This paper shows how Kirundi speakers pronounce French, which is how a child or relative will say such a name aloud, and how a caseworker may then write it.

**Corpus and limits:** 12 university-educated adults (4 women, mean age 38.5), PFC protocol (word list, text reading, narration). Bujumbura-born speakers were closest to standard French; the authors attribute differences to schooling. **Less-schooled speakers and children are not covered and may deviate more.** Name examples in the pack marked "derived" apply the pattern and are not in the paper.

**Added to bi-kirundi 0.7.0 (5 phonetic rules, 2 listener confusions):**
- `fr-nasal-vowel-split` (medium): French nasal vowels said as oral vowel + a nasal consonant matching the next consonant, as in Kirundi prenasals: 65.2% word-internal, 26% initial, 11.3% final (Table 3); *campagne* [kampaɲ], *cinquante* [sɛŋkant].
- `fr-vowel-glide` (medium): glide between vowels: **Louis [luwi] (10/12)**, *étrier* [etʁije] (11/12); French *ui* → [wi] (*huit*, 12/12).
- `fr-r-dropped` (medium): r dropped word-finally and after a consonant (*trois* [twa], *quatre* [kaːt], 7/12 each), never word-initially.
- `fr-u-to-u-or-i` (low, occasional), `fr-h-pronounced` (low, 1 speaker in 3).

**Same session: a bug in the packs and a guard.** 8 sound entries (3 packs) still had the note "Wikipedia only" after their source had been replaced by Cornevin (1984) or the FSI course on 5 Nov; the note contradicted the source. Notes fixed (bi-kirundi 0.6.1, cd-swc-ln 0.4.1, rw-kiny 0.5.2). **Guard:** `validate_pack` now rejects a "Wikipedia only" note when the source is not Wikipedia; test `test_note_cannot_contradict_source`.

**Audit, still open (for the user to decide):** about 16 pack entries still list Wikipedia **alongside** another source (e.g. Kirundi transliteration with the Comparative Grammar; Lingala spelling with APiCS; the Chichewa r/l rule with Wikipedia and Wiktionary). Per the "Wikipedia is not a source" rule they should cite only the non-wiki source, or be marked `low` where Wikipedia is the only real support (the Chichewa entries look like that case).

**Tests:** 133 pass; graph valid.

## 2026-11-09 — Library search by Tavily (the user found nothing at NYU): Adekunle (2007), Simbananiye (2005)

**Adekunle, J. O. (2007), *Culture and Customs of Rwanda* (Greenwood)**, chapter "Gender Roles, Marriage, and Family", read from an online copy. Its taboo section is "taken from" Kimenyi (1978), "An Ethnolinguistic Analysis of Kinyarwanda Kinship Terms" (note 19), and its in-law address passage cites **Kimenyi (1989), pp. 106–108** (note 22), so it is a route to Kimenyi's own findings:
- A married woman may address her parents-in-law as "the father or mother of so-and-so", **using the name of the youngest child**, or by praise names, or by a name she creates. `order-teknonym` raised to **medium** (Rwanda-specific for in-laws).
- **gutsinda:** a wife traditionally does not say her husband's or parents-in-law's names, nor her husband's siblings' and cousins' first names; "many aspects of the traditional culture, especially the taboos on women, are no longer applicable". New failure mode `wife-avoids-husband-name` (rw-kiny 0.6.0): a wife reporting a missing husband may not say his name; that is not a sign of a false claim.
- The naming ceremony is dated to the eighth day here, against the seventh in Kimenyi (1978, p. 258). Not used; noted as a discrepancy.
- Not covered: everyday use of the given name vs the Kinyarwanda name (`order-spoken-given-name` stays `low`).

**Simbananiye, L. (2005), "Les noms de personnes au Burundi : un support du lien social", *Anthropologie et Sociétés* 29(1): 167–181** (peer-reviewed, open on Érudit; it draws on Ntahombaye 1983 and Rodegem 1965). Read in full. Nothing on forms of address. Used (bi-kirundi 0.8.0):
- p. 171: the traditional system (a name different from the father's) **coexists** with the patronymic system brought by colonisation and Christianity; missionaries' attempt to impose the father's name was "un fiasco" (Rodegem 1965). Added to `structure-inheritance-disputed`; it supports keeping the varied parameter p.
- p. 171: **mwene** marks descent ("Gahungu mwene Bucumi" = Gahungu, son of Bucumi). New structure and failure mode `mwene-read-as-name`.
- pp. 171–172: birth-order and twin names (Nyandwi, Minani, Nyawenda, Bucumi, Karenzo; Bukuru/Butoyi; Nkurikiye, Ciza, Congera). Common names; not evidence of kinship on their own.
- p. 171: protective names meaning "nothing" or "no name" (Ntazina, Busabusa, Ntakije): failure mode `name-means-no-name`.
- Not used: the article's mentions of ethnic conflict (DR-1.7).

**Ntahombaye (1983)** itself is not online; the AfricaMuseum (Tervuren) library holds it (call number NTAHOMBAYE-J62). **Tests:** 133 pass; graph valid.

## 2026-11-09 — Children's speech (Swahili) and the remaining library gaps

**Gangji, N. (2012), *Phonological development in Swahili*, MSc thesis, University of Cape Town (open access, hdl 11427/2916)**; published as Gangji, Pascoe & Smouse (2015), *IJLCD* 50(2): 151–164. 24 children aged 3;0–5;11 in Dar es Salaam, single words named from pictures. Read §4.3 and Figure 3. **First source on children's pronunciation** (gap open since 28 Oct). Added to cd-swc-ln 0.5.0:
- `child-r-to-l` (medium): the most widespread pattern at every age (redio → ledio, lori → loli); r acquired last (by ~6).
- `child-weak-syllable-deletion` (medium): words of 3+ syllables lose unstressed syllables up to ~5;5 (themanini → nini). For names: a young child may give only the end of a long name.
- `child-initial-consonant-deletion` (low; nanasi → anasi), `child-cluster-reduction` (low; mwamvuli → mavuli, ages 3–4).
- Limits: coastal Tanzanian Swahili, children with English as a second language, n = 24. **Still no source for Kinyarwanda, Kirundi or Chichewa-speaking children**; name examples in Kirundi are marked derived and untested.

**Nassenstein (2019)**, *Modern Africa* 7(1) (already cited 28 Oct), re-read for mission spelling: it documents the rw/mw/tw choices and the Kinyarwanda *by* vs Kirundi *vy* split, but **not Catholic vs Protestant differences**. One addition: in at least one Kinyarwanda variety of eastern DRC, *bw* is written *bg* (p. 27, note 14; fieldwork statements), rw-kiny listener confusion at `low`. Also quoted there: van der Burgt (1917) says Germans, English and Dutch wrote *Warundi*, the French *Barundi* (writer-language effect on the prefix).

**Searched, not available online:** Ntahombaye (1983) (held by the AfricaMuseum library, Tervuren); Kimenyi (1989); Mioni (1975, 1970). These need interlibrary loan.

**Tests:** 133 pass; graph valid.

## 2026-11-09 — Gangji, Pascoe & Smouse (2015), published version, read in full

Copy obtained by the user through NYU. Same data as the thesis. Changes (cd-swc-ln 0.5.1): the published article is now the primary citation; **`child-r-to-l` lowered to `low`**, because the authors state that "much of the evidence for lateralization comes from the production of /lɛdiɔ/ for redio" (one word); weak syllable deletion is described as "the second most frequent process" (ages 3;0–5;6). The authors also caution that all 24 children spoke English as a second language and that their full language profiles were not recorded. **Tests:** 133 pass.

## 2026-11-09 — Field observation located (Malawi); print-only sources dropped

**Correction of the earlier entry today ("Mama X" has two readings):** the user's observation was made **in Malawi**, not in the Great Lakes: everyone used *mama* and *papa* to refer to a person, as Portuguese uses *senhora*/*senhor*. The people there were mostly from the DRC, some from Rwanda. A Kenyan colleague of the user speaks the same way (second-hand). Source wording corrected in rw-kiny 0.6.2 and added to cd-swc-ln 0.5.2 (`order-mama-x`), where it supports the honorific reading for Congolese speakers.

**User's decision:** Kimenyi (1989), Ntahombaye (1983) and Mioni (1975) exist only in print and will **not** be requested; their key content already arrived second-hand (Adekunle 2007 citing Kimenyi pp. 106–108; Simbananiye 2005 drawing on Ntahombaye). `order-spoken-given-name` stays `low`; Catholic vs Protestant Kirundi spelling stays undocumented. Item 1 of the next-session list is closed.

## 2026-11-09 — Wikis removed as sources (user's decision)

Per the rule "Wikipedia is not a source" (5 Nov), the user decided to remove every remaining wiki citation. **20 entries** across the three packs: 17 citing Wikipedia/Wiktionary alongside another source, plus 3 citing **Wikibooks** (missed by the first audit, which searched only for "Wikipedia").

**Confidence after removal:**
- Unchanged (a published source remains): Kirundi transliteration (Comparative Grammar), length/tone (Comparative Grammar, van de Vijver et al., Rusanganwa), Kinyarwanda name structure (Kimenyi 1978, HRW), Lingala spelling and e/ɛ (APiCS), Congo Swahili (Bose 2016), rw/mw confusions (FSI, Nassenstein, Rusanganwa), colonial place names (Statoids, plus Niyonkuru 1987).
- **Lowered:** Chichewa r/l writing rule, 3 entries → `low` (the remaining "Lyons & Mchombo, *Chichewa Grammar*" could not be confirmed as a published book); Kinyarwanda glide table → `medium` (sw, by, py, ty rest on the FSI synopsis only); Kinyarwanda r/l rule and liquid inventory → `medium` (one IJLRHSS article remains; the Kirundi r/l rule has stronger sources); Swahili/Lingala prenasals → `medium` (website only); the Lingala "1976 standard" date removed (Wikipedia only).
- `order-spoken-given-name` → **`hypothesis`**; its source now states that no published source was found and that Wikipedia was only the pointer.

**Guards:** `validate_pack` rejects any source containing "wiki" (rule entries and failure modes) unless it says "only as a pointer"; `test_no_wiki_source_anywhere_in_repo_graph` scans every graph file (packs, cross-pack names, places). **Tests:** 135 pass; graph valid. Packs: bi-kirundi 0.8.1, cd-swc-ln 0.5.3, rw-kiny 0.6.4.

**Gaps opened by this (sources to find later):** a Chichewa orthography source (Malawi's 1973 rules); a Swahili or Lingala grammar for prenasals; a Kinyarwanda phonology for the full glide table.

## 2026-11-09 — Chichewa spelling sourced; confidence policy

**User's request:** all entries at `high`. Agreed approach: confidence is raised **only when a strong source is found**, entry by entry; `disputed` (7) and `hypothesis` (7) are kept because they describe the state of the evidence. Baseline before this work: 53 high, 74 medium, 11 low.

**Chichewa r/l (3 entries, `low` → `high`):** Chirwa, M. N. (2008), *Trill maintenance and replacement in Chichewa*, MA dissertation, University of Cape Town (open access), pp. 4–5 and 31, citing Mchombo (2001) and the Chichewa Orthography Rules: r and l are allophones of one phoneme; **r after i and e, l after a, o, u**, within a morpheme; **no Chichewa word begins with r**; in speech r is often replaced by l, and writers hypercorrect (*ndili* written *ndiri*). Date: UK Government, *Malawi Toponymic Factfile* (2025): "standardised in 1973 in the New Chichewa Orthography Rules". The unconfirmed "Lyons & Mchombo" citation was replaced. Spellings now include word-initial l and hypercorrect r. **Still a hypothesis:** that Malawian clerks apply these rules to refugees' names (benchmark cases stay hypothesis-weighted).

**Chichewa c → ch (3 entries, `medium` → `high`):** Downing, L. J. & Mtenje, A. (2017), *The Phonology of Chichewa* (Oxford University Press), ch. 1 note 2 (publisher preview): the Chichewa Board writes the plain affricate **ch** and the aspirated one **tch**; Watkins (1937) and some linguists write c. Added *tch* as a spelling. Peace Corps Malawi kept as a second source.

Packs: bi-kirundi 0.9.0, cd-swc-ln 0.6.0, rw-kiny 0.7.0. **Tests:** 135 pass; graph valid.

## 2026-11-09 — Batch 1: how French writers spell African sounds

**New evidence from our own official data:** spelling patterns counted in the official place names already in `places-2026.1` (DRC 588 names, mainly the RGC; Burundi 149; Rwanda 48):

| Pattern | DRC | Burundi | Rwanda |
|---|---|---|---|
| tsh / tch | **19** / 1 | 0 / 0 | 0 / 0 |
| sh / ch | 16 / 2 | 7 / 0 | 1 / 0 |
| dj / j | **16** / 11 | 0 / 4 | 0 / 4 |
| w / ou | 63 / 4 (colonial: Luluabourg, Kivou) | 13 / 0 | — |
| ny / gn | 13 / **0** | 17 / 0 | 3 / 0 |

**Findings:** (1) in the DRC the sound /tʃ/ is written **tsh** (Belgian-era spelling), not the French *tch* the packs assumed; *tsh* added first. (2) **dj** for /dʒ/ is common in DRC names (Djolu, Budjala), a convention missing from the packs; added to cd-swc-ln (Djuma/Juma-type pairs are one name). (3) *ou* for /w/ survives mainly in colonial-era names. (4) *gn* for /ɲ/ is unattested in all 785 names: a French writer by ear may use it, but official names do not. (5) Burundian and Rwandan official names contain **no** French-style spellings.

**Confidence:** the French spelling correspondences (ou, ch, tch, gn, ss) are facts of French orthography (Cornevin 1984; FSI French phonology) now backed by the official data on where they occur: **13 entries raised to `high`**, with prevalence in the notes. The Kinyarwanda c/cy correspondence (Comparative Grammar, Table 1) raised to `high`. **Kept at `medium`:** the Swahili writer's *j* for /ʒ/ (2 entries): Swahili lacks /ʒ/ (FSI), but that a Swahili writer writes it *j* is an inference.

**Next evidence step:** the naming profiles (CongoNames, NESA) will measure these spellings in **personal** names, which is the stronger test. Packs: bi-kirundi 0.10.0, cd-swc-ln 0.7.0, rw-kiny 0.8.0. Totals now: high 73, medium 58, low 8, hypothesis 7, disputed 7, unknown 1. **Tests:** 135 pass.

## 2026-11-09 — Batch 2 (part 1): glides, prenasals, r/l

**New sources:**
- **Demolin, D. (2016)**, "Clicks, stop bursts, vocoids and the timing of articulatory gestures in Kinyarwanda", *Studies in African Linguistics* 45(1&2), Table 1: Jouannet's (1983) phonetic transcriptions against Coupez et al. (2005) spellings, with acoustic data from seven speakers. Written *-bwá* "dog" = [ímbgá]; *-rwáara* = [índgwâɾà]; *-nwa* = [ùmùnŋwà]; written *mp* (*-hweempwe*) = [m̥h].
- **Myers, S. (2006)**, "Kinyarwanda: Introduction", *Phonology: case studies*, UT Austin: consonant table with one tap ɾ and **no l**; affricates pf, ts, ʧ.
- **Nimbona & Simon (2022)** §3.2 (already read): "La consonne /l/ n'existe pas en kirundi"; prenasals are single syllable-initial units.

**Policy for listener confusions:** raised to `high` only when the confusion is **attested in writing**, not just in pronunciation.

**Raised to `high` (14):** rw-kiny glide strengthening (four sources), mp = [mh], r/l rule, phonemes /ɾ/ /tʃ/ /pf/ /ts/, prenasals, r/l confusion (UN 1533 aliases), bw/bg confusion (pronunciation in four sources; *bg* attested in writing by Nassenstein; the two bw/bg entries merged). bi-kirundi /ɾ/, prenasals, r/l confusion (Cox's four spellings, ISALE/Isare), nr/r confusion (Nyarusange/Nyanrusange and Nyiragongo/Nyirangongo in official sources).

**Kept at `medium`, with reasons:** rw/tw/sw/mw/vy confusions (pronunciation sourced, spellings like *rgw* not yet attested; the naming profiles will test this); Nimbona & Simon and Gangji rules (one study each); Kirundi o→w (one source); shy (scholars differ). **Waiting:** Kochetov (2016), *Glossa* 1(1): 1–31, on Kirundi consonant + glide sequences (site blocks scripts; the user will download it).

Packs: rw-kiny 0.9.0, bi-kirundi 0.11.0. **Tests:** 135 pass.

## 2026-11-09 — Batch 2 (part 2): Kochetov (2016) read in full

**Source:** Kochetov, A. (2016), "Palatalization and glide strengthening as competing repair strategies: evidence from Kirundi", *Glossa* 1(1): 14, 1–31, doi:10.5334/gjgl.32 (open access; downloaded by the user because the site blocks scripts). Data from Ntihirageza (1993), Broselow & Niyondagara (1990) and Meeussen (1959), cross-checked with Cox (1969) and Rodegem (1970), confirmed with a Kirundi speaker from Bujumbura and by acoustic analysis.

**Findings (examples (4) and (28)):** tw [tkw], sw [skw], dw [dgw], bw [bg], pw [pk], fw [fk], mw [mŋ], nw [nŋw]; rw [ɾgw] or **[gw] with the r deleted** (*kurwaara* [kugwaːra]); b+y [vzɟ] (*vy* contains a z); m+y [mɲ]; the rhotic varies [r~ɾ~ɽ~l].

**Changes (bi-kirundi 0.12.0):** `cluster-pronunciation` → **`high`**, rewritten with the full list. **Correction:** mw is [mŋ], not "[my] or [mg]" as first recorded from the FSI synopsis. New listener confusion rw ~ gw (`medium`). The rw/sw/tw/mw/vy confusions keep `medium` under the writing-attestation policy, now with Kochetov as their pronunciation source.

**Tests:** 135 pass.

## 2026-11-09 — Incident (DR-5): CENI ethnicity column exposed while checking a layout

**What happened:** to verify the name layout of a CENI 2025 candidate list (Bujumbura, deputies), Claude downloaded the PDF to `~/namebridge-ref/ceni/`, converted it to text on disk, and printed its first ~20 lines into the Claude Code session. Those lines include the list's **"Ethnie" column** for about ten candidates. This breaks DR-1.7 ("never written to disk"; drop on read).

**Contain:** the PDF and the text file were deleted minutes later (`rm -rf ~/namebridge-ref/ceni`). Nothing was committed: no ethnicity value is in the repo, the packs or the graph (the commit that follows contains only the layout facts: column order, capitals).

**Assess:** the data is public (published by CENI) and concerns adult political candidates, not refugees or minors. It remains in the transcript of this session (sent to the AI provider as part of the conversation). Harm judged low; the breach is of our own rule, not of a confidentiality duty.

**Notify:** DR-5 step 4 (inform the professor) **waived by the user** on 9 Nov 2026: nobody accessed the exposed commit in the hour it was public, the data was a public official list, and the history has been rewritten. No GitHub purge requested.

**Second finding, same incident:** a commit pushed on 9 Nov 2026 (since rewritten) put **one candidate's real full name**, copied from the list as a layout example, into a bi-kirundi source note and the graph (DR-1.1, DR-1.4). Removed, and **history rewritten** with the user's approval (DR-5 step 2): the two commits of this work were squashed into one that never contains the name, and pushed with `--force-with-lease`. GitHub may keep the old commit reachable by its hash for a while; asking GitHub support to purge it is optional. Given names copied from the same rows were also removed.

**Learn:** new procedure in DR-1.7: inspect such files by column headers only, never dump text or rows to the terminal, a file or an AI session. DR-1 numbering fixed (two items were numbered 7).

## 2026-11-09 — Batch 3 (part 1): Rwanda's Law 71/2024 read; CENI layout corrected

**Rwanda, Law No 71/2024 governing persons and family** (Official Gazette n° Special of 30/07/2024), English text read (arts 2, 36–43):
- art. 2(p): a **surname** "may be a family name shared by descendants of the same family, or any specific name, or both". This resolves the rw-kiny `structure-father-element` dispute (The New Times 2026 vs HRW 1999): both practices are legal, so the accounts describe different families. Entry rewritten, `high`; the benchmark keeps the varied parameter q. `relationship_implications.surname_agreement` changed from `disputed` to `context-dependent`.
- art. 36(2): in administrative documents the **family name is placed first**, or the document is invalid. `order-surname-first-uppercase` → `high` (order now a legal rule; capitals remain library practice).
- arts 37–39: legal name = birth record; parents choose freely; a child **cannot bear only all** of a parent's or sibling's names. `structure-law-71-2024` → `high`, article text replacing the summary.
- art. 40: marriage does not change a name, but **a spouse may add the other's surname** before the civil registrar; a **religious vow name** may be added to the usual name. Two new structures (`high`).
- arts 42–43: change of name by the Minister, effective when recorded in the birth register; **documents under the former name remain valid**. New failure mode `documents-under-former-name` (relevant to `NAME_CHANGE.md`).

**CENI layout correction (bi-kirundi 0.13.0):** the candidate lists have separate **Nom** and **Prénoms** columns, **both entirely in capitals**. The earlier entries (surname in capitals, given names in lower case) were wrong; corrected and raised to `high`. The lists also confirm the structure Kirundi surname + Christian given name (`structure-kirundi-first-then-christian` → `high`); `structure-no-precolonial-family-name` → `high` with Simbananiye (2005) as a second source.

`GATE_EXAMPLES.md` example 1 ("NSHIMIRIMANA Belyse") is an invented **case-database** record, not a CENI list, so it is left as is.

Packs: rw-kiny 0.10.0, bi-kirundi 0.13.0. **Tests:** see commit.

## 2026-11-09 — Batch 3 (part 2): Kirundi dictionary, DRC Family Code, Swahili textbook

**Cox (1969, rev. 2023), Kirundi-English dictionary:** "child (of) mwene", "son (of) mwene" → `structure-mwene-filiation` **high** (second source after Simbananiye). New: **Nyirababiri** "mother of twins", **Sebabiri** "father of twins": titles, not names (new structure + failure mode `title-read-as-name`).

**Birth-order names:** second source, the University of Burundi paper already cited for bi-kirundi (server unreachable today; passage confirmed from the search index): "Nyandwi, the seventh child; Minani, the eighth child; Nyabenda, the ninth child". It spells the ninth-child name **Nyabenda**, Simbananiye **Nyawenda**: both recorded as variants; entry → **high**.

**DRC Family Code** (Loi 87-010 of 1987, amended by Loi 16/008 of 2016; consolidated text on Leganet), arts 56–67 read directly. The pack already held arts 56, 57, 62 and 63–64 at `high`. New: **art. 60**, a child with no known parents gets a **registrar-assigned name**, changeable until age five (structure + failure mode `assigned-foundling-name`: for such children matching must rest on non-name evidence); **art. 59**, a father recognised later may **add** an element (failure mode `name-element-added-later`). Arts 56/57/61/64 back `order-no-traditional-surname` and `order-foreign-forms` → **high**. Art. 66 confirms that court name changes are published in the *Journal officiel* (the subject of gate G8).

**Also:** `structure-dual-origin` → high (Radio-Canada 2020 on authenticité, plus art. 58); `order-mama-x` → high with a second academic source (Wawire 2025, Baylor University open Swahili textbook: Mama/Baba as respectful titles, and "Mama Juma" for Juma's mother).

**Kept below high, with reasons:** rw-kiny gendered prefixes (Kimenyi 1978 only); `order-teknonym` (Rwanda-specific only for in-laws); bi-kirundi `order-aggregators-swap` (one observation of a non-authoritative site); mission spellings (`hypothesis`, Mioni not obtainable).

Packs: bi-kirundi 0.14.0, cd-swc-ln 0.8.0. Totals: **high 106**, medium 32, low 7, hypothesis 7, disputed 6, unknown 1. **Tests:** 135 pass.

## 2026-11-09 — Week 4 item 4: DRC naming profile from published aggregates (no raw data)

**Approach (safer than the plan):** the CongoNames corpus is not distributed as a dataset; reproducing it means crawling the DRC Ministry's exam-result PDFs (8 million names, mostly of minors). The authors, however, publish **aggregate tables** in their repository (`reports/name_analysis/*.csv`). The profile was built **from those aggregates only**: no individual record was downloaded or read. Two published tables that list **full names** (`normalized_duplicate_names`, `unusual_names`) were identified from their headers and **deleted unread** (DR-1). The repository declares no licence; the paper (MDPI *Data*) is CC BY 4.0, and the profile holds statistical facts with attribution.

**Profile** `namebridge/data/profiles/cd-congonames-2026.1.json` (script `scripts/build_profile_congonames.py`; source commit and file checksums recorded): 8,053,983 records, 2008–2023, 12 provinces. Token count: 3 tokens 78.5%, 2 tokens 17.6%, 4 tokens 3.5%; median 21 characters; 76% of distinct full names occur once. Top-50 first and last tokens by sex (smallest count 9,793), n-grams, letters, province and year distributions. No ethnicity, clan or religion pattern.

**Findings used in cd-swc-ln 0.9.0:**
- New order rule (high): exam lists write **nom, postnom, prénom** (Bantu first tokens, Christian last tokens).
- Attested variant sets among the 50 most frequent first tokens: **ngoy / ngoyi / ngoie** and **mwamba / muamba** (recorded as `proposed` variant pairs in the profile; evidence added to `lingala-spelling-vacillates`).
- **tsh** is a top-50 trigram of the Bantu name parts (370,097): the batch-1 place-name finding holds for personal names.
- New failure mode: compound given names split or joined ("dieu" is a frequent final token; interpretation of an aggregate).
- Diacritics in only 0.09% of names: supports folding.

**Limits:** exam candidates (adolescents and young adults), not older adults or refugees; only the top 50 elements per position are published, so rare-name slots will be filled by invented elements built from the n-grams (as planned). *dj*, *ou* and *gn* are not in the published top-50 n-grams, so nothing is concluded about them.

**Bug found and fixed (guard):** the ethnicity field guard matched the stem "tribu" inside **dis-tribu-tion** and **at-tribu-te**, rejecting the profile's `token_count_distribution`. Benign words are now removed before the stem search; tests in both directions (`test_guard.py`), plus guard tests for profiles (`test_profiles.py`: sources, counts ≥ 5, single-token elements, no forbidden fields). **Tests:** 141 pass.

**Open for the user (protocol change):** the copy test (BENCHMARK_PROTOCOL §2.4, DR-1.2 step 3) assumes the raw list is held; with aggregates only it cannot be run as written. Proposed replacement: since the generator recombines published top-frequency elements and invents rare ones, measure instead the share of generated full names built only from top-50 elements, and keep no list of real full names at all.

**Still to do in item 4:** Rwanda (NESA lists) and Burundi (NESA elements weighted by CENI frequencies). No published aggregates are known for these; they would need local processing of raw lists under DR-1.

## 2026-11-09 — Copy-test change approved; Rwanda naming profile from NISR (no raw data)

**User's decisions:** (1) the copy-test change is **approved** (BENCHMARK_PROTOCOL §2.4 realism check 2 rewritten: with aggregate-only profiles, measure the share of synthetic full names built only from top-frequency elements; the original test still applies to any profile built from a raw list). DATA_RULES DR-1.2 now says **published aggregates first**. (2) For Rwanda and Burundi, **look for published aggregates before processing any raw list** (option B).

**Rwanda: found.** The National Institute of Statistics of Rwanda publishes, in each *Rwanda Vital Statistics Report*, an annex "Top 20 most preferred babies' surnames by sex" from the CRVS system: **2024** (Annex 1) and **2025** (Annex 2). Profile `data/profiles/rw-nisr-2026.1.json` (script `scripts/build_profile_nisr.py`, report checksums recorded): 4 lists of 20 Kinyarwanda names with counts (largest: ISHIMWE, male, 8,407 in 2025; INEZA, female, 8,216), plus births registered (341,029 in 2024; 356,838 in 2025).

**Findings:** most top names are **unisex** (failure mode `kinyarwanda-names-unisex`); names sharing a root are **distinct names** (Ishimwe/Ashimwe/Nishimwe, Iganze/Aganze, Mpano/Impano; failure mode `same-root-different-names`); none of the top names uses the gendered prefixes nyira-/muka-, which therefore mark older names (note on the prefix entries; they stay `medium`). rw-kiny 0.11.0.

**Data quality, kept as published:** the same name appears twice in one column in both years (e.g. female INEZA ranks 1 and 11 in 2024). An earlier copy of the 2025 report (`alpha.statistics.gov.rw`) prints the 2024 figures under the 2025 title; the final report is used.

**Limits:** newborns of 2024–2025, not the refugees' generation; Kinyarwanda names only, no Christian given names. Older cohorts would need other sources (e.g. NESA exam lists, raw).

**Burundi: no published aggregates found.** INSBU (formerly ISTEEBU) publishes no name frequencies; Geneanet and Forebears are aggregators, allowed only as a cross-check (G6). Decision needed (see the user).

**Tests:** 141 pass.
