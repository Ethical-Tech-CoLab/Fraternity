# NameBridge — does the semester work need NYU IRB review? (gate G3)

Draft, 26 Oct 2026. This is an analysis for the professor (faculty sponsor), **not an IRB determination**. Under NYU's process, only the professor and the student, or the HRPP, can make that call. Sources are listed at the end ([I1]–[I6]).

## The question

To make the synthetic benchmark realistic, the plan (`BENCHMARK_PROTOCOL.md` §2.4) is to:

1. **Download public name lists:**
   - CongoNames: 8.05 M names from DRC state-exam result lists, published under CC BY 4.0;
   - NESA Rwanda: published national-exam results;
   - the UN Security Council 1533 sanctions list.
2. **Analyse them locally** and keep only aggregates (elements seen 5 or more times; no ethnicity patterns).
3. **Delete the raw lists.**

The project:

- has **no interaction** with anyone;
- uses **no private data**;
- includes **no refugees' data** this semester;
- publishes only aggregate statistics and synthetic data.

Does this need IRB review?

## The rules

**Federal definition (Common Rule, 45 CFR 46.102(e)(1)) [I1].** A *human subject* is a living individual about whom an investigator "(whether professional or student)":

- (i) obtains information through **intervention or interaction**; or
- (ii) obtains, uses, studies or analyses **identifiable private information**.

*Private information* is information about behaviour where a person can reasonably expect no observation or recording, **or** information "provided for specific purposes … that the individual can reasonably expect will not be made public" (46.102(e)(4)) [I1].

**NYU's own decision tree (existing / secondary data) [I2].**

- If the data are **publicly available** ("Is all the information … available in the public domain?"), the project is "Not human subjects research. **No application to the IRB office is needed.**"
- But course work whose results "may lead to use … outside of the course (e.g. for a publication, presentation, thesis…)" counts as **research**. So the decision for NameBridge turns on the data, not on whether it is coursework.

**NYU HRPP on formal determinations [I3].**

- "Investigators are **not required** to obtain a formal determination from the HRPP **if they are sure** that their project does not involve human subjects research."
- Investigators who are **unsure** "should contact the HRPP for guidance".
- A formal *Not Human Subjects Research* (NHSR) determination is made through an **abridged application in Cayuse IRB**. It is usually requested when an external party needs it (a funder, a data provider, a journal).

**Exempt category 4 (45 CFR 46.104(d)(4)(i)) [I1][I4].** Even if the data were judged identifiable *private* information, secondary research on **publicly available** information is exempt. Exempt status is still decided through the IRB, not by the investigator.

## Analysis for NameBridge (semester work)

| Test | NameBridge | Result |
| --- | --- | --- |
| Research? (systematic, generalisable knowledge) | Yes: an evaluation report and a public release are planned | **Research** |
| Intervention or interaction with people? | None | No |
| Information obtained | Names (and sex, year, region) from lists the governments **published** | Identifiable, but **public** |
| Private? (a reasonable expectation that it will not be made public) | No: exam results are published by the ministries; the UN list is public by design | **Not private** |
| **Human subjects?** | No interaction, no private information | **Probably not** |

**Likely conclusion:** the semester work is **Not Human Subjects Research** under 45 CFR 46.102(e), and NYU's decision tree says no IRB application is needed for publicly available existing data.

**Why it is still worth asking instead of deciding alone:**

1. **The names identify people, some of them minors** (exam candidates are about 17–18). Some IRBs prefer to confirm this kind of case.
2. **The topic is sensitive:** refugees, tracing, and data that could be misused. A short, written confirmation protects the project if a journal or a future partner asks.
3. **NYU's rule** is that you may self-determine only if you are **sure**; otherwise you contact the HRPP.

**Not covered by this analysis:**

- **Phase 3:** real case data with a tracing partner **will** be human subjects research and will need full IRB review.
- **Any contact with people:** interviews with linguists, community reviewers or refugees **is** human subjects research. The Jan–Mar 2027 native-speaker review may need IRB review, unless it is limited to reviewing the name data and asks nothing about the reviewers themselves.

## Options for gate G3 (the professor chooses)

| Option | Effort | When to use it |
| --- | --- | --- |
| **A. Self-determination.** The professor confirms that the work is NHSR; the decision is recorded in `RESEARCH_LOG.md` with this analysis | Minutes | The professor is sure, and nobody external needs a formal letter |
| **B. Email the HRPP** (`ask.humansubjects@nyu.edu`) with the draft below | One email, a few days | Recommended. Some doubt remains, and it costs little |
| **C. Formal NHSR determination** via an abridged Cayuse IRB application (the student needs a Cayuse account; the professor acts as faculty sponsor) | About 1–2 weeks | A journal, data provider or partner will ask for a formal letter |

**Recommendation:** **B**, upgrading to **C** if a publication is planned. Gate G3 closes when either written answer is recorded.

## Draft email to the NYU HRPP (for the professor or the student, cc the professor)

> **To:** ask.humansubjects@nyu.edu
> **Subject:** Guidance request: Not Human Subjects Research? Aggregate analysis of public name lists (independent study)
>
> Dear HRPP team,
>
> I am an NYU student doing an independent study with Prof. [name] (faculty sponsor). We are building an open-source research prototype that matches personal names written differently across countries, for future use by humanitarian family-tracing services. This semester the work uses **synthetic data only**.
>
> To make the synthetic names realistic, we would like to compute **aggregate statistics** (frequency of name elements seen at least 5 times, name length, number of names per person, distribution by province and year) from **publicly available** name lists:
> - the CongoNames corpus (published under CC BY 4.0 in the journal *Data*, 2026, compiled from DRC state-exam results);
> - published Rwandan national-exam results;
> - the UN Security Council sanctions list.
>
> We would process the lists locally, keep only the aggregates, delete the raw lists, and publish nothing that identifies an individual. There is no interaction with any person and no private information.
>
> Could you confirm whether this activity is *not human subjects research*, or whether we should submit an abridged application in Cayuse IRB for a formal determination? We may later publish the evaluation.
>
> Thank you,
> [name], NYU [school]

## Sources

- [I1] [45 CFR 46.102](https://www.law.cornell.edu/cfr/text/45/46.102) (definitions) and [45 CFR Part 46](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46) (46.104(d)(4), exempt category 4).
- [I2] NYU HRPP, [Human Subjects Research Decision Tree](https://www.nyu.edu/content/dam/nyu/research/documents/IRB/IRBDecisionTree.pdf).
- [I3] NYU HRPP, [How to Apply](https://www.nyu.edu/research/resources-and-support-offices/getting-started-withyourresearch/human-subjects-research/how-to-apply.html) (formal determinations, Cayuse) and [Forms & Guidance](https://www.nyu.edu/research/resources-and-support-offices/getting-started-withyourresearch/human-subjects-research/forms-guidance.html) (Not Human Subjects Research checklist; student-led research; guidance for faculty sponsors).
- [I4] UAB, [Exempt category 4: secondary use of data](https://www.uab.edu/research/home/category-4-secondary-use-of-data): "In most cases, publicly available datasets … qualify for review under Not Human Subjects Research."
- [I5] NIH IRBO, [Not Human Subjects Research](https://irbo.nih.gov/irb-review/not-human-subjects-research): investigators may self-determine but "should consult with the IRB, if there is any question". This is another institution's practice, given for comparison.
- [I6] NYU HRPP, [About Us](https://www.nyu.edu/research/resources-and-support-offices/getting-started-withyourresearch/human-subjects-research/about0.html) (Washington Square HRPP).
