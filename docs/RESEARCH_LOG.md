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
