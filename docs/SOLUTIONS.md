# Solutions — Dzaleka

Draft, 15 Oct 2026, for discussion with Professor Yorke Rhodes. Earlier versions are in the git history.

## 1. The ideas at a glance

These are some ideas for what we could do, grouped by path. None has been selected. Each is explained one by one below.

| # | Idea | Path | Feasibility | How it changes reality | Main blocker |
| --- | --- | --- | --- | --- | --- |
| 1A | Talk to DOS, Inua Advocacy, Yetu Radio, TakenoLAB and residents | **1. Change a constraint** | **Very high** (an email) | Indirect: it unlocks every idea that needs a partner, and may change this list | Ethics approval before talking to residents |
| 1B | Apply for funding | **1. Change a constraint** | Medium | Indirect: turns zero budget into some budget | Time; competitive calls |
| 2A | Evidence for the Refugee Bill | **2. Structural lever: the law** | **High** (desk research) | **Largest potential:** right to work and to live outside the camp for tens of thousands. Indirect and uncertain | Advocates must use it; Cabinet must act |
| 2B | Legislative tracker + "proposed vs in force" explainer | **2. Structural lever: the law** | **Very high** | Prevents false hope, rumours and scams around the bill | Full bill text |
| 2C | Implementation monitoring | **2. Structural lever: the law** | High, once the law passes | Checks that the law is applied in practice | The law must pass first |
| 2D | Eligibility guide | **2. Structural lever: the law** | Low for now | Helps people use new rights | Law, commencement and regulations (2027 or later) |
| 3A | Rain warnings in shadow mode (PhD) | **3. Small, real, research** | High | Research now; possibly safer evacuation later | Ground truth; rains from mid-Dec |
| 3B | Open map data (OSM) | **3. Small, real, research** | **Very high** | Indirect: a base for planning, 3A and 3E | None to start |
| 3C | Essentials translated into Kirundi / Kinyarwanda | **3. Small, real, research** | High to build, medium to launch | Direct but marginal: help reaches those excluded by language | Translators; a partner |
| 3D | Guided keyword chatbot | **3. Small, real, research** | High to prototype, medium to launch | Direct but marginal: answers in the user's language, 24/7 | A partner; content maintenance |
| 3E | Live map: service status, then environmental hazards | **3. Small, real, research** | Medium | Direct: "is it working today?"; hazard reports feed 3A | Critical mass of users; a partner |

**The three paths**
1. **Change a constraint.** The constraints (no money, no presence, no partner) limit impact more than the ideas do.
2. **The structural lever.** The draft Refugee Bill is the only thing in sight that would change life for most residents.
3. **Small and real.** These help at the margins, and each is also a research output.

**Proposed focus:** 1A immediately, 2A as the main line, 2B and 3A in parallel. 3C–3E follow only if partners ask for them.

---

## 2. Path 1 — Change a constraint

### 1A. Talk to partners and residents

- **What:** contact DOS (dzalekaconnect@gmail.com), Inua Advocacy (info@inuaadvocacy.org; +265 882 717 995), Yetu Radio and TakenoLAB. Later, with ethics approval, residents.
- **Questions:**
  1. How do residents get practical information today, and what is missing, in which languages?
  2. Would evidence on the Refugee Bill be useful to you (2A), and in what form?
  3. Would you review content or receive referrals for the tools in Path 3?
  4. Does a chatbot or live map already exist or exist in plans? (Web search found none, 15 Oct 2026.)
- **Why first:** we have not spoken to a single resident, and every idea that reaches residents needs a local partner to launch.
- **Ethics:** talking to residents is research with vulnerable people. University ethics approval comes first.
- **Done when:** a written note with the answers and a go / no-go for each idea.

### 1B. Apply for funding

- **What:** humanitarian innovation calls such as Elrha's Humanitarian Innovation Fund and MIT Solve (TakenoLAB, in Dzaleka, has applied), plus university and cloud credits for academic projects.
- **Not advertising:** revenue would be negligible, ad networks track users (which breaks anonymity), and ads in camps often push predatory loans, "jobs abroad" (a trafficking lure) and scams.

---

## 3. Path 2 — The structural lever: the Refugee Bill

On 9 Oct 2026 the Special Law Commission presented a draft Refugees (Protection and Management) Bill. Refugees could apply to live outside the camp, work, run small businesses and appeal to the courts. It is **not law**: it still needs Cabinet and Parliament, the earliest realistic vote is 2027, and law-reform bills in Malawi have stalled for years (details and sources: `DZALEKA_SITUATION_RESEARCH.md` §2.1). We cannot pass it, but we can support those pushing it: MHRC urged Cabinet to fast-track it on 13 Oct, and Inua Advocacy is campaigning.

### 2A. Evidence for the bill

| Product | Question it answers | Basis |
| --- | --- | --- |
| Comparative brief | What happened when Kenya (Refugees Act 2021), Uganda and Zambia gave refugees the right to work or to live outside camps? | Case files (`docs/cases/`), published evaluations |
| Cost brief | What does keeping Dzaleka closed cost Malawi, compared with partial integration? | WFP / UNHCR funding data (situation research). The Homeland Security Minister said in July 2026 that the current model "may no longer be sustainable" |
| Checklist scoring | How does the bill score against Inua Advocacy's 7-point checklist? | Full bill text (to obtain) |

- **How it changes reality:** if the bill passes and is applied, tens of thousands gain the right to work and to apply to live outside the camp. The effect is indirect and uncertain.
- **Risk:** it is close to advocacy. Keep it to neutral, sourced analysis under the academic project's name, offered to Inua / MHRC rather than published as a campaign.

### 2B. Legislative tracker and explainer

- **What:** a public page with each step (Cabinet, Gazette, readings, assent, commencement) and its source, plus a plain-language explainer of what is **proposed** and what is **in force**.
- **How it changes reality:** prevents false hope and scams such as "pay to get on the list".
- **Effort:** low; it changes only at legislative steps.

### 2C. Implementation monitoring

- **What:** once the law is in force, check whether the Eligibility Committee works, and whether "valid reasons" and "designated areas" are read narrowly.
- **Why:** the Kenya case shows that a law and its practice can diverge.

### 2D. Eligibility guide

- **What:** who can apply to live outside the camp or to work, how, where and with which documents.
- **When:** only after commencement and the regulations, with a legal partner. Until then it stays a template.

**If the bill stalls or dies:** stop 2C–2D, keep 2B at minimal effort, and keep 2A for any later reform. Proposed checkpoint: if the bill has not reached Cabinet by the end of the 2027 budget meeting, reassess.

---

## 4. Path 3 — Small, real, and research

### 3A. Rain warnings in shadow mode (PhD track)

- **What:** "heavy rain forecast" (Met Malawi's public CAP feed, district-level) combined with a fixed map of the zones most exposed to house collapse, from Friedman (2021, Virginia Tech; drone model, misclassification below 17%; [thesis](https://vtechworks.lib.vt.edu/items/fabeecfe-edd2-4db0-8d9d-235f327d3c2c)).
- **Shadow mode, Dec 2026 – Apr 2027:** warnings are computed but not published, then compared with what happened.
- **Needs:** ground truth (where houses collapsed), which 3E could later provide. The 2021 model predates the camp's growth from ~43,000 to ~63,000 people.
- **How it changes reality:** not yet. It tests whether a low-cost model plus a public forecast could support evacuation decisions in a data-poor camp, which is the PhD question. Nothing goes live without a full season of testing.

### 3B. Open map data (OSM)

- **What:** improve and analyse OpenStreetMap data for Dzaleka (paths, drainage, services).
- **Status (14 Oct 2026):** OSM has the site, hospital, health centre and market; the HOT Tasking Manager has no Dzaleka project; building and path completeness is not yet measured.
- **Safeguard:** no layers that could identify vulnerable groups or sensitive sites.

### Principles shared by 3C, 3D and 3E

- **Build on DOS, do not duplicate it.** The Rights Navigator already covers the rules in force (in English, on the web), and the DOS map already lists 99 places. Our contribution: **languages** (Kirundi, Kinyarwanda, Swahili, French), **channels** (radio, A4, WhatsApp) and **live status**.
- **One content file → every format**, with a status label (**IN FORCE** / **PROPOSED – NOT LAW**) and a "last checked" date on every item.
- **A local partner is a launch condition, not a start condition.** Without one, the tools stay research prototypes on test content.

### 3C. Essentials translated

- **What:** urgent help, hotlines (GBV 5600, child protection 116), legal aid, and scam warnings, translated once into Kirundi and Kinyarwanda. Delivered as radio spots, A4 sheets and WhatsApp cards.
- **Why:** it is the only documented gap. DOS has nothing in those languages, and Burundians and Rwandans are 35% of residents.
- **Limits:** human translation (machine translation is weak for Kirundi); no weekly work.
- **Later content:** "Online work that really pays" (`ONLINE_MICROWORK.md`), which becomes more relevant if the right to work passes.

### 3D. Guided keyword chatbot

- **What:** residents type or pick a topic; the bot answers from verified content, showing 2–3 options. Every answer carries its status label, its date and a referral line (e.g. Inua Advocacy).
- **Not an open AI chat**, because of:
  - legal risk;
  - Signpost's finding that AI is "not safe without a human in the loop" ([Signpost AI](https://www.signpostai.org/insights/executive-summary-signpost-ai-information-assistant-pilot-program));
  - WhatsApp Business's ban on general-purpose AI bots since 15 Jan 2026.
- **Safeguards:** no stored queries linked to phone numbers; one official number; the bot repeats that the service never charges.
- **Models:**
  - Signpost (IRC and Mercy Corps; not in Malawi);
  - ALMA (IRC: WhatsApp, no legal advice);
  - Mona (IRAP: information plus referral);
  - La Chama (UNHCR: counters misinformation).

### 3E. Live map (Waze-like)

- **What:** anonymous reports, shown on the map by frequency and removed when users stop confirming them.
  - **Phase 1, service status:** a water point is working, the clinic is open, a distribution has started.
  - **Phase 2, environmental hazards:** a flooded path, erosion, a collapsed latrine. These also provide ground truth for 3A.
- **Excluded:** reports about people (crime, "dangerous places", violence). They bring stigma, retaliation and manipulation between communities, and they can expose survivors. Protection hotlines are shown instead.
- **Safeguards:** zones, not GPS points; delayed publication; builds on the DOS map.
- **Main risk:** too few users means an empty map. Reports must also come through WhatsApp, and Yetu Radio could read out the alerts.

---

## 5. Set aside

| Idea | Why |
| --- | --- |
| Reporting to organisations | Nobody has been identified to receive and act on reports. 3E replaces it, with residents as the audience |
| Household needs assessment | High privacy and ethics risk; duplicates UNHCR surveys |
| Live-map alerts about people or "dangerous places" | Exposes the people at the marked places; open to manipulation |
| Advertising | See 1B |
| A new standalone app; weekly digest; rumour loop | Digital litter; thin content; needs paid staff |
| Paid pilots (cash, farming), devices, offline servers | Need money or an operator in the camp |

## 6. Cross-cutting risks

| Risk | Response |
| --- | --- |
| The need isn't real | 1A before any launch; if partners and residents say no, stop and record why |
| "Proposed" read as "in force" (could lead to arrest; over 900 people were detained in 2023) | Status label and date on every item; never mix proposed and in-force content |
| Outdated or wrong information | Expiry dates; human translation and review; every item cites its source |
| Political sensitivity | Neutral, official-source content under the academic project's name |
| Research ethics and privacy | University ethics approval; no personal data; no stored queries |
| Unpaid work for people in the camp | Rarely-changing content; no weekly duties without agreement |

## 7. Context

**Why there are three paths:** what weighs most on life in Dzaleka is food (about $8 per person per month since Sept 2026), the encampment rule, the ban on work, and the lack of any way out. Information tools only help at the margins. With no money, no presence in the camp and no partner, nothing we build will change these structurally.

| Starting point | |
| --- | --- |
| Who builds | Me (with Claude writing much of the code), with the professor supporting |
| Money | None; free tools only |
| Presence in the camp | None. Nothing may add unpaid weekly work for people there |
| Partner / residents consulted | None yet; none approached |
| Ambition | Small but real change inside the camp; open source; replicable |

| Key fact | Source |
| --- | --- |
| DOS (refugee-led): 149 services, hotlines, a map of 99 places, a Rights Navigator on the 1989 Act | [services.dzaleka.com](https://services.dzaleka.com), checked 15 Oct 2026 |
| DOS reach in 2025: 3,705 users in Malawi, against ~63,000 residents | [DOS 2025 report](https://services.dzaleka.com/news/2025-digital-performance-report/) |
| No DOS content in Kirundi or Kinyarwanda (Burundians 22%, Rwandans 13%) | [DOS languages](https://services.dzaleka.com/languages) |
| About a third of refugees in comparable camps have ever used mobile internet | [GSMA / UNHCR, 2026](https://www.gsma.com/mobilefordevelopment/blog/the-digital-lives-of-refugees-how-displaced-populations-use-mobile-phones-and-what-gets-in-the-way) |
| 58% of displaced people surveyed fear phone scams | [GSMA, 2022](https://www.theresearchpeople.org/trp/digital-worlds) |
| Most of 169 refugee apps from 2015–16 were dead by 2018 | [Migration Policy Institute](https://www.migrationpolicy.org/article/digital-litter-downside-using-technology-help-refugees) |
| Most humanitarian chatbots are menus or keyword routing, not machine learning | [Access Now, 2024](https://www.accessnow.org/wp-content/uploads/2024/02/Mapping-humanitarian-tech-February-2024.pdf) |

## 8. Open questions

- What share of residents have a radio, a phone or WhatsApp?
- How many residents are recognised refugees and how many are asylum seekers? (Only recognised refugees could apply to live outside the camp.)
- The full text of the bill and report; does any legal route out of the camp or to work already exist?
- Does the UNHCR HELP site for Malawi exist? (help.unhcr.org/malawi returned 403 to automated requests.)
- Is the 2021 drone imagery openly available, and under what licence?
- Where is the line between legal information and legal advice under Malawian law?

## Sources

Linked inline. Checked 7–15 Oct 2026 via Tavily, web search, GitHub, HDX, the HOT Tasking Manager, the Met Malawi CAP feed and direct page fetches. Full detail: `DZALEKA_SITUATION_RESEARCH.md`, `ONLINE_MICROWORK.md`, `RESEARCH_LOG.md`.
