# Solutions — Dzaleka Info Bridge

Draft, 7 Oct 2026, for discussion with the professor. **Revised after a critical review the same day:** the proposal is still a hypothesis, so it now starts with validation. Earlier versions are in the git history. Supporting research: `ONLINE_MICROWORK.md`; situation context: `DZALEKA_SITUATION_RESEARCH.md`.

## In one paragraph

Dzaleka already has good, verified, practical information (hotlines, services, rights, weather) on a platform built by refugees, **Dzaleka Online Services (DOS)**. The evidence suggests it reaches few people in the camp: 3,705 users in all of Malawi in 2025, against ~63,000 residents, and nothing in Kirundi or Kinyarwanda. **Our hypothesis is that a free, open-source "bridge" can carry this information to the channels people actually use (community radio, WhatsApp and printed notices) in the languages they speak.** We start with the clearest documented gap: the essential, rarely-changing information (urgent help, hotlines, scam warnings) translated once into Kirundi and Kinyarwanda and turned into radio spots and printed sheets. In parallel, the PhD-linked research track tests heavy-rain warnings for the camp in "shadow mode". **Nothing is built until people in the camp confirm the need.**

---

## 1. Our starting point

| | |
| --- | --- |
| **Who builds** | Me (with Claude writing much of the code), with the professor supporting |
| **FSF** | Context only |
| **Money** | None. Everything must run on free tools |
| **Presence in the camp** | None. Anything we build must be run and distributed by people already there, **without adding unpaid weekly work to them** |
| **Ambition** | Small but real change inside the camp, open source, replicable, the start of a technology line |

## 2. The problem: what we know and what we don't

### What the evidence shows

| Fact | Source |
| --- | --- |
| DOS has 149 services, a "Get help now" page with free hotlines (GBV 5600, child protection 116), a Rights Navigator, jobs and Met Malawi weather | [services.dzaleka.com](https://services.dzaleka.com), checked 7 Oct 2026 |
| In 2025: 17,952 users, but **only 3,705 in Malawi** and 1,697 returning | [DOS 2025 report](https://services.dzaleka.com/news/2025-digital-performance-report/) |
| Newcomer guides exist in English, French, Swahili and Chichewa. **Nothing is in Kirundi or Kinyarwanda**, the languages of Burundians (22%) and Rwandans (13%) | [DOS languages page](https://services.dzaleka.com/languages) |
| In comparable camps (Kiziba in Rwanda, Bidi Bidi in Uganda), **only about a third of refugees have ever used mobile internet** | [GSMA / UNHCR, 2026](https://www.gsma.com/mobilefordevelopment/blog/the-digital-lives-of-refugees-how-displaced-populations-use-mobile-phones-and-what-gets-in-the-way) |
| **58% of displaced people surveyed fear phone scams**, and 43% fear fake news | [GSMA, 2022](https://www.theresearchpeople.org/trp/digital-worlds) |
| Yetu Community Radio broadcasts inside Dzaleka (17 staff, five or six languages) and was active in 2026 | [DOS Yetu page](https://services.dzaleka.com/yetu-radio); [UNHCR](https://www.unhcr.ca/news/community-radio-fosters-refugee-inclusion-in-malawi/) |

### What we don't know (and must ask before building)

- **Whether information is actually missing.** Low website traffic does not prove people lack the information. They may get it through DOS's Facebook page, WhatsApp groups, churches, block leaders or UNHCR. **We have not spoken to a single resident.**
- **Whether Yetu Radio already reads DOS or UNHCR notices.** If it does, a weekly script adds little.
- **Whether there is enough new content every week.** DOS lists 18 jobs and 26 events in total, and many jobs are in Lilongwe or need a work permit refugees can't get. A weekly bulletin could run dry.
- **Who would do the human work** (reviewing translations, printing, sharing) and whether they have time without pay.

## 3. The proposal, in steps

```
Step 0  VALIDATE ─── ask DOS, Yetu Radio, TakenoLAB; get ethics approval
   │
   ├── Step 1  ESSENTIALS IN EVERY LANGUAGE  (main line, starts if Step 0 confirms)
   │             fixed content → radio spots + A4 sheets + WhatsApp cards
   │
   ├── Step 2  WEEKLY / MONTHLY DIGEST       (only if Step 0 shows it's needed)
   │
   └── Research track  HEAVY-RAIN WARNINGS, SHADOW MODE  (PhD-linked, runs in parallel)
```

### Step 0 — Validate (before any code)

**Three questions for Dzaleka Connect, Yetu Radio and TakenoLAB:**
1. How do residents get practical information today (radio, WhatsApp, churches, leaders, UNHCR)?
2. What information is missing or arrives too late, and in which languages?
3. Does Yetu Radio already air DOS or UNHCR notices? Would it air short recorded spots?

**Ethics:** any conversation with residents, collection of questions, or impact assessment is research with vulnerable people. **Ask the professor about ethics approval from the university now**, before any contact that gathers information from residents.

**Outcome:** a short note recording the answers. It decides whether Step 1, Step 2 or neither goes ahead.

### Step 1 — Essentials in every language (main line)

| | |
| --- | --- |
| **What** | The information that **rarely changes** and matters most: urgent help, the hotlines (5600, 116, police), where to go for protection, health and legal aid, and how to recognise a scam (never pay for a job or resettlement). **Translated once** into Kirundi and Kinyarwanda, and into Swahili and French where DOS has no version yet. |
| **Formats** | **Radio spots** (30–60 seconds, recorded once and replayed), **A4 sheets** to print for churches, schools and community centres, and **WhatsApp image cards**. All generated from one source file, so an update changes every format at once. |
| **Why this first** | It is the **only gap that is documented** (no Kirundi or Kinyarwanda), it needs **no weekly work** from anyone, and it reaches people without smartphones. |
| **Translation** | By humans: Kirundi is poorly served by machine translation ([CLEAR Global](https://clearglobal.org/translators-without-borders)). Possible volunteers: TakenoLAB or DOS contacts, Translators without Borders, the diaspora. A machine draft can help, but a person must check it. |
| **What we build** | A small open-source tool: one content file per language → radio script, print-ready PDF and image cards. Contributed to DOS if they want it. |
| **What changes** | Burundian and Rwandan residents, and those without internet, hear and see where to get help in their own language. |
| **Cost** | Zero for us. Printing costs paper: who pays is a question for Step 0. |

### Step 2 — Digest of what's new (only if Step 0 confirms)

A tool that reads DOS's public API and produces a short radio script, WhatsApp text and an A4 sheet of **what's new**: deadlines, events, notices and alerts. **Monthly by default**, weekly only if there is enough new content and someone has time to review it. Swahili and French first.

**Condition to start:** Step 0 shows that the information is missing and the radio doesn't already cover it.

### Research track — Heavy-rain warnings, shadow mode (PhD-linked)

| | |
| --- | --- |
| **What it is, honestly** | The Met Malawi forecast covers the **whole area, not individual zones**. The tool combines "heavy rain is forecast" with a **fixed map of the zones most at risk** of house collapse, from the 2021 flood model. In other words: *heavy rain expected → these zones are the most exposed.* |
| **Evidence** | Friedman (2021, Virginia Tech) modelled Dzaleka from 3.5 cm drone imagery. Erosion patterns predicted where houses collapsed, with misclassification below 17% ([thesis](https://vtechworks.lib.vt.edu/items/fabeecfe-edd2-4db0-8d9d-235f327d3c2c)). Cox's Bazar runs rainfall-threshold alerts delivered by refugee volunteers ([UNDP Bangladesh](https://www.undp.org/bangladesh/stories/until-everyone-safe-early-warning-systems-strengthening-safety-and-resilience-coxs-bazar)). |
| **Shadow mode, 2026–27 season** | The tool computes warnings **without publishing them**, and they are compared with what actually happened. |
| **What it needs** | **Ground truth:** reports of where houses collapsed after heavy rain. This also depends on people in the camp (DOS alerts, news, a local contact), so it is a Step 0 question too. |
| **Limits** | The 2021 model predates the camp's growth (from ~43,000 to ~63,000 people), and a false alarm would destroy trust. Nothing is published until a full season of testing. |
| **Research value** | High, even if the warnings never go live: it tests whether a low-cost risk model plus a public forecast could support evacuation decisions in a data-poor camp. This is the PhD's question. |

### Content to add later

- **"Online work that really pays"**: one sheet and one radio spot on which platforms have actually paid people in Dzaleka, the payout route, the exchange-rate loss and scam warnings. It becomes part of Step 1's content once residents supply the facts. Research: `ONLINE_MICROWORK.md`.

### Removed from this version

- **Questions and rumours loop.** Internews runs this with paid staff who collect, check and answer rumours ([Internews](https://internews.org/areas-of-expertise/humanitarian/approaches/rumour-tracking)). We cannot do that, and it would put unpaid work on people in the camp. It could come back later if a local partner wants to own it.

## 4. What we learned from similar projects

| Project | What it does | Lesson for us |
| --- | --- | --- |
| **ConnectRefugee**, Nakivale, Uganda ([Campus Digital Hub](https://campusdigitalhub.org/connectrefugee-story)) | An app built by refugees where NGOs post verified announcements in five languages, readable offline | Closest example to ours. Its value is **one trusted source**. It needs a smartphone, so we add radio and paper. |
| **Signpost**, IRC ([IRC](https://www.rescue.org/uk/press-release/irc-signpost-project-eu-prize-humanitarian-innovation)) | Information through Facebook, web and chat, in local languages | Use the channels people already use. |
| **Internews rumour tracking** ([Internews](https://internews.org/areas-of-expertise/humanitarian/approaches/rumour-tracking)) | Maps rumours and answers them through local media | Valuable, but needs paid staff: removed for now. |
| **Hello Hubs**, Rhino Camp, Uganda ([Internet Society, May 2026](https://www.internetsociety.org/wp-content/uploads/2026/06/Rhino-Camp-Report-EN.pdf)) | Community-owned internet hubs with an elected committee and local trainers | Lasting projects have **local owners with clear roles**, which is why Step 0 comes first. |
| **Cox's Bazar early warning** ([UNDP](https://www.undp.org/bangladesh/stories/until-everyone-safe-early-warning-systems-strengthening-safety-and-resilience-coxs-bazar)) | Rainfall thresholds, alerts passed on by 3,400 refugee volunteers | Basis for the research track; the last mile is human. |
| **"Digital litter"** ([Migration Policy Institute](https://www.migrationpolicy.org/article/digital-litter-downside-using-technology-help-refugees)) | Most of 169 refugee apps from 2015–16 were dead by 2018 | Don't build a new app; build into what exists, with local owners. |
| **Connectivity for Refugees** (UNHCR, ITU, GSMA; [refugeeconnectivity.org](https://refugeeconnectivity.org/)) | Networks, devices and affordability in 11 countries (**not Malawi**) | That level needs money and governments. Ours is the content and channels layer on top. |

## 5. Why not the other ideas

| Idea | Why not now |
| --- | --- |
| A new app for refugees | Most die; few residents have smartphones with data; DOS already exists |
| Paid pilots (cash, remote-work programmes, farming) | No funding |
| Tools for FSF (medicine stock planner, clinic translation) | FSF gives context only, not a user |
| A help directory | DOS already has one |
| Advocacy tools, awareness games | Useful outside the camp, little change inside it |
| Offline servers, devices, community currency, collective buying | Need hardware money, an operator in the camp, or carry legal risk |

## 6. Risks and what we do about them

| Risk | Response |
| --- | --- |
| **The need isn't real** (people already get the information) | Step 0 before any code. If the answer is no, we stop and record why |
| **We add unpaid work to people in the camp** | Start with fixed content (Step 1) that is translated once; the digest only if someone has time; keep printing optional |
| DOS or Yetu Radio don't want it | Ask first. Without them, print and WhatsApp through churches and leaders still work, with less reach |
| Bad translations or wrong information | Human translation and review; every item cites its source |
| Research ethics | University ethics approval before gathering anything from residents |
| One-person dependency (DOS has one main developer; we are two) | Open code, simple design, documentation |
| False rain alerts | A full season in shadow mode before anything is published |
| Sensitive topics (protection, legal status, online-work grey area) | No personal data collected; legal wording checked with Inua Advocacy or a legal partner |

## 7. Roadmap

| Phase | When (realistic) | What | Done when |
| --- | --- | --- | --- |
| **0. Validate** | Oct–Dec 2026 | Talk with the professor (and about ethics). Contact Dzaleka Connect (dzalekaconnect@gmail.com), and through them or FSF, Yetu Radio and TakenoLAB. Ask the three questions | A written note with the answers, and a go / no-go decision |
| **Research track: shadow mode** | Dec 2026 – Apr 2027 | Rebuild the 2021 risk map against current OSM data, compute warnings during the rains, compare with real events | We know whether the warnings would have been right |
| **1. Essentials** | After a "go" in Step 0 | Content file + Kirundi/Kinyarwanda translations → radio spots, A4 sheets, WhatsApp cards | Spots aired and sheets in use |
| **2. Digest** | Only if Step 0 shows it's needed | Monthly digest from the DOS API | Several issues published and aired |
| **Later** | 2027 | "Online work that really pays" content | Published, with facts from residents |

**How we will know it worked:**
- Step 1: spots aired, sheets in use, and feedback through the radio or DOS.
- Step 2: DOS analytics (visits from Malawi, Facebook referrals) before and after.
- Research track: warnings compared with recorded house collapses.

## 8. Open questions

- What share of Dzaleka residents have a radio, a phone, or WhatsApp? (No Dzaleka figure found.)
- Does Yetu Radio broadcast in Kirundi? Sources disagree.
- Who could translate into Kirundi and Kinyarwanda, and who pays for printing?
- Is the 2021 drone imagery openly available, and under what licence?
- Who could report house collapses during the rains, for ground truth?
- Does DOS's code licence allow contributions to be reused in other camps?

---

## Sources

All linked inline. Consulted 7 Oct 2026 through Tavily and web search. Earlier context and figures: `DZALEKA_SITUATION_RESEARCH.md`, `ONLINE_MICROWORK.md`, `RESEARCH_LOG.md`.
