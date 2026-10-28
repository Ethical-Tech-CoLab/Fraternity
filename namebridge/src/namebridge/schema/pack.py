"""Country/language pack: template and validator (CONCEPT-IDEA.md §11).

A pack separates cultural practice, legal-document practice and database
convention, and allows "unknown" and "disputed" instead of forcing a rule.

The sound layer (§5.4A) adds three lists: the language's sounds, including
digraphs that are one sound (mb, nd, cy, rw); how each sound is written by
someone who writes in another language (French "ou" for /w/); and the sounds
a listener tends to confuse (Rwanda-Rundi r/l). They let a name told aloud,
for example by a child who cannot write, be matched by sound.

Template: data/packs/TEMPLATE.json.

Run: python -m namebridge.schema.pack data/packs/<pack>.json
"""

import json
import re
import sys

from namebridge.schema import forbidden_keys

REQUIRED = (
    "pack_id", "languages", "scripts", "regions", "name_structures", "order_rules",
    "particles_and_morphemes", "transliteration_rules", "phonetic_rules",
    "common_administrative_forms", "phoneme_inventory", "spelling_conventions", "listener_confusions",
    "relationship_implications", "known_failure_modes",
    "protected_or_sensitive_forms", "benchmark_cases", "reviewers", "version",
)
LIST_FIELDS = REQUIRED[4:13] + ("known_failure_modes", "protected_or_sensitive_forms", "benchmark_cases", "reviewers")
SOUND_FIELDS = ("phoneme_inventory", "spelling_conventions", "listener_confusions")
RULE_FIELDS = (
    "name_structures", "order_rules", "particles_and_morphemes", "transliteration_rules",
    "phonetic_rules", "common_administrative_forms",
) + SOUND_FIELDS
IMPLICATION_VALUES = {"weak", "neutral", "strong", "context-dependent", "unknown", "disputed"}
PRACTICE_KINDS = {"cultural", "legal_document", "database"}
CONFIDENCE_LEVELS = {"high", "medium", "low", "unknown", "disputed", "hypothesis"}

_SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
_PACK_ID = re.compile(r"^[a-z]{2}(-[a-z0-9]+)+-\d{4}\.\d+$")


def validate_pack(pack):
    pid = pack.get("pack_id", "?")
    errors = [f"pack {pid}: missing {f!r}" for f in REQUIRED if f not in pack]
    if errors:
        return errors
    if not _PACK_ID.match(pack["pack_id"]):
        errors.append(f"pack {pid}: pack_id must look like 'rw-kiny-2026.1'")
    if not _SEMVER.match(str(pack["version"])):
        errors.append(f"pack {pid}: version must be semver (e.g. 0.1.0)")
    for f in LIST_FIELDS:
        if not isinstance(pack[f], list):
            errors.append(f"pack {pid}: {f} must be a list")

    # Every entry of every rule list needs a source and a confidence; structure
    # and order rules also say which practice they describe.
    for f in RULE_FIELDS:
        for i, rule in enumerate(pack[f] if isinstance(pack[f], list) else []):
            where = f"pack {pid}: {f}[{rule.get('id', i)}]"
            if not isinstance(rule, dict):
                errors.append(f"{where}: must be an object with a source")
                continue
            if not rule.get("source"):
                errors.append(f"{where}: every rule needs a source")
            if rule.get("confidence") not in CONFIDENCE_LEVELS:
                errors.append(f"{where}: confidence must be one of {sorted(CONFIDENCE_LEVELS)}")
            if f in ("name_structures", "order_rules") and rule.get("practice") not in PRACTICE_KINDS:
                errors.append(f"{where}: practice must be one of {sorted(PRACTICE_KINDS)}")

    for i, conv in enumerate(pack["spelling_conventions"] if isinstance(pack["spelling_conventions"], list) else []):
        if not conv.get("writer_language") or not conv.get("sound") or not conv.get("spellings"):
            errors.append(f"pack {pid}: spelling_conventions[{i}] needs writer_language, sound and spellings")
    for i, conf in enumerate(pack["listener_confusions"] if isinstance(pack["listener_confusions"], list) else []):
        if len(conf.get("sounds", [])) < 2:
            errors.append(f"pack {pid}: listener_confusions[{i}] needs at least two sounds")

    impl = pack["relationship_implications"]
    for f in ("surname_agreement", "surname_disagreement"):
        if impl.get(f) not in IMPLICATION_VALUES:
            errors.append(f"pack {pid}: relationship_implications.{f} must be one of {sorted(IMPLICATION_VALUES)}")

    for key in forbidden_keys(pack):
        errors.append(f"pack {pid}: forbidden attribute {key!r} (packs never encode ethnicity, clan or religion)")
    return errors


if __name__ == "__main__":
    problems = []
    for path in sys.argv[1:]:
        with open(path, encoding="utf-8") as f:
            problems.extend(validate_pack(json.load(f)))
    print("\n".join(problems) or "valid")
    sys.exit(1 if problems else 0)
