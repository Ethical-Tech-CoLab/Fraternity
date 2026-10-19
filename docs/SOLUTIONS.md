# Solutions — Dzaleka

Draft, 15 Oct 2026, for discussion with Professor Yorke Rhodes. Earlier versions are in the git history.

## 1. The ideas at a glance

These are some ideas for what we could do, grouped by path. None has been selected. Each is explained one by one below.

| # | Idea | Path | Feasibility | How it changes reality | Main blocker |
| --- | --- | --- | --- | --- | --- |
| 1A | Evidence for the Refugee Bill | **1. Structural lever: the law** | **High** (desk research) | **Largest potential:** right to work and to live outside the camp for tens of thousands. Indirect and uncertain | Others must use it; Cabinet must act |
| 1B | Legislative tracker + "proposed vs in force" explainer | **1. Structural lever: the law** | **Very high** | Prevents false hope, rumours and scams around the bill | Full bill text |
| 1C | Implementation monitoring | **1. Structural lever: the law** | High, once the law passes | Checks that the law is applied in practice | The law must pass first |
| 1D | Eligibility guide | **1. Structural lever: the law** | Low for now | Helps people use new rights | Law, commencement and regulations (2027 or later) |
| 2A | Rain warnings in shadow mode | **2. Small, real, research** | High | Research now; possibly safer evacuation later | Ground truth; rains from mid-Dec |
| 2B | Open map data (OSM) | **2. Small, real, research** | **Very high** | Indirect: a base for planning, 2A and 2E | None to start |
| 2C | Essentials translated into Kirundi / Kinyarwanda | **2. Small, real, research** | High to build; prototype only | Direct but marginal: help reaches those excluded by language | Human translation; no one to distribute it |
| 2D | Guided keyword chatbot | **2. Small, real, research** | High to build; prototype only | Direct but marginal: answers in the user's language, 24/7 | Content maintenance; no one to run it locally |
| 2E | Live map: service status, then environmental hazards | **2. Small, real, research** | Medium; prototype only | Direct: "is it working today?"; hazard reports feed 2A | Critical mass of users |
| 2F | Open Great Lakes Names: open dictionary, matching module and intake guide for family tracing | **2. Small, real, research** | **High** (remote, technical, measurable) | Indirect but real: more true matches on platforms that already serve millions (REFUNITE: 1M+ registrations); the open dictionary is usable even without adoption | Adoption; dual use |

**The two paths**
1. **The structural lever.** The draft Refugee Bill is the only thing in sight that would change life for most residents.
2. **Small and real.** These help at the margins, and each is also a research output.

**Proposed focus:** 1A as the main line, with 1B, 2A and 2F in parallel.

---

## 2. Path 1 — The structural lever: the Refugee Bill

On 9 Oct 2026 the Special Law Commission presented a draft Refugees (Protection and Management) Bill. Refugees could apply to live outside the camp, work, run small businesses and appeal to the courts. It is **not law**: it still needs Cabinet and Parliament, the earliest realistic vote is 2027, and law-reform bills in Malawi have stalled for years (details and sources: `DZALEKA_SITUATION_RESEARCH.md` §2.1). We cannot pass it, but we can produce evidence relevant to it. MHRC urged Cabinet to fast-track it on 13 Oct, and Inua Advocacy is campaigning for it.

### 1A. Evidence for the bill

| Product | Question it answers | Basis |
| --- | --- | --- |
| Comparative brief | What happened when Kenya (Refugees Act 2021), Uganda and Zambia gave refugees the right to work or to live outside camps? | Case files (`docs/cases/`), published evaluations |
| Cost brief | What does keeping Dzaleka closed cost Malawi, compared with partial integration? | WFP / UNHCR funding data (situation research). The Homeland Security Minister said in July 2026 that the current model "may no longer be sustainable" |
| Checklist scoring | How does the bill score against Inua Advocacy's 7-point checklist? | Full bill text (to obtain) |

- **How it changes reality:** if the bill passes and is applied, tens of thousands gain the right to work and to apply to live outside the camp. The effect is indirect and uncertain.
- **Risk:** it is close to advocacy. Keep it to neutral, sourced analysis under the academic project's name.

### 1B. Legislative tracker and explainer

- **What:** a public page with each step (Cabinet, Gazette, readings, assent, commencement) and its source, plus a plain-language explainer of what is **proposed** and what is **in force**.
- **How it changes reality:** prevents false hope and scams such as "pay to get on the list".
- **Effort:** low; it changes only at legislative steps.

### 1C. Implementation monitoring

- **What:** once the law is in force, check whether the Eligibility Committee works, and whether "valid reasons" and "designated areas" are read narrowly.
- **Why:** the Kenya case shows that a law and its practice can diverge.

### 1D. Eligibility guide

- **What:** who can apply to live outside the camp or to work, how, where and with which documents.
- **When:** only after commencement and the regulations. Until then it stays a template.

**If the bill stalls or dies:** stop 1C–1D, keep 1B at minimal effort, and keep 1A for any later reform. Proposed checkpoint: if the bill has not reached Cabinet by the end of the 2027 budget meeting, reassess.

---

## 3. Path 2 — Small, real, and research

### 2A. Rain warnings in shadow mode

- **What:** "heavy rain forecast" (Met Malawi's public CAP feed, district-level) combined with a fixed map of the zones most exposed to house collapse, from Friedman (2021, Virginia Tech; drone model, misclassification below 17%; [thesis](https://vtechworks.lib.vt.edu/items/fabeecfe-edd2-4db0-8d9d-235f327d3c2c)).
- **Shadow mode, Dec 2026 – Apr 2027:** warnings are computed but not published, then compared with what happened.
- **Needs:** ground truth (where houses collapsed), from public reports and news. The 2021 model predates the camp's growth from ~43,000 to ~63,000 people.
- **How it changes reality:** not yet. It tests whether a low-cost model plus a public forecast could support evacuation decisions in a data-poor camp. Nothing goes live without a full season of testing.

### 2B. Open map data (OSM)

- **What:** improve and analyse OpenStreetMap data for Dzaleka (paths, drainage, services).
- **Status (14 Oct 2026):** OSM has the site, hospital, health centre and market; the HOT Tasking Manager has no Dzaleka project; building and path completeness is not yet measured.
- **Safeguard:** no layers that could identify vulnerable groups or sensitive sites.

### Principles shared by 2C, 2D and 2E

- **Build on DOS, do not duplicate it.** The refugee-led Dzaleka Online Services already has a Rights Navigator on the rules in force (in English, on the web) and a map of 99 places. Our contribution: **languages** (Kirundi, Kinyarwanda, Swahili, French), **formats** (radio script, A4, WhatsApp) and **live status**.
- **One content file → every format**, with a status label (**IN FORCE** / **PROPOSED – NOT LAW**) and a "last checked" date on every item.
- **Prototypes only.** With no one in the camp to distribute, review or run them, these tools stay research prototypes on test content and are not offered to residents.

### 2C. Essentials translated

- **What:** urgent help, hotlines (GBV 5600, child protection 116), legal aid, and scam warnings, translated into Kirundi and Kinyarwanda, as radio scripts, A4 sheets and WhatsApp cards.
- **Why:** it is the only documented gap. DOS has nothing in those languages, and Burundians and Rwandans are 35% of residents.
- **Limits:** human translation (machine translation is weak for Kirundi).
- **Later content:** "Online work that really pays" (`ONLINE_MICROWORK.md`), which becomes more relevant if the right to work passes.

### 2D. Guided keyword chatbot

- **What:** the user types or picks a topic; the bot answers from verified content, showing 2–3 options. Every answer carries its status label, its date and a referral line (e.g. Inua Advocacy's public number).
- **Not an open AI chat**, because of:
  - legal risk;
  - Signpost's finding that AI is "not safe without a human in the loop" ([Signpost AI](https://www.signpostai.org/insights/executive-summary-signpost-ai-information-assistant-pilot-program));
  - WhatsApp Business's ban on general-purpose AI bots since 15 Jan 2026.
- **Safeguards:** no stored queries linked to phone numbers; the bot says it never charges.
- **Models:**
  - Signpost (IRC and Mercy Corps; not in Malawi);
  - ALMA (IRC: WhatsApp, no legal advice);
  - Mona (IRAP: information plus referral);
  - La Chama (UNHCR: counters misinformation).

### 2E. Live map (Waze-like)

- **What:** anonymous reports, shown on the map by frequency and removed when users stop confirming them.
  - **Phase 1, service status:** a water point is working, the clinic is open, a distribution has started.
  - **Phase 2, environmental hazards:** a flooded path, erosion, a collapsed latrine. These would also provide ground truth for 2A.
- **Excluded:** reports about people (crime, "dangerous places", violence). They bring stigma, retaliation and manipulation between communities, and they can expose survivors. Protection hotlines are shown instead.
- **Safeguards:** zones, not GPS points; delayed publication.
- **Main risk:** too few users means an empty map.

### 2F. Open Great Lakes Names: matching names for family tracing

**In one sentence:** an open dictionary, plus optional tools, that tells family-tracing services when two differently written records are probably the same person, for names from Burundi, Rwanda and the DRC.

**Why it matters.** Family separation is large and growing. No source counts separated families directly, but every proxy is rising:
- **284,400** people were registered as missing with the Red Cross Family Links Network at the end of 2024, **+68% since 2019**;
- in 2025 the network received **178,329 new tracing requests**;
- in Africa, registered missing rose **75%** from 2019 to mid-2024 (40,708 → 71,000+), and Africa has the most unaccompanied children registered by the ICRC;
- UNHCR registered **218,000 unaccompanied and separated children** in 2024;
- the 2025 Kivu fighting caused new family separations among Congolese fleeing to Burundi, Rwanda and Uganda;
- in Dzaleka, 67 unaccompanied children were registered in Dec 2025.

Sources, divergent counts and gaps: `DZALEKA_SITUATION_RESEARCH.md` §5.2 ("Family separation in displacement").

**Why a module and not a platform.** Family tracing for Dzaleka already exists, so a new platform is not the answer (see "Set aside"):
- **REFUNITE** (refunite.org): anonymous profiles searched by name, birthplace, tribe or clan, mother's name and other markers; private messages when a match is found. It claims 1M+ registrations and 75,000+ families reconnected. It lists Malawi, the DRC, Burundi and Rwanda among its countries. The search site m.refunite.org was live on 15 Oct 2026, and the [EUAA 2025 family-tracing guide](https://www.euaa.europa.eu/sites/default/files/publications/2025-11/practical-guide-family-tracing-part-i-principles-practices.pdf) recommends it.
- **Red Cross Restoring Family Links:** works inside Dzaleka (calls, Wi-Fi, tracing, unaccompanied children) ([Dzaleka Online, Mar 2025](https://www.dzaleka.com/2025/03/red-cross-program-reunites-refugees.html)).
- **ICRC Trace the Face:** a photo gallery with a southern Africa version ([ICRC](https://www.icrc.org/en/document/southern-africa-website-launched-help-families-find-missing-relatives)).

These searches rely on names, and Great Lakes names defeat ordinary matching. Examples below are illustrative:

| Problem | Example |
| --- | --- |
| No family surname: in Rwanda and Burundi each child gets a personal name, often a phrase ("Habimana": "it is God who gives"); siblings share no name | Searching for a sister by "surname" fails |
| Name order varies; DRC names follow nom + postnom + prénom (from the 1970s *authenticité* policy), which Western forms misplace | "Habimana Jean" vs "Jean Habimana"; "Kasongo Ilunga Jean" |
| One name, several spellings | Kinyarwanda "Cyiza", Kirundi "Ciza", English-style "Chiza"; "Ndayishimiye" vs "Ndayishimye" |
| Christian names change with language | Jean / John / Yohana; Marie / Mary / Maria |
| Place names change | Burundi's 2025 province reform (Muyinga now in Buhumuza province, [SOS Médias Burundi](https://www.sosmediasburundi.org/en/2026/10/09/dzaleka-suspicious-death-of-a-burundian-refugee-after-a-collision-with-police-more-than-2-million-kwacha-missing)); Rwanda's 2006 reform; the DRC's 2015 change from 11 to 26 provinces |

REFUNITE has adapted its fields for other regions ("clan" for Somalis, "mother's name" for Iraqis; [Refunite](https://refunite.org/whats-name-four-names)). No equivalent for the Great Lakes region was found. Its interface has 12 languages, none of them Kirundi, Kinyarwanda, Lingala or Chichewa (m.refunite.org, checked 15 Oct 2026).

#### Four deliverables

| # | Deliverable | What it is | Useful without adoption? |
| --- | --- | --- | --- |
| 1 | **Open dictionary** (the core) | Open data files (CSV / JSON, CC BY 4.0) that any team can use, even by hand | **Yes** |
| 2 | **Matching module** (optional) | Open-source Python code that applies the dictionary and scores possible matches | Partly (as published code) |
| 3 | **Intake guide** | Which questions to ask when someone registers a search, so a Great Lakes person can be found | **Yes** |
| 4 | **Evaluation report** | How much better matching gets, measured on synthetic data | **Yes** (research output) |

**Why the dictionary is the core:** a module needs a platform to integrate our code; a dictionary can be used by any team in any system. If no one adopts the module, the dictionary still stands on its own.

#### 1. Open dictionary

| Part | Example | Possible source |
| --- | --- | --- |
| Spelling variants | Cyiza = Ciza = Chiza | Onomastic literature; public name lists |
| Christian-name equivalents | Jean = John = Yohana; Marie = Mary = Maria | Public sources |
| Orthographic rules | "cy" and "c" ≈ "ch"; "-iye" ≈ "-ye" | Kirundi and Kinyarwanda grammars |
| Places, old and new names | Muyinga → Buhumuza province (Burundi, 2025); Rwanda 2006; DRC 2015 | Official administrative boundaries on HDX (OCHA common operational datasets) |

**It contains names as vocabulary, never records of people:** it says that "Ciza" and "Cyiza" are the same name, not that a given person lives anywhere. This greatly reduces the dual-use risk.

#### 2. Matching module (five layers)

1. **Normalise:** remove accents and hyphens; split names into parts.
2. **Ignore order:** treat a name as a set of parts, not "first + last".
3. **Regional spelling rules,** with a phonetic key designed for these languages (Soundex and similar keys are built for English).
4. **Dictionary lookups:** Christian names; old and new place names.
5. **Score and explain:** combine name similarity with age range, birthplace and parents' names; return ranked **possible** matches with the reason.

#### 3. Intake guide (for tracing services)

A supplement to existing tracing forms (e.g. the Red Cross's), in the spirit of REFUNITE adding "clan" for Somalis.

| Ask | Why |
| --- | --- |
| **All names, in any order**, including the Christian name and, for the DRC, the postnom | Order and naming systems vary |
| Father's and mother's names | There is no shared family surname |
| The **hill (colline)** of origin, the parish and the school | The colline is the smallest locality unit in Rwanda and Burundi |
| The province name **as it was at the time**, and approximate dates | Provinces were renamed in 2006, 2015 and 2025 |

**Never ask:** ethnicity (Hutu / Tutsi) or clan. In the region these have been used to persecute and kill, and asking about ethnicity is legally sensitive in Rwanda.

**Delivery:** published openly, so any tracing service (Red Cross, REFUNITE, UNHCR) can use it. Offering it directly to an organisation is the **final phase** (see Steps).

#### 4. Evaluation (synthetic data only)

- **Synthetic test set:** invented people with typical regional names, then deliberately corrupted with realistic errors (swapped order, variant spelling, translated Christian name, renamed province).
- **Comparison of three methods:** exact search; generic fuzzy search (roughly what platforms do now); the dictionary plus module.
- **Measures:** true matches found (recall, and recall in the top 10 results); false matches shown (precision); false-match rate at the suggestion threshold. Reported per language, never only as a global average, and name-only search measured separately from search with age, place and parents' names.
- **Test set rules:** include hard negatives (different people with common names); keep all records of one invented person or family on the same side of any split.
- **No real refugee data is ever used.**

#### Languages: one "pack" per language

Each language becomes a pack of rules, dictionary entries and a synthetic test set, built the same way.

| Phase | Languages | Why |
| --- | --- | --- |
| **1** | Kirundi, Kinyarwanda, Congolese Swahili | The main languages in Dzaleka |
| **2** | Lingala, Mashi and other eastern DRC languages | Completes the DRC group (65% of residents) |
| **3** | Other Latin-script African languages (e.g. Somali, South Sudanese languages) | Regions where REFUNITE works |
| **Not for now** | Arabic, Amharic, Tigrinya | Transliteration from other scripts is a different, harder problem, with existing work on Arabic names |

Each language takes a few weeks of literature research. Ideally, a native-speaker linguist or translator reviews each pack.

#### What 2F takes from NameBridge

`CONCEPT-IDEA.md` ("NameBridge", 19 Oct 2026) analyses a full cross-border missing-person system. 2F is a small, open subset of it. Decided 19 Oct 2026:

| Adopted | How it applies to 2F |
| --- | --- |
| **Every dictionary entry is sourced and typed** (§5.1A) | Each entry records: relation type (spelling variant, Christian-name equivalent, orthographic rule, renamed place, historical cognate), language, region, period, source, confidence, how the confidence was set (attested / expert / generated / disputed) and review status (proposed / reviewed) |
| **Generated entries never become authoritative on their own** | Anything suggested by an AI or a rule enters as `proposed` until a source is found |
| **"Not the same name" entries** | Pairs that look alike but are different names are recorded too, to cut false matches |
| **Etymology is not an alias** (§2.1) | Historical cognates get a low weight and only widen a search; they never count as a match |
| **Never overwrite the original name** (§5.3) | The module keeps the name exactly as written and adds variants alongside it, logging how each was produced, so every suggested match shows its reason |
| **Language-pack format** (§11) | Each pack (Kirundi, Kinyarwanda, Congolese Swahili …) follows that format, including what a shared or different name says about kinship, and allows "unknown" or "disputed" instead of forcing a rule |
| **Burundi as an open question** (§2.3) | Whether Burundian siblings share a name is not assumed from the Rwandan case; it stays an evidence gap until a source settles it |
| **Metrics** (§9.2–9.3) | See "Evaluation" above |
| **Splink** (§5.6) | Optional third comparison in the evaluation |
| **Candidate sources to review** (§7) | Onomaverse (CC BY 4.0) and Wikidata aliases, used only after checking their provenance, coverage and licence |

| Not adopted | Why |
| --- | --- |
| Protected graph of people, cases and relatives (§5.1B) | 2F holds no records of people |
| Human review interface, shadow pilot with an organisation, live deployment (§10 phases 3–4) | Needs a partner and real cases; outside the current constraints |
| Benchmark on real error patterns (§9.1) | Synthetic data only; the report states this limit |
| Federated or privacy-preserving linkage between organisations; biometrics | Only relevant to a live system |
| Advisory group and review panel (§10 phase 0) | Needs outside people; native-speaker review stays "ideally", as above |

#### Risks and safeguards

| Risk | Safeguard |
| --- | --- |
| **Dual use:** better person-finding also helps persecutors | The dictionary holds names as vocabulary, never records of people; the module is published with no data and recommended only for consent-based platforms with mutual matching; no search over public data |
| Sensitive fields in the intake guide | Ethnicity and clan excluded |
| False positives (false hope, contact with a stranger) | Only possible matches are suggested; the user confirms, e.g. with questions only family can answer |
| Synthetic results may not hold on real records | State this limit clearly; native-speaker review of the rules |
| No one adopts it | The dictionary, guide and report are published openly and stand on their own |

#### Steps (phase 1, about 2–3 months, no cost)

| Step | What | Time |
| --- | --- | --- |
| 1. Linguistic research | Naming conventions in Rwanda, Burundi and the DRC; orthography; province reforms (literature only) | 2–3 weeks |
| 2. Dictionary and intake guide | First version of the open data files; the guide | 2 weeks |
| 3. Synthetic data and module | Generator of people and realistic errors; Python module | 3–4 weeks |
| 4. Evaluate and write up | Comparison with the two baselines; report | 2 weeks |
| Later | Phase 2 and 3 language packs | A few weeks per language |
| **Final phase (decided later)** | Whether to offer the dictionary, module and guide directly to REFUNITE, the Red Cross or UNHCR | After the evaluation |

**Build first, decide on delivery later.** Nothing in steps 1–4 depends on any organisation agreeing: the dictionary, guide and report are published openly and stand on their own (the plan B). Whether to offer them directly is decided at the end, with a tested result in hand. It would be a one-off offer to an organisation, not a partnership, and not contact with residents.

**Why it stands out:** it is the only idea here where our technical work improves something that already serves over a million people, instead of creating a new tool that may never find users. It fits the constraints: remote, technical, measurable, and needs no contact with residents.

---

## 4. Set aside

| Idea | Why |
| --- | --- |
| Reporting to organisations | Nobody to receive and act on reports |
| Household needs assessment | High privacy and ethics risk; duplicates UNHCR surveys |
| Live-map alerts about people or "dangerous places" | Exposes the people at the marked places; open to manipulation |
| A new standalone app; weekly digest; rumour loop | Digital litter; thin content; needs paid staff |
| A new family-tracing platform with mutual matching | REFUNITE and the Red Cross already do this; a new platform would split users (a match needs both people on the same platform); a database of names and relatives of DRC, Burundian and Rwandan refugees is a target for persecutors; no human verification. 2F improves the existing platforms instead |
| Paid pilots, devices, offline servers | Need money or an operator in the camp |

## 5. Cross-cutting risks

| Risk | Response |
| --- | --- |
| "Proposed" read as "in force" (could lead to arrest; over 900 people were detained in 2023) | Status label and date on every item; never mix proposed and in-force content |
| Outdated or wrong information | Expiry dates; human translation; every item cites its source |
| Political sensitivity | Neutral, official-source content under the academic project's name |
| Privacy | No personal data; no stored queries |

## 6. Context

**Why these paths:** what weighs most on life in Dzaleka is food (about $8 per person per month since Sept 2026), the encampment rule, the ban on work, and the lack of any way out. Information tools only help at the margins. With no money and no presence in the camp, nothing we build will change these structurally.

| Starting point | |
| --- | --- |
| Who builds | Me (with Claude writing much of the code), with the professor supporting |
| Money | None; free tools only |
| Presence in the camp | None |
| Ambition | Small but real change; open source; replicable |

| Key fact | Source |
| --- | --- |
| DOS (refugee-led): 149 services, hotlines, a map of 99 places, a Rights Navigator on the 1989 Act | [services.dzaleka.com](https://services.dzaleka.com), checked 15 Oct 2026 |
| DOS reach in 2025: 3,705 users in Malawi, against ~63,000 residents | [DOS 2025 report](https://services.dzaleka.com/news/2025-digital-performance-report/) |
| No DOS content in Kirundi or Kinyarwanda (Burundians 22%, Rwandans 13%) | [DOS languages](https://services.dzaleka.com/languages) |
| About a third of refugees in comparable camps have ever used mobile internet | [GSMA / UNHCR, 2026](https://www.gsma.com/mobilefordevelopment/blog/the-digital-lives-of-refugees-how-displaced-populations-use-mobile-phones-and-what-gets-in-the-way) |
| 58% of displaced people surveyed fear phone scams | [GSMA, 2022](https://www.theresearchpeople.org/trp/digital-worlds) |
| Most of 169 refugee apps from 2015–16 were dead by 2018 | [Migration Policy Institute](https://www.migrationpolicy.org/article/digital-litter-downside-using-technology-help-refugees) |
| Most humanitarian chatbots are menus or keyword routing, not machine learning | [Access Now, 2024](https://www.accessnow.org/wp-content/uploads/2024/02/Mapping-humanitarian-tech-February-2024.pdf) |

## 7. Open questions

- The full text of the bill and the Law Commission report.
- Does any legal route out of the camp, or to work, already exist?
- How many residents are recognised refugees and how many are asylum seekers? (Only recognised refugees could apply to live outside the camp.)
- Is the 2021 drone imagery openly available, and under what licence?
- Where is the line between legal information and legal advice under Malawian law?

## Sources

Linked inline. Checked 7–15 Oct 2026 via Tavily, web search, GitHub, HDX, the HOT Tasking Manager, the Met Malawi CAP feed and direct page fetches. Full detail: `DZALEKA_SITUATION_RESEARCH.md`, `ONLINE_MICROWORK.md`, `RESEARCH_LOG.md`.
