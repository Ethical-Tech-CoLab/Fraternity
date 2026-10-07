# Online microwork and paid surveys — can Dzaleka refugees earn and actually get the money?

Researched 7 Oct 2026 with Tavily. **Status: desk research only; nothing here has been tested by someone in the camp.** Related: `SOLUTIONS.md`.

**Question:** sites that pay for simple online tasks (surveys, data labelling, AI training, small checks) exist. Could refugees in Dzaleka use them, get paid, and turn the payment into money they can spend?

**Short answer: possible, but narrow and fragile.** A few platforms accept Malawi and pay through Payoneer. The money can reach a bank account inside the camp. But along the way it loses about half its real value at Malawi's official exchange rate. The ID check may block refugees, and scams are common. It is worth doing only with a verified guide and people in the camp who have already been paid.

---

## 1. The chain the money must travel

```
Task done → platform pays → payout service → bank / mobile money in Malawi → cash in kwacha
```

Every link has to work. The research found the following for each one.

### 1.1 Payout services

| Service | Works in Malawi? | Notes |
| --- | --- | --- |
| **PayPal** | **No** | Not available to receive or withdraw in Malawi ([OneSafe](https://www.onesafe.io/blog/does-paypal-work-in-malawi); [Wise](https://wise.com/gb/hub/payment-methods/malawi)). This blocks every PayPal-only platform. |
| **Payoneer** | **Yes** (Malawi listed) | Withdraws to a local bank. Fees of 1–4% plus up to 2% currency markup ([Payoneer FAQ](https://payoneer.custhelp.com/app/answers/detail/a_id/18605/~/withdraw-to-bank---faq)). **ID check:** it asks for government ID (passport, national ID, driving licence) and **does not list refugee ID** ([Payoneer](https://payoneer.custhelp.com/app/answers/detail/a_id/34658/~/document-verification-%E2%80%93-faq)). Whether a Malawian refugee document passes is **unknown ⚠️**. |
| **Airtm** | Unclear | A US-dollar wallet that cashes out peer-to-peer. Used by Outlier. No confirmed route to Malawian mobile money. |
| **Wise** | Accepts refugee ID for verification ([Wise](https://wise.com/help/articles/DXdm1XINRFievCdLcpzZQ/verification-for-refugees)) | Few task platforms pay through Wise; Malawi coverage is not confirmed. |

### 1.2 Accounts in Malawi

- **Bank:** **Centenary Bank has an agency inside Dzaleka with 17,420 accounts, "representing all families in the camp"**. It handles remittances and foreign-exchange transactions ([Crown Agents Bank case study](https://www.crownagentsbank.com/case-study/advancing-financial-inclusion-for-one-of-the-most-excluded-populations-refugees)). **This is the most realistic place for Payoneer withdrawals.** Whether Centenary accepts Payoneer transfers is not confirmed ⚠️.
- **Mobile money (Airtel Money, TNM Mpamba):** in 2018 refugees could not register SIM cards because a Malawian national ID was required ([Malawi24, 2018](https://malawi24.com/2018/04/19/no-arrangement-yet-for-refugees-to-register-sim-cards)). Whether this has changed is **not confirmed for Malawi**. Kenya changed its rules in 2025, and a search result that seemed to say otherwise was about Kenya, not Malawi.

### 1.3 The exchange-rate problem (the biggest catch)

Money from abroad arrives in US dollars and is converted to kwacha by the bank **at or near the official rate, ~MWK 1,750 per dollar**. On the street, a dollar is worth **MWK 3,500–4,500**: a premium of 100–157% in 2025, according to Malawi's Chamber of Commerce ([MCCCI, June 2026](https://www.mccci.org/wp-content/uploads/2026/06/A-CALL-FOR-ACTION-THE-URGENT-CASE-FOR-EXCHANGE-RATE-UNIFICATION-June-2026-pdf.pdf)). Prices in the camp follow the real market (maize doubled). So **$10 earned online buys roughly what $4–5 would buy at market value** (*derived*). Holding dollars in a foreign-currency account is possible for people earning abroad, but new 2025 forex rules restrict cash and transfers ([US State Dept, 2026](https://www.state.gov/reports/2026-investment-climate-statements/malawi)). Selling dollars on the parallel market is illegal.

## 2. Platforms

| Platform | Type of task | Accepts Malawi? | Pays via | Verdict |
| --- | --- | --- | --- | --- |
| **Toloka** | Labelling images/audio, small checks | Yes (Malawi not on its restricted list) | **Payoneer only**; minimum $20, $1 fee ([Toloka eligibility](https://toloka.ai/legal/eligibility-and-geographic-restrictions)) | **Candidate** |
| **Clickworker** | Short text, surveys, checks | "Multiple countries" | PayPal, **Payoneer** (min €20) ([Clickworker](https://support-workplace.clickworker.com/support/solutions/articles/80000672350-what-payment-options-do-i-have-)) | **Candidate** via Payoneer |
| **Outlier (AI training)** | Writing and evaluating AI answers | **Malawi listed** ([Outlier](https://outlier.ai/legal/flexible-working-guidelines)) | PayPal, Airtm, ACH | Pays better (up to ~$11/h on core projects) but needs strong English or expertise and passes a test; payout route from Malawi unclear |
| **Premise** | Local surveys, photos | 140+ countries; Malawi not confirmed | Payoneer, crypto | To check |
| **Prolific (academic surveys)** | Research surveys | Malawi in the "small populations" list | **PayPal only** | **Blocked in practice** (no PayPal in Malawi) |
| **Appen / CrowdGen** | Labelling, transcription | Payoneer table lists Kenya, Tanzania, Zambia, not Malawi ([CrowdGen](https://crowdgen.com/docs/payments/general-payments-faq/payout-options-and-fees)) | Payoneer / others | Unclear |
| **Upwork** (freelancing, not microtasks) | Data entry, translation, design | Yes | **Payoneer** | **Proven at Dzaleka**: a UNHCR-supported cohort of 54 refugees earned $20,000+ in 6 months ([UNHCR Innovation](https://medium.com/unhcr-innovation-service/paving-a-way-to-digital-livelihoods-357f85ad1145)) |
| Generic "paid survey" sites | Surveys | Varies | Often PayPal or gift cards | **High scam risk**; avoid |

## 3. What people realistically earn

- **Data annotators in Uganda:** about **$1.40 per hour** ([ILO, 2021](https://www.ilo.org/sites/default/files/wcmsp5/groups/public/@ed_emp/documents/publication/wcms_816539.pdf)). Refugee platform workers in the same study took home about $11 a day working ~5 hours.
- **Microtask workers worldwide:** **$3.78–$5.55 per hour** on average ([meta-analysis, 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9425816)).
- Work is **irregular**, and African accounts often see few tasks. A refugee annotator in Lebanon called the workload and income "irregular" ([Humans in the Loop / Data Workers' Inquiry](https://data-workers.org/roukaya)).
- **For scale:** the WFP transfer is ~$8 per person per month (`SOLUTIONS.md`). Even 10 hours of work at $2 an hour, $20, would more than double it on paper, though less after the exchange-rate loss.

## 4. Barriers specific to refugees

| Barrier | Evidence |
| --- | --- |
| Device, data and electricity | The main barriers in Kakuma and Dadaab ([ILO, Digital refugee livelihoods](https://www.ilo.org/media/386221/download)) |
| ID / KYC checks | UNHCR calls "regulatory exclusion" one of the main challenges. In Kenya, refugees borrowed locals' IDs ("proxy IDs"), which exposed them to fraud and legal risk ([UNHCR Innovation](https://medium.com/unhcr-innovation-service/the-identity-issue-digital-risks-of-proxy-ids-in-kenyas-digital-economy-52eec129ebea)) |
| Scams | Malawians lose ~MWK 120 million a month to mobile-money scams ([Rest of World, 2023](https://restofworld.org/2023/malawi-kwacha-scam-sim-card)). Fake job offers asking for fees are common, and refugees report job offers that "didn't materialise in exchange for a fee" (UNHCR Innovation) |
| Legal status | Online work by refugees in Malawi is a "grey area" ([Refugee-Led Research Hub, 2026](https://refugeeledresearch.org/wp-content/uploads/2026/01/MALAWI.pdf)) |
| Fairness | Impact-sourcing firms have been criticised for pay of ~$1.50–2 per hour and hard content ([Sama controversy](https://en.wikipedia.org/wiki/Sama_(company))) |

## 5. What this means for us

We cannot test the chain ourselves: we are not in Malawi and we don't have a refugee ID. But **people in the camp already know which routes work**: TakenoLAB reports 200+ online jobs, and the Upwork cohort was paid. What is missing is that this knowledge is scattered and unverified, while scams are everywhere.

**What we could build (zero cost, fits Option 1 in `SOLUTIONS.md`): a verified "online work that really pays" guide for Dzaleka.**
- Which platforms accept Malawi, **confirmed by residents who were actually paid**.
- The step-by-step payout route, for example Payoneer to Centenary Bank, with the documents that worked.
- An honest note on fees and the exchange-rate loss.
- Scam warning signs, such as never paying a fee to get work.
- In Swahili and French, on DOS, and read on Yetu Radio.
- Optionally, a simple "did it pay?" report form, so the guide stays current through the community.

**Before building anything, ask TakenoLAB and Dzaleka Connect:**
1. Which platforms have paid people in Dzaleka?
2. How did the money arrive (Payoneer? which bank? mobile money)?
3. Which ID did Payoneer accept?
4. What did they lose in conversion?

## 6. Open questions

- Does Payoneer accept a Malawian refugee document for verification?
- Does Centenary Bank's Dzaleka agency receive Payoneer withdrawals, and at what rate?
- Can refugees now register Airtel Money or TNM Mpamba with their refugee ID?
- How many tasks do Malawian accounts actually get on Toloka and Clickworker?
