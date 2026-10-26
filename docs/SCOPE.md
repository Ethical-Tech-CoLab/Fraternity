# NameBridge — scope (phase 0, week 1)

Draft, 26 Oct 2026, for the professor's review. Sections refer to `CONCEPT-IDEA.md`; the plan is `TIMETABLE.md`.

**What NameBridge is this semester:** a research prototype that finds candidate matches between records of people whose names were written differently in different countries, languages or registries. It runs **offline, on synthetic data only**, and makes no decision about any real person (§10 phase 2 exit).

## 1. Pilot corridor

**Great Lakes → Malawi (Dzaleka).** Confirmed on the evidence below.

| Origin | Share of Dzaleka | Name languages in the pilot | Languages of the records |
| --- | --- | --- | --- |
| DRC | 37,245 of 57,438 (65%) | Congolese Swahili; French prénoms; nom + postnom + prénom structure | French, English |
| Burundi | 12,604 (22%) | Kirundi | French, English |
| Rwanda | 7,135 (12%) | Kinyarwanda | French, English |

Population, Mar 2025, from services.dzaleka.com/data (`DZALEKA_SITUATION_RESEARCH.md`). New arrivals keep the same mix (62% DRC, 19% Burundi, 7% Rwanda; UNHCR).

Why this corridor:

- It covers 99% of Dzaleka's population.
- Family separation in this region is documented (situation research §5.2).
- The project's existing research is about this corridor.
- All three languages use the Latin script, which keeps the corridor bounded.

**Limits:**

- **Script:** cross-script search (§5.4) is barely tested in this corridor.
- **Other DRC languages:** Lingala, Mashi and other eastern DRC languages come after the semester.
- **Burundi (§2.3):** whether Burundian siblings share a surname is an **open question**. The Kirundi pack records surname agreement as `unknown` until a source settles it, and Kinyarwanda rules are not copied over.

## 2. Users

| User | Role in NameBridge | When |
| --- | --- | --- |
| Tracing caseworkers in authorised services (ICRC Restoring Family Links and national Red Cross societies, REFUNITE, UNHCR protection staff) | Run the matching and review candidates. They make every identity decision (§5.7) | Phase 3 onward, only with a partner |
| Linguists and community experts | Propose and review edges in the public name graph | From phase 1 (as a gap this semester: no outside reviewers yet) |
| FSF | Uses the intake guide only, and refers cases to an authorised tracing service. Does not run the system (§10 final phase) | Final phase |
| The researchers (student and professor) | Build and evaluate the prototype on synthetic data | This semester |

**Not users:**

- **The public:** no public person search (§12).
- **Families searching directly:** they go through a tracing service.
- **Law enforcement and governments:** not users in the pilot. In this corridor, governments and armed groups are among the actors people flee (§8; situation research §2.4). Any request goes through the tracing organisation under its own rules. *Proposed; to confirm with the professor.*

## 3. Purposes (§8 control 1)

The **allowed purposes** are:

1. Finding candidate records of a missing person across differently written names, for an authorised tracing service.
2. Finding possible relatives (family restoration), as candidates for human review, never as an inferred relationship.
3. Research: the open name graph, the language packs, and an evaluation on synthetic data.

Every other purpose is out of scope by default.

## 4. Prohibited uses

These come from §8 and the §12 "should not have" list. The code and the documentation both state them.

- Public reverse lookup of a person, or any search open to anonymous users.
- Automatic identity confirmation, or any action taken on a name-only score.
- Inferring family relationships automatically.
- Inferring ethnicity, clan, religion or gender from a name as a fact. The intake guide never records ethnicity or clan.
- Locating people for immigration enforcement, deportation, prosecution, surveillance, debt collection, or anyone who has not shown an authorised tracing purpose.
- Disclosing a location or contact details because of a high score (control 6).
- Ingesting scraped social-media data, or any real case data, this semester.
- Storing raw biometrics.
- Adding LLM-generated name equivalences without a source. They enter as `proposed` only.
- Using one global threshold.

## 5. Deliverables this semester

| Item | Detail |
| --- | --- |
| Name graph | Open and sourced; packs `rw-kiny`, `bi-kirundi` and `cd-*` |
| Code | `namebridge/` |
| Benchmark | Synthetic |
| Evaluation report | Covers every option tested |
| Release | v0.1, 18 Dec |
| Licences | Code under Apache-2.0 (open source, with a patent grant); name graph and packs under CC BY 4.0 |

## 6. Gaps recorded in phase 0

- No community advisory group, linguistic review panel or named data stewards (§10 phase 0 exit). Native-speaker review is planned for Jan–Mar 2027.
- No tracing partner, so there is no lawful basis for real data. All results are labelled **preliminary (synthetic only)**.
- No residents or affected families consulted. This is out of scope for the semester by decision.
