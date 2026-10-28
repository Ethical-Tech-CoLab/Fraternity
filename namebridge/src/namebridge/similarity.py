"""String similarity for names (standard library only).

Jaro-Winkler (Winkler 1990), compared on folded forms: case-folded, with
diacritics removed. The folded form is for comparison only; the original
text is always kept (CONCEPT-IDEA.md §5.3).
"""

import unicodedata


def fold(text):
    decomposed = unicodedata.normalize("NFKD", text.casefold())
    return "".join(c for c in decomposed if not unicodedata.combining(c))


def jaro(a, b):
    if a == b:
        return 1.0
    if not a or not b:
        return 0.0
    window = max(max(len(a), len(b)) // 2 - 1, 0)
    a_hits, b_hits = [False] * len(a), [False] * len(b)
    matches = 0
    for i, ch in enumerate(a):
        for j in range(max(0, i - window), min(i + window + 1, len(b))):
            if not b_hits[j] and b[j] == ch:
                a_hits[i] = b_hits[j] = True
                matches += 1
                break
    if not matches:
        return 0.0
    a_seq = [c for c, hit in zip(a, a_hits) if hit]
    b_seq = [c for c, hit in zip(b, b_hits) if hit]
    transpositions = sum(x != y for x, y in zip(a_seq, b_seq)) / 2
    return (matches / len(a) + matches / len(b) + (matches - transpositions) / matches) / 3


def jaro_winkler(a, b, prefix_scale=0.1):
    a, b = fold(a), fold(b)
    j = jaro(a, b)
    prefix = 0
    for x, y in zip(a[:4], b[:4]):
        if x != y:
            break
        prefix += 1
    return j + prefix * prefix_scale * (1 - j)
