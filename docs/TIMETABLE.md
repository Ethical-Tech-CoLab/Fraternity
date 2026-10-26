# Timetable — NameBridge, weekly scope of work

Draft, 19 Oct 2026. The project is **NameBridge** (`CONCEPT-IDEA.md`). This is a week-by-week plan for the rest of the fall semester. Earlier versions are in the git history.

## Assumptions

- **Period:** Mon 19 Oct to Fri 18 Dec 2026 (9 weeks, assumed end of the NYU fall semester).
- **Who:** me, with Claude writing much of the code; the professor reviewing.
- **Scope this semester:** NameBridge §10 **phases 0–2**, compressed into 9 weeks. Phases 3–4 need an authorised tracing organisation and real cases, so they come after the semester and only if a partner is found.
- **Pilot corridor:** the Great Lakes → Malawi (Dzaleka): Kinyarwanda, Kirundi and Congolese Swahili, with French and English as the languages of the records. This reuses the situation research. Confirmed 26 Oct in `SCOPE.md` §1.
- **Data:** synthetic only during the semester. No real case data until there is a lawful basis and a partner (§8, §9.1).
- **Not used:** the other ideas in `SOLUTIONS.md` (kept for reference).

## Differences from `CONCEPT-IDEA.md`

Deliberate, because of the project's limits:

| `CONCEPT-IDEA.md` | This timetable | Why |
| --- | --- | --- |
| Phases 0–2 take 12–22 weeks (§10) | 9 weeks | The semester ends 18 Dec |
| The decisive benchmark needs real error patterns (§9.1) | Synthetic data only | No partner, no lawful basis for real data yet; results are labelled preliminary |
| Phase 0 sets up an advisory group, a linguistic review panel and named data stewards | Recorded as a gap | No outside people yet |
| Two or three languages/scripts, with cross-script search central | Three Latin-script languages | The Great Lakes corridor; cross-script work is barely tested in this pilot |
| 2,000–10,000 curated relationships (phase 1) | About 2,000 | Time |
| Phases 3–4 | After the semester, only with a partner | They need real cases |
| §8 controls 10 (production security: encryption, tenant isolation, regional hosting, key separation, breach response, abuse testing) and 11 (per-region model governance, drift review) | Phases 3–4 | Only meaningful for a system running on real data |
| Naming systems in §3 outside the corridor (Arabic, Chinese, Slavic …) | Future language packs | One bounded corridor first (§10 phase 0) |
| Most research questions in §13 | Still open after the semester | Several need partners or real data |

Deferred "should have" items (§12): passport VIZ/MRZ field mapping, OCR-confidence ingestion, active-learning queue, privacy-preserving federation proof of concept.

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
- ✔ done 26 Oct: **corridor** confirmed in `SCOPE.md` §1 (DRC 65%, Burundi 22%, Rwanda 12% of Dzaleka, Mar 2025); §2.3 (Burundi) kept as an open question.
- ✔ done 26 Oct: **users, purposes and prohibited uses** in `SCOPE.md` §2–4. Proposed: law enforcement and governments are not users in the pilot (to confirm with the professor).
- ✔ done 26 Oct: **repo** skeleton `namebridge/`: Python package, pytest suite, `data/graph` and `data/packs`, licences (code Apache-2.0; graph and packs CC BY 4.0).
- **Done when:** a one-page scope is written (✔ `SCOPE.md`) and the professor has seen it (pending).

### Week 2 — 26–30 Oct: risks and test rules (phase 0)

- **Threat model:** who could misuse the system (§8: stalkers, traffickers, hostile governments, armed groups) and which controls block each risk.
- **Data-protection assessment (desk version):** what data the system would hold, why, for how long, and who could see it, using the ICRC handbook.
- **Data rules (§10 phase 0):** data sharing, retention and deletion, disclosure, and incident response.
- **Benchmark protocol (§9):** what the test set must contain; the metrics, including the fairness slices (§9.2); the splits by person and family and a temporal holdout (§9.3); name-only search measured separately from full-evidence resolution; and the cost of a false positive vs a false negative.
- **Start the research:** Kinyarwanda naming (HRW 1999, the onomastic sources in §2.2).
- **Done when:** the phase 0 exit criteria are written: purpose, benchmark protocol, data rules, threat model. Data stewards and an advisory group can't be named yet, so record that as a gap.

### Week 3 — 2–6 Nov: schema (phase 1)

- **Name Knowledge Graph** (§5.1A): node and edge types, and the required edge metadata, as a schema with a validator.
- **Case graph** (§5.1B): schema only, kept empty and separate.
- **Language-pack template** (§11).
- **Regression suite:** set up the test suite that every later change must pass (§12).
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
- **Graph API** (§12): given a name, return the typed paths to its variants, with confidence and source.
- **Intake guide** derived from the packs (§2.2; final phase in §10): which names and relationship evidence to record; never ethnicity or clan.
- **Done when:** graph v0.1 is versioned, every edge is sourced and has a confidence level (phase 1 exit), and the graph API answers queries.

### Week 6 — 23–27 Nov: benchmark (phase 2, light week)

- **Synthetic gold set** (§9.1): invented people and families, with the corridor's error types (order, spelling, Christian names, renamed places, typos, incomplete dates, OCR errors), hard negatives with common names, and adversarially similar records.
- **Splits:** by person and family, so the same identity can't appear in both training and test; plus a temporal holdout (later invented records with newer patterns, e.g. renamed provinces).
- **Done when:** the gold set has reviewed matches, non-matches and family relationships.

### Week 7 — 30 Nov–4 Dec: pipeline (phase 2)

- **Ingestion:** keep the original name exactly as written, and add parallel normalised forms (§5.3).
- **Transliteration and variants** as hypotheses, with the path that produced each one (§5.4).
- **Blocking:** the strategies in §5.5, aiming for high recall.
- **Baseline:** deterministic rules and phonetic matching (option 5).
- **Access controls on the case side** (§8, §12), on synthetic data: roles, an access log, and the retention and deletion flow. Person and family views kept separate.
- **Consent and lawful basis** (§8 control 4): every case record stores why it may be used and with whom it may be shared.
- **Protected-person flags** (§8 control 7): minors, trafficking, domestic violence, asylum, witness protection, or a person who may not wish to be found. Flagged cases are suppressed or routed separately; every case involving a minor is flagged.
- **Done when:** the baseline runs on the benchmark and gives results; the access log records every read of case data; a flagged synthetic case never appears in an ordinary search.

### Week 8 — 7–11 Dec: model and evaluation (phase 2)

- **Splink** with name, age or date, place and family evidence; term-frequency adjustments (§5.6).
- **Graph features:** add graph-derived comparisons, and make sure one graph path isn't counted twice.
- **Calibration and thresholds:** separate thresholds for retrieval, review priority and confirmation.
- **Evaluation:** deterministic, Splink only, graph expansion only, and hybrid; metrics from §9.2 reported per language and per fairness slice; name-only search reported separately from full-evidence resolution; results on the temporal holdout.
- **Commercial option** (option 4): run it on the same benchmark only if a free evaluation licence exists and no data leaves our machine; otherwise record it as not tested.
- **Done when:** there are results for every option tested.

### Week 9 — 14–18 Dec: explain and publish (phase 2)

- **Explanation view** (§5.7): a simple local view that shows two records side by side, the path that produced the candidate, and the weight of each field. The actions are same, different, possible and insufficient evidence.
- **Progressive disclosure** (§8 control 8): the reviewer first sees the minimum evidence; sensitive fields open only on request, and each opening is logged.
- **Challenge and correction** (§8 control 9): a match decision can be challenged and reversed, and corrections reach the graph edges and decisions that depended on it (§13 question 10).
- **Evaluation report:** results, limits (synthetic data only), and how the scores compare with the design judgments in §6.
- **Release v0.1:** graph, packs, code, benchmark generator, report.
- **Semester summary** for the professor.
- **Done when:** the phase 2 exit is met: offline results, and no live case decisions; controls 4, 7, 8 and 9 pass their tests on synthetic data.

## After the semester

| When | What | Condition |
| --- | --- | --- |
| Jan–Mar 2027 | More packs (Lingala, Mashi and other eastern DRC languages); native-speaker review of existing packs | None |
| Jan 2027 on | Open research questions (§13), especially 1, 3, 4 and 7 | None |
| When ready | Phase 3: shadow pilot beside an authorised tracing workflow | Needs a partner (e.g. REFUNITE, the Red Cross, UNHCR) and real data under their rules |
| After phase 3 | Phase 4: controlled deployment; federation only if needed | Phase 3 exit criteria met |
| Final phase | Offer NameBridge free of charge to the tracing organisations **and to Fraternidade Sem Fronteiras (FSF)**, for its work with children in care (foster children, the Órfãos do Congo project). FSF does not run the system: it uses the intake guide and refers cases to an authorised tracing service such as the Red Cross. Cases involving minors follow the protected-person rules (§8, control 7). Details: `CONCEPT-IDEA.md` §10, "Final phase" | Tested result in hand. NameBridge is not sold |
