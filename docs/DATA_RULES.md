# NameBridge — data rules (phase 0, week 2)

Draft, 26 Oct 2026. These are the rules for data sharing, retention and deletion, disclosure, and incident response required by `CONCEPT-IDEA.md` §10 phase 0. They derive from `THREAT_MODEL.md` and `DPIA.md`.

- **"Now"** means this semester. These rules bind us.
- **"Partner phase"** means the minimum we will require of any tracing partner before real data is used. That partner's own rules, such as the RFL Code of Conduct [R1], apply on top.

## DR-0. Data classes

| Class | What | Where it may live | Now |
| --- | --- | --- | --- |
| **P: public knowledge** | Name graph, packs, sources, rules | Public repo, CC BY 4.0 | Yes |
| **S: synthetic** | Generated people, families, records, gold labels | Public repo (generator and seeds); generated files may be published | Yes |
| **R: reference data with real names** | E.g. CongoNames [R2] | **Outside the repo**, on the researcher's machine only; only aggregate statistics are committed | Yes, restricted |
| **C: case data** | Real tracing requests and records | Only on the partner's systems | **No** |
| **L: logs** | Access and decision logs about class C | Partner's systems; treated like class C | **No** (synthetic logs only) |

## DR-1. What may enter the repository (now)

1. **Only class P and class S** may be committed. No real person's data, ever. This includes names copied from news stories, court documents or social media together with any other attribute.
2. **Class R** stays outside the repo (e.g. `~/namebridge-ref/`, listed in `.gitignore` if it is near the repo). What may be committed from it:
   - token frequencies, with counts under 5 suppressed;
   - name-structure statistics;
   - province-level distributions.

   Never full names, rows, or exam IDs.
3. **Synthetic records** combine tokens at random. A generated full name is never paired with real attributes (a real date of birth, a real school list, real relatives).
4. **Examples in docs and tests** use invented names, or names already used as public examples in the sources (e.g. MUGISHA Jean [R3]). Never a living private person's name.
5. **Graph edges** carry a source, licence, confidence and `review_status` (§5.1A). LLM suggestions enter only as `proposed`.
6. **No ethnicity, clan, tribe or religion** attributes anywhere in the graph or the schema (`THREAT_MODEL.md` §4.2).

## DR-2. Sharing

**Now:**

- Class P and S are shared openly (graph CC BY 4.0, code Apache-2.0).
- Class R is not shared. Each user downloads it from its source under its licence.

**Partner phase:**

1. Case data is shared only **within the authorised tracing network**, for the tracing purpose. Every transfer is recorded (date, recipient, basis) [R1].
2. **Never** shared with government agencies, law enforcement or immigration authorities through NameBridge (`SCOPE.md` §2). Any request goes to the partner, who decides under its own rules. NameBridge holds no copy that could be handed over.
3. **Cross-border transfers** only with an adequacy basis or another lawful condition under Malawi's Data Protection Act, ss. 38–39 [R4], and with a record of the basis kept (s. 38(2)).
4. If partners cannot pool data, use **federated or privacy-preserving matching** instead of pooling, after cryptographic review (§8, "Federated matching").

## DR-3. Retention and deletion

**Now:**

- Class S is kept with each release, so results can be reproduced.
- Class R aggregates are kept. Raw class R data is deleted from the machine at the end of the semester, unless the next phase needs it.

**Partner phase** (minimum):

| Data | Retention | Then |
| --- | --- | --- |
| Open tracing case | While the case is open | — |
| Closed case: the person was found and agreed to contact, or declined, or died, or the request was withdrawn [R5] | Per the partner's RFL retention schedule; NameBridge keeps no copy | Deleted from NameBridge's index on closure |
| Candidate lists that were not confirmed | **30 days** after the case decision (proposed) | Deleted. Only the decision and its audit record remain |
| Access and decision logs | As long as needed for audit and redress, set by the partner | Deleted or archived under the partner's rules |
| Graph edges derived from a case | Never. The public graph holds only general naming knowledge, never person-specific facts (§5.1A) | — |

**Right to deletion:** a data subject's request goes to the partner. NameBridge must be able to delete a person's records and every derived index entry (§13 question 10; week 9 correction flow).

## DR-4. Disclosure

1. **A search result discloses no location or contact details** (C6). It returns a case reference, the evidence and the graph path.
2. **Contact only with consent.** When someone is located, their contact details reach the enquirer only with their consent. They may decline [R5].
3. **Progressive disclosure** (C8): the reviewer sees the minimum first. Sensitive fields open on request, with a reason, and each opening is logged.
4. **Protected-person cases** (C7) are minors, trafficking, domestic violence, asylum, witness protection, or a person who may not wish to be found. They are suppressed from ordinary search and routed to a senior caseworker.
5. **Publication** of names (radio, lists, websites) is the partner's decision under RFL rules, never NameBridge's. It needs the consent of the person whose name is published [R6].
6. **Research outputs** (the report, papers) contain only aggregate results on synthetic data.

## DR-5. Incident response

An incident is any loss, theft, unauthorised access, accidental publication or wrongful disclosure of class C, L or R data. A real name committed to the public repo also counts.

| Step | Now (research repo) | Partner phase |
| --- | --- | --- |
| 1. Detect and report | Whoever notices tells the other researcher the same day | Report to the partner's data protection officer at once |
| 2. Contain | Remove the data. Rewrite git history if it was committed. Rotate any exposed keys | Isolate the affected systems. Suspend the affected search features |
| 3. Assess | What, whose, how many, what harm | Same, plus a risk assessment for the people concerned (located persons, minors) |
| 4. Notify | Inform the professor. If class R was involved, inform the dataset's authors | Controller → **MACRA within 72 hours**. Data subjects within 72 hours if the risk is high (ss. 36–37) [R4]. The processor informs the controller within 72 hours [R7] |
| 5. Record and learn | Entry in `RESEARCH_LOG.md`; fix the cause | Breach record (required); update the threat model |

**Drill:** before phase 3, run a tabletop exercise with the partner, using the 2022 Red Cross breach as the scenario [R8].

## DR-6. Who is responsible

- **Now:** the student researcher, reviewed by the professor.
- **Partner phase:** named data stewards from the partner. They don't exist yet; this is recorded as a phase 0 gap in `SCOPE.md` §8.

## Sources

- [R1] ICRC, [RFL Code of Conduct on Data Protection](https://www.icrc.org/en/download/file/18229/rfl-code-of-conduct.pdf) (records of transfers, deletion, file closure, archiving).
- [R2] Tshabu Ngandu et al., ["CongoNames Corpus"](https://www.mdpi.com/2306-5729/11/7/169), *Data* 11(7):169, 2026 (CC BY 4.0).
- [R3] [Rwandan names](https://en.wikipedia.org/wiki/Rwandan_names) (example "MUGISHA Jean").
- [R4] Malawi, [Data Protection Act 2024](https://www.mca.ac.mw/mca-siteup/uploads/Data%20Protection%20Act%202024.pdf), ss. 36–39.
- [R5] ICRC, [*Restoring Family Links: a guide for National Societies*](https://icrcndresourcecentre.org/wp-content/uploads/2019/06/RESTORINGFAMILY-LINKS-A-GUIDE.pdf), §7.3.2 (consent to disclose contact details) and §7.4.3 (closure).
- [R6] ICRC, [Guidelines on providing RFL services to migrants](https://icrcndresourcecentre.org/wp-content/uploads/2025/02/Guidelines-RFL-and-migration-en.pdf), 2025 (consent to publication; risk assessment for community media).
- [R7] [Tech Hive Advisory summary](https://www.techhiveadvisory.africa/insights/malawis-data-protection-act-aligning-to-the-new-regulatory-framework) of ss. 36–37 (processor → controller within 72 hours).
- [R8] ICRC, ["Cyber security incident: How could it affect me?"](https://www.icrc.org/en/document/cyber-security-how-it-affect-me), updated 24 Jun 2022.
