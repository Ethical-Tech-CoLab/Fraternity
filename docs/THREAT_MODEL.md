# NameBridge — threat model (phase 0, week 2)

Draft, 26 Oct 2026, for the professor's review. Section numbers (§) refer to `CONCEPT-IDEA.md`; the scope is in `SCOPE.md`. Sources are listed at the end ([T1]–[T12]).

**Question:** who could use NameBridge, its data or its results to harm the people it is meant to help, and which control blocks each harm?

**Method:**

- **Misuse actors**, in the terms of §8: who wants to harm whom, and through what.
- **LINDDUN privacy threat types** [T1]: Linking, Identifying, Non-repudiation, Detecting, Data disclosure, Unawareness, Non-compliance.
- **Phases:** each threat is rated for this semester (synthetic data only) and for a future phase with real cases and a tracing partner.

## 1. What is being protected

| # | Asset | Sensitivity | Exists this semester? |
| --- | --- | --- | --- |
| A1 | **Public name graph and packs** (§5.1A): name forms, variants, rules, sources | Low on its own; high if it maps names to ethnicity, clan or a small locality | Yes |
| A2 | **Case graph** (§5.1B): people, observed names, relatives, places, events | Very high | Schema only (week 3); synthetic records (weeks 6–9) |
| A3 | **Search results**: candidate lists, scores, graph paths. A result can reveal that someone is being sought, by whom, and where they were last seen | Very high | Synthetic only |
| A4 | **Benchmark and generator** | Low if truly synthetic; high if built from real people | Yes (week 6) |
| A5 | **Access and decision logs** | High (they show who looked for whom) | Synthetic only |
| A6 | **Code and model** (integrity) | Medium: tampering changes who gets found | Yes |

## 2. Misuse actors

| # | Actor | Goal | Evidence it is real |
| --- | --- | --- | --- |
| M1 | **Abusive partner or relative, or stalker, posing as family** | Locate someone who fled them | RFL practice lets a located person refuse to have their address shared [T2] |
| M2 | **Trafficker, including a trafficker who is a relative** | Claim a child or adult as "family", or find a victim who escaped | "Sometimes traffickers are parents/relatives" (Red Cross RFL guidance) [T3]. In Jul 2025, 10 police officers were jailed for aiding trafficking around Dzaleka (situation research §5.1) |
| M3 | **Government of the country of origin, or the host government for removal** | Screen people for repatriation; find opponents, defectors or witnesses | Rohingya registration data reached Myanmar, and refugees went into hiding [T4]. Burundi returns raise coercion concerns (situation research §2.4) |
| M4 | **Armed groups** (e.g. M23 in eastern DRC) | Find deserters, witnesses or relatives of opponents | Active conflict in the origin areas (situation research §2.4) |
| M5 | **External attacker**, possibly state-backed | Steal tracing data in bulk | In 2022, the Red Cross Restoring Family Links data on more than 515,000 people was breached, and the service had to shut down [T5] |
| M6 | **Insider**: caseworker, volunteer or developer | Curiosity, bribery, or passing data to M1–M4 | Corruption in the camp's security apparatus (situation research §5.1) |
| M7 | **Graph poisoner** | Add false name equivalences so that people are wrongly matched or hidden | Any open, crowd-edited knowledge source can be poisoned |
| M8 | **Well-meaning user who over-trusts the score** | None. The harm comes from automation bias, e.g. releasing a child to an unrelated adult because of a high score | §5.6: "never let a name-only score trigger a consequential action" |
| M9 | **Profiler** | Use the public name graph to guess ethnicity, clan or origin from a name, e.g. at a roadblock or in a list | In Rwanda in 1994, identity cards that recorded ethnicity were used to select victims [T6]. Name-to-ethnicity inference is banned (§8 control 12) |
| M10 | **Us**: the researchers | Not malicious. Real names could leak into the repo through a dataset such as CongoNames, or through realistic "synthetic" examples | `SCOPE.md` §6 |

## 3. Threats and controls

Codes: **C1–C12** are the §8 controls. **DR-** rules are in `DATA_RULES.md`. "Tested" names the week in which a test on synthetic data shows the control works.

| # | Threat (actor, asset; LINDDUN type) | Semester | Real phase | Controls | Tested |
| --- | --- | --- | --- | --- | --- |
| T1 | M1 or M2 files a tracing request as "family" to locate someone (A2, A3; Identifying, Disclosure) | n/a | **High** | C2 roles: only caseworkers search. C6: a match never discloses a location. The located person decides whether their contact details are shared [T2]. C7: protected-person flags | Wk 7 (C7), wk 9 (C8) |
| T2 | M2 claims a separated child as their own after a high score (A3; Linking) | n/a | **High** | Every minor is a protected-person case (C7). No automatic confirmation (§12). Best-interest assessment by an authorised service. A name-only score never confirms anything | Wk 7, wk 9 |
| T3 | M3 asks for, or forces, access to case data for repatriation screening or removal (A2, A5; Disclosure, Non-compliance) | n/a | **High** | Government and law enforcement are not users (`SCOPE.md` §2). No transfer outside the RFL Code of Conduct [T7]. Stricter than UNHCR's own policy [T11]. Data minimised and retained for a short time (DR-3) | Policy; DR-5 drill |
| T4 | M4 or M3 links lists across camps to find a specific person (A3; Linking, Identifying) | n/a | **High** | No public or bulk search; only one case at a time, with a purpose (C1, C2). Rate limits and an access log reviewed for unusual patterns (C9) | Wk 7 (log) |
| T5 | M5 steals the case graph or logs (A2, A5; Disclosure) | n/a | **High** | C10 (encryption, isolation, regional hosting, key separation). Breach response within 72 hours (DR-5) [T8]. Data minimisation, so less can be lost | Phase 3–4 (C10 deferred) |
| T6 | M6 insider searches for someone without a case (A2, A3; Detecting, Disclosure) | n/a | Medium | C2. Every read is logged (C9). Progressive disclosure, with each opening of a sensitive field logged (C8). Log review | Wk 7, wk 9 |
| T7 | M7 poisons the public graph (A1; integrity) | **Medium** | Medium | Every edge needs a source and a confidence level. `proposed` → `reviewed` workflow. LLM-generated edges stay `proposed`. Negative constraints. Versioned releases | Wk 3 (validator), wk 5 (review) |
| T8 | M9 uses the graph to infer ethnicity, clan or locality from a name (A1; Identifying, Linking) | **Medium** | Medium | The graph holds no ethnicity, clan or religion attributes. Regions only at the level needed for spelling and naming practice (country or province, never colline or village). No name→group classifier (§12; C12). Ethnic origin is sensitive data in Malawi law [T8] | Wk 3 (schema check) |
| T9 | M8 treats a candidate as confirmed (A3; Unawareness) | n/a | **High** | Separate thresholds for retrieval, review and confirmation. Outcomes `possible` and `insufficient evidence`. Calibrated scores. The explanation view shows the path (§5.7). Malawi law gives a right not to be subject to decisions based solely on automated processing [T8] | Wk 8–9 |
| T10 | M10 commits real names to the repo or publishes realistic records (A4; Disclosure, Non-compliance) | **Medium** | Medium | DR-1: no real person's data in the repo. CongoNames is used for aggregate statistics only. The generator recombines name tokens and never copies a full real name together with real attributes | Wk 6 (generator check) |
| T11 | Tampering with code or model changes who is found (A6; integrity) | Low | Medium | Reviewed commits. Regression suite. Versioned, reproducible runs (C11) | Wk 3 on |
| T12 | People whose names are in partner records do not know about the matching (A2; Unawareness) | n/a | Medium | The partner's privacy notices. Purpose limitation. Right of access and correction through the partner (C9) [T7][T8] | Phase 3 |
| T13 | A connected system (e.g. CPIMS+) sends fields NameBridge must not hold: ethnicity, sub-ethnicity, religion, photos (A2; Non-compliance, Identifying) [T13] | n/a | **High** | Ingestion **allowlist**: only named fields are accepted; any other field is dropped before storage, and the drop is logged without its value. Contract test against Primero's field list | Wk 3 (allowlist), wk 7 |
| T14 | Matching across a **deliberate name change** exposes someone who changed name to stay invisible. Burundian refugees in Tanzania adopted Swahili names, or kept pseudonyms even after naturalisation [T14] (A2, A3; Linking, Identifying) | n/a | **High** | The graph has no edges between unrelated names; an adopted name is not a variant. A candidate linked **only** through non-name evidence across two unrelated names is routed as a protected-person case ("may not wish to be found", C7). A record-level `name_changed` flag routes the same way | Wk 7 (C7 routing) |

## 4. What the threat model changes in the design

1. **No location in results.** A match result carries a case reference, not an address or a camp block. Location is released only through the partner's RFL procedure, with the located person's consent [T2].
2. **Ethnicity guard in the schema (week 3).** The validator rejects edge or node attributes such as `ethnicity`, `clan`, `tribe` or `religion`, and region tags finer than province.
3. **Minor equals protected.** In the synthetic case schema, any person under 18 at the record date is flagged by default (C7).
4. **Rate and pattern checks on searches.** These go into the access-log design (week 7), so that bulk or list-based searching stands out.
5. **No "find by name" endpoint for anyone outside the caseworker role.** This holds even in demos.
6. **Field allowlist on ingestion.** Every adapter (CPIMS+ first) accepts only the fields NameBridge needs (`DPIA.md` (d)). It never receives a field and then ignores it (T13).

## 5. Residual risks and gaps

- **No independent review yet.** Security, protection and linguistic experts have not reviewed this model (phase 0 gap).
- **Coercion of the partner.** A tracing partner could be compelled by a host government. NameBridge can minimise what exists to be taken; it cannot prevent the compulsion.
- **The graph can be misused even if it is clean.** Knowing that a name *form* is typical of a country is unavoidable for spelling work. We limit granularity; we cannot remove the signal.
- **Deferred controls.** C10 (production security) and C11 (per-region governance) are deferred to phases 3–4 (`TIMETABLE.md`).

## Sources

- [T1] KU Leuven, [LINDDUN privacy threat modeling](https://linddun.org/).
- [T2] ICRC, [*Restoring Family Links: a guide for National Red Cross and Red Crescent Societies*](https://icrcndresourcecentre.org/wp-content/uploads/2019/06/RESTORINGFAMILY-LINKS-A-GUIDE.pdf), §7.3.2: "No contact details may be disclosed to the enquirer without the consent of the person located."
- [T3] IFRC PrepareCenter, [Restoring Family Links](https://preparecenter.org/toolkit/humanitarian-service-points-toolkit/implementation-programmes-and-activities/restoring-family-links).
- [T4] Human Rights Watch, ["UN Shared Rohingya Data Without Informed Consent"](https://www.hrw.org/news/2021/06/15/un-shared-rohingya-data-without-informed-consent), 15 Jun 2021.
- [T5] ICRC, ["Cyber-attack targets Red Cross Red Crescent data on 500,000 people"](https://www.icrc.org/en/document/sophisticated-cyber-attack-targets-red-cross-red-crescent-data-500000-people), Jan 2022; ["How could it affect me?"](https://www.icrc.org/en/document/cyber-security-how-it-affect-me), updated 24 Jun 2022.
- [T6] Human Rights Watch, ["Propaganda and Practice"](https://www.hrw.org/reports/1999/rwanda/Geno1-3-10.htm), *Leave None to Tell the Story*, 1999: "Tutsi attempting to pass the barriers were usually identified by their identity cards and then slain." See also ["History"](https://www.hrw.org/reports/1999/rwanda/Geno1-3-09.htm) on ethnic labels kept on identity cards after 1959.
- [T7] ICRC, [RFL Code of Conduct on Data Protection](https://www.icrc.org/en/download/file/18229/rfl-code-of-conduct.pdf).
- [T8] Malawi, [Data Protection Act 2024](https://www.mca.ac.mw/mca-siteup/uploads/Data%20Protection%20Act%202024.pdf): s. 2 (sensitive data), ss. 19–24 (rights), s. 25 (automated decision-making), ss. 36–37 (breach within 72 h); summaries by [Tech Hive Advisory](https://www.techhiveadvisory.africa/insights/malawis-data-protection-act-aligning-to-the-new-regulatory-framework) and [ITLawCo](https://itlawco.com/focus-areas/data-protection-and-privacy/malawis-data-protection-act-2024-an-overview).
- [T9] IASC, [Operational Guidance on Data Responsibility in Humanitarian Action](https://interagencystandingcommittee.org/sites/default/files/migrated/2023-04/IASC%20Operational%20Guidance%20on%20Data%20Responsibility%20in%20Humanitarian%20Action%2C%202023.pdf), Apr 2023.
- [T10] ICRC, [*Handbook on Data Protection in Humanitarian Action*, 3rd ed.](https://www.icrc.org/en/data-protection-humanitarian-action-handbook), 2024 (ch. 17, Artificial Intelligence).
- [T11] UNHCR, [Policy on the Protection of Personal Data of Persons of Concern](https://www.ictworks.org/wp-content/uploads/2017/10/UNHCR-data-protection-policy.pdf), 2015, §6.3.2. Transfers to law enforcement are allowed only for a serious criminal offence, to a competent authority, among other conditions. NameBridge's rule is stricter.
- [T12] Situation research: `DZALEKA_SITUATION_RESEARCH.md` §2.4 and §5.1.
- [T13] [Primero / CPIMS+](https://www.primero.org): source code at [primeroIMS/primero](https://github.com/primeroIMS/primero) (AGPL-3.0), `app/services/matching_service.rb` and `language_service.rb`, read 26 Oct 2026; [community forum on family tracing](https://support.primero.org/forum/t/family-tracing-and-reunification/318).
- [T14] Daley, ["Citizenship and Belonging Among Former Burundian Refugees"](https://ora.ox.ac.uk/objects/uuid:3dc69194-d9db-469f-b179-25ed7fbeaf0e/files/m26e06f9e8dadd209e37449ce8f2a12b6), Oxford, 2018, citing Duchaj & Ntihirageza (2009): "Name change was another strategy of invisibility."
