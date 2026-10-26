"""Minimum benchmark size, derived from the targets in BENCHMARK_PROTOCOL.md §7.

Run: python -m namebridge.benchmark.sample_size
"""

from math import ceil, comb, sqrt
from statistics import NormalDist

# Targets and design assumptions (BENCHMARK_PROTOCOL.md §2.1, §6, §7)
CONFIDENCE = 0.95
ADULT_MAX_FALSE_MATCH = 0.01  # precision >= 0.99 at confirmation
MINOR_MAX_FALSE_MATCH = 0.001  # precision >= 0.999 at confirmation
ALLOWED_FALSE_MATCHES = 1  # the bound must hold even with one false match
RECALL_TARGET = 0.95  # recall@20 at retrieval
EXPECTED_RECALL = 0.97
GAP_BEST_FNR = 0.05  # fairness: detect a slice missing 1.5x more often than the best
GAP_RATIO = 1.5
GAP_POWER = 0.80
DESIGN_EFFECT = 1.6  # families: 1 + (3 - 1) * 0.3
RECORDS_PER_PERSON = 3
TRUE_PAIRS_PER_PERSON = comb(RECORDS_PER_PERSON, 2)
KEY_SLICES = 6  # 3 origins x (child, adult)
MINOR_SHARE = 0.5
TEST_SHARE = 0.2


def error_upper_bound(errors, n, confidence=CONFIDENCE):
    """One-sided Clopper-Pearson upper bound on an error rate."""

    def cdf(p):
        return sum(comb(n, i) * p**i * (1 - p) ** (n - i) for i in range(errors + 1))

    lo, hi = 0.0, 1.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if cdf(mid) > 1 - confidence:
            lo = mid
        else:
            hi = mid
    return hi


def pairs_for_error_bound(max_error, errors=ALLOWED_FALSE_MATCHES):
    """Smallest n whose upper bound stays at or under max_error with `errors` false matches."""
    n, step = errors + 1, 1000
    while True:
        if error_upper_bound(errors, n) <= max_error:
            if step == 1:
                return n
            n, step = n - step, step // 10
        n += step


def wilson_lower(successes, n, confidence=CONFIDENCE):
    z = NormalDist().inv_cdf(1 - (1 - confidence) / 2)
    p = successes / n
    centre = p + z * z / (2 * n)
    spread = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (centre - spread) / (1 + z * z / n)


def queries_for_recall(target=RECALL_TARGET, observed=EXPECTED_RECALL):
    n = 10
    while wilson_lower(round(observed * n), n) < target:
        n += 1
    return n


def pairs_for_gap(best=GAP_BEST_FNR, ratio=GAP_RATIO, power=GAP_POWER, alpha=0.05):
    """Pairs per slice to detect a false-non-match rate `ratio` times the best one."""
    worse = best * ratio
    z_a = NormalDist().inv_cdf(1 - alpha / 2)
    z_b = NormalDist().inv_cdf(power)
    mean = (best + worse) / 2
    top = z_a * sqrt(2 * mean * (1 - mean)) + z_b * sqrt(best * (1 - best) + worse * (1 - worse))
    return ceil(top**2 / (worse - best) ** 2)


def minimum_people():
    """Total invented people needed, and the binding constraint."""
    gap_persons_per_slice = ceil(pairs_for_gap() * DESIGN_EFFECT / TRUE_PAIRS_PER_PERSON)
    by_fairness = gap_persons_per_slice * KEY_SLICES / TEST_SHARE

    minor_pairs = pairs_for_error_bound(MINOR_MAX_FALSE_MATCH) * DESIGN_EFFECT
    minor_test_persons = ceil(minor_pairs / TRUE_PAIRS_PER_PERSON)
    by_minor_precision = minor_test_persons / MINOR_SHARE / TEST_SHARE

    total = ceil(max(by_fairness, by_minor_precision))
    binding = "minor precision" if by_minor_precision >= by_fairness else "fairness slices"
    return {
        "by_fairness": ceil(by_fairness),
        "by_minor_precision": ceil(by_minor_precision),
        "total": total,
        "binding": binding,
    }


def main():
    print("Per-target minimums in the test set")
    print(f"  adult precision >= 0.99 : {pairs_for_error_bound(ADULT_MAX_FALSE_MATCH)} pairs (1 false match allowed)")
    print(f"  minor precision >= 0.999: {pairs_for_error_bound(MINOR_MAX_FALSE_MATCH)} pairs (1 false match allowed)")
    print(f"  recall@20 >= 0.95       : {queries_for_recall()} queries per slice (if 0.97 observed)")
    print(f"  fairness gap 1.5x       : {pairs_for_gap()} pairs per slice (power 80%)")
    print(f"  design effect (families): x{DESIGN_EFFECT}")
    size = minimum_people()
    print("\nTotal invented people")
    print(f"  from fairness slices    : {size['by_fairness']}")
    print(f"  from minor precision    : {size['by_minor_precision']}")
    print(f"  minimum                 : {size['total']} (binding: {size['binding']})")


if __name__ == "__main__":
    main()
