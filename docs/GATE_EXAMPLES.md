# Examples for gates G4 and G5

Draft, 28 Oct 2026. On 26 Oct the user deferred G4 (error costs) and G5 (`NAME_CHANGE.md` rule 5) "until we see examples". This page gives those examples, so that the user and then the professor can decide.

**All people below are invented.** Their names are recombined from common name elements; any resemblance to a real person is accidental. Nothing here is real case data (`DATA_RULES.md` DR-1).

---

## G4: what the error costs mean in practice

The defaults (decided by the user on 26 Oct; `BENCHMARK_PROTOCOL.md` §7):

| Step | Default | In plain words |
| --- | --- | --- |
| Retrieval | Missed : false = 10 : 1; **recall@20 ≥ 0.95** | In 100 searches where the person *is* in the data, they appear in the top 20 at least 95 times. The price is reviewers looking at wrong candidates |
| Confirmation (adults) | False : missed = 10 : 1; **precision ≥ 0.99** | Of 100 pairs shown as "strong evidence", at most 1 is two different people |
| Confirmation (minors) | False : missed = 100 : 1; **precision ≥ 0.999** | Of 1,000 such pairs involving a child, at most 1 is wrong. More true matches drop to "not enough evidence" |

### Example 1: retrieval (why a miss is worse)

A girl of about 7 (invented) tells a caseworker her mother is "Mama Belyse" and that they lived "near the big market in Kayanza". In the data, her mother is registered as **NSHIMIRIMANA Belyse, b. 1991, Kayanza**.

- The child's request has only a given name, a nickname form and a province, so the name score is weak.
- **If retrieval drops her** (a miss), no human ever sees the mother's record. The search fails silently.
- **If retrieval also returns 19 other "Belyse"s from Kayanza** (false candidates), a caseworker spends some minutes ruling them out.

That is why a miss costs 10 times more here. **Question:** is 1 silent miss in 20 searches (recall 0.95) acceptable, or should it be 1 in 50 (0.98), which means longer queues?

### Example 2: confirmation for a minor (why a false match is worse)

Two invented boys are both **HAKIZIMANA Eloi**: one born 2015 in Ngozi, the other born 2016 in Kirundo. A father is searching for "Eloi Hakizimana, about 10, from Ngozi".

- Name, sex and age all agree. Only the province and one year differ, and children's ages are often estimated.
- **A false match** could mean the wrong child is presented to the father, possibly released to him. That is the worst outcome in child tracing.
- **A miss** means the pair is marked "not enough evidence" and goes to further verification (photos, questions only the family can answer). It is slower, but not lost.

So minors use 100 : 1. At precision 0.999, a pair like this one would never be shown as "strong evidence" on names and age alone, which is the intent. **Question:** is 100 : 1 enough, or should a minor *never* reach "strong evidence" without a non-name confirmation (e.g. a family photo check)? The second option is a rule, not a threshold.

### Example 3: confirmation for an adult

Two invented men, **NDAYISENGA Jean-Paul** (b. 1984, Muyinga) and **NDAYISENGA Paul** (b. 1985, Muyinga), and a sister searching for "Jean-Paul, my brother, about 40".

- A false match means a stranger is contacted and asked whether he wants to be put in touch. The RFL rule (the person found decides) limits the harm: no location is shared without his consent.
- So adults use 10 : 1, not 100 : 1.

**Question:** are the adult and minor ratios right, and is "under 18 at the time of the search" the right line, or "under 18 at the time of separation"?

### What the professor decides for G4

1. Retrieval: keep recall@20 ≥ 0.95, or raise it.
2. Minors: keep 100 : 1, or add the rule "never strong evidence without a non-name check".
3. Adults: keep 10 : 1.
4. Age line: at the search, or at separation.

---

## G5: rule 5 in four cases

Rule 5 as written: *no support for identity-verification or citizenship-revocation campaigns, or for searches for people who changed their names, including alleged perpetrators* (`NAME_CHANGE.md`).

| # | Case (invented) | Under rule 5 as written | Why |
| --- | --- | --- | --- |
| **C1** | A mother in Dzaleka searches for her son, **BIZIMANA Claude** (b. 2003). He left for Lilongwe in 2021 and may now use a Swahili Muslim name | **Allowed** as a tracing search. If a candidate agrees on surname, age and family but not on the given name, it is a **"possible name change"**: senior caseworker only, no location shown, and the son decides whether to be contacted (rules 2 and 6) | This is family tracing. The person found keeps control |
| **C2** | A government department asks a tracing partner to run a list of 55 names through NameBridge to find people "now using Malawian names" | **Refused** | A verification or revocation campaign, and governments are not users (G2; `SCOPE.md` §2 and §4) |
| **C3** | An association of genocide survivors asks a tracing partner to search for a man it believes is a perpetrator living under a new name | **Refused** | This is the contested case. Rule 5 says finding alleged perpetrators is for courts and police, with their own legal means |
| **C4** | An ordinary tracing request for a missing uncle who, unknown to anyone, is wanted abroad | **Normal tracing.** NameBridge cannot know and does not ask | The person found still decides on contact, and the output never goes to authorities (rule 4, prohibited uses) |

### The choice for the professor (G5)

| Option | What it means | Risk |
| --- | --- | --- |
| **A. Keep rule 5 as written** (current default) | C3 is refused; C1 and C4 work as above | Survivors may see the tool as protecting perpetrators. Answer: the tool is for reuniting families, and courts have their own channels |
| **B. Allow C3 with a court order** | A search is run only on a court's written request | NameBridge becomes a law-enforcement tool, which contradicts G2 and the threat model (T15). The same path could be used against refugees in campaigns like C2 |
| **C. Allow C3 for accredited survivor groups** | No court; the group is vetted | The hardest to control: anyone can claim a person is a perpetrator, and in Malawi the accusation itself is dangerous (`NAME_CHANGE.md` §4) |

**Recommendation:** **A**. B and C would each need the threat model and the scope redone, and both conflict with G2.

### Related evidence (28 Oct 2026)

A documented case shows what a perpetrator search would be up against: one suspect claimed asylum as a Burundian under three aliases and also used a Malawian identity (`NAME_CHANGE.md` §4 [N9]). None of those names is a spelling variant of another, so under rule 1 the graph would not link them anyway. **Name matching would not find such a person**, whatever rule 5 says. It could only produce suspicion about innocent people with similar names, which is the harm C2 describes.
