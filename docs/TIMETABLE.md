# Timetable — weekly scope of work

Draft, 19 Oct 2026. A plan for the rest of the fall semester, week by week. Adjust it as decisions change; earlier versions are in the git history.

## Assumptions

- **Period:** Mon 19 Oct to Fri 18 Dec 2026 (9 weeks, assumed end of the NYU fall semester). After that, a lighter plan to April 2027.
- **Who:** me, with Claude writing much of the code; the professor reviewing.
- **Constraints (from `SOLUTIONS.md`):** no funding, no partner contact, no contact with residents, synthetic data only.
- **Priorities:**
  1. **2F Open Great Lakes Names** is the main track (most of each week).
  2. **1A Evidence for the Refugee Bill** is the second track (briefs).
  3. **1B tracker** and **2A rain warnings** are small, fixed tasks.
- **NameBridge (`CONCEPT-IDEA.md`)** feeds into 2F: its typed, sourced edge model, its language-pack format and its metrics (recall@K, precision, false-match rate). Its phases 3–4 (shadow pilot with an organisation, live deployment) are out of scope.

## Every week

- **1B check (~30 min):** Cabinet, Parliament and Gazette news on the Refugee Bill (Malawi24, MBC, Nation Online, Inua Advocacy). Update the watch list in `DZALEKA_SITUATION_RESEARCH.md` §13 if anything moved.
- **Log:** one entry in `RESEARCH_LOG.md` (what was done, sources, decisions, next steps).
- **Commit and push** at the end of each work session.

## At a glance

| Week | Dates | 2F (main) | 1A / 1B / 2A | Done when |
| --- | --- | --- | --- | --- |
| 1 | 19–23 Oct | Merge NameBridge into 2F; start Kinyarwanda research | 1B tracker page; look for the full bill text | 2F scope fixed; tracker published |
| 2 | 26–30 Oct | Kinyarwanda and Kirundi naming and spelling | 1A comparative brief outline | Rules list for both languages, with sources |
| 3 | 2–6 Nov | DRC naming; Christian names; province reforms; threat model | 2A data check (CAP feed, Friedman 2021 data) | Research notes complete; threat model written |
| 4 | 9–13 Nov | Dictionary v0.1; intake guide draft | 1A comparative brief draft | First data files in the repo |
| 5 | 16–20 Nov | Dictionary v0.2; intake guide v1; design the synthetic data | 2A shadow-mode design | Guide v1; test-data spec |
| 6 | 23–27 Nov | Synthetic data generator (light week: Thanksgiving) | 2A logger running; 1A cost brief draft | Generator produces a test set |
| 7 | 30 Nov–4 Dec | Matching module layers 1–3; two baselines | — | Baselines run on the test set |
| 8 | 7–11 Dec | Layers 4–5; run the evaluation | 1A briefs final; 2A shadow mode starts with the rains | Results table |
| 9 | 14–18 Dec | Evaluation report; release v1.0 | Semester wrap-up for the professor | Everything published and documented |

## Week by week

### Week 1 — 19–23 Oct: scope

- **2F:** ✔ done 19 Oct. Decide which NameBridge parts 2F adopts: the edge metadata (source, relation type, region, confidence, review status), the language-pack format (§11) and the metrics (§9.2). Write this into `SOLUTIONS.md` 2F. Fix `CONCEPT-IDEA.md` §14 (it says `SOLUTIONS.md` is missing).
- **2F:** start the Kinyarwanda literature: how names are formed, the orthography, and why siblings share no name (HRW 1999 and the onomastic sources NameBridge cites).
- **1B:** create the tracker page: the legislative steps (Cabinet → Gazette → readings → assent → commencement), each with a status, a date and a source. Plus a short "proposed vs in force" explainer.
- **1A:** look for the full bill text and the Law Commission report (open question in `SOLUTIONS.md` §7).
- **Done when:** 2F's scope is written down and the tracker is published.

### Week 2 — 26–30 Oct: Kinyarwanda and Kirundi

- **2F:** naming systems and spelling rules for both languages: "cy"/"c"/"ch", "-iye"/"-ye", and other common variants.
- **2F:** check the open question from NameBridge §2.3: do Burundian siblings share a name? Record it as an evidence gap if no source settles it. Don't assume it from the Rwandan case.
- **1A:** outline the comparative brief: Kenya (Refugees Act 2021), Uganda, Zambia. Use the case files in `docs/cases/`.
- **Done when:** there is a list of rules for both languages, each with a source and a confidence level.

### Week 3 — 2–6 Nov: DRC, Christian names, places, risks

- **2F:** DRC naming: nom + postnom + prénom, and the *authenticité* policy. Congolese Swahili spelling.
- **2F:** Christian-name equivalents (Jean / John / Yohana …).
- **2F:** province reforms: Burundi 2025, Rwanda 2006, DRC 2015. Get the official boundaries from HDX (OCHA common operational datasets).
- **2F:** write a short threat model: who could misuse the work, and the safeguards (from `SOLUTIONS.md` 2F and NameBridge §8, as far as they apply to a public dictionary).
- **2A:** check that the Met Malawi CAP feed is still readable. Find out whether the 2021 drone data or model is openly available, and under what licence (open question).
- **Done when:** the research notes for all three languages are complete and the threat model is written.

### Week 4 — 9–13 Nov: first dictionary

- **2F:** dictionary v0.1 as CSV / JSON (CC BY 4.0): spelling variants, Christian names, orthographic rules, places old and new. Every entry carries its source and confidence.
- **2F:** first draft of the intake guide (ask all names in any order, parents' names, colline, province as it was then; never ethnicity or clan).
- **1A:** draft of the comparative brief.
- **Done when:** the first data files are in the repo.

### Week 5 — 16–20 Nov: guide and test data design

- **2F:** dictionary v0.2 (fill the gaps found in week 4); intake guide v1.
- **2F:** design the synthetic test set: how invented people are built, and the list of realistic errors (swapped order, spelling variant, translated Christian name, renamed province, typos, missing dates). Include hard negatives: different people with common names.
- **2A:** design shadow mode: what counts as a warning (forecast + exposed zones), what gets logged, and where the ground truth comes from (news, public reports).
- **Done when:** guide v1 is written and the test-data spec is ready.

### Week 6 — 23–27 Nov: generator (light week)

- **2F:** code the synthetic data generator.
- **2A:** start the logger before the rains (expected mid-Dec).
- **1A:** draft of the cost brief (WFP / UNHCR funding data from the situation research).
- **Done when:** the generator produces a test set.

### Week 7 — 30 Nov–4 Dec: matching module, part 1

- **2F:** layers 1–3: normalise; ignore name order; regional spelling rules and a phonetic key for these languages.
- **2F:** two baselines: exact search, and generic fuzzy search (roughly what platforms do now).
- **Done when:** both baselines run on the test set.

### Week 8 — 7–11 Dec: matching module, part 2, and evaluation

- **2F:** layers 4–5: dictionary lookups; scoring with age, birthplace and parents' names, returning ranked possible matches with the reason.
- **2F:** optional: Splink as a third comparison (NameBridge's MVP choice).
- **2F:** run the evaluation: recall, precision and false matches for each method.
- **1A:** finish both briefs. Add checklist scoring if the bill text has been found.
- **2A:** shadow mode starts with the rains: warnings computed, not published.
- **Done when:** the results table exists.

### Week 9 — 14–18 Dec: write up and release

- **2F:** evaluation report. State the limit clearly: synthetic data only, so results may not hold on real records.
- **2F:** release v1.0: dictionary, intake guide, module, report.
- **All:** update `SOLUTIONS.md` and `README.md`; prepare a short semester summary for the professor.
- **Done when:** everything is published and documented.

## After the semester (Jan–Apr 2027)

| When | What |
| --- | --- |
| Weekly, Jan–Apr | 2A shadow mode: log warnings and what happened (~1 h/week) |
| Jan–Mar | 2F phase 2 language packs: Lingala, Mashi and other eastern DRC languages (a few weeks each) |
| At each legislative step | 1B tracker update; 1C starts only if the law passes |
| End Apr 2027 | 2A season review: did the warnings match what happened? |
| After the 2F evaluation | Decide whether to offer 2F to REFUNITE, the Red Cross or UNHCR (final phase) |
