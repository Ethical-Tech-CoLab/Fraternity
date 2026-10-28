# NameBridge — deliberate name change in exile

Draft, 26 Oct 2026. **This is a cross-cutting rule: it applies to the graph, the matching, the benchmark, the intake guide and every integration (CPIMS+ included).** Sources are listed at the end ([N1]–[N8]).

## Why it matters

Refugees in the Great Lakes region change or hide their names **on purpose**:

- to become invisible in the host society;
- to protect themselves (from abusers, from people who wish them harm, from authorities);
- for religious or social reasons.

A system that links names across countries can undo that protection. The same system can also reunite a family whose child now uses another name. Both are true, so NameBridge needs explicit rules.

## What the evidence shows: the patterns

### 1. Burundian refugees in Tanzania: an *ordered* change [N1][N2][N3]

- **Step 1: the Christian (French) given name goes first.** It is commonly replaced by a **Muslim (Swahili/Arabic) name**, and the **Kirundi surname is kept**. ("It is common to change the Christian name to a Muslim name, leaving the surname." [N1])
- **Step 2: the surname changes only if it is "too noticeable".** It is then replaced by a Burundian name that "passes for a Tanzanian name" [N1]. Tanzania's Ha people speak a language close to Kirundi, so such names exist.
- **Conclusion of the authors:** "the Christian name is given up first, then the surname, since the latter defines the individual as truly Burundian" [N1].
- **Where it happens:**
  - **in towns, and where refugees are a minority:** in Kigoma town, refugees took Muslim names, became Muslim, and called themselves Tanzanian Ha [N2][N3];
  - **not in the settlements:** there, refugees **kept** their names to remain visible as a people [N1][N2];
  - **after naturalisation too:** some new citizens kept pseudonyms or adopted names [N3].

### 2. Rwandan refugees in Uganda: a changed name *and* a changed origin [N4]

Under threat of forced return, refugees "hide their identities and change their names". Some present themselves as **Congolese**, or as **Banyankole**, a Ugandan people whose language they speak. **Claimed nationality and origin can be false for protection reasons.**

### 3. Congolese refugees: several names *by design* [N5]

- Congolese people commonly have **names used openly and names kept close**, shared only with a few people. This protects against witchcraft, identity theft, "anyone with malicious intentions", and sometimes the authorities.
- **Spelling is not fixed**, and sound-alike names can be interchangeable (`Rashindi` / `Kashindi`).
- **Kinship words are used loosely** ("brother" and "cousin" interchangeably).
- In a Tanzanian camp, UNHCR staff treated such discrepancies **with suspicion**. That can harm a refugee's protection or resettlement case [N5].

### 4. Malawi: name change is politically charged [N6][N7]

- **2023:** Malawi's Minister of Homeland Security said that **55 genocide suspects sought by Rwanda** may be hiding in Malawi "using Malawian names" and fraudulent passports. The government began **revoking citizenships and passports**. Critics said the campaign could ensnare legitimate refugees [N7].
- **2020:** a former Minister of Homeland Security was **jailed for issuing fraudulent citizenships and passports to Burundians and Rwandans** [N7].
- **One documented case shows the whole chain** [N9]: a Rwandan genocide suspect arrested in South Africa in May 2023 had claimed asylum **as a Burundian** under three successive aliases (1998, 1999, 2017) and also used a **Malawian identity with a Chichewa name**, on a Malawian passport issued in 2007. So a person can change given name, surname *and* claimed nationality, more than once, across four countries. *Single source chain* (The New Times, Kigali, via Nyasa Times); the arrest itself is confirmed by the UN residual mechanism (IRMCT), as reported in [N6]. Names are deliberately not copied here (`DATA_RULES.md` DR-1.1).
- **Scale of the 2023 campaign** [N10]: Malawi said it had revoked papers for **396 foreigners**; the head of the Centre for Human Rights and Rehabilitation said it was "targeting everyone, indiscriminately". UNHCR had also asked Malawi to repatriate 522 asylum-seekers "associated with criminalities" (minister's statement, single source).
- **The double edge:** in Malawi, the people who hide behind changed names include both victims and alleged perpetrators, and the government is actively looking for some of them. A tool that links old and new names is exactly what such a campaign would want.

## What can and cannot be modelled

| Change | Can a name link find it? | What the system does |
| --- | --- | --- |
| Christian or French given name → Muslim or Swahili name, **surname kept** (step 1) | **Partly:** the surname still links; the given name does not | Find it only with other evidence (surname plus family, age, place). Label it **"possible name change"** |
| Surname also replaced (step 2) | **No** | Only non-name evidence can find it. That evidence alone never confirms identity |
| Interchangeable sound-alike spellings (`Rashindi` / `Kashindi`) | **Yes**: an ordinary variant | Normal graph edge, with a source |
| Open name vs close name | **No**: the close name is never given | Not modelled. We never ask for it |
| False nationality or origin given for protection | n/a | Nationality is **weak evidence**, never a hard filter |

## The rules (in every context)

1. **No graph edge between unrelated names.** An adopted name (e.g. `Jean` → `Hamisi`) is not a variant. The graph never links them, not even as `proposed`. A cognate (`Jean` → `Yohana`) is a variant; an adopted name is not.
2. **"Possible name change" is a protected-person case.** When a candidate agrees on the surname and on non-name evidence but differs completely on the given name, or agrees only on non-name evidence:
   - it goes to a senior caseworker only (C7);
   - its location and contact details are never shown (C6);
   - contact happens only if the person found agrees (RFL practice).

   A family can still find a child who took a new name, but the person found keeps control.
3. **Nationality and claimed origin are weak evidence.** They may raise or lower a score slightly; they never exclude a candidate.
4. **Inconsistent names are normal, not suspicious.** NameBridge output, including scores, graph paths and "name differs" flags, must **never** be used as evidence about a person's credibility in refugee status determination, resettlement, or citizenship decisions. This is a new prohibited use (`SCOPE.md` §4).
5. **Tracing people who changed their names is supported; exposing them is not.** *(Reworded 28 Oct 2026; the earlier text, "no support … for searches for people who changed their names", read as if such people could not be traced.)* A person may change name to escape a trafficker or a persecutor and still want to be found by their family, safely. NameBridge supports that search through the safety layers below. It does **not** support searches whose purpose is to expose or verify a person's identity against their will: identity-verification or citizenship-revocation campaigns, or locating alleged perpetrators. Those belong to courts and police, with their own legal means (`SCOPE.md` §2). *Confirmed by the professor on 28 Oct 2026 (G5, option A).*
6. **The intake guide records the names a person chooses to give**, in any order, plus "other names used". It never presses for a "real" or close name.
7. **Setting matters in the benchmark.** Records made outside the camp (towns, work, school) carry a higher rate of name change than camp registration records (`BENCHMARK_PROTOCOL.md` §2.3).

## Finding people who changed their names: the safety layers

The goal is that a family **can** find a person who changed name, and that nobody else can use the same path to expose them. The layers below already exist as controls; this section puts them in one place.

| # | Layer | What it stops | Where |
| --- | --- | --- | --- |
| 1 | **Only authorised tracing caseworkers search.** No public search, no governments or police (G2) | A persecutor or campaign running searches directly | C2; `SCOPE.md` §2; T3 |
| 2 | **One case at a time, with a purpose and a named requester.** No bulk lists; rate limits | "Run these 55 names" campaigns | C1, C2; T4 |
| 3 | **Every search and every opened field is logged and reviewed** | A caseworker searching for someone without a case | C8, C9; T6 |
| 4 | **"Possible name change" is a protected-person case:** senior caseworker only | Ordinary staff seeing the link between old and new identity | Rule 2; C7; T14 |
| 5 | **No location or contact details shown** because of a match | The requester learning where the person is | C6 |
| 6 | **The person found decides.** They are asked, privately, whether they want contact. If they say no, the requester learns only that no result can be shared | The person being found against their will | RFL guide §7.3.2; rule 2 |
| 7 | **The requester is checked before contact** when there are signs of trafficking or abuse; the requester may be the abuser, even a relative | A trafficker posing as family | M2, T1; trafficking cases handled with a specialised protection actor |
| 8 | **Abuse signals:** one requester searching many unrelated people, or many "possible name change" results | Fishing for hidden people | C9 log review |
| 9 | **The public dictionary holds spelling variants only** (rule 1). It contains no link between an old and an adopted name, so having it does not reveal who changed name to what | Someone with the dictionary unmasking people | Rule 1; T8 |

**Restricted name-change layer: approved with conditions by the professor on 28 Oct 2026 (G5).** It is built only after a sourced pattern set, the week 7 access controls and a legal check. The matcher could find more people if it knew common substitutions (for example which Swahili or Muslim given names Burundian Christians tend to adopt). That would mean links between unrelated names, which rule 1 forbids in the public graph. The proposal: keep such patterns in a **separate, restricted layer** that is never published, never exported (e.g. not in the CPIMS+ synonym lists), and used only inside layers 4–6. Risk: if the layer leaks, it is a guide to unmasking people. Sources for such patterns are also thin today (Tanzania only). **Legal risk:** a Christian → Muslim substitution can reveal religion, sensitive data under Malawi's Act (s. 2, s. 16); see `DPIA.md` (c).

## Open questions

- No study was found of name change **among refugees in Malawi** (in Dzaleka, or among people living outside the camp). The patterns above come from Tanzania and Uganda and are applied by analogy. *Searched again 28 Oct 2026 (Tavily): still none.* The only Malawi evidence is about alleged perpetrators [N6][N7][N9][N10], which is exactly the case rule 5 excludes, so it must not shape the benchmark's name-change rates.
- How often step 1 and step 2 happen is unknown. Both are **varied parameters** in the benchmark, never a single value.

## Sources

- [N1] Duchaj & Ntihirageza, ["Survival by Loss of Identity: The Power of Names among Burundian Refugees in Tanzania"](https://yorkspace.library.yorku.ca/items/9b20b57a-99b6-45b0-a212-95dfe823c88c), *Proceedings of the 23rd International Congress of Onomastic Sciences*, York University, 2009.
- [N2] Malkki, *Purity and Exile*, 1995, pp. 168–169 (Kigoma town vs Mishamo settlement), as summarised in ["Ethnicity and Burundi's Refugees"](https://journals.flvc.org/ASQ/article/download/136391/140951/262982), *African Studies Quarterly*.
- [N3] Daley, ["Undoing Traceable Beginnings"](https://www.berghahnjournals.com/view/journals/migration-and-society/1/1/arms010104.xml), *Migration and Society* 1(1), 2018; [Oxford version](https://ora.ox.ac.uk/objects/uuid:3dc69194-d9db-469f-b179-25ed7fbeaf0e/files/m26e06f9e8dadd209e37449ce8f2a12b6).
- [N4] International Refugee Rights Initiative, [*A Dangerous Impasse: Rwandan Refugees in Uganda*](http://citizenshiprightsafrica.org/wp-content/uploads/2016/08/IRRI_Dangerous-Impasse-Rwandan-refugees-Uganda_2010.pdf), 2010.
- [N5] ["Names are Problems: For Congolese Refugees, for the Humanitarian System, and for Anthropological Writing"](https://americanethnologist.org/online-content/collections/rethinking-pseudonyms-in-ethnography/names-are-problems-for-congolese-refugees-for-the-humanitarian-system-and-for-anthropological-writing), *American Ethnologist* online collection.
- [N6] TRT Afrika, ["Malawi says 55 Rwanda genocide suspects hiding in country after 'changing names'"](https://www.trtafrika.com/english/article/13514666), Jun 2023.
- [N7] VOA, ["Malawi Revokes Dubious Citizenship of Refugees Wanted Abroad"](https://www.voanews.com/a/malawi-revokes-dubious-citizenship-of-refugees-wanted-abroad-/7125615.html), Jun 2023.
- [N9] Nyasa Times, ["Rwandan genocide fugitive … used Malawian passport to evade capture"](https://www.nyasatimes.com/rwandan-genocide-fugitive-kayishema-used-malawian-passport-to-evade-capture), Jun 2023, citing *The New Times* (Kigali). Accessed 28 Oct 2026.
- [N10] Citizenship Rights in Africa Initiative, [republication of the VOA report with the full critic quotes](https://citizenshiprightsafrica.org/malawi-revokes-dubious-citizenship-of-refugees-wanted-abroad), Jun 2023. Accessed 28 Oct 2026.
- [N8] ICRC, [*Restoring Family Links: a guide for National Societies*](https://icrcndresourcecentre.org/wp-content/uploads/2019/06/RESTORINGFAMILY-LINKS-A-GUIDE.pdf), §7.3.2 (the located person decides whether contact details are shared).
