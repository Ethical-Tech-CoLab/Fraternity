# NameBridge — data-protection impact assessment, desk version (phase 0, week 2)

Draft, 26 Oct 2026. It follows the contents required by **Malawi's Data Protection Act 2024, s. 30(3)(a)–(g)** [D1], read with the ICRC *Handbook on Data Protection in Humanitarian Action* [D2] and the RFL Code of Conduct [D3]. Threats are in `THREAT_MODEL.md` and rules in `DATA_RULES.md`.

**Two phases are assessed**, because they differ completely:

| | **Semester** (now – 18 Dec 2026) | **Future phase** (phase 3 onward, with a tracing partner) |
| --- | --- | --- |
| Personal data | **None.** Public name knowledge and synthetic records only | Real case data held by an authorised tracing service |
| Controller | n/a | The tracing organisation, e.g. a national Red Cross society |
| NameBridge's role | Research software | Software, and possibly a processor acting on the partner's instructions |
| Statutory DPIA? | **Not triggered**: no personal data | **Required.** Processing is high-risk (sensitive data, children, automated processing), so a DPIA must go to MACRA **before** processing (s. 30) [D1][D4] |

This desk version is therefore a **pre-assessment**. It fixes the design choices now, so that the partner's statutory DPIA can build on them later.

## (a) Systematic description of the processing

**Semester:**

- The public name graph is curated from published sources (§5.1A).
- Synthetic people, families and records are generated, matched and evaluated offline on one machine.

**Future phase:**

1. A caseworker enters or imports a tracing request and candidate source records: camp lists, registration extracts or tracing forms that the partner is already allowed to use.
2. NameBridge keeps the names exactly as observed and generates variants through the graph.
3. It retrieves and scores candidates.
4. A trained reviewer decides same / different / possible / insufficient evidence.
5. Contact between the people concerned follows the partner's RFL procedure, never NameBridge.

## (b) Purpose

Tracing missing persons and restoring family links for an authorised tracing service. Research on synthetic data. Nothing else (`SCOPE.md` §3).

## (c) Lawful basis

- **Consent is not a workable basis for the person being sought.** It is "impossible to obtain informed and freely-given consent from people being sought by family members, and very difficult to obtain it from vulnerable enquirers" [D5].
- RFL practice relies on **vital interest** or **public interest** instead [D3][D5]. Malawi's Act lists both in s. 8 [D4].
- **Children:** under s. 17, where *consent* is the basis, consent must come from a parent or guardian [D1]. For an unaccompanied or separated child there may be no parent or guardian. The basis is then vital interest, under a best-interest assessment by the authorised service, not consent.
- **Sensitive data:** ethnic origin, religion and biometrics are sensitive data (s. 2) and need a specific condition (s. 16) [D4]. NameBridge **does not collect them at all** (data minimisation below).
- **Recording the basis:** each case record stores its basis and sharing limits (§8 control 4; built in week 7).

## (d) Necessity and proportionality: data minimisation

| Field | Needed? | Why |
| --- | --- | --- |
| All names as observed, in any order, with the source field label | **Yes** | Core of name matching (§5.3) |
| Parents' and caregivers' names | **Yes** | In Rwanda and Burundi, surnames rarely show kinship; parents' names do (`SCOPE.md` §1) |
| Approximate age or date of birth (range allowed) | **Yes** | Independent evidence; Splink needs more than names [D6] |
| Place of origin as it was named at the time (to commune or colline only if the caseworker needs it), and place last seen | **Yes**, minimal | Place evidence; renamed places are handled by the graph |
| Separation event and date; travel companions | Optional | Relationship evidence |
| School, faith community | Optional, coarse | Community anchors (`CONCEPT-IDEA.md` §2.2). Never used to infer religion |
| Sex as recorded | Optional | Evidence and fairness slices; no inference |
| Phone number or address of the enquirer | **No**, held by the partner | Not needed for matching (C6) |
| Ethnicity, clan, tribe, religion as an attribute | **Never** | Sensitive, high-risk, not needed (C12) |
| Photographs, fingerprints, iris scans | **Never** in NameBridge | At most a pointer to the partner's own authorised system (§5.1B) |

## (e) Risks to rights and freedoms

From `THREAT_MODEL.md`, in short:

- **Location exposure** to abusers, traffickers or governments (T1–T4).
- **Wrongful reunification of a child** (T2, T9).
- **Breach** (T5).
- **Insider misuse** (T6).
- **Ethnic profiling** through the graph (T8).
- **Unawareness** of the people whose records are matched (T12).

The real-phase risk is **high**. The semester risk is **low**, and comes from graph poisoning, profiling and real-name leakage (T7, T8, T10).

## (f) Measures

Each measure is listed against the threat it addresses (`THREAT_MODEL.md` §3).

- **C1–C12 from §8.** Controls 4, 7, 8 and 9 are built and tested on synthetic data this semester. Controls 10 and 11 are deferred.
- **No location in results**, and the located person decides whether their contact details are shared [D7].
- **Human review before any consequential step.** This also respects the right not to be subject to decisions based solely on automated processing (s. 25) [D1].
- **Retention and deletion** (DR-3).
- **Breach response within 72 hours** (DR-5).
- **No cross-border transfer** of case data without an adequacy basis under ss. 38–39 [D8], *and* the RFL Code of Conduct's rules [D3].
- **Federation instead of pooling**, if partners cannot share data (§8).

## (g) Other matters

- **Registration and officer.** A controller processing the data of more than 10,000 people resident in Malawi is a "controller of significant importance" and must register with the authority **before** processing (s. 41) [D1]. A data protection officer is required where core activities process sensitive data on a large scale (s. 33) [D1]. A tracing partner in Dzaleka would likely meet both tests.
- **AI-specific risks.** The ICRC handbook's ch. 17 on artificial intelligence applies to the matching model [D2]. The ICRC's 2024 AI policy is relevant for a Red Cross partner [D9].
- **International organisations.** UNHCR and the ICRC apply their own data rules rather than national law, so the binding framework depends on which partner is the controller. This is an open question for phase 3.
- **Gap:** this pre-assessment has not been reviewed by a data-protection officer or a lawyer in Malawi.

## Conclusion

The **semester can proceed**: there is no personal data, and the residual risks are controlled by DR-1, the schema guard and the review workflow.

The **future phase must not start** until the partner, as controller, does the statutory DPIA, submits it to MACRA, and agrees the data rules. This pre-assessment, `THREAT_MODEL.md` and `DATA_RULES.md` are inputs to that DPIA.

## Sources

- [D1] Malawi, [Data Protection Act 2024](https://www.mca.ac.mw/mca-siteup/uploads/Data%20Protection%20Act%202024.pdf), ss. 17, 30(3).
- [D2] ICRC, [*Handbook on Data Protection in Humanitarian Action*, 3rd ed.](https://www.icrc.org/en/data-protection-humanitarian-action-handbook), 2024; [ch. 17, Artificial Intelligence](https://www.cambridge.org/core/books/handbook-on-data-protection-in-humanitarian-action/artificial-intelligence/84780BB35FAFF04F403AB7A7AA5C0934).
- [D3] ICRC, [RFL Code of Conduct on Data Protection](https://www.icrc.org/en/download/file/18229/rfl-code-of-conduct.pdf) (vital interest; deletion; transfers).
- [D4] Summaries of the Act by [ITLawCo](https://itlawco.com/focus-areas/data-protection-and-privacy/malawis-data-protection-act-2024-an-overview) and [Tech Hive Advisory](https://www.techhiveadvisory.africa/insights/malawis-data-protection-act-aligning-to-the-new-regulatory-framework). Section numbers were **checked against the Act's text** on 26 Oct 2026: s. 17 (children), ss. 19–24 (rights), s. 25 (automated decision-making), s. 26 (derogations), s. 29 (records), s. 30 (DPIA), s. 33 (DPO), s. 41 (registration; more than 10,000 data subjects).
- [D5] IFRC PrepareCenter, [Restoring Family Links](https://preparecenter.org/toolkit/humanitarian-service-points-toolkit/implementation-programmes-and-activities/restoring-family-links).
- [D6] Splink, [documentation](https://moj-analytical-services.github.io/splink/index.html).
- [D7] ICRC, [*Restoring Family Links: a guide for National Societies*](https://icrcndresourcecentre.org/wp-content/uploads/2019/06/RESTORINGFAMILY-LINKS-A-GUIDE.pdf), §7.3.2.
- [D8] DS-I Africa Law, [Malawi country guide: cross-border sharing of data](https://www.datalaw.africa/wp-content/uploads/2024/09/Malawi_country-guide_30-Sept.pdf), Jul 2024.
- [D9] ICRC, [Policy on Artificial Intelligence](https://alnap.org/help-library/resources/icrcs-policy-ai), Nov 2024.
