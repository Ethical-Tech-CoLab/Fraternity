# Timetable — NameBridge, weekly scope of work

Draft, 19 Oct 2026; progress updated 26 Oct 2026. The project is **NameBridge** (`CONCEPT-IDEA.md`). This is a week-by-week plan for the rest of the fall semester. Earlier versions are in the git history.

## ⛔ Gates: decisions that block work

**Rule:** a task listed under "Blocks" must **not start** while its gate is open. Before any work session, check this table. Claude checks it too (`CLAUDE.md`), and stops and warns if a request would start blocked work.

- **⛔ hard gate:** do not proceed. The decision changes what we build, or whether we may do it at all.
- **⚠ soft gate:** you may proceed on the stated default, but the work may have to be redone.

If you choose to go ahead anyway, record it as an **override** in `RESEARCH_LOG.md` (who, why, what may need redoing).

| Gate | Decision needed | Who | Blocks | Must be resolved by | Status |
| --- | --- | --- | --- | --- | --- |
| **G1** ⛔ | Approve the phase 0 scope (`SCOPE.md`): purpose, users, prohibited uses. This is week 1's "done when" | Professor | **All of phase 1** (week 3 onward) | Mon 2 Nov | Open: to discuss with the professor on **Wed 28 Oct** |
| **G2** ⛔ | Governments and law enforcement are not users (`SCOPE.md` §2) | Professor | Week 3 role model in the case schema; week 7 access controls | Mon 2 Nov | Open: to discuss on **Wed 28 Oct** |
| **G3** ⛔ | Does NYU's IRB need to confirm the aggregate use of public name lists (CongoNames, NESA, the UN list)? Analysis in `IRB_DETERMINATION.md`: **likely Not Human Subjects Research** (public, not private, no interaction). The professor chooses **A** (self-determine, recorded in the log), **B** (email the HRPP; recommended) or **C** (formal NHSR via Cayuse) | Professor (→ HRPP if B or C) | Week 4: **downloading or processing any real name list**, and the naming profiles | Mon 9 Nov (B needs a few days; C about 1–2 weeks) | Open; analysis and draft email ready (26 Oct); to discuss on **Wed 28 Oct** |
| **G4** ⚠ | Error costs and targets (`BENCHMARK_PROTOCOL.md` §7). Default: the ratios decided by the user on 26 Oct | Professor | Week 6: benchmark size (26,000 is derived from them) and generation; week 8 thresholds | Mon 23 Nov | Deferred by the user on 26 Oct, to decide after seeing example records; default in use. **Examples ready 28 Oct:** `GATE_EXAMPLES.md` |
| **G5** ⚠ | `NAME_CHANGE.md` rule 5: no support for searches for people who changed names, including alleged perpetrators. Default: the rule as written | Professor | Week 7 protected-person routing; final wording of `SCOPE.md` §4 | Mon 30 Nov | Deferred by the user on 26 Oct, to decide after seeing examples; default in use. **Examples ready 28 Oct:** `GATE_EXAMPLES.md` (recommended: option A) |
| **G6** ⚠ | A source for Burundian names (data dependency, not an approval) | Us | Week 4 `bi-kirundi` pack and Burundi profile | Mon 9 Nov | Candidate proposed 28 Oct: CENI 2025 candidate lists, ethnicity column dropped on read (`RESEARCH_LOG.md`). **User to confirm**; download still waits for G3 |

**Not gates for the semester** (they block phase 3, not phases 0–2):

- named data stewards and an advisory group;
- a tracing partner;
- the text of UNHCR's 2022 policy;
- a study of name change in Malawi;
- **IRB review for anything involving contact with people** (native-speaker review in Jan–Mar 2027; phase 3 case data). This becomes a gate when that work is planned (`IRB_DETERMINATION.md`).

**Today (26 Oct):** nothing is blocked yet, because week 3 starts on 2 Nov. **Meeting with the professor: Wed 28 Oct** (G1, G2, G3). **If G1 and G2 are still open on 2 Nov, week 3 does not start.**

## Progress (as of 26 Oct 2026)

**Phase 0 (weeks 1–2) is done**, a week ahead of the original week-2 end (30 Oct). Everything that doesn't need outside people is written: 7 phase 0 documents, the code skeleton, and a tested sample-size module.

**Still open:**

- the professor's review (questions below);
- the gaps that need outside people: data stewards and an advisory group (`SCOPE.md` §8–9);
- UNHCR's 2022 policy text on law-enforcement transfers (could not be fetched);
- no study yet of name change among refugees in Malawi (`NAME_CHANGE.md`);
- Burundi name source: candidate proposed 28 Oct (CENI 2025 lists), user to confirm.

**Next:** week 3, schema and validator. The user decided on 26 Oct to keep G1 as a hard gate and to settle G1–G3 with the professor on **Wed 28 Oct**. If G1 and G2 are resolved then, week 3 starts that day (planned for 2 Nov); if not, it waits.

**Done ahead of schedule** (◐ marks in weeks 3–7): CPIMS+ field list; the Burundi sibling question; naming-profile sources and method; CongoNames source review; real-pattern sources; intake-guide rules; CPIMS+ baseline algorithm.

| What | Status | Where | Commit |
| --- | --- | --- | --- |
| Scope: corridor, users, purposes, prohibited uses | ✔ done | `SCOPE.md` | `b160a33` |
| Code skeleton and licences | ✔ done | `namebridge/` | `b160a33` |
| Evidence check of the scope (16 sources) | ✔ done (extra) | `SCOPE.md` §7 | `a272130` |
| Threat model | ✔ done | `THREAT_MODEL.md` | `e608432` |
| Data-protection assessment (desk version) | ✔ done | `DPIA.md` | `e608432` |
| Data rules | ✔ done | `DATA_RULES.md` | `e608432` |
| Benchmark protocol, including the cost of errors | ✔ done | `BENCHMARK_PROTOCOL.md` | `e608432` |
| Benchmark size derived from the targets (26,000), and the realism plan (naming profiles) | ✔ done (extra) | `BENCHMARK_PROTOCOL.md` §2; `sample_size.py` | `070c525` |
| Phase 0 exit check | ✔ done | `SCOPE.md` §8 | `e608432` |
| Kinyarwanda research (week 2 groundwork) | ✔ done; packs in week 4 | `RESEARCH_LOG.md` | `cbcf4fe` |
| Verification of open items (Malawi Act sections, HRW chapter, Burundi paper, Rwanda conflict) | ✔ done, except UNHCR's 2022 policy text | `RESEARCH_LOG.md` | `cbcf4fe` |
| UNICEF sources (child tracing, data, AI) | ✔ done (extra) | `RESEARCH_LOG.md` | `d27f327` |
| CPIMS+ analysis and decision: integration target and baseline | ✔ done (extra) | `RESEARCH_LOG.md`; `SCOPE.md`; this file | `59c8130`, `8fb9343` |
| Deliberate name change in exile: patterns and cross-cutting rules | ✔ done (extra) | `NAME_CHANGE.md` | `f02521d` |
| Professor review of the phase 0 documents | ⏳ pending | — | — |

**Waiting on the professor:**

- the not-a-user rule for governments and law enforcement (`SCOPE.md` §2);
- the error costs and targets (`BENCHMARK_PROTOCOL.md` §7);
- whether NYU's IRB needs to confirm that the aggregate use of public name lists (CongoNames, NESA) is not human-subjects research;
- `NAME_CHANGE.md` rule 5: no support for searches for people who changed their names, including alleged perpetrators.

**Phase 0 documents:** `SCOPE.md`, `THREAT_MODEL.md`, `DPIA.md`, `DATA_RULES.md`, `BENCHMARK_PROTOCOL.md`, `NAME_CHANGE.md`, and `RESEARCH_LOG.md` (the evidence trail).

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

| Week | Dates | §10 phase | Main work | Done when | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | 19–23 Oct | 0. Governance | Corridor, users, purposes, prohibited uses; repo skeleton | Scope document approved by the professor | ✔ done 26 Oct (review pending) |
| 2 | 26–30 Oct | 0. Governance | Threat model, data-protection assessment (desk), benchmark protocol | Phase 0 exit criteria written | ✔ done 26 Oct |
| 3 | 2–6 Nov | 1. Name corpus | Two-graph schema; language-pack template; CPIMS+ field mapping; Kinyarwanda and Kirundi research | Schema and validator in the repo | next |
| 4 | 9–13 Nov | 1. Name corpus | Curate the Kinyarwanda, Kirundi and DRC packs; ICU / CLDR set-up | First packs load into the graph | — |
| 5 | 16–20 Nov | 1. Name corpus | Reach the pilot corpus; negative constraints; review workflow | Graph v0.1, every edge sourced | — |
| 6 | 23–27 Nov | 2. Linkage MVP | Synthetic benchmark (light week: Thanksgiving) | Gold set of matches, non-matches and families | — |
| 7 | 30 Nov–4 Dec | 2. Linkage MVP | Preserve-first ingestion; transliteration; blocking; deterministic and CPIMS+-style baselines | Baseline results on the benchmark | — |
| 8 | 7–11 Dec | 2. Linkage MVP | Splink model plus graph features; calibration; evaluation | Results for every option tested | — |
| 9 | 14–18 Dec | 2. Linkage MVP | Explanation view; evaluation report; release v0.1; CPIMS+ synonym export | Phase 2 exit: offline results, no live decisions | — |

## Week by week

### Week 1 — 19–23 Oct: scope (phase 0)

- ✔ done 19 Oct: `CONCEPT-IDEA.md` added to the repo, and §14 corrected.
- ✔ done 26 Oct: **corridor** confirmed in `SCOPE.md` §1 (DRC 65%, Burundi 22%, Rwanda 12% of Dzaleka, Mar 2025); §2.3 (Burundi) kept as an open question.
- ✔ done 26 Oct: **users, purposes and prohibited uses** in `SCOPE.md` §2–4. Proposed: law enforcement and governments are not users in the pilot (to confirm with the professor).
- ✔ done 26 Oct: **repo** skeleton `namebridge/`: Python package, pytest suite, `data/graph` and `data/packs`, licences (code Apache-2.0; graph and packs CC BY 4.0).
- **Done when:** a one-page scope is written (✔ `SCOPE.md`) and the professor has seen it (pending).

### Week 2 — 26–30 Oct: risks and test rules (phase 0)

- ✔ done 26 Oct: **threat model** in `THREAT_MODEL.md`: 10 misuse actors and 13 threats, each with its controls.
- ✔ done 26 Oct: **data-protection assessment** in `DPIA.md`, following Malawi's Data Protection Act 2024, s. 30(3).
- ✔ done 26 Oct: **data rules** in `DATA_RULES.md`: sharing, retention, disclosure, and incidents (72 hours).
- ✔ done 26 Oct: **benchmark protocol** in `BENCHMARK_PROTOCOL.md`. The error costs were decided by the user: at the search step a missed candidate is worse; at the confirmation step a false match is worse (100 : 1 for minors).
- ✔ done 26 Oct: **exit check** in `SCOPE.md` §8. Phase 0 is complete except for the gaps.
- ✔ done 26 Oct: **Kinyarwanda research** groundwork: Kimenyi (1978) on gender-marked prefixes; the 2014 spelling reform; the fathers'-surname conflict, now modelled as a varied parameter (`RESEARCH_LOG.md`).
- ✔ done 26 Oct: **open items verified** against primary texts: Malawi Act sections, the HRW chapter, Duchaj & Ntihirageza. Still open: the text of UNHCR's 2022 policy on law-enforcement transfers, which could not be fetched.
- ✔ extra, 26 Oct: **UNICEF sources** and the **CPIMS+ code** were read. CPIMS+ was adopted as the integration target and baseline (`RESEARCH_LOG.md`).

Plan (all items done 26 Oct):

- ✔ **Threat model** (`THREAT_MODEL.md`): who could misuse the system (§8: stalkers, traffickers, hostile governments, armed groups) and which controls block each risk.
- ✔ **Data-protection assessment (desk version)** (`DPIA.md`): what data the system would hold, why, for how long, and who could see it, using the ICRC handbook, Malawi's Data Protection Act 2024 and the RFL Code of Conduct (`SCOPE.md` §5).
- ✔ **Data rules (§10 phase 0)** (`DATA_RULES.md`): data sharing, retention and deletion, disclosure, and incident response.
- ✔ **Benchmark protocol (§9)** (`BENCHMARK_PROTOCOL.md`): what the test set must contain; the metrics, including the fairness slices (§9.2); the splits by person and family and a temporal holdout (§9.3); name-only search measured separately from full-evidence resolution; and the cost of a false positive vs a false negative.
- ✔ **Start the research** (`RESEARCH_LOG.md`): Kinyarwanda naming (HRW 1999, the onomastic sources in §2.2).
- ✔ **Done when:** the phase 0 exit criteria are written (`SCOPE.md` §8): purpose, benchmark protocol, data rules, threat model. Data stewards and an advisory group can't be named yet, so record that as a gap.

### Week 3 — 2–6 Nov: schema (phase 1)

⛔ **Gated by G1 and G2.** Do not start until both are resolved.


- **Name Knowledge Graph** (§5.1A): node and edge types, and the required edge metadata, as a schema with a validator.
- **Case graph** (§5.1B): schema only, kept empty and separate.
- ◐ **CPIMS+ mapping** (field names already known from Primero's code, 26 Oct: `name`, `name_other`, `name_nickname`, `relation_name`, `relation_nickname`, `relation_other_family`, `relation`, `relation_age`, `date_of_birth`, `sex`, `age`, plus the ethnicity, sub-ethnicity and religion fields to refuse; `RESEARCH_LOG.md`): map the case schema to Primero's case and tracing-request fields (`name`, `name_other`, `name_nickname`, relatives' names). Names arrive as one typed string, so the parser must not rely on separate fields. An ingestion allowlist refuses ethnicity, sub-ethnicity and religion (`THREAT_MODEL.md` T13).
- **Name-change rules in the schema** (`NAME_CHANGE.md`): the validator rejects edges between unrelated names; case records carry `other_names_used` and a `possible_name_change` route to protected handling.
- **Language-pack template** (§11).
- **Regression suite:** set up the test suite that every later change must pass (§12).
- ◐ **Research:** Kirundi naming and spelling; whether Burundian siblings share a name (§2.3). *Partly done 26 Oct:* sibling question answered as **disputed / context-dependent**, with legal (1993 code, art. 13) and onomastic sources (Bigangara 1982; Duchaj & Ntihirageza 2009), and modelled as a varied parameter. **Remaining:** Kirundi spelling rules.
- **Done when:** the schema and validator are in the repo, with tests.

### Week 4 — 9–13 Nov: first packs (phase 1)

⛔ **Gated by G3** (real name lists) · ⚠ **G6** (Burundi source).


- **Packs:** first versions of `rw-kiny`, `bi-kirundi` and the DRC (nom + postnom + prénom; Congolese Swahili).
- **Cross-pack data:** Christian names (Jean / John / Yohana …); places old and new (Burundi 2025, Rwanda 2006, DRC 2015; HDX boundaries).
- **ICU / CLDR:** set up normalisation, transforms and transform-path logging (§5.4).
- ◐ **Naming profiles (DRC, Rwanda):** sources identified on 26 Oct (CongoNames, CC BY 4.0, 8.05 M names; NESA 2024/25 lists); method fixed (`BENCHMARK_PROTOCOL.md` §2.4). **Remaining:** build them locally from CongoNames and the NESA lists, then delete the raw lists (`DATA_RULES.md` DR-1). Burundi source: CENI 2025 candidate lists proposed 28 Oct (G6).
- **Done when:** the first packs load into the graph and pass the validator.

### Week 5 — 16–20 Nov: pilot corpus (phase 1)

- **Corpus:** aim for about 2,000 sourced relationships for the corridor (§10 says 2,000–10,000).
- **Negative constraints** (`not_equivalent_to`) and ambiguous paths.
- **Review workflow:** `proposed` → `reviewed` → `deprecated`; a source and licence register.
- ◐ **Candidate sources** (CongoNames reviewed 26 Oct: provenance = DRC state-exam lists 2008–2023; licence CC BY 4.0; real names, so aggregates only. **Remaining:** Onomaverse and Wikidata): review Onomaverse, Wikidata aliases (§7) and CongoNames (`SCOPE.md` §6; real names, so aggregate statistics only) for provenance, coverage and licence before using them.
- **Graph API** (§12): given a name, return the typed paths to its variants, with confidence and source.
- ◐ **Real-pattern variants** (sources found 26 Oct: UN 1533 list, e.g. `KAKOLELE`/`KAKORERE`; 2014 spelling reform. **Remaining:** collect them): collect the sanctions-list aliases and the 2014 Kinyarwanda spelling forms (`BENCHMARK_PROTOCOL.md` §2.4). Variant pairs from the profiles enter the graph as `proposed` edges.
- ◐ **Intake guide** derived from the packs (§2.2; final phase in §10): which names and relationship evidence to record; never ethnicity or clan. *Rules already written 26 Oct:* the fields to record in `DPIA.md` (d), and the names a person chooses to give in `NAME_CHANGE.md` rule 6 and `DATA_RULES.md` DR-1.7. **Remaining:** the guide itself.
- **Done when:** graph v0.1 is versioned, every edge is sourced and has a confidence level (phase 1 exit), and the graph API answers queries.

### Week 6 — 23–27 Nov: benchmark (phase 2, light week)

⚠ **G4:** the size and targets use the 26 Oct default until the professor confirms.


- **Synthetic gold set** (§9.1): about **26,000 invented people** (size derived in `BENCHMARK_PROTOCOL.md` §2.1), generated by recombination from the naming profiles. Invented people and families, with the corridor's error types (order, spelling, Christian names, renamed places, typos, incomplete dates, OCR errors), hard negatives with common names, and adversarially similar records.
- **Splits:** by person and family, so the same identity can't appear in both training and test; plus a temporal holdout (later invented records with newer patterns, e.g. renamed provinces).
- **Child-report errors:** first names or nicknames only, and relationships confused, as in a young child's tracing request (`BENCHMARK_PROTOCOL.md` §2.3).
- **Realism checks** before the freeze: the fidelity test and the copy test.
- **Done when:** the gold set passes the realism checks, and a sample of 300 pairs has had a human check.

### Week 7 — 30 Nov–4 Dec: pipeline (phase 2)

⚠ **G2** (roles) · ⚠ **G5** (routing for possible name change).


- **Ingestion:** keep the original name exactly as written, and add parallel normalised forms (§5.3).
- **Transliteration and variants** as hypotheses, with the path that produced each one (§5.4).
- **Blocking:** the strategies in §5.5, aiming for high recall.
- **Baseline:** deterministic rules and phonetic matching (option 5).
- ◐ **CPIMS+-style baseline** (algorithm documented from Primero's source on 26 Oct: field boosts, Double Metaphone, score/max, likely/possible; `RESEARCH_LOG.md`. **Remaining:** implement it): Double Metaphone, boosted field match and score/max normalisation, reimplemented from Primero's source.
- **Access controls on the case side** (§8, §12), on synthetic data: roles, an access log, and the retention and deletion flow. Person and family views kept separate.
- **Consent and lawful basis** (§8 control 4): every case record stores why it may be used and with whom it may be shared.
- **Protected-person flags** (§8 control 7), including **"possible name change"** candidates (`NAME_CHANGE.md` rule 2): minors, trafficking, domestic violence, asylum, witness protection, or a person who may not wish to be found. Flagged cases are suppressed or routed separately; every case involving a minor is flagged.
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
- **CPIMS+ synonym export:** reviewed, high-confidence attested variants only, as search synonym lists. Plus a design note for the companion service over the Primero API.
- **Semester summary** for the professor.
- **Done when:** the phase 2 exit is met: offline results, and no live case decisions; controls 4, 7, 8 and 9 pass their tests on synthetic data.

## After the semester

| When | What | Condition |
| --- | --- | --- |
| Jan–Mar 2027 | More packs (Lingala, Mashi and other eastern DRC languages); native-speaker review of existing packs | None |
| Jan 2027 on | Open research questions (§13), especially 1, 3, 4 and 7 | None |
| Jan 2027 on | CPIMS+ companion service over the Primero API (separate service, Apache-2.0) | Needs an agency running CPIMS+ for testing beyond synthetic data |
| When ready | Phase 3: shadow pilot beside an authorised tracing workflow | Needs a partner (e.g. REFUNITE, the Red Cross, UNHCR) and real data under their rules |
| After phase 3 | Phase 4: controlled deployment; federation only if needed | Phase 3 exit criteria met |
| Final phase | Offer NameBridge free of charge to the tracing organisations **and to Fraternidade Sem Fronteiras (FSF)**, for its work with children in care (foster children, the Órfãos do Congo project). FSF does not run the system: it uses the intake guide and refers cases to an authorised tracing service such as the Red Cross. Cases involving minors follow the protected-person rules (§8, control 7). Details: `CONCEPT-IDEA.md` §10, "Final phase" | Tested result in hand. NameBridge is not sold |
