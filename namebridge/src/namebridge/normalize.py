"""Name normalisation: parallel search forms with a logged transform path (CONCEPT-IDEA.md §5.4).

A name is never collapsed into one canonical string. `forms(name)` keeps the original
exactly as written and adds parallel forms, recording every step that changed it:

- `nfc`: Unicode NFC (composed and decomposed spellings of the same letter become equal);
- `preserving`: NFC, case-folded, spaces tidied; accents and tone marks KEPT;
- `folded`: accents and tone marks removed, special letters mapped (ŵ→w, ɛ→e, ɔ→o, ŋ→ng),
  apostrophes and hyphens treated as word breaks;
- `variants`: joined and split forms of hyphenated or apostrophe names (Jean-Marie →
  "jean marie", "jeanmarie"), and the form without a filiation particle (mwene, wa).

Why the standard library and not ICU: every name in this corridor is in Latin script, so
ICU's script transliterators are not needed; what is needed is Unicode normalisation,
which Python's `unicodedata` implements (decided 9 Nov 2026, RESEARCH_LOG.md).

Sources for the mappings: ŵ (Chichewa/Chitumbuka, UK Malawi Toponymic Factfile 2025);
ɛ/ɔ (Lingala standard spelling, APiCS survey 60); tone and length marks unwritten in
ordinary Kinyarwanda/Kirundi spelling (Comparative Grammar 2007, Table 28); particles
mwene (Kirundi 'child of', Cox; Simbananiye 2005) and wa (Congolese postnom 'of',
Radio-Canada 2020; CongoNames particle flag).
"""

import re
import unicodedata

# Letters with no Unicode decomposition: removing combining marks leaves them unchanged,
# and an ASCII conversion would silently DROP them (the bug fixed on 9 Nov 2026).
SPECIAL = {"ɛ": "e", "ɔ": "o", "ŋ": "ng", "ɲ": "ny", "ʃ": "sh", "ʒ": "zh", "ß": "ss", "æ": "ae", "œ": "oe", "ø": "o", "đ": "d", "ł": "l"}
APOSTROPHES = "'’ʼ`´‘"
HYPHENS = "-‐‑‒–—"
PARTICLES = {"mwene", "wa"}
_BREAK = "[" + re.escape(APOSTROPHES + HYPHENS) + "]"


def _step(path, name, before, after):
    if before != after:
        path.append({"step": name, "from": before, "to": after})
    return after


def _strip_marks(text):
    decomposed = unicodedata.normalize("NFD", text)
    return unicodedata.normalize("NFC", "".join(c for c in decomposed if not unicodedata.combining(c)))


def forms(name):
    """Return the original name, its parallel search forms and the transform path."""
    original = str(name)
    path = []
    nfc = _step(path, "unicode_nfc", original, unicodedata.normalize("NFC", original))
    preserving = _step(path, "casefold_and_spaces", nfc, re.sub(r"\s+", " ", nfc.casefold()).strip())
    text = _step(path, "remove_accents_and_tone_marks", preserving, _strip_marks(preserving))
    text = _step(path, "map_special_letters", text, "".join(SPECIAL.get(c, c) for c in text))
    text = _step(path, "apostrophes_and_hyphens_to_spaces", text, re.sub(_BREAK, " ", text))
    folded = _step(path, "drop_other_punctuation", text, re.sub(r"\s+", " ", re.sub(r"[^\w ]", " ", text)).strip())

    tokens = folded.split()
    variants = set()
    if re.search(_BREAK, preserving):
        for part in re.split(r"\s+", preserving):
            pieces = [p for p in re.split(_BREAK, part) if p]
            if len(pieces) > 1:
                joined = folded.replace(" ".join(_fold_piece(p) for p in pieces), "".join(_fold_piece(p) for p in pieces))
                variants.add(joined)
    without_particles = [t for t in tokens if t not in PARTICLES]
    if len(without_particles) < len(tokens) and without_particles:
        variants.add(" ".join(without_particles))
    variants.discard(folded)
    return {"original": original, "nfc": nfc, "preserving": preserving, "folded": folded,
            "tokens": tokens, "variants": sorted(variants), "path": path}


def _fold_piece(piece):
    return "".join(SPECIAL.get(c, c) for c in _strip_marks(piece.casefold()))


def fold(name):
    """The folded search form only (accent-free, special letters mapped, word breaks unified)."""
    return forms(name)["folded"]
