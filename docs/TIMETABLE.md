# Timetable — NameBridge, weekly scope of work

Draft, 19 Oct 2026. The project is **NameBridge** (`CONCEPT-IDEA.md`). This is a week-by-week plan for the rest of the fall semester. Earlier versions are in the git history.

## Assumptions

- **Period:** Mon 19 Oct to Fri 18 Dec 2026 (9 weeks, assumed end of the NYU fall semester).
- **Who:** me, with Claude writing much of the code; the professor reviewing.
- **Scope this semester:** NameBridge §10 **phases 0–2**, compressed into 9 weeks. Phases 3–4 need an authorised tracing organisation and real cases, so they come after the semester and only if a partner is found.
- **Pilot corridor (proposed):** the Great Lakes → Malawi (Dzaleka): Kinyarwanda, Kirundi and Congolese Swahili, with French and English as the languages of the records. This reuses the situation research. To confirm in week 1.
- **Data:** synthetic only during the semester. No real case data until there is a lawful basis and a partner (§8, §9.1).
- **Not used:** the other ideas in `SOLUTIONS.md` (kept for reference).

## Every week

- **Log:** one entry in `RESEARCH_LOG.md` (what was done, sources, decisions, next steps).
- **Commit and push** at the end of each work session.
- **Sources:** every graph edge and rule has a source and a confidence level. Nothing enters as `reviewed` without one.

## At a glance

| Week | Dates | §10 phase | Main work | Done when |
| --- | --- | --- | --- | --- |
| 1 | 19–23 Oct | 0. Governance | Corridor, users, purposes, prohibited uses; repo skeleton | Scope document approved by the professor |
| 2 | 26–30 Oct | 0. Governance | Threat model, data-protection assessment (desk), benchmark protocol | Phase 0 exit criteria written |
| 3 | 2–6 Nov | 1. Name corpus | Two-graph schema; language-pack template; Kinyarwanda and Kirundi research | Schema and validator in the repo |
| 4 | 9–13 Nov | 1. Name corpus | Curate the Kinyarwanda, Kirundi and DRC packs; ICU / CLDR set-up | First packs load into the graph |
| 5 | 16–20 Nov | 1. Name corpus | Reach the pilot corpus; negative constraints; review workflow | Graph v0.1, every edge sourced |
| 6 | 23–27 Nov | 2. Linkage MVP | Synthetic benchmark (light week: Thanksgiving) | Gold set of matches, non-matches and families |
| 7 | 30 Nov–4 Dec | 2. Linkage MVP | Preserve-first ingestion; transliteration; blocking; deterministic baseline | Baseline results on the benchmark |
| 8 | 7–11 Dec | 2. Linkage MVP | Splink model plus graph features; calibration; evaluation | Results for every option tested |
| 9 | 14–18 Dec | 2. Linkage MVP | Explanation view; evaluation report; release v0.1 | Phase 2 exit: offline results, no live decisions |

## Week by week

### Week 1 — 19–23 Oct: scope (phase 0)

- ✔ done 19 Oct: `CONCEPT-IDEA.md` added to the repo, and §14 corrected.
- **Corridor:** confirm the pilot corridor and its languages and scripts (proposal above). Note that §2.3 (Burundi) is an open question.
- **Users and purposes:** who would use NameBridge (tracing caseworkers, family-tracing platforms), for what (§8 control 1), and the prohibited uses (§12 "should not have").
- **Repo:** a skeleton for the code (`namebridge/`): package, tests, data folder for the graph, and the licence (code open source; graph CC BY 4.0).
- **Done when:** a one-page scope is written and the professor has seen it.

### Week 2 — 26–30 Oct: risks and test rules (phase 0)

- **Threat model:** who could misuse the system (§8: stalkers, traffickers, hostile governments, armed groups) and which controls block each risk.
- **Data-protection assessment (desk version):** what data the system would hold, why, for how long, and who could see it, using the ICRC handbook.
- **Benchmark protocol (§9):** what the test set must contain, the metrics, the splits, and the cost of a false positive vs a false negative.
- **Start the research:** Kinyarwanda naming (HRW 1999, the onomastic sources in §2.2).
- **Done when:** the phase 0 exit criteria are written: purpose, benchmark protocol, data rules. Data stewards and an advisory group can't be named yet, so record that as a gap.

### Week 3 — 2–6 Nov: schema (phase 1)

- **Name Knowledge Graph** (§5.1A): node and edge types, and the required edge metadata, as a schema with a validator.
- **Case graph** (§5.1B): schema only, kept empty and separate.
- **Language-pack template** (§11).
- **Research:** Kirundi naming and spelling; whether Burundian siblings share a name (§2.3).
- **Done when:** the schema and validator are in the repo, with tests.

### Week 4 — 9–13 Nov: first packs (phase 1)

- **Packs:** first versions of `rw-kiny`, `bi-kirundi` and the DRC (nom + postnom + prénom; Congolese Swahili).
- **Cross-pack data:** Christian names (Jean / John / Yohana …); places old and new (Burundi 2025, Rwanda 2006, DRC 2015; HDX boundaries).
- **ICU / CLDR:** set up normalisation, transforms and transform-path logging (§5.4).
- **Done when:** the first packs load into the graph and pass the validator.

### Week 5 — 16–20 Nov: pilot corpus (phase 1)

- **Corpus:** aim for about 2,000 sourced relationships for the corridor (§10 says 2,000–10,000).
- **Negative constraints** (`not_equivalent_to`) and ambiguous paths.
- **Review workflow:** `proposed` → `reviewed` → `deprecated`; a source and licence register.
- **Candidate sources:** review Onomaverse and Wikidata aliases (§7) for provenance, coverage and licence before using them.
- **Done when:** graph v0.1 is versioned and every edge is sourced and has a confidence level (phase 1 exit).

### Week 6 — 23–27 Nov: benchmark (phase 2, light week)

- **Synthetic gold set** (§9.1): invented people and families, with the corridor's error types (order, spelling, Christian names, renamed places, typos, incomplete dates, OCR errors), hard negatives with common names, and adversarially similar records.
- **Splits:** by person and family, so the same identity can't appear in both training and test.
- **Done when:** the gold set has reviewed matches, non-matches and family relationships.

### Week 7 — 30 Nov–4 Dec: pipeline (phase 2)

- **Ingestion:** keep the original name exactly as written, and add parallel normalised forms (§5.3).
- **Transliteration and variants** as hypotheses, with the path that produced each one (§5.4).
- **Blocking:** the strategies in §5.5, aiming for high recall.
- **Baseline:** deterministic rules and phonetic matching (option 5).
- **Done when:** the baseline runs on the benchmark and gives results.

### Week 8 — 7–11 Dec: model and evaluation (phase 2)

- **Splink** with name, age or date, place and family evidence; term-frequency adjustments (§5.6).
- **Graph features:** add graph-derived comparisons, and make sure one graph path isn't counted twice.
- **Calibration and thresholds:** separate thresholds for retrieval, review priority and confirmation.
- **Evaluation:** deterministic, Splink only, graph expansion only, and hybrid; metrics from §9.2, reported per language.
- **Done when:** there are results for every option tested.

### Week 9 — 14–18 Dec: explain and publish (phase 2)

- **Explanation view** (§5.7): a simple local view that shows two records side by side, the path that produced the candidate, and the weight of each field. The actions are same, different, possible and insufficient evidence.
- **Evaluation report:** results, limits (synthetic data only), and how the scores compare with the design judgments in §6.
- **Release v0.1:** graph, packs, code, benchmark generator, report.
- **Semester summary** for the professor.
- **Done when:** the phase 2 exit is met: offline results, and no live case decisions.

## After the semester

| When | What | Condition |
| --- | --- | --- |
| Jan–Mar 2027 | More packs (Lingala, Mashi and other eastern DRC languages); native-speaker review of existing packs | None |
| Jan 2027 on | Open research questions (§13), especially 1, 3, 4 and 7 | None |
| When ready | Phase 3: shadow pilot beside an authorised tracing workflow | Needs a partner (e.g. REFUNITE, the Red Cross, UNHCR) and real data under their rules |
| After phase 3 | Phase 4: controlled deployment; federation only if needed | Phase 3 exit criteria met |
| Final phase | Offer NameBridge free of charge to the tracing organisations **and to Fraternidade Sem Fronteiras (FSF)**: it could help FSF's work with children in care (foster children, the Órfãos do Congo project) to trace relatives. Cases involving minors follow the protected-person rules (§8, control 7) | Tested result in hand. NameBridge is not sold |
