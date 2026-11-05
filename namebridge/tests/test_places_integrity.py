"""Structural checks on the place data. Added 5 Nov 2026 after an over-broad
filter silently removed the 42 commune -> province links: any such loss, or a
dangling unit or source, now fails here."""
import json
from collections import Counter, defaultdict
from pathlib import Path

PLACES = Path(__file__).resolve().parents[1] / "data" / "places" / "places-2026.1.json"
TEMPORAL = {"renamed_to", "merged_into", "split_into", "continues_as"}
CURRENT = {"2025-", "2006-", "1966-", "2015-", "1962-", "1988-", "current", "1997-2015"}


def load():
    d = json.loads(PLACES.read_text(encoding="utf-8"))
    out, inn = defaultdict(list), defaultdict(list)
    for c in d["changes"]:
        out[c["from"]].append(c)
        inn[c["to"]].append(c)
    return d, {u["key"]: u for u in d["units"]}, out, inn


def test_no_orphan_units():
    _, units, out, inn = load()
    assert [k for k in units if not out[k] and not inn[k]] == []


def test_no_duplicate_links():
    d, *_ = load()
    counts = Counter((c["from"], c["to"], c["relation"]) for c in d["changes"])
    assert [k for k, v in counts.items() if v > 1] == []


def test_every_old_unit_has_a_successor():
    _, units, out, _ = load()
    ended = [k for k, u in units.items() if u["period"] not in CURRENT
             and not any(c["relation"] in TEMPORAL for c in out[k])]
    assert ended == []


def test_every_sub_province_unit_is_placed():
    _, units, out, _ = load()
    levels = {"commune", "zone", "quarter", "district", "town", "sector", "territory", "admin2"}
    # Current units must be placed; old ones reach a placed unit through their
    # successor (test_every_old_unit_has_a_successor).
    unplaced = [k for k, u in units.items() if u["level"] in levels and u["period"] in CURRENT
                and not any(c["relation"] == "located_in" for c in out[k])]
    assert unplaced == []


def test_crosswalk_shares_cover_each_old_commune():
    d, *_ = load()
    total = defaultdict(float)
    for c in d["changes"]:
        if c.get("share") is not None:
            total[c["from"]] += c["share"]
    assert {k: v for k, v in total.items() if v < 0.9} == {}


def test_sources_are_defined_and_used():
    d, units, *_ = load()
    used = {s for c in d["changes"] for s in c["sources"]}
    for u in units.values():
        used |= {u.get("name_source")} | set(u.get("name_also_in", []))
        for o in u.get("other_names", []):
            used |= {o.get("source")} | set(o.get("also_in", []))
    used.discard(None)
    assert used - set(d["sources"]) == set()
    assert set(d["sources"]) - used == set()
