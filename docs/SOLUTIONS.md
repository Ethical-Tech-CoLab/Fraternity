# Solutions — what we can realistically build for Dzaleka

Started 7 Oct 2026; **rewritten the same day with a reality filter, then re-researched with Tavily.** Status: draft, for discussion with the professor. Earlier versions are in the git history.

**Why this document exists.** The professor's feedback on the Theory of Change (Oct 2026) was that the research should start from *what we can do that actually changes something in the camp*. The situation research (`DZALEKA_SITUATION_RESEARCH.md`, `docs/cases/`, `comparison.md`) is unchanged and used here as context.

---

## 1. The reality filter

| Who / what | Reality |
| --- | --- |
| **Builders** | Me (with Claude writing much of the code), with the professor supporting |
| **FSF** | Context only. It is not a guaranteed user, operator or distributor |
| **Money** | None. Hosting, data and tools must be free |
| **Field presence** | None. We cannot run a team, a helpline or a pilot inside the camp |
| **Goal** | Something small that changes something real inside Dzaleka, open source, and the start of a technology line |

**What the filter rules out:** anything needing a budget (cash, devices, a WhatsApp Business account), anything that needs us on the ground to run or update it, and anything whose only user would be FSF.

**What it requires:** someone *in* the camp who distributes the tool and keeps it alive after we stop working on it.

## 2. What the research found

### 2.1 Lesson from other camps: don't build a new standalone app

- Of **169 apps and tech projects for refugees launched in 2015–16, most were defunct by 2018**. The Migration Policy Institute calls this "digital litter" ([MPI](https://www.migrationpolicy.org/article/digital-litter-downside-using-technology-help-refugees)).
- Refugees reported that the apps didn't fit their needs, weren't in their language, or that they had never heard of them. They rely on **WhatsApp, Facebook and general tools**. Projects died when short-term funding and enthusiasm ran out (same source; [UNHCR Innovation](https://www.unhcr.org/innovation/app-best-way-help-refugees-improving-collaboration-humanitarian-actors-tech-industry/)).
- **What works instead:** IRC's *Signpost* reaches people through channels they already use, in their own languages ([IRC, 2024](https://www.rescue.org/uk/press-release/irc-signpost-project-eu-prize-humanitarian-innovation)). In Cox's Bazar, rainfall alerts work because **3,400 refugee volunteers** pass them on by megaphone, flags and mosque loudspeakers ([UNDP Bangladesh](https://www.undp.org/bangladesh/stories/until-everyone-safe-early-warning-systems-strengthening-safety-and-resilience-coxs-bazar)). Radio is described as "a wide-reach and high-impact tool in humanitarian settings" (Uganda response analysis, [Population Council Knowledge Commons](https://knowledgecommons.popcouncil.org/cgi/viewcontent.cgi?article=1006&context=hubs_humanitarian)).

With no money, no field team and two people, we fit exactly the profile that produces digital litter. **The way around it is to build *into* what refugees at Dzaleka already run.**

### 2.2 What already exists at Dzaleka

Dzaleka has its own **refugee-led technology ecosystem**, and it is more developed than we thought.

**Dzaleka Online Services (DOS)**, at [services.dzaleka.com](https://services.dzaleka.com), is part of Dzaleka Digital Heritage and is built mainly by **Bakari Mustafa** ([GitHub: Dzaleka-Connect](https://github.com/Dzaleka-Connect); [bakarimustafa.com](https://bakarimustafa.com/dzaleka-online-services-good-news-roundup)). Checked on 7 Oct 2026:
- **Active:** the main repository (`dos`) was last updated on 5 Oct 2026.
- **Content:**
  - a services directory (**149 services** in the public API), jobs, events, a marketplace and courses;
  - a **"Get help now"** page with free hotlines (GBV 5600, child protection 116; contacts checked 18 Apr 2026), a Rights Navigator and incident reporting;
  - a Wellbeing Hub, a Help Desk, and weather from **Met Malawi** with alerts;
  - an interactive map, an encyclopaedia, an **open data platform** and a public API.
- **Languages:** most pages are in English, but newcomer guides exist in **English, French, Swahili and Chichewa**, there is an **Easy Read** section, and a languages page points people to Yetu Radio ([DOS languages page](https://services.dzaleka.com/languages)). **There is no Kirundi or Kinyarwanda version.**
- **Population by origin** (DOS, checked 18 Apr 2026): DR Congo 65%, Burundi 22%, Rwanda 13%, others 1%. **Swahili is the camp's common language.**
- **Risk:** one main developer (about 310 commits). The `dos` repository has **no licence file**, while other repositories in the organisation use MIT. A contributing guide exists ([DOS docs](https://dos.dzaleka.com/introduction)).

**Yetu Community Radio**, Dzaleka's community station:
- **On air since 7 Aug 2018** and still active in 2026 (Facebook posts in March and September 2026).
- **Languages:** the station's own site lists five languages (English, Chichewa, Swahili, French, Kinyarwanda), while UNHCR's 2024 story lists six, adding Kirundi. The two disagree; this is to be checked.
- **Frequency:** the station's site lists 107.6 MHz; another listing says 99.1 MHz.
- It also streams online.

Sources: [DOS Yetu page](https://services.dzaleka.com/yetu-radio); [UNHCR](https://www.unhcr.ca/news/community-radio-fosters-refugee-inclusion-in-malawi/).

**TakenoLAB** is a refugee-led tech school founded in 2015. It is still running, under local leadership after its founder was resettled ([takenoLAB](https://takenolab.org/)). It reports 3,000+ trained and 200+ online jobs, and its students helped map the camp ([HOT/MapMalawi](https://www.hotosm.org/en/news/mapmalawis-dzaleka-mapping-project-osm-mapping-for-people-living-in-protracted-crisis/)).

### 2.3 The real gap: reach inside the camp

DOS's own **2025 Annual Digital Performance Report** ([DOS, 24 Apr 2026](https://services.dzaleka.com/news/2025-digital-performance-report/)) shows:
- 17,952 active users in the year, but **only 1,697 returning users**;
- **3,705 active users in Malawi**, fewer than in the US (4,000) or China (3,728). Some of the foreign traffic may be automated; that is our reading, not the report's;
- Facebook (mobile) as the top referring site.

Dzaleka has ~63,000 residents. **At most a few thousand people in Malawi used the site in a year**, and not all of them live in the camp. The platform has rich, checked, practical content (hotlines, rights, services, jobs, alerts), but **most residents probably never see it**. The likely reasons:
- **Phones:** only 22% of refugee households in rural areas worldwide have an internet-capable phone ([UNHCR Connectivity](https://www.unhcr.org/innovation/internet-mobile-connectivity-refugees-leaving-no-one-behind/)). No Dzaleka figure was found.
- **Language:** the site is mostly English; there is nothing in Kirundi or Kinyarwanda (35% of residents by origin). Kirundi is a "low-resource" language for machine translation, so it needs human translators ([CLEAR Global / TWB](https://clearglobal.org/translators-without-borders)).
- **Channel:** people get information from radio, WhatsApp, Facebook, churches and word of mouth, not by browsing a website.

**So the most useful thing to build is not new content, and not a new app. It is the bridge between the content that already exists and the channels people actually use.**

### 2.4 Flooding: the hazard is documented

The earlier draft said we had no evidence of what floods at Dzaleka. **That was wrong.**
- A 2021 Virginia Tech master's thesis (Friedman) modelled flooding in Dzaleka using **3.5 cm drone imagery**. It found that **water-caused erosion patterns predict where houses collapsed**, with misclassification below 17%, far better than standard hydrological models (54–67%) ([Friedman, 2021](https://vtechworks.lib.vt.edu/items/fabeecfe-edd2-4db0-8d9d-235f327d3c2c)).
- More recently, Plan International reported leaking roofs and few sound classrooms during heavy rain ([Plan International, Jun 2025](https://plan-international.org/malawi/news/2025/06/24/world-refugee-day-2025-dzaleka-on-shaky-ground)). A 2026 social-media post describes walls and roofs collapsing (single, unverified source ⚠️).

**The risk at Dzaleka is house collapse from runoff and erosion in heavy rain, and it has been mapped once (2021).**

## 3. Options that pass the filter

### Option 1 — "Last-mile kit" for Dzaleka Online Services (recommended)

**What it is:** a small open-source tool that reads the DOS public API and, every week, automatically produces **ready-to-use versions of what changed** for the channels people actually use:
1. **Radio script:** a 3–5 minute bulletin (new jobs and deadlines, events, notices, weather alerts, one hotline reminder) for Yetu Radio presenters to read.
2. **WhatsApp/Facebook text and image cards:** short, forwardable messages in Swahili and French. No WhatsApp Business account is needed, because people forward them.
3. **Printable noticeboard sheet (A4 PDF):** for churches, schools, community centres and block leaders.
4. **Languages:** Swahili and French first, generated as drafts and **reviewed by a person in the camp** before release. Kinyarwanda and Kirundi only with human translators.

**Why it passes the filter:**
- **Zero cost:** a script run on a free schedule (GitHub Actions) that writes files; nothing to host.
- **No field team needed:** DOS already maintains the content. Yetu Radio, DOS's Facebook page and community groups distribute it.
- **Respectful:** it strengthens a refugee-led platform instead of competing with it.

**The small, real change:** practical information that already exists (a job deadline, the GBV hotline, a weather alert, a new service) reaches people **without a smartphone, without English, and without browsing a website**.

**How we would know:**
- DOS analytics (visits from Malawi, Facebook referrals) before and after;
- mentions in radio phone-ins;
- a question on DOS's "Have your say" form.

**Research angle:** how a refugee-run information platform reaches, or misses, its own camp, and whether low-tech channels close the gap. This is a small version of an information ecosystem assessment, the method Internews uses in camps.

**Replicable:** any camp with an information source (a website, UNHCR notices) and a radio, WhatsApp groups or noticeboards.

### Option 2 — Heavy-rain warnings by zone (research track, PhD-linked)

**What it is:** combine three things that already exist:
- the 2021 Dzaleka flood and erosion model (Friedman);
- the camp's OpenStreetMap base (MapMalawi, 2021);
- the live Met Malawi weather already in DOS.

When forecast rainfall crosses a threshold, the tool flags **which zones of the camp face collapse risk**. It then produces a short alert that feeds into Option 1's radio, WhatsApp and print outputs. The threshold logic is borrowed from Cox's Bazar's landslide early-warning system ([UNDP Bangladesh](https://www.undp.org/bangladesh/stories/until-everyone-safe-early-warning-systems-strengthening-safety-and-resilience-coxs-bazar)).

**Why it fits:**
- It is the closest to the PhD (evacuation risk).
- The rains start in mid-December.
- The hazard is documented (§2.4).
- Option 1 gives it a delivery channel.

**Limits:** the 2021 model predates the camp's growth (from ~43,000 to ~63,000 people), so it needs updating with newer imagery or OSM data. Thresholds must be validated with past rain events, and alerts must not create false alarms. **Research first, then a prototype.**

### Option 3 — Our sourced figures on DOS's open data platform (by-product)

DOS already has an **open data platform and data catalogue**. Rather than publishing our dataset separately, we could offer it to DOS: each figure with its source, date and conflicting values kept side by side. It is cheap and certain, but it changes little inside the camp.

### Later: a free phone information line

Viamo's **3-2-1 service** in Malawi, run with Airtel, gives **free** voice-menu information to any phone, including basic phones ([UNDP Digital X](https://digitalx.undp.org/viamo-3-2-1-platform_1.html)). If Option 1 works, its weekly content could later be offered to 3-2-1 through a partner. This needs an organisational agreement we cannot make on our own, so it is noted for later.

## 4. Earlier ideas, through the filter

| Earlier idea | Verdict | Why |
| --- | --- | --- |
| Funded pilots (remote work, cash, farming) | Out | Need money |
| G1 caravan and stock planner (FSF) | On hold | FSF is context only |
| D1 "where to get help" directory | **Already exists** | DOS "Get help now", Rights Navigator and 149 services |
| C1 risk and evacuation map | Becomes Option 2 | The 2021 model gives it a base |
| A1 law comparator, B1 funding tracker | Possible later | Advocacy tools; little change inside the camp |
| X1 "Is this offer real?" scam checker | Possible as Option 1 content | A recurring radio/WhatsApp item instead of a separate app |
| X2–X9 (papers safe, skills passport, clinic translation, mental health, Kolibri, reverse caravan, collective buying, community currency) | Out for now | Each needs devices, an operator in the camp, FSF as operator, or carries legal risk |
| X10 "Live on $8", X11 "No way out" (awareness) | Side project | Buildable by us, but they change things outside the camp, not inside |
| Translating the whole DOS site (previous draft) | Narrowed | Essentials already exist in FR/SW; translate what changes weekly, via Option 1 |

## 5. Recommendation

**Start with Option 1 (the last-mile kit) and run Option 2 (heavy-rain warnings by zone) as the PhD-linked research track.**

- **Option 1** is the only option where people in the camp already produce and distribute the content. What is missing is the bridge, and that is exactly what two people with code can build for free.
- **Option 2** gives the research depth and a natural deadline, and its alerts travel through Option 1.
- The "app" you had in mind becomes **a tool for the camp's own information providers** (DOS, the radio, community leaders), not a new app that residents would have to discover and install.

## 6. Next steps

1. **Discuss with the professor:** Option 1 + Option 2.
2. **Contact Bakari Mustafa / Dzaleka Connect** (dzalekaconnect@gmail.com) **before writing code.** Ask:
   - Would a weekly radio/WhatsApp/print kit from the DOS API help?
   - Who could review Swahili and French drafts?
   - What licence applies to `dos`?
   - Does DOS already work with Yetu Radio?
   - Is there anything else they would rather have help with?
3. **Ask FSF (context):** do they know DOS, Yetu Radio or TakenoLAB, and can they introduce us?
4. **Option 2 groundwork:**
   - read Friedman (2021) in full;
   - find the drone imagery (OpenAerialMap / MapMalawi);
   - compare the 2021 extent with today's OSM data;
   - collect past heavy-rain events and house collapses at Dzaleka.
5. **Prototype only after DOS agrees:** a script that turns one week of the DOS API into a Swahili radio script, as a demo for that conversation.

## 7. Open questions

- What share of residents have a smartphone, WhatsApp or a radio? (No Dzaleka figure found.)
- Does Yetu Radio broadcast in Kirundi? Sources disagree.
- Who reviews translations so they are correct and not just machine output?
- Is the 2021 drone imagery openly available, and under what licence?
- Would DOS want outside contributors? One developer carries most of the work, so help may be welcome, but this has to be asked.

---

## Sources

All linked inline. Consulted 7 Oct 2026 through Tavily and web search: Migration Policy Institute ("Digital litter"), UNHCR Innovation, IRC (Signpost), UNDP Bangladesh (Cox's Bazar early warning), Population Council Knowledge Commons (radio in Uganda's response), Dzaleka Online Services (site pages, public API, GitHub, 2025 Annual Digital Performance Report), bakarimustafa.com (Jul 2026), UNHCR (Yetu Radio), takenoLAB, HOT/MapMalawi, UNHCR Connectivity, CLEAR Global / Translators without Borders, Friedman (2021, Virginia Tech thesis), Plan International (Jun 2025), UNDP Digital X (Viamo 3-2-1). Situation figures come from `DZALEKA_SITUATION_RESEARCH.md`.
