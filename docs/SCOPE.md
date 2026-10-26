# NameBridge — scope (phase 0, week 1)

Draft, 26 Oct 2026, for the professor's review. Section numbers (§) refer to `CONCEPT-IDEA.md`; the plan is in `TIMETABLE.md`. Sources are listed at the end ([S1]–[S16]). On 26 Oct, a second desk-research pass checked every claim; the result is in §7. The phase 0 exit check is in §8.

**What NameBridge is this semester:** a research prototype. It finds candidate matches between records of people whose names were written differently in different countries, languages or registries. It runs **offline, on synthetic data only**, and makes no decision about any real person (§10 phase 2 exit).

## 1. Pilot corridor

**Great Lakes → Malawi (Dzaleka)**, confirmed by three independent counts:

| Origin | DOS, Mar 2025 [S1] | UNHCR, 31 Oct 2024 [S2] | Name traditions in the pilot | Languages of the records |
| --- | --- | --- | --- | --- |
| DRC | 37,245 (65%) | 36,469 | Prénom + nom + postnom (Family Code art. 56) [S5]; Bantu names mixed with Christian and French names | French, English |
| Burundi | 12,604 (22%) | 12,291 | Kirundi | French, English |
| Rwanda | 7,135 (12%) | 7,019 | Kinyarwanda | French, English |

New arrivals show the same mix: 62% DRC, 19% Burundi, 7% Rwanda (UNHCR). The three groups make up about 99% of the camp.

**Why this corridor:**

- **The need is documented.** In Dzaleka, unaccompanied and separated children are referred to the Red Cross, a UNHCR implementing partner, which had 67 registered in Dec 2025. Tracing is hard because the Red Cross "can only cross-reference lists of other refugee camps in the region" [S3]. Cross-referencing name lists across camps is exactly the task NameBridge supports.
- **The tracing service is already running.** The Malawi Red Cross Society runs Restoring Family Links in Dzaleka with the ICRC [S4].
- **The script is shared.** All three origins write names in the Latin script, which keeps the corridor bounded.

**Naming facts the packs must respect** (checked 26 Oct):

- **Rwanda:** parents choose the child's name freely, and the law forbids a child from bearing only all of a parent's or a sibling's names (Law 71/2024, arts 38–39, which repealed Law 32/2016 with the same rule) [S6]. Sharing a surname is weak evidence of kinship, and a different surname is no evidence against it. This matches HRW (1999). *Conflicting evidence (found 26 Oct):* The New Times (Kigali), 6 May 2026, says children "traditionally take the father's surname". The law permits a child to share some elements with a parent, so the Kinyarwanda pack records partial agreement as possible, and the conflict is logged for week 4.
- **Burundi:** the evidence is **disputed**, not missing. The name is "given by the person who declares the birth; the choice of name is free" (Code des personnes et de la famille 1993, art. 13) [S7]. Family names did not exist before Christianity except for kings, and missionaries brought in a patronymic system [S8]. More recently, sons have also been named after their father or grandfather [S8]. The Kirundi pack therefore records surname agreement as `context-dependent` and `disputed`, citing these sources. It does not copy the Rwandan rule.
- **DRC:** names are prénom + nom + postnom. In several groups, siblings can have different noms [S5]. The law forbids permuting the components of a name in civil records [S9], but oral reports and other countries' forms don't follow that order. Order is therefore stored as observed (§5.3).
- **Camp languages:** Swahili is Dzaleka's lingua franca, and Lingala, French, Kinyarwanda and Kirundi are also spoken [S10]. Packs are built by **naming system**, not by spoken language. The DRC pack covers names of Lingala and other origins as they appear in Congolese records. Lingala and eastern-DRC linguistic packs remain later work.

**Limits:**

- **Script:** cross-script search (§5.4) is barely tested in this corridor.
- **Data:** no 2026 count by nationality for Dzaleka was found. The latest camp-level counts are from Oct 2024 and Mar 2025. UNHCR's DRC situation page gives **41,071** DRC refugees and asylum seekers in all of Malawi on 30 Apr 2026, consistent with the camp shares.

## 2. Users

| User | Role | When |
| --- | --- | --- |
| Tracing caseworkers in authorised services: the ICRC and national Red Cross societies (in Dzaleka, the Malawi Red Cross Society), REFUNITE, UNHCR protection staff | Run the matching and review candidates. They make every identity decision (§5.7) | Phase 3 onward, only with a partner |
| Linguists and community experts | Propose and review edges in the public name graph | From phase 1 (a gap this semester: no outside reviewers yet) |
| FSF | Uses the intake guide only, and refers cases to an authorised tracing service. Does not run the system (§10 final phase) | Final phase |
| The researchers (student and professor) | Build and evaluate on synthetic data | This semester |

**Not users:**

- **The public:** no public person search (§12).
- **Families searching directly:** they go through a tracing service.
- **Law enforcement and government agencies:** they are not users of the matching. *Proposed; to confirm with the professor.* The reasons:
  - In this corridor, governments and armed groups are among the actors people flee (situation research §2.4).
  - There is a precedent for this harm. Refugee registration data, including biometrics, was passed from Bangladesh to Myanmar, the country the Rohingya fled, for repatriation checks without informed consent, and some refugees went into hiding [S11].
  - This rule is stricter than UNHCR's own policy, which allows transfers to law enforcement "in appropriate circumstances" [S12]. It follows the Red Cross Movement's Restoring Family Links Code of Conduct on Data Protection [S13].
  - In Malawi, the government registers refugees [S3]. Host-government records may one day be a *data source*, but only through a tracing partner's agreement and under the Data Protection Act. That does not make the government a user.

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
- Inferring ethnicity, clan, religion or gender from a name as a fact. The intake guide never records ethnicity or clan. Ethnic origin, religion and biometrics are "sensitive personal data" under Malawi's Data Protection Act 2024 [S14]. Some platforms do ask about clan (REFUNITE's questions include it [S15]); NameBridge does not.
- Locating people for immigration enforcement, deportation, repatriation screening, prosecution, surveillance or debt collection, or for anyone who has not shown an authorised tracing purpose.
- Disclosing a location or contact details because of a high score (control 6).
- Ingesting scraped social-media data, or any real case data, this semester.
- Storing raw biometrics.
- Adding LLM-generated name equivalences without a source. They enter as `proposed` only.
- Using one global threshold.

## 5. Applicable rules (detail in week 2)

- **Malawi Data Protection Act 2024**, in force since 3 Jun 2024 and overseen by MACRA [S14]. Its main rules:
  - Sensitive data includes ethnic origin, religion and biometrics.
  - Cross-border transfers need adequate protection or another legal basis (ss. 38–39).
  - Breaches must be notified within 72 hours.
  - Data controllers must register.

  It does not apply to the semester's synthetic data. It applies to any later phase with real records.
- **Red Cross Movement Restoring Family Links Code of Conduct on Data Protection** (2015, revised 2024) [S13]: the standard a tracing partner will hold us to.
- **ICRC Handbook on Data Protection in Humanitarian Action**, 3rd edition (2024).

## 6. Deliverables this semester

| Item | Detail |
| --- | --- |
| Name graph | Open and sourced; packs `rw-kiny`, `bi-kirundi` and `cd-*` |
| Code | `namebridge/` |
| Benchmark | Synthetic |
| Evaluation report | Covers every option tested |
| Release | v0.1, 18 Dec |
| Licences | Code under Apache-2.0 (open source, with a patent grant). Name graph and packs under CC BY 4.0, compatible with CC BY sources such as CongoNames [S16] |

**Candidate source for weeks 4–6: CongoNames** [S16]. It holds 8,053,983 names from DRC state-exam lists (2008–2023, 12 provinces) under CC BY 4.0. These are **real people's full names**, so they never enter `namebridge/data`. If the week 5 source review approves it, only aggregate statistics (token frequencies, structure by province) are used, for term-frequency weights and for realistic synthetic names.

## 7. What the 26 Oct evidence check changed

**Confirmed:**

- The corridor and its population shares.
- The documented need for cross-camp name matching.
- The Rwanda naming rule, now backed by statute.
- The ban on inferring ethnicity, now backed by Malawi law.

**Changed:**

- **Burundi:** moved from "unknown" to "disputed / context-dependent", with the sources above.
- **DRC:** packs are organised by naming system, and the camp languages (Swahili, Lingala) are noted.
- **Users:** the tracing actor in Dzaleka is now named: the Malawi Red Cross Society with the ICRC.
- **Governments:** the not-a-user rule is refined to separate *users* from *data sources*. Repatriation screening is added to the prohibited uses.
- **Law:** Malawi's Data Protection Act and the Restoring Family Links Code of Conduct are added.
- **New source:** CongoNames is a candidate source, with conditions.

## 8. Phase 0 exit check (26 Oct 2026)

`CONCEPT-IDEA.md` §10 sets the phase 0 exit: approved purpose, test data, benchmark protocol, named data stewards.

| Exit item | Status | Where |
| --- | --- | --- |
| Corridor, users, purposes, prohibited uses | ✔ written; professor review pending | This file |
| Threat model | ✔ written | `THREAT_MODEL.md` |
| Data-protection impact assessment (desk version) | ✔ written: no personal data this semester; a statutory DPIA is required before the partner phase | `DPIA.md` |
| Data rules: sharing, retention, disclosure, incidents | ✔ written | `DATA_RULES.md` |
| Benchmark protocol and test-data plan | ✔ written, fixed before any data exists | `BENCHMARK_PROTOCOL.md` |
| Named data stewards | ✗ **gap** (no partner yet) | §9 |
| Community advisory group, linguistic review panel | ✗ **gap** | §9 |
| Professor approval of the purpose | Pending | — |

**Verdict:** phase 0 is complete *as far as it can be without outside people*. Phase 1 can start (week 3). The gaps block phase 3, not phases 1–2.

## 9. Gaps recorded in phase 0

- No community advisory group, linguistic review panel or named data stewards (§10 phase 0 exit). Native-speaker review is planned for Jan–Mar 2027.
- No tracing partner, so there is no lawful basis for real data. All results are labelled **preliminary (synthetic only)**.
- No residents or affected families consulted. This is out of scope for the semester by decision.

## Sources

- [S1] Dzaleka Online Services, [Dzaleka data and statistics](https://services.dzaleka.com/data), figures as of 31 Mar 2025; accessed 26 Oct 2026.
- [S2] FairPlanet, ["Funding cuts push Malawi's Dzaleka Refugee Camp to the brink"](https://www.fairplanet.org/story/funding-cuts-push-malawis-dzaleka-refugee-camp-to-the-brink), 2025, citing UNHCR figures as of 31 Oct 2024.
- [S3] USCRI, ["Finding Care Without Support in Dzaleka Refugee Camp"](https://refugees.org/finding-care-without-support-in-dzaleka-refugee-camp), 2026 (cites Red Cross data of Dec 2025).
- [S4] Dzaleka Online, ["Red Cross Program Reunites Refugees with Family Members"](https://www.dzaleka.com/2025/03/red-cross-program-reunites-refugees.html), Mar 2025.
- [S5] FamilySearch, [DRC Naming Customs](https://www.familysearch.org/en/wiki/Democratic_Republic_of_the_Congo_Naming_Customs); Wikipedia, [DRC naming customs](https://en.wikipedia.org/wiki/Democratic_Republic_of_the_Congo_naming_customs) (quotes Family Code art. 56). These are secondary sources; verify against the Family Code.
- [S6] Rwanda, [Law No 71/2024 of 26/06/2024 governing persons and family](https://www.minijust.gov.rw/fileadmin/user_upload/Minijust/Publications/Laws/OG_n___Special_of_30.07.2024_Abantu_n_umuryango.pdf), arts 38–39; earlier [Law No 32/2016](https://faolex.fao.org/docs/pdf/rwa208272.pdf), arts 36–39.
- [S7] Burundi, [Décret-loi 1/024 du 28 avril 1993, Code des personnes et de la famille](http://jafbase.fr/docAfrique/Burundi/Burundi-Code-civil.pdf), arts 11–14 (droit-afrique compilation, updated 2006).
- [S8] Université du Burundi repository, ["Sociocultural prerequisites for understanding the Rundi …"](https://repository.ub.edu.bi/bitstreams/c2369042-37ce-4c26-8692-fdefc04a65d1/download), §11.1.3, citing Bigangara (1982). Also Duchaj & Ntihirageza (York University): "Traditional Burundian society does not use family names". The full text could not be fetched.
- [S9] ICC, [Annex 1, "The issue of names used to identify citizens of the DRC"](https://www.icc-cpi.int/sites/default/files/RelatedRecords/CR2009_05425.PDF) (citing Family Code arts 64–70).
- [S10] Routed Magazine, ["The spaces in between: Social memory at Dzaleka refugee camp"](https://www.routedmagazine.com/spaces-in-between-dzaleka-camp).
- [S11] Human Rights Watch, ["UN Shared Rohingya Data Without Informed Consent"](https://www.hrw.org/news/2021/06/15/un-shared-rohingya-data-without-informed-consent), 15 Jun 2021.
- [S12] UNHCR, [Policy on the Protection of Personal Data of Persons of Concern](https://www.ictworks.org/wp-content/uploads/2017/10/UNHCR-data-protection-policy.pdf) (2015), §6.3. It was superseded by the [General Policy on Personal Data Protection and Privacy](https://www.refworld.org/policy/strategy/unhcr/2022/en/124207) (2022), which has not yet been checked on this point.
- [S13] ICRC, [Restoring Family Links Code of Conduct on Data Protection](https://www.icrc.org/en/document/rfl-code-conduct); [progress report, 34th International Conference](https://rcrcconference.org/app/uploads/2024/09/34IC_10.4-Progress-Report-RFL-EN.pdf), Sept 2024.
- [S14] Malawi, [Data Protection Act 2024](https://www.mca.ac.mw/mca-siteup/uploads/Data%20Protection%20Act%202024.pdf), s. 2 and ss. 36–42; [Tech Hive Advisory summary](https://www.techhiveadvisory.africa/insights/malawis-data-protection-act-aligning-to-the-new-regulatory-framework).
- [S15] PBS NewsHour, ["When refugees scatter, here's how family members can find each other"](https://www.pbs.org/newshour/world/refugees-find-each-other).
- [S16] Tshabu Ngandu et al., ["CongoNames Corpus"](https://www.mdpi.com/2306-5729/11/7/169), *Data* 11(7):169, 8 Jul 2026; [code](https://github.com/bernard-ng/drc-names-corpus). Dataset licence: CC BY 4.0.
