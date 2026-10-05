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
