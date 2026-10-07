# Solutions — a technology line for Dzaleka

Started 7 Oct 2026, revised the same day. **Status: draft, for discussion with the professor.**

**Why this document exists.** The professor's feedback on the Theory of Change (Oct 2026) was that the research should start from *what we can do that actually changes something in the camp*. Everything written so far (`DZALEKA_SITUATION_RESEARCH.md`, `docs/cases/`, `comparison.md`) describes the problem. It is unchanged and used here as context. This document adds solutions.

**Constraints (set 7 Oct 2026):**
- **Who:** the professor and I, working for Fraternidade Sem Fronteiras (FSF).
- **No funding.** What we build is **free and open source**.
- **Small impact is fine.** The goal is to start a **line of technology development** that grows with the research, not to fix the camp.
- **Dzaleka first**, but each tool should work in other camps.

Same sourcing rules as the rest of the project. Numbers marked *derived* are computed here, not sourced.

---

## 1. What counts as a good first tool

| Criterion | Question |
| --- | --- |
| **Real user** | Is there a named person or organisation who will actually use it? |
| **Small, visible change** | What concretely gets better, and can we measure it? |
| **Zero budget** | Can two people build it with public data, free tools and no field team? |
| **Data safety** | Does it avoid holding personal data about refugees? (Context: allegations of police complicity, §5.1.) |
| **Not duplicated** | Does something already do this at Dzaleka? |
| **Research value** | Does it produce findings, ideally linked to the PhD on evacuation risk? |
| **Replicable** | Would it work in Kakuma, Bidibidi or Cox's Bazar? |

## 2. Candidate tools, cluster by cluster

Clusters as defined in `DZALEKA_SITUATION_RESEARCH.md` §10.

### A. Legal & durable solutions

**A1 — Refugee law comparator.**
- **What it is:** an open web page that compares, clause by clause, the 1989 Refugees Act, the new draft bill once released, and the laws of Uganda, Ethiopia and Kenya (already researched in `docs/cases/`). It would cover work, movement, business licences and ID.
- **Users:** Inua Advocacy (lobbying for the amendment), people making submissions to the Law Commission, journalists.
- **Small change:** better-informed submissions while the Refugees Act is under review ([Malawi Voice, 1 Jul 2026](https://www.malawivoice.com/2026/07/01/wfp-engages-malawi-speaker-on-refugee-legislation-review/)).
- **Existing:** AfricanLII's *Malawi Refugee Law Reader* collects the texts ([AfricanLII](https://africanlii.org/en/akn/mw/doc/book/2023-11-01/malawi-refugee-law-reader/eng@2025-01-01)) but does not compare them.
- **Limits:** depends on the draft being public, and the timing is uncertain. A comparison is not legal advice.

### B. Funding

**B1 — Open funding-gap tracker for Dzaleka.**
- **What it is:** one public page, updated on a schedule, that brings together scattered public numbers. These include UNHCR Malawi funding by outcome area, WFP transfer value per person against the $28 food basket, OCHA's financial tracking service (FTS), and new donors.
- **Users:** journalists, Inua Advocacy, FSF, donors.
- **Small change:** the gap becomes visible in one place. Malawi has no inter-agency plan, so FTS on its own shows almost nothing (§3).
- **Existing:** none found for Malawi.
- **Limits:** it doesn't change anyone's day directly, and many sources are PDFs that need manual updating.

### C. Disaster & institutional capacity

**C1 — Open risk and evacuation map of Dzaleka.**
- **What it is:** build on the OpenStreetMap data MapMalawi produced in 2021 with a HOT grant, which covered services, water, health and buildings ([OSM wiki](https://wiki.openstreetmap.org/wiki/Humanitarian_OSM_Team/HOT_Microgrants/Community_Impact_Microgrants_2021/Proposal/Dzaleka_Mapping)). Add flood-prone zones (terrain plus rainfall), fire-risk density and assembly points. Output printable maps per block, plus a one-page activation checklist adapted from the Cox's Bazar protocol (`docs/cases/coxs-bazar.md`).
- **Users:** block leaders and refugee-led organisations, DoDMA, UNHCR.
- **Small change:** before the rains start in mid-December, people know where the water goes and where to go.
- **Research fit:** the strongest of all the candidates. It is the PhD topic (evacuation risk), and ERCF's engine already exists.
- **Limits:** needs local validation (walking the routes) and partners on the ground. The user is not guaranteed, and it is time-sensitive.

### D. Protection & F. Actor landscape

**D1 — "Where to get help" directory.**
- **What it is:** a list of who does what and where in and around Dzaleka (GBV, child protection, health, legal aid, food), with contacts and opening hours. It would be multilingual (French, Swahili, Kinyarwanda/Kirundi, English) and come as a printable sheet and a WhatsApp-shareable page. **It stores no case data.**
- **Users:** refugees and community focal points.
- **Small change:** fewer dead ends when someone seeks help. NGO exits make the old referral lists wrong (§9).
- **Existing:** UNHCR runs WhatsApp lines elsewhere, and directories like Kompasi exist in the UK ([civictech.guide](https://civictech.guide/projects/unhcr-chatbots)). None was found for Dzaleka.
- **Limits:** it is only useful if kept up to date, which means someone local must own the updates. It also fits the earlier principle that the G tool "must start from the refugee's entry point" (`RESEARCH_LOG.md`, 5 Oct).

### E. Data blackout

**E1 — Dzaleka open dataset.**
- **What it is:** publish the figures we have already sourced as open data (CSV/JSON plus a simple page). Each figure carries its source, date and reporting period, and conflicting figures are kept side by side. That is our sourcing discipline turned into a public good.
- **Users:** researchers, journalists, refugee-led organisations.
- **Small change:** the next person doesn't start from zero. The most-used source in this research was a refugee-run archive (§9). This would complement it.
- **Limits:** it is an advocacy and research tool, not a field tool. Effort is very low because the work is done. It is also the data base under B1, C1 and A1.

### G. Local & faith-based response

**G1 — Caravan and stock planner for volunteer-supplied clinics.**
- **What it is:** a small open-source tool for the FSF clinic, with three parts:
  1. **Stock:** replaces the spreadsheet; records what came in, what was used and expiry dates.
  2. **Caravan planner:** each caravan carries only **24–90 kg** (8–30 volunteers × 3 kg, about every 3 months). The planner suggests *what to pack*, based on consumption, expiry and the weight limit, so the scarce kilograms go to what will run out first.
  3. **Aggregate report:** stock-out days and the share of carried weight used before expiry. No patient data.
- **User:** **FSF, a guaranteed user.** It is the only candidate with one.
- **Small change:** fewer stock-outs at the clinic and less wasted luggage. It is measurable from caravan to caravan.
- **Existing:** OpenLMIS (used in Malawi's national supply chain) and mSupply manage stock at scale ([GHSC-PSM, 2019](https://www.ghsupplychain.org/sites/default/files/2019-05/Malawi%20OpenLMIS%20TechBrief%20FINAL%205-8-19.pdf)). They are built for national systems with procurement. **Neither plans weight-limited donated supply.** That niche is ours.
- **Replicable:** any clinic supplied by volunteers or donations, which is the pattern after agency withdrawal (clinics ran out of medicine in Jun 2025, §11).
- **Earlier correction to respect:** on 5 Oct, clinic records were judged to sit in D/E rather than G. G1 is framed here as **continuity of a local actor's service** (the G research level), not as clinic records. To confirm with the professor.

**G2 — Help-seeking entry point.** This is the idea from 5 Oct: start from how a refugee asks for help, through trusted focal points, and let the refugee choose where the case goes. It **needs the ethical field mapping first**, so it is a later step. D1 is its simplest first version.

### Livelihoods (cross-cutting)

The morning draft of this document proposed remote-work and cash pilots. They need funding, so they are out of scope now. What we learned stays useful as context:
- a UNHCR pilot at Dzaleka where 54 refugees earned $21,137 online in 6 months ([JRS](https://ear.jrs.net/en/story/bridging-the-digital-divide-for-refugee-youth-in-dzaleka-malawi/));
- refugees cannot get work permits or business licences ([RLRH, Jan 2026](https://refugeeledresearch.org/wp-content/uploads/2026/01/MALAWI.pdf));
- cash to refugees produced $1.51–$1.95 per dollar in Rwanda's local economy ([IFPRI](https://www.ifpri.org/news-release/study-refugees-can-boost-host-economies/)).

These figures can feed A1. Technology is not the bottleneck there; legal status and paying clients are.

## 3. Outside the box

Section 2 sticks to one tool per cluster. This section starts from **daily life in the camp** instead: what a refugee would actually open on a phone, what moves money or information, and what makes people outside care. Each idea is grounded in a finding from Part I.

### 3.1 Apps for refugees

| # | Idea | Why (finding) | What already exists |
| --- | --- | --- | --- |
| X1 | **"Is this offer real?"** A WhatsApp bot and printable checklist for resettlement, job and travel offers. It answers in the refugee's language, explains that UNHCR never charges for resettlement, flags known scam patterns, and lets people report a scam anonymously (aggregate counts only). | UNHCR describes Dzaleka as a trafficking hotspot (§5.1). A syndicate was reported to be monetising resettlement, and 52 people were stopped from travelling to the US ([Nation Online](https://mwnation.com/un-seeks-probe-on-refugees-syndicate-reports/)). With resettlement collapsing and Canada's EMPP paused, desperation makes people easy prey. | UNHCR posts general warnings ("resettlement is free"). No Dzaleka-specific, multilingual tool was found. |
| X2 | **"My papers" safe.** An offline app that keeps encrypted photos of a family's documents (refugee ID, asylum papers, birth certificates, school and course certificates) **only on the person's own phone**, with an optional backup that only they can open. | Fire and flood risk (§4); children are born into refugee status, and every route out (resettlement, the new law, platforms, banks) depends on papers. | General-purpose encrypted vaults exist, but none are designed and translated for refugees. |
| X3 | **Skills passport.** A portable, verifiable record of skills and courses (JRS, JWL, There Is Hope, the digital-skills pilot) that a refugee can show to an online client or a resettlement programme. | 54 refugees earned $21,137 online in 6 months ([JRS](https://ear.jrs.net/en/story/bridging-the-digital-divide-for-refugee-youth-in-dzaleka-malawi/)), and pathways like Canada's EMPP select on skills. Training exists, but there is no proof that travels with the person (RLRH, Jan 2026). | Open verifiable-credential standards exist (W3C). No refugee-run issuer was found at Dzaleka. |
| X4 | **Clinic translation layer for FSF.** A WhatsApp intake for the FSF clinic: the patient describes symptoms in French or Swahili with photos, and the Brazilian doctors read it in Portuguese. The diagnosis goes back in the patient's language. | FSF runs asynchronous telemedicine with doctors in Brazil, and patients come back another day for the diagnosis (§11). The language gap between French/Swahili and Portuguese is built into that model. | Generic translation exists. Nothing fits this specific clinic workflow. |
| X5 | **Offline mental-health support.** The WHO's *Self-Help Plus* stress-management course (audio plus an illustrated book), delivered offline through phones or a speaker in group sessions led by trained lay facilitators. | 78% probable depression in the one study at Dzaleka (§5.3), and no mental-health services found. A randomised trial with South Sudanese refugee women in Uganda showed meaningful reductions in distress at 3 months ([Tol et al., *Lancet Global Health*, Feb 2020](https://news.liverpool.ac.uk/2020/01/23/study-highlights-effectiveness-of-behavioural-interventions-in-conflict-affected-regions/)). | WHO materials exist. Translations into Kinyarwanda/Kirundi and the licence to adapt them must be checked ⚠️. |
| X6 | **Offline school in a box.** A Kolibri server (open source, works offline) with lessons in French, Swahili and English, installed at the FSF site or a school in the camp. | Low connectivity; children out of school as families cope with cuts (allAfrica, 30 Sept 2026). | Kolibri is already used in Kakuma and northern Uganda ([Learning Equality / Solve](https://solve.mit.edu/solutions/52786)). Our work would be installing and curating it for Dzaleka, not building it. Needs a cheap device (~$100–200, not zero). |

### 3.2 Moving money without funding

| # | Idea | Why (finding) | What already exists |
| --- | --- | --- | --- |
| X7 | **Reverse caravan.** FSF caravans fly *in* with medicines. On the way *back*, the same luggage could carry crafts made in the camp (baskets from Umoja Women Craft, Tumaini artisans) to sell in Brazil through FSF's network. Our part is the open tool: a small catalogue, an order list per caravan, and a ledger that shows each artisan what was sold and what they were paid. | Money from outside is the only thing that grows the camp economy (Taylor et al.: $1.51–$1.95 per dollar in Rwanda). Refugees *may* run businesses inside the camp (RLRH, Jan 2026). FSF already has the logistics. | Fair-trade platforms exist, but none is linked to this route. Export rules and payment to refugees must be checked ⚠️. |
| X8 | **Collective buying.** A WhatsApp tool that lets groups pool their $8 to buy maize and beans in bulk directly from Malawian farmers around the camp, at a lower price per kg. | Maize prices doubled, and the transfer is ~$8 against a $28 food basket (allAfrica, 30 Sept 2026). The host community is ~50,000 subsistence farmers who need buyers (IAFR). | Group-buying cooperatives exist in many places; no tool was found at Dzaleka. |
| X9 | **Community currency or time bank.** People trade services (tailoring, tutoring, haircuts, repairs) using credits instead of cash, recorded by phone. | There is almost no cash in the camp, but plenty of skills. In a randomised trial in Kenya, Sarafu community-currency transfers of $30 raised food and water spending by $28 ([Frontiers in Blockchain, 2021](https://www.frontiersin.org/journals/blockchain/articles/10.3389/fbloc.2021.739751/pdf)). | Sarafu is open source (Grassroots Economics). **Legal risk:** the organisation's earlier Kenyan currency (Bangla-Pesa) led to arrests in 2013 before charges were dropped (from memory, not re-sourced ⚠️), so this would need careful checking with Malawian law ⚠️. |

### 3.3 Awareness

| # | Idea | Why (finding) | What already exists |
| --- | --- | --- | --- |
| X10 | **"Live on $8."** A web game: try to feed a family for one month in Dzaleka with real prices and the real transfer. Every choice shows what a family there gives up (a meal, school, soap). It ends with the facts and how to help FSF. In Portuguese, English and French. | The most concrete number in the whole research: ~$8 received against $28 needed (allAfrica, 30 Sept 2026). "The invisible camp" is the awareness angle in §12. | Games like this have been made for other crises (e.g. *Spent*, on US poverty). None was found for Dzaleka. |
| X11 | **"No way out" interactive story.** A scrolling page built on the open dataset (E1): 32 years, three exits all closing, 775 people out vs ~3,600 in during 2025. | Awareness angle 5 (§12), already fully sourced. | Nothing similar found for Dzaleka. |
| X12 | **Camp voices on a map.** The OpenStreetMap base (C1) with short stories, photos and audio recorded by refugees themselves, with consent and no faces or names unless people choose otherwise. | The most-used source in this research was a refugee-run archive (§9). Refugee-made content is more credible than ours. | Dzaleka.com has the archive; a map-based storytelling layer was not found. |

### 3.4 Favourites

Of everything above, three stand out. Each is cheap, small, useful and unlike anything already at Dzaleka:

1. **X10 "Live on $8": the fastest win.** It needs only data we already have and real market prices. It carries no risk to anyone in the camp, and it gives FSF something to share in Brazil. It works for any camp by changing the inputs.
2. **X1 "Is this offer real?": the most protective.** It reaches straight into a documented harm (scams and trafficking), holds no personal data, and could be a printed sheet before it is ever a bot.
3. **X7 "Reverse caravan": the most original.** It turns FSF's existing logistics into income for artisans with no new funding, and our tool is small (catalogue + ledger). It depends on FSF agreeing and on export and payment rules.

G1 (caravan and stock planner) from Section 2 still stands as the tool with a guaranteed user. Together, G1 and X7 make one "caravan" theme: medicines in, crafts out.

## 4. Side-by-side (cluster tools)

| Tool | Real user | Small change | Zero budget | Data safety | Not duplicated | Research value | Replicable |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A1 Law comparator | Possible (Inua) | Better submissions | Yes | Safe | Partly (texts exist) | Medium | High |
| B1 Funding tracker | Possible | Gap made visible | Yes | Safe | Yes | Medium | High |
| C1 Risk & evacuation map | Not yet | Readiness before the rains | Mostly (needs local validation) | Safe (no names) | Partly (base map exists) | **High (PhD)** | High |
| D1 Help directory | Refugees, if kept current | Fewer dead ends | Yes, needs a local owner | Safe if no case data | Yes | Low–medium | High |
| E1 Open dataset | Researchers | Saves others work | Yes, almost done | Safe | Yes | Medium | High (the method) |
| **G1 Caravan & stock planner** | **FSF, guaranteed** | **Fewer stock-outs, less waste** | **Yes** | **Safe (no patient data)** | **Yes (niche)** | Medium | **High** |

## 5. Recommendation

**Pick one awareness piece and one practical tool, and start both small.**

- **Awareness: X10 "Live on $8".** It can be built in weeks from data we already hold, and it creates an audience in Brazil for everything that follows.
- **Practical: choose with the professor between G1 + X7 (the caravan theme, with FSF as the user) and X1 (the scam checker, with refugees as the user).** The caravan theme is safer to start because FSF is a known user. X1 reaches refugees directly, but it needs a partner in the camp (for example a refugee-led organisation) to spread it and keep it accurate.
- **Research track: C1**, the risk and evacuation map, closest to the PhD. **E1** stays as a by-product.

All tools share one rule: **no personal data about refugees leaves the tool, only aggregates or what the person chooses to share.**

## 6. Next steps

1. **Discuss with the professor:** the three favourites plus G1, and which practical tool comes first.
2. **FSF:** ask (a) for the structure of the stock spreadsheet and the next caravan date (G1); (b) whether returning caravans could carry crafts, and whether FSF would sell them in Brazil (X7).
3. **X10:** collect current food prices around Dzaleka/Dowa (maize, beans, oil, soap, school items), with sources and dates.
4. **X1:** gather the scam patterns already reported (UNHCR warnings, the resettlement syndicate case), and ask Inua Advocacy or another refugee-led organisation whether they would co-own it.
5. **C1:** download MapMalawi's OSM data for Dzaleka and check its date and coverage.

## 7. Open questions

- **Phones:** how many people in Dzaleka have a smartphone, WhatsApp and data? This decides whether X1–X5 are apps, bots or paper. Phone access is not confirmed (§8 assumptions).
- **Languages:** which languages matter most (French, Swahili, Kinyarwanda, Kirundi, Somali, English)?
- **G1:** who at FSF would use it day to day, on a laptop or a phone, and is there connectivity at the clinic?
- **X7:** what are Malawi's export rules for crafts, and how can artisans without bank access be paid (mobile money)?
- Is MapMalawi's 2021 data still current, given the camp has grown from ~43,000 to ~63,000?
- **Licence:** MIT for code and CC BY for data is a common pair.
- **Where the code lives:** a new repository, or under the Ethical Tech CoLab organisation where ERCF already lives?

---

## Sources

All linked inline. New sources consulted on 7 Oct 2026: Malawi Voice (1 Jul 2026), AfricanLII, OpenStreetMap wiki (MapMalawi/HOT 2021), GHSC-PSM (OpenLMIS Malawi, 2019), civictech.guide (UNHCR chatbots), JRS (Dzaleka digital pilot), Refugee-Led Research Hub (Jan 2026), IFPRI (Taylor et al., 2016), allAfrica (30 Sept 2026), Nation Online (resettlement syndicate), University of Liverpool / *Lancet Global Health* (Self-Help Plus, 2020), Learning Equality / MIT Solve (Kolibri), Frontiers in Blockchain (Sarafu RCT, 2021). FSF caravan figures come from the team (`RESEARCH_LOG.md`, 5 Oct 2026), not from a public source. All other figures come from `DZALEKA_SITUATION_RESEARCH.md` (section numbers given inline).
