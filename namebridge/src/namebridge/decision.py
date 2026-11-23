"""When in doubt, stop: turning a candidate's evidence into a status (Dzaleka SOP 2019; ICRC RFL 8.3.2).

Principle (docs/G4_REVERSE_STRESS.md §5B): a match is never confirmed on doubt. Every status other
than "strong_evidence" stops the process and goes to a person. The function never confirms a match
on its own; a human decides every confirmation.

Statuses are kept apart (feedback: never collapse epistemic states):
  conflict              a verified field contradicts the match: stop, not a match
  insufficient_evidence the score is below the possible threshold: stop
  ambiguous             a second candidate is nearly as good: stop, the caseworker chooses
  needs_independent_check a child's match with no check that avoids names: stop
  possible              some evidence, not enough to be strong: stop
  strong_evidence       clear score, clear margin, no conflict, and for a child an independent check

The thresholds are inputs, not defaults. The numbers are decided by the owner (G4, DECISIONS_OPEN.md),
so the code cannot run without them.
"""

from dataclasses import dataclass, field

STATUSES = ("conflict", "insufficient_evidence", "ambiguous", "needs_independent_check",
            "possible", "strong_evidence")


@dataclass(frozen=True)
class Thresholds:
    possible: float        # score at or above which a candidate is worth a human look
    strong: float          # score at or above which a candidate may be "strong evidence"
    margin: float          # gap to the next-best candidate needed to avoid "ambiguous"

    def __post_init__(self):
        if not (0.0 <= self.possible <= self.strong <= 1.0) or not (0.0 <= self.margin <= 1.0):
            raise ValueError("thresholds must satisfy 0 <= possible <= strong <= 1 and 0 <= margin <= 1")


@dataclass(frozen=True)
class Candidate:
    record_id: str
    score: float                     # 0..1, from any matcher; not a probability
    minor: bool                      # the sought person is under 18 at the time of the search
    independent_check: bool = False  # a check that did not use names (e.g. a verified reciprocal match)
    conflicts: tuple = ()            # verified fields that contradict the match, e.g. ("birth_year",)


@dataclass(frozen=True)
class Verdict:
    record_id: str
    status: str
    reasons: tuple = field(default=())

    @property
    def stopped(self):
        return self.status != "strong_evidence"


def decide(candidates, thresholds):
    """Return one verdict per candidate. Nothing here confirms a match: a person does."""
    if not isinstance(thresholds, Thresholds):
        raise TypeError("thresholds are required: they are decided by the owner (G4), not by default")
    ranked = sorted(candidates, key=lambda c: c.score, reverse=True)
    verdicts = []
    for c in ranked:
        # the rival is the best OTHER candidate: a candidate below another one is never "strong"
        others = [o.score for o in ranked if o is not c]
        rival = max(others) if others else 0.0
        verdicts.append(_one(c, rival, thresholds))
    return verdicts


def _one(c, rival_score, t):
    if c.conflicts:
        return Verdict(c.record_id, "conflict", tuple(f"verified conflict: {f}" for f in c.conflicts))
    if c.score < t.possible:
        return Verdict(c.record_id, "insufficient_evidence", (f"score {c.score:.3f} below {t.possible}",))
    if c.score < t.strong:
        return Verdict(c.record_id, "possible", (f"score {c.score:.3f} below strong {t.strong}",))
    if c.score - rival_score < t.margin:
        return Verdict(c.record_id, "ambiguous",
                       (f"best other candidate {rival_score:.3f} within margin {t.margin}",))
    if c.minor and not c.independent_check:
        return Verdict(c.record_id, "needs_independent_check",
                       ("a child is never confirmed on names alone",))
    return Verdict(c.record_id, "strong_evidence", ())
