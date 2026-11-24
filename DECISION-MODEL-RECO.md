# Decision-model recommendation: source and claim triage

Date: 2026-10-11. Status: research-workflow proposal.
Scope: this repository. Public evidence only; no live experiment.

## Research boundaries

Reviewed revision `8a82b42483ab87344b1f88e5ba4528f98b774cdf`:
[README](https://github.com/Ethical-Tech-CoLab/Fraternity/blob/8a82b42483ab87344b1f88e5ba4528f98b774cdf/README.md)
and [concept](https://github.com/Ethical-Tech-CoLab/Fraternity/blob/8a82b42483ab87344b1f88e5ba4528f98b774cdf/CONCEPT.md).
This is a document-level assessment.

The project organizes research across legal/policy, funding, disaster/risk and
protection pathways, retaining source, date and period for claims. Conflicting
figures are not silently reconciled. The solutions phase focuses on Dzaleka.

## Recommended use

Use bounded decisions to assist researchers with:

- multi-label source routing to the existing pathways;
- duplicate-report or syndicated-source detection;
- exact source/claim support triage;
- ranking already retrieved documents for a specific research question.

For multi-label routing, ask independent membership questions rather than
forcing every document into one mutually exclusive Choice. Include
insufficient evidence; keep source and time-period metadata.

Perform exact quote and numeric/date checks deterministically. Related reports
may depend on the same original source and are not independent corroboration.
Contradictions should create review items, not an averaged synthesized fact.

## Non-goals and models

Never rank displaced people by deservingness, infer individual eligibility,
automate protection decisions, or turn model certainty into authoritative
policy facts. No sensitive person-level records should enter this pilot.

Compare human/checklist review and lexical retrieval with a local reranker,
Jev's [citation](https://docs.typesafe.ai/cookbooks/citation_check.md) and
[batching](https://docs.typesafe.ai/cookbooks/parallel_questions.md) recipes,
Microsoft-Decision-1 and Sage on approved public sources. Exact proprietary
checkpoints are not locally runnable; local candidates need their own license
and quality assessment.

## Test design

Use question/report-family/time-disjoint examples, including superseded
policies, different reporting periods, quoted claims without endorsement,
multi-pathway reports and contradictory figures. Have researchers adjudicate
path membership and support labels.

Measure pathway recall, unsupported-claim false acceptance, duplicate-family
precision, retrieval recall, calibration, reviewer time and total cost per
accepted source record. Check regional/language/period slices where labeled
data supports conclusions.

Gate: all dates, caveats and disagreements remain visible; no published claim
changes without human review. Reject any apparent saving obtained by dropping
hard or under-documented cases. Missing evidence remains missing.

## Pilot

Start with an archived public-source batch and preserve unchanged originals.
Add only derived routing/support annotations. This recommendation does not
propose a runtime change in humanitarian operations or any related project.
