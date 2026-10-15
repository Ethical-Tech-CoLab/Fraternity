# Solutions — Dzaleka Info Bridge

Draft, 7 Oct 2026, for discussion with the professor. **Revised after a critical review the same day:** the proposal is still a hypothesis, so it now starts with validation. Earlier versions are in the git history. Supporting research: `ONLINE_MICROWORK.md`; situation context: `DZALEKA_SITUATION_RESEARCH.md`.

**Update, 14 Oct 2026:** section 9 sets out seven options for discussion with Professor Yorke Rhodes on 15 Oct. No option has been selected; a community reporting platform is the current preference.

**Update, 15 Oct 2026 — the Refugee Bill.** On 9 Oct the Special Law Commission presented a draft Refugees (Protection and Management) Bill. Refugees could apply to live outside the camp, work, and run small businesses (details and sources: `DZALEKA_SITUATION_RESEARCH.md` §2.1). It is **not law yet**: it still needs Cabinet and Parliament. For this document it creates a concrete, time-bound information need: residents will need to know what the bill says, what has *not* changed yet, and how to apply once it passes, in their own languages. That fits option 9.2 and Step 1 (**hypothesis**; to confirm with DOS, Yetu Radio and Inua Advocacy). It also makes the "Online work that really pays" content more relevant if the right to work passes. **Proposal built on this: section 10.**

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

## 9. Options for discussion (14 Oct 2026)

Prepared for the meeting with Professor Yorke Rhodes on 15 Oct 2026. **No option has been selected.** The community reporting platform (9.1) is the current preference, but all seven options stay open for comparison. Sections 1–8 above remain the earlier analysis; options 9.2 and 9.5 overlap with the Info Bridge and the research track.

Labels used below: **Verified** (checked against a source, with date), **Hypothesis** (plausible but untested), **To check** (unknown; needs research or a partner's answer).

### 9.1 Community reporting and problem mapping (current preference)

A simple, mobile-friendly form where residents report non-sensitive community problems (blocked drainage, damaged paths, broken water points, unlit public spaces, flooding), choosing a category, a short description and, optionally, an approximate zone. Moderated reports appear on a map or dashboard that shows recurring problems.

- **Aim (hypothesis):** a channel for residents to make local needs visible and help organisations prioritise.
- **Protection boundary:** reports of violence, including sexual violence, are **out of scope**. Even with blurred locations, timing and context can identify survivors. Such incidents need confidential, survivor-centred referral through specialised services ([WHO, 2007](https://www.who.int/publications/i/item/9789241595681)). The prototype would show referral information (e.g. the GBV 5600 and child-protection 116 hotlines listed by DOS) instead of accepting these reports.
- **Safeguards:** nothing is published automatically; moderation before display; zones rather than GPS points; minimal data; no accounts required; protection against retaliation and false reports.
- **Existing systems (verified 14 Oct 2026):** [Ushahidi](https://github.com/ushahidi/platform) (AGPL, active) maps citizen reports from SMS, web and apps. UNHCR's early-warning platform in the Central African Republic was built on it, with reports verified and cleaned of confidential information before display ([UNHCR](https://data.unhcr.org/ar/news/10189)). [FixMyStreet](https://github.com/mysociety/fixmystreet) (AGPL, active) routes each report to the body responsible for fixing it.
- **Main uncertainty:** the reporting platforms that work have **someone who receives and acts on reports**. We have no presence in the camp, and no responder has been identified. Without one, reports go nowhere and could damage trust. This conflicts with the constraints in section 1, unless a local partner takes on that role.

### 9.2 Multilingual news and community information

AI-assisted translation of announcements that already exist (mainly from DOS), with human review of sensitive content and distribution through WhatsApp, radio and print, plus optional personalisation by language and topic. This is close to the Info Bridge in section 3.

- **Verified:** DOS guides exist in English, French, Swahili and Chichewa, but not in Kirundi or Kinyarwanda (section 2). Kirundi is poorly served by machine translation (section 3, Step 1).
- **Earlier variant:** voluntary family profiles (demographics, health). This variant is **set aside for the prototype** because of privacy concerns, and kept as a possible later research question (see 9.6).
- **Key question:** do residents need a new application, or better access to information that already exists through existing channels? Section 5 records why a new app is risky.

### 9.3 Community emergency and weather alerts

Localised alerts for heavy rain, flooding and heat, inspired by Brazil's Defesa Civil Alerta, run in **simulation or shadow mode only**.

- **Verified (14 Oct 2026):** Malawi's Department of Climate Change and Meteorological Services publishes a public CAP alert feed ([RSS](https://www.metmalawi.gov.mw/api/cap/rss.xml), marked "public domain", latest item 12 Oct 2026). It is listed in the [WMO Register of Alerting Authorities](https://alertingauthority.wmo.int/authorities.php?recId=93). The alerts are written for districts or the whole country, not for zones of the camp.
- **Verified:** Defesa Civil Alerta uses cell broadcast. Alerts reach every 4G/5G phone in an area through the mobile operators, with no sign-up, coordinated by the Ministry of Integration and Regional Development (MIDR) and Anatel; it began in December 2024 ([Metrópoles](https://www.metropoles.com/brasil/alerta-defesa-civil-entenda-como-funciona-o-sistema-cell-broadcast); [Teletime](https://teletime.com.br/29/01/2025/rio-emite-alerta-extremo-pela-primeira-vez-via-cell-broadcast/)). This depends on government and operator infrastructure that we cannot replicate. The **design** (CAP format, area targeting, short standard messages) is what transfers.
- **To check:** whether Malawi has any cell-broadcast capability, and which channels camp residents would receive alerts on.

### 9.4 Open geographic data and community mapping

Review and improve open map data for Dzaleka (roads, drainage, services) on OpenStreetMap, and use it for analysis such as access to services. The aim is to produce or analyse data that supports planning, not to duplicate consumer maps.

- **Verified (14 Oct 2026):** OSM already has the Dzaleka refugee site, hospital, health centre and market ([Nominatim](https://nominatim.openstreetmap.org/search?q=Dzaleka)). A search of the HOT Tasking Manager for "Dzaleka" returned no projects. On HDX, the five Dzaleka datasets are all UNHCR surveys; none is a map layer ([HDX](https://data.humdata.org/search?q=Dzaleka)).
- **To check:** how complete the building and path layers are (not measured; the query service was unavailable), and whether UNHCR or local mappers hold unpublished site maps.
- **Safeguard:** no layers that could identify vulnerable groups or sensitive sites.

### 9.5 Climate risk and exposure analysis

Use satellite imagery, rainfall data, OSM and earlier research to identify zones exposed to flooding, erosion or house collapse, and compare model estimates with past events where validation data exist. This is the research track in section 3.

- **Builds on:** Friedman (2021), which used drone imagery of Dzaleka ([thesis](https://vtechworks.lib.vt.edu/items/fabeecfe-edd2-4db0-8d9d-235f327d3c2c)). The methodology and the availability of its imagery still have to be confirmed.
- **Limit:** a research output, not public warnings, until validated.

### 9.6 Voluntary community needs assessment

An optional, privacy-protected survey of participating households (composition, disability, access to services) producing aggregated insights for advocacy.

- **Concerns:** consent, sensitive data, re-identification in small groups, and a non-representative sample.
- **Verified:** UNHCR already runs household surveys in Dzaleka, e.g. the 2023 Results Monitoring Survey and the 2017 socio-economic assessment ([HDX](https://data.humdata.org/search?q=Dzaleka)). A new instrument could duplicate them; analysing the existing data may be a lower-risk first step (**hypothesis**).
- **Status:** a longer-term possibility only. Synthetic data only until ethics approval, local consultation and data governance are in place.

### 9.7 Building on existing systems

| System | What it offers | Status (checked 14 Oct 2026) |
| --- | --- | --- |
| DOS | Services, hotlines, news, public API | Live; see section 2 |
| OpenStreetMap / HOT Tasking Manager | Open map data; coordination of remote mapping | No Dzaleka project found |
| [Sahana Eden](https://github.com/sahana/eden) | Open-source emergency management (registries, requests, mapping) | MIT licence, actively maintained |
| [Ushahidi](https://github.com/ushahidi/platform) | Crowdsourced reports on a map | AGPL, actively maintained |
| [FixMyStreet](https://github.com/mysociety/fixmystreet) | Problem reports routed to a responsible body | AGPL, actively maintained |
| Met Malawi CAP feed | Official alerts, machine-readable | Public, active |
| Defesa Civil Alerta | Cell-broadcast alerts in Brazil | Operator-based; detailed technical documentation is restricted to ITU-D TIES users ([ITU](https://www.itu.int/md/D26-SG01-C-0088/en)) |

Suitability for Dzaleka (language, low bandwidth, hosting at no cost) has **not** been tested for any of these.

### 9.8 Comparison

| Option | Problem addressed | Potential benefit to residents | Feasibility for the Independent Study | Depends on partners / missing data | Privacy and protection risk | Prototype by Dec 2026? |
| --- | --- | --- | --- | --- | --- | --- |
| 9.1 Reporting | Local problems not visible to decision-makers | High, **if** someone responds | High (could build on Ushahidi) | **High:** a responder and moderators are needed | Medium; high if protection cases leak in | Yes, with synthetic reports |
| 9.2 Multilingual information | Information not reaching non-English speakers | Medium; depends on channels | High | Medium: translators, DOS, radio | Low (without profiles) | Yes |
| 9.3 Weather alerts | Warnings not localised to the camp | Potentially high, but a false alarm is costly | Medium | Medium: channels and ground truth | Low data risk, high safety risk if live | Yes, simulation only |
| 9.4 Open map data | Incomplete or outdated maps | Indirect | High (remote) | Low to start; local validation later | Low, with layer restrictions | Yes |
| 9.5 Climate risk | Unknown exposure to floods and erosion | Indirect, research | Medium; technically demanding | Medium: imagery and validation data | Low | Partial |
| 9.6 Needs assessment | Unmet needs not visible | Uncertain | Medium | High: ethics and governance | **High** | Synthetic demo only |
| 9.7 Existing systems | Avoids building from scratch | Supports the others | High | Varies | Varies | Not a standalone output |

### 9.9 Current preference: a minimum viable prototype for 9.1

A **demonstration only**, with no live service and no real personal data:

1. **Synthetic data:** a set of fictional reports (category, short text, zone, date) written to resemble plausible infrastructure and service problems.
2. **Report form:** a mobile-friendly, low-bandwidth form. Fixed categories, a zone chosen from a coarse grid instead of GPS, and no account or name.
3. **Moderation queue:** every report starts as "submitted" and is published only after review. Text that suggests violence or a personal emergency is never published, and the form shows referral contacts instead.
4. **Public view:** counts by zone and category on a map, with a minimum-count threshold, rather than individual reports.
5. **Partner export:** a summary that a hypothetical responsible body could receive.
6. **Evaluation:** first decide whether to configure Ushahidi or build a minimal custom tool, and document what each requires.

### 9.10 Questions for local partners before implementing 9.1

1. Who would receive reports, and who can actually fix the problems (UNHCR, camp administration, block leaders, DOS, or others)?
2. Does a reporting or feedback channel already exist, such as UNHCR feedback mechanisms, hotlines or community leaders? If so, would a new one help or fragment it?
3. Who would moderate reports, in which languages, and would that be paid or unpaid work?
4. How do residents prefer to report: phone, SMS, WhatsApp, radio call-in, or in person?
5. Could public mapping of problems create tension with authorities or between communities, or expose reporters to retaliation?
6. How should protection-related reports be referred if they arrive anyway?
7. What ethics approval and data-protection rules apply (NYU, and Malawi's data-protection law; **to check**)?

---

## 10. Proposal (15 Oct 2026): "Know your status" — legal information that survives the bill

**Status: proposal for discussion, not selected.** It extends option 9.2 and Step 1. Facts on the bill and its legislative path: `DZALEKA_SITUATION_RESEARCH.md` §2.1.

### The idea

Residents of Dzaleka will need clear, accurate information on the draft Refugees (Protection and Management) Bill, in their own languages: what it proposes, what has **not** changed, where it stands, and later, who is eligible and how to apply. The legislative process is slow (Cabinet has no deadline; the earliest realistic window is 2027), and that gives us time to build carefully.

**The main risk is that the bill is never passed**, or passes in a narrower form. Malawi has law-reform bills that have waited at the Ministry of Justice for years. The project is therefore designed so that **most of the work is useful whatever happens to the bill**, and only a thin final layer depends on it.

### Design principle: three layers

| Layer | What | Depends on the bill? | Useful if the bill dies? |
| --- | --- | --- | --- |
| **1. Base** | "Your rules today": what the 1989 Act and the 2023 directive mean in practice, which legal permissions already exist (to check), where to get legal help, scam warnings ("nobody can sell you a place on a list"). A glossary of legal terms in Kirundi, Kinyarwanda, Swahili and French. The content tool (one source → radio script, A4 sheet, WhatsApp card) | No | **Yes**. This is the core value |
| **2. Tracker and explainer** | Where the bill stands (Cabinet, Gazette, readings, assent, commencement), with a source for every step. A plain-language explainer: "proposed, not law" | Yes, but cheap to maintain | Partly. It prevents false hope and rumours |
| **3. Eligibility guide** | Who can apply to live outside the camp or to work, how, where, and with which documents | **Fully**. Built only after commencement and regulations | No. Kept as a template until then |

### Phases and decision gates

| Phase | When (realistic) | What | Gate to the next phase |
| --- | --- | --- | --- |
| **0. Discovery** | Oct 2026 – Jan 2027 | Collect the knowledge listed below; talk to a legal partner, DOS and Yetu Radio; ethics approval | A legal partner agrees to review content, and no one is already doing the same |
| **1. Base layer** | Jan – Mar 2027 | "Your rules today" content, glossary, content tool; radio and print pilot | Partner sign-off on every legal sentence |
| **2. Tracker and explainer** | As soon as the full bill text is public | Explainer of the text as published; tracker updated at each step | Text confirmed against an official copy |
| **3. Eligibility guide** | Only after assent, Gazette publication **and** regulations | Fill the template; "who / how / where" | Reviewed by the legal partner; the Eligibility Committee exists and accepts applications |

**Stop or pivot rules (to agree with the professor):**
- If the bill has not reached Cabinet by a set date (e.g. end of the 2027 budget meeting), freeze layer 3 and keep layers 1–2 alive at minimal effort.
- If the bill is rejected, or replaced by a harsher policy (e.g. relocation to the Chitipa site), layer 2 explains the change and layer 1 carries on.
- If Inua Advocacy, DOS or UNHCR already produce this content, we contribute translations and formats to theirs instead of building a parallel product.

### Knowledge we need to collect

**A. Law and procedure**
1. The full text of the Special Law Commission report and draft bill (Law Commission, Inua Advocacy, MHRC).
2. The law in force: the 1989 Act, the March 2023 directive, and whether court rulings on the 2023 relocations changed anything.
3. Whether **any legal route out of the camp, or to work, already exists** today (permissions from the Commissioner for Refugees, Immigration Act permits, business licences). This feeds layer 1 whatever happens to the bill.
4. How "valid reasons" and "designated areas" would be defined (in the bill, or left to regulations?), and who writes the regulations.
5. Where to follow each step: Cabinet communiqués, the Malawi Gazette, Parliament order papers and Hansard. Who can access the Gazette regularly?
6. Whether the bill's commencement date and transitional provisions cover people already living outside the camp.

**B. Politics and timing**
1. The positions of the Ministry of Homeland Security and the Ministry of Justice, and whether the bill enters the government's 2027 legislative programme.
2. Pressure points: MHRC, the EU, UNHCR, the Malawi Law Society, and the IMF/donor context.
3. Signals that the bill is stalling (no Cabinet item after the Law Commission formally submits it) or changing (a relocation to Chitipa moving forward instead).

**C. The people the information is for**
1. **How many residents are recognised refugees and how many are asylum seekers.** Only recognised refugees could apply to live outside the camp, so the RSD backlog decides who could ever benefit (UNHCR data; Malawi reported 939 decisions in 2026).
2. Languages, literacy, and access to radio, phone and WhatsApp (no Dzaleka figure yet; see section 8).
3. What residents already believe about the bill. Are there rumours, or scams built on it?
4. Which groups would be most affected or most at risk (women-headed households, unaccompanied children, people already living informally outside the camp).

**D. The information ecosystem**
1. Does DOS's Rights Navigator already cover this, and could the content live there?
2. Do Inua Advocacy, UNHCR or Yetu Radio plan their own explainers?
3. Who are the trusted messengers (block leaders, churches, Yetu presenters)?

**E. Translation**
1. Legal terminology in Kirundi and Kinyarwanda. Do glossaries exist, from UNHCR or the courts in Rwanda and Burundi?
2. Translators, with review by a native speaker **and** a lawyer, plus back-translation for the key sentences.

**F. Safety, ethics and liability**
1. **Misinformation can cause arrests.** A resident who reads "you can live outside the camp" before the law is in force risks detention (over 900 people were detained in 2023). Every item must show its legal status ("proposed" / "in force") and the date it was checked.
2. Rules on giving legal information without being a lawyer in Malawi (Legal Education and Legal Practitioners Act). Where is the line between information and advice?
3. Political sensitivity: will the government read this as advocacy? Is it safer under a Malawian partner's name?
4. Data protection: no personal data in layers 1–2; Malawi's Data Protection Act 2024 (to check); university ethics approval.
5. False hope: messaging is tested with residents so that "proposed" is not heard as "approved".

**G. Technical**
1. A content model with a **legal status and a "last checked" date** on every item, so that an update to the law changes every format at once.
2. Formats: radio script, A4 sheet, WhatsApp card, an optional page on DOS; low bandwidth, offline.
3. Hosting at no cost and an open licence, so that other camps can reuse it (the Kenya Refugees Act 2021 is a comparable case).

### Does something like this already exist? (checked 15 Oct 2026)

The user is considering a chatbot: residents say what they need, and the bot points them to the right information or service.

**In Dzaleka / Malawi**

| What | What it covers | Gap |
| --- | --- | --- |
| **DOS Rights Navigator** ([services.dzaleka.com/rights-navigator](https://services.dzaleka.com/rights-navigator), checked 15 Oct) | "Know your rights": the 1989 Act, the 1990 Regulations and travel documents, the Constitution, the Convention reservations; status cards (freedom of movement "requires gate pass"; right to work "restricted"); legal aid directory, protection hotlines, an incident tracker, link to Inua Advocacy | **Already covers most of our layer 1**, in English, on the web. No mention of the 2026 bill was seen. No chatbot. Kirundi/Kinyarwanda not offered (section 2) |
| DOS Help Desk | One entry point for technical, business and follow-up help | Human, web-based |
| Inua Advocacy, "Refugees in Malawi: All you need to know" ([Dec 2024 PDF](https://inuaadvocacy.org/wp-content/uploads/2024/12/MALAWI-REFUGEE-GUIDE-DEC-2024-sm.pdf)) | History, legal framework, myths, "who does what in Dzaleka" | Written for the public, officials and advocates, not as a practical guide for residents |
| UNHCR HELP site for Malawi | UNHCR runs country HELP sites (e.g. [South Africa](https://help.unhcr.org/southafrica), with work, legal aid and documentation pages) | **To check:** help.unhcr.org/malawi returned 403 to automated requests. Open it by hand |

**No chatbot for Dzaleka or Malawi refugees was found.** This is an absence of evidence from web search, not proof: DOS, Inua Advocacy or TakenoLAB must be asked directly.

**Elsewhere (models to learn from)**

| Project | Lesson |
| --- | --- |
| **Signpost** (IRC, Mercy Corps; ~20 countries; [signpost.ngo](https://www.signpost.ngo)). The AI assistant was piloted in Kenya, Greece, Italy, El Salvador, Mexico and Libya ([data.org](https://data.org/our-work/challenges/artificial-intelligence-to-accelerate-inclusion-challenge/awardees/irc)). Not in Malawi; the IRC does not operate there | The pilot found the AI assistant **"not safe without a human in the loop"**, and found that "a robust context-specific knowledge base is the most critical component" ([Signpost AI](https://www.signpostai.org/insights/executive-summary-signpost-ai-information-assistant-pilot-program)) |
| **ALMA** (IRC, US, WhatsApp; Dari, English, Spanish, Swahili; Nov 2025) ([IRC](https://www.rescue.org/press-release/alma)) | Gives no legal advice; redirects to trusted services; tells users not to share their immigration status |
| **Mona** (IRAP and Marhub, 2019; Messenger and Telegram) ([IRAP](https://refugeerights.org/news-resources/irap-and-marhub-launch-chatbot-to-provide-legal-information-to-refugees-seeking-assistance)) | Legal information plus screening for referral to human lawyers |
| **La Chama** (UNHCR, Latin America) ([UNHCR](https://www.unhcr.org/digitalstrategy/case-studies/one-message-at-a-time-la-chama-chatbot-combats-falsehoods)) | Chatbot against misinformation, with a route to ask UNHCR directly |
| **Rafiki AI**, Kakuma (Kenya) ([Facebook post](https://www.facebook.com/Kayodealabiinitiative/posts/have-you-heard-about-rafiki-airafiki-is-a-swahili-term-meaning-friend-so-rafiki-/1246113417528991) ⚠️ single source) | A refugee-camp chatbot by a local initiative; status and scope unknown |
| Access Now mapping ([Feb 2024](https://www.accessnow.org/wp-content/uploads/2024/02/Mapping-humanitarian-tech-February-2024.pdf)) | "Hardly any" humanitarian chatbots use machine learning. Most are menus or keyword routing, with staff overseeing the content |

**What this means for the design**

1. **Do not rewrite the rights content.** Build on the Rights Navigator with DOS. Our contribution is the **channel** (conversation, radio, print), the **languages** (Kirundi, Kinyarwanda, Swahili, French) and the **bill layer** (2–3).
2. **A guided bot, not an open AI chat.** Menus and keyword routing over verified content, with free text only to pick a topic. The reasons:
   - legal risk (a wrong answer can lead to an arrest);
   - weak machine-translation support for Kirundi (section 3);
   - Signpost's finding that AI needs a human in the loop;
   - since 15 Jan 2026, WhatsApp Business no longer allows general-purpose AI chatbots; task-specific bots are still allowed ([summary](https://simplyboost.io/blogs/whatsapp-business-automation-guide); check the terms themselves).
3. **Someone must answer what the bot cannot.** Hand-off to the DOS Help Desk or Inua Advocacy needs their agreement. This is a smaller version of the 9.1 responder problem.
4. **The bot complements radio and print; it does not replace them.** Only about a third of refugees in comparable camps have used mobile internet (section 2).
5. **Who owns the WhatsApp number** (DOS? Inua?) is a Phase 0 question.

### Risks of a keyword-search bot (15 Oct 2026)

The bot is a keyword search over verified sources, not legal assistance. That removes the main risk of an AI chat, which is invented answers. A disclaimer alone does not protect users, though: few people read it, especially in translation or with low literacy. The remaining risk lies in the **content and how it is read**:

| Risk | Example | Mitigation |
| --- | --- | --- |
| **"Proposed" read as "in force"** (most serious) | A search for "work" returns the bill's proposed right to work | Never mix the two. Every answer opens with a label, **IN FORCE** or **PROPOSED – NOT LAW**, and the date it was last checked |
| Outdated content | The law changes and the bot keeps the old answer | Each item has an expiry date; expired items are hidden until reviewed; a full review at each legislative step |
| Keyword returns the wrong passage | "Leave" could mean repatriation, a gate pass or the bill | Show 2–3 options for the user to choose from, not a single answer |
| Disclaimer not read | A long notice at the start | A short notice **in every answer**, in the user's language, plus a fixed referral line (e.g. Inua Advocacy's number) |
| Privacy of searches | "How to leave the camp without a pass" reveals intent, linked to a phone number | Do not store query text with phone numbers; keep only aggregated topic counts |
| Scammers imitating the bot | A fake "official bot" charges for "a place on the list" | One official number, announced through trusted channels; the bot repeats that the service never charges |
| Political risk | The government reads the bot as advocacy | Neutral content, official sources only, no campaign language |

The bot shows "what source X says, with the link" and who to contact. It does not answer about anyone's individual case. This is legal *information*, not advice, as with a library or the Rights Navigator. The line under Malawian law on legal practice is still **to check**.

### Decision (15 Oct 2026): a local partner is a launch condition, not a start condition

The project has **no Malawian partner**. Publishing under a Malawian partner's name is therefore dropped as a mitigation. Instead, the work would appear under the academic project's name, with neutral, official-source content, approved by the professor and the university ethics committee.

Without a partner, the project also lacks an owner for legal review of content, for hand-off of questions the bot cannot answer, for the WhatsApp number, and for announcing the official number. A partner does not have to be a formal Malawian organisation. DOS is refugee-led and works inside the camp, and it is the first contact planned in Phase 0. We have no partner today because none has been approached yet.

| Can be done without a partner | Requires a partner (launch condition) |
| --- | --- |
| Content in four languages, with IN FORCE / PROPOSED labels and dates | Legal review of every item |
| The legislative tracker (public sources) | Referral for questions the bot cannot answer |
| A bot prototype running on test content | Ownership and announcement of the official number |
| Documentation and open-source code | Any use by real residents |

**Rule:** if neither DOS nor Inua Advocacy agrees by the end of Phase 0 to review content or receive referrals, the bot stays a **research prototype** and is not offered to residents. That result is recorded as a finding (what an outside, partnerless project can and cannot responsibly do).

### Why this fits our constraints

- **No presence in the camp:** layers 1–2 need a legal partner and channels, not a responder in the camp (unlike option 9.1).
- **No unpaid weekly work:** the base content changes rarely, and the tracker changes only at legislative steps.
- **No funding:** only free tools; printing is optional.
- **Research value:** it documents how a law-reform process reaches (or does not reach) the people it is for, and the Kenya case shows that law and practice can diverge.

---

## Sources

All linked inline. Consulted 7 Oct 2026 through Tavily and web search; section 9 sources checked 14 Oct 2026 (web search, GitHub, HDX and HOT Tasking Manager APIs, Met Malawi CAP feed). Earlier context and figures: `DZALEKA_SITUATION_RESEARCH.md`, `ONLINE_MICROWORK.md`, `RESEARCH_LOG.md`.
