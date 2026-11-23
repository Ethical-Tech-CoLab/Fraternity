# Decisions Making: decisions still open

*NameBridge · NYU independent study · meeting brief. Prepared 9 Nov 2026, updated 16 Nov and 23 Nov 2026, from the gates table in `TIMETABLE.md` and `GATE_EXAMPLES.md`.*

Three questions only the professor can settle. Everything already decided has been left out. Each item says what is being decided, why it matters, the options, and what we do if nothing changes. **All people in the examples are invented.** When a decision is made, it is recorded in `TIMETABLE.md` and removed from this page.

| Decision | What it changes | Needed by | Default if undecided |
| --- | --- | --- | --- |
| **G4** Cost of errors | Benchmark size and match thresholds | **23 Nov (passed)**: the benchmark was frozen on 23 Nov on the 26 Oct ratios, as a soft-gate override (`RESEARCH_LOG.md`) | The ratios set on 26 Oct (in use) |
| **Look-alike pairs** (new, 23 Nov) | How the hard-negative pairs are reported | Before the week 8 results | Separate stratum, "not verifiable from the record", not counted as correct or wrong (`BENCHMARK_PROTOCOL.md` §5) |
| **Legal check** for Muslim names | Whether those names enter the graph | no deadline (professor researching, 16 Nov) | Left out of v0.1 |

---

## G4 — How much worse is one kind of error than the other? (by 23 Nov)

NameBridge makes two kinds of mistake: it can **miss** the right person, or it can **show the wrong one**. How we weigh them sets the match thresholds and the size of the test set (26,000 invented people is calculated from these targets). The benchmark in week 6 cannot be built until this is settled.

### Method asked for on 16 Nov: reverse stress testing

The professor did not set numbers. The professor asked us to study the professor's reverse stress testing atlas (github.com/Ethical-Tech-CoLab/reverse-stress) and work out from it what could count as **acceptable**, because NameBridge deals with people's lives. The analysis is in **`G4_REVERSE_STRESS.md`**. In short:

- **Start from what must not happen**, not from a ratio. Five outcomes: U1 a child handed to the wrong adult; U2 a location reaching a non-relative; U3 a silent missed reunion; U4 a person who changed their name exposed; U5 a review queue too long to check.
- **Harms that cannot be undone (U1, U4) get rules, not thresholds**: a step that cannot be skipped. Thresholds only check that the rule holds.
- **Safeguards are not independent**: a confident wrong match makes the human check more likely to pass it, so later checks get credit only for evidence the matcher did not use.
- **The same score means less in a bigger database**: DNA identification of missing persons sets its threshold after accounting for how many people are missing (ICMP reports a match at ≥ 99.95%). Targets must state the pool size.
- **Queue length is a safety limit**: clinicians override 49–96% of safety alerts when most are noise.

| # | Draft tolerance (middle level; strict and loose levels also tested) |
| --- | --- |
| U1 | Zero by design: no minor reaches "strong evidence" without a non-name check; model precision ≥ 0.999 on the worst slice |
| U2 | Adult precision ≥ 0.99 on the worst slice; location only after consent |
| U3 | recall@20 ≥ 0.95 overall and ≥ 0.90 on the worst slice |
| U4 | Zero by design; adversarial searches in the benchmark must all be refused |
| U5 | ≤ 20 candidates per search; ≥ half of "strong evidence" flags true |

*Decided 16 Nov: a child is anyone **under 18 at the time of the search** (former question 4).*

> **For the professor: are these the right outcomes, and which level (strict, middle, loose) is acceptable for each?** Five questions are listed in `G4_REVERSE_STRESS.md` §7. The benchmark size (26,000 today) is recalculated from the answer, and will grow if targets apply to the worst slice.

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

---

## Look-alike pairs — how do we report them? (new, 23 Nov)

Hard negatives are pairs built to look like another family: same origin, same or similar name, birth years close. Their gold label is "different people". In the human check (300 pairs, dev split), the reviewer agreed with that label on **12.5%** of the decided look-alike pairs (7 agree, 49 disagree). Across the 60 look-alike pairs, 56 share the same name, 55 the same sex, and 58 the same claimed origin. The label depends on hidden person ids that a caseworker cannot see, so it cannot be checked from the records. Every other stratum agreed well (same person 99%, relatives 98%, request vs record 100%).

We tried a fix that would make look-alikes differ on a visible field. It changes the whole benchmark sample, so it would need the 300 pairs answered again. We have not done that.

**Decided by the user (23 Nov), for your confirmation:** report look-alikes as a separate stratum marked "not verifiable from the record". They are not counted as correct or wrong in the headline metrics. Every other stratum is reported as before.

> **For the professor: do you accept this reporting rule for the v0.1 benchmark report, or do you want the look-alike pairs rebuilt with a visible difference (which means a new sample and a new human check)?**

*Also for information:* the frozen sets (commit 63a40e9) passed all nine realism checks under the original rule. A change to the look-alike generator was prepared and set aside, because it would need the new human check.

---

## Legal check — May Muslim names enter the graph? (no deadline)

*16 Nov 2026: the professor will answer later, after researching it further.*

Many people in the corridor carry Muslim names (Hassan / Hasani, Fatuma / Fatima, Juma). A list of such names can reveal religion, which is sensitive data under Malawi's Data Protection Act. When the professor allowed the restricted name-change layer (G5), one condition was a legal check before religion-linked names are used.

> **Who does that legal check, and when?**

- **A check this semester**: by NYU or a contact the professor names.
- **After the semester** *(default if undecided)*: Muslim names stay out of v0.1; the gap is stated in the release note.

