# Solutions — Dzaleka Info Bridge

Draft, 7 Oct 2026, for discussion with the professor. **Revised after a critical review the same day:** the proposal is still a hypothesis, so it now starts with validation. Earlier versions are in the git history. Supporting research: `ONLINE_MICROWORK.md`; situation context: `DZALEKA_SITUATION_RESEARCH.md`.

**Update, 14 Oct 2026:** section 9 sets out seven options for discussion with Professor Yorke Rhodes on 15 Oct. No option has been selected; a community reporting platform is the current preference.

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

## Sources

All linked inline. Consulted 7 Oct 2026 through Tavily and web search; section 9 sources checked 14 Oct 2026 (web search, GitHub, HDX and HOT Tasking Manager APIs, Met Malawi CAP feed). Earlier context and figures: `DZALEKA_SITUATION_RESEARCH.md`, `ONLINE_MICROWORK.md`, `RESEARCH_LOG.md`.
