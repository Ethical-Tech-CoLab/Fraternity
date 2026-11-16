# Decisions Making: decisions still open

*NameBridge · NYU independent study · meeting brief. Prepared 9 Nov 2026, updated 16 Nov 2026, from the gates table in `TIMETABLE.md` and `GATE_EXAMPLES.md`.*

Three questions only the professor can settle. Everything already decided has been left out. Each item says what is being decided, why it matters, the options, and what we do if nothing changes. **All people in the examples are invented.** When a decision is made, it is recorded in `TIMETABLE.md` and removed from this page.

| Decision | What it changes | Needed by | Default if undecided |
| --- | --- | --- | --- |
| **G4** Cost of errors | Benchmark size and match thresholds | **23 Nov** (blocks week 6) | The ratios set on 26 Oct |
| **Reviewers** for the name graph | Whether any edge can move past "proposed" | before release | Everything stays "proposed" |
| **Legal check** for Muslim names | Whether those names enter the graph | no deadline | Left out of v0.1 |

---

## G4 — How much worse is one kind of error than the other? (by 23 Nov)

NameBridge makes two kinds of mistake: it can **miss** the right person, or it can **show the wrong one**. How we weigh them sets the match thresholds and the size of the test set (26,000 invented people is calculated from these targets). The benchmark in week 6 cannot be built until this is settled.

### Method agreed on 16 Nov: reverse stress testing

The professor asked that the targets come from **reverse stress testing**, the method in the professor's teaching atlas (github.com/Ethical-Tech-CoLab/reverse-stress). Because NameBridge deals with people's lives, the targets are not picked as ratios. We start from the outcomes that must not happen, agree how much of each is acceptable, and then work backward to the error rates and thresholds that keep every outcome inside that limit. The atlas's own steps are: define what must not fail (its owner, unit, tolerance and time horizon); find which combinations of upstream conditions produce it; then forward-test the controls. A reverse stress test finds **failure paths worth fixing**. It does not predict how likely they are.

**Step 1: what must not fail.** The critical function is that *a separated person is found by their family, and nobody is put at risk on the way*. Candidate unacceptable outcomes, to agree with the professor (each needs a tolerance, e.g. "at most N per 10,000 searches", or "zero by design"):

| # | Unacceptable outcome | Which error causes it | Tolerance (to decide) |
| --- | --- | --- | --- |
| U1 | A **child is handed to the wrong adult** | False confirmation, minor | Proposed: **zero by design**. No child is confirmed on names, age and place alone; a non-name check is required (question 2 below) |
| U2 | A person's **location or contact reaches someone who is not their family** | False confirmation, adult | ? per 10,000 confirmations; consent comes before any location is shared, so this outcome needs a false match *and* a failed consent step |
| U3 | A relative who **is in the data is never shown** to the searcher (a silent missed reunion) | Missed at retrieval | ? per 100 searches |
| U4 | A person who **changed their name for safety** is exposed by a search | Search used against `NAME_CHANGE.md` | Zero by design (rules 5–7, SCOPE §4) |
| U5 | The **review queue is so long** that caseworkers stop checking and accept the first candidate | Too many wrong candidates | ? candidates per search a caseworker can really check |

**Step 2: work backward.** For each outcome, search the synthetic world (week 6) for the conditions that most plausibly produce it, instead of reporting only an average. Candidates already in the benchmark: two different people with the same name in neighbouring provinces (the Eloi example below); children's ages estimated; a name written by ear; a given name changed in exile; only a given name and a province remembered (the Belyse example). The result is a list of **failure paths**, each with the slice of records where it happens.

**Step 3: set the controls.** Choose thresholds, rules and queue limits so that each outcome stays within its tolerance **on its worst slice**, not just on average. The current ratios (table below) become a starting point to test, not the answer.

**Step 4: forward test.** Run the failure paths found in step 2 through the pipeline and check that the controls hold, including weeks 7–8 baselines.

> **The question for the professor and the student: which tolerance is acceptable for each outcome?** Everything else follows from it, including the benchmark size (26,000 people today, derived from the ratios; it is recalculated from the tolerances).

Limits: the atlas is teaching material, and its examples are supply chains, not people. Here, the method is used to choose the targets and the tests. All data stay synthetic.

### The default ratios (in use until the tolerances are agreed)

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

