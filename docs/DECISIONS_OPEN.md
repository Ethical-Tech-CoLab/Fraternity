# Decisions Making: decisions still open

*NameBridge · NYU independent study · meeting brief. Prepared 9 Nov 2026 from the gates table in `TIMETABLE.md` and `GATE_EXAMPLES.md`. Also published as a page: https://claude.ai/artifact/WXeszv3CEeaBwC3WVq7ZmY (private until shared).*

Five questions only the professor can settle. Everything already decided has been left out. Each item says what is being decided, why it matters, the options, and what we do if nothing changes. **All people in the examples are invented.** When a decision is made, it is recorded in `TIMETABLE.md` and removed from this page.

| Decision | What it changes | Needed by | Default if undecided |
| --- | --- | --- | --- |
| **G9** Size of the name corpus | Wording of the first public release (graph v0.1) | **20 Nov** | Release with the count stated |
| **G4** Cost of errors | Benchmark size and match thresholds | **23 Nov** (blocks week 6) | The ratios set on 26 Oct |
| **Reviewers** for the name graph | Whether any edge can move past "proposed" | before release | Everything stays "proposed" |
| **Legal check** for Muslim names | Whether those names enter the graph | no deadline | Left out of v0.1 |
| **G8** Name-change notices | One possible source of name-change patterns | after week 7 | Not used |

---

## G9 — How big must the name corpus be? (by 20 Nov)

The concept paper (§10, phase 1) asks for **2,000–10,000** sourced relationships between names. The graph has **299** today, and with sourced material only the semester projection is about **600–900**.

The gap comes from a deliberate rule: we add only relationships that a source attests (Bible translations, official name lists, published studies), never variants we invent ourselves, because invented variants produce false matches. Spelling variants are still handled, but by the matcher at search time, not stored in the graph.

> **Is a smaller, fully sourced corpus acceptable for this semester?**

- **Accept it for the semester** *(default in use)*: release graph v0.1 with the real count, state the shortfall against §10, keep adding sourced relationships in later weeks.
- **Extend phase 1**: spend more weeks on the corpus before the benchmark; the rest of the timetable moves later.

The exit criterion for phase 1, "every edge sourced and confidence-scored", is met either way.

---

## G4 — How much worse is one kind of error than the other? (by 23 Nov)

NameBridge makes two kinds of mistake: it can **miss** the right person, or it can **show the wrong one**. How we weigh them sets the match thresholds and the size of the test set (26,000 invented people is calculated from these targets). The benchmark in week 6 cannot be built until this is settled.

| Step | Default ratio | Target | In plain words |
| --- | --- | --- | --- |
| Search | missed : wrong = 10 : 1 | recall ≥ 0.95 | In 20 searches for someone who is in the data, at most 1 fails to show them |
| Confirm, adult | wrong : missed = 10 : 1 | precision ≥ 0.99 | Of 100 pairs called "strong evidence", at most 1 is two different people |
| Confirm, child | wrong : missed = 100 : 1 | precision ≥ 0.999 | Of 1,000 such pairs with a child, at most 1 is wrong |

### 1. Search: is missing 1 person in 20 acceptable?

- **Keep recall ≥ 0.95** *(default in use)*: shorter review queues.
- **Raise to 0.98 (1 in 50)**: fewer silent misses; caseworkers look at more wrong candidates.

*Example.* A girl of about 7 says her mother is "Mama Belyse" and they lived "near the big market in Kayanza". Her mother is registered as NSHIMIRIMANA Belyse, born 1991, Kayanza. The child gave only a given name and a province, so the name score is weak. If the search drops the mother's record, nobody ever sees it: the failure is silent.

### 2. Children: is a threshold enough, or do we need a rule?

- **Keep 100 : 1 as a threshold** *(default in use)*: a child can reach "strong evidence" on names, age and place if the score is high enough.
- **Add a rule**: a child never reaches "strong evidence" without a check that does not use names. The candidate check: a **reciprocal match**, where the child's family is also searching for the child and the details both sides give agree, verified by a caseworker.

*Example.* Two different boys are both HAKIZIMANA Eloi, one born 2015 in Ngozi, one born 2016 in Kirundo. A father searches for "Eloi Hakizimana, about 10, from Ngozi". Name, sex and age agree; only the province and one year differ, and children's ages are often estimated. A false match could hand the wrong child to this father.

### 3. Adults: is 10 : 1 right?

- **Keep 10 : 1** *(default in use)*: a wrong adult match means a stranger is asked whether he wants contact; no location is shared without his consent.
- **Make it stricter**: fewer wrong contacts, more missed reunions.

*Example.* NDAYISENGA Jean-Paul (born 1984, Muyinga) and NDAYISENGA Paul (born 1985, Muyinga) are different men. A sister searches for "Jean-Paul, my brother, about 40".

### 4. Who counts as a child?

- **Under 18 at the time of the search** *(default in use)*.
- **Under 18 at the time of separation**: covers adults who were separated as children and may not remember their family's names well.

---

## Reviewers — Who can review the name graph? (before release)

Every relationship in the graph is marked **proposed** until a person with a stated role reviews it (linguist, community expert, investigator or data steward). The review tool is built, and each decision is logged with a name, role and reason. Nothing has been reviewed yet: the rules forbid a script or an AI assistant from doing it.

> **Who reviews this semester, and in which role?**

- **The student as investigator**: reviews a sample of edges this semester.
- **A linguist the professor knows**: for Kinyarwanda, Kirundi or Lingala. Contact with people may need ethics review first.
- **Nobody this semester** *(default if undecided)*: v0.1 ships with every edge "proposed", and says so.

One concrete question a linguist could answer: are *Ntakarutimana* and *Ntakirutimana*, both common in Burundi, two forms of one name? No source says so, so they are not linked.

---

## Legal check — May Muslim names enter the graph? (no deadline)

Many people in the corridor carry Muslim names (Hassan / Hasani, Fatuma / Fatima, Juma). A list of such names can reveal religion, which is sensitive data under Malawi's Data Protection Act. When the professor allowed the restricted name-change layer (G5), one condition was a legal check before religion-linked names are used.

> **Who does that legal check, and when?**

- **A check this semester**: by NYU or a contact the professor names.
- **After the semester** *(default if undecided)*: Muslim names stay out of v0.1; the gap is stated in the release note.

---

## G8 — May we read published name-change notices? (after week 7)

Courts publish legal name changes in official journals (DRC *Journal officiel*, Family Code art. 66; the Rwanda Official Gazette). Read only for **patterns** (what kinds of change occur), they would help us model people who change their names. They are personal data, though, and fall outside what the earlier IRB decision (G3) covered.

A known limit: only formal changes appear. The people most at risk, who change names informally or to hide, are absent from these notices.

> **May notices be read for aggregate patterns only, with no individual kept?**

- **Yes, aggregate patterns only**: under the same rules as the public name lists.
- **Yes, after an IRB opinion**: as option B was for G3.
- **No** *(default in use)*: the pattern set relies on published studies instead.
