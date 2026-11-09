"""Guards for naming profiles (BENCHMARK_PROTOCOL.md §2.4; DATA_RULES.md DR-1)."""
import json
from pathlib import Path

from namebridge.schema import forbidden_keys

PROFILES = Path(__file__).resolve().parents[1] / "data" / "profiles"


def _profiles():
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(PROFILES.glob("*.json"))]


def test_profiles_exist_and_are_sourced():
    profiles = _profiles()
    assert profiles
    for p in profiles:
        assert p["sources"] and all(s.get("name") for s in p["sources"]), p["profile_id"]


def test_no_element_below_five_occurrences():
    # DR-1.2: only elements seen 5 or more times may be committed.
    for p in _profiles():
        for lst in p.get("elements", {}).values():
            assert all(e["count"] >= 5 for e in lst), p["profile_id"]


def test_no_full_names_or_identifying_rows():
    # Elements are single tokens; a multi-word value would be a full name.
    for p in _profiles():
        for lst in p.get("elements", {}).values():
            assert all(" " not in e["element"] for e in lst), p["profile_id"]


def test_no_ethnicity_clan_or_religion_fields():
    for p in _profiles():
        assert list(forbidden_keys(p)) == [], p["profile_id"]
