import json
from pathlib import Path

from namebridge.schema.pack import validate_pack

PACKS = Path(__file__).resolve().parents[1] / "data" / "packs"


def template():
    return json.loads((PACKS / "TEMPLATE.json").read_text(encoding="utf-8"))


def test_template_is_valid():
    assert validate_pack(template()) == []


def test_every_pack_in_repo_is_valid():
    for path in PACKS.glob("*.json"):
        assert validate_pack(json.loads(path.read_text(encoding="utf-8"))) == [], path.name


def test_unknown_and_disputed_allowed():
    pack = template()
    pack["relationship_implications"] = {"surname_agreement": "disputed", "surname_disagreement": "context-dependent"}
    assert validate_pack(pack) == []


def test_rule_needs_source_and_practice():
    pack = template()
    pack["name_structures"][0].update(source="", practice="folk")
    assert len(validate_pack(pack)) == 2


def test_pack_cannot_encode_ethnicity():
    pack = template()
    pack["name_structures"][0]["ethnic_group"] = "any"
    assert any("forbidden attribute" in e for e in validate_pack(pack))


def test_sound_entries_need_source():
    pack = template()
    pack["listener_confusions"][0]["source"] = ""
    assert any("needs a source" in e for e in validate_pack(pack))


def test_confusion_needs_two_sounds():
    pack = template()
    pack["listener_confusions"][0]["sounds"] = ["/r/"]
    assert any("two sounds" in e for e in validate_pack(pack))


def test_spelling_convention_names_the_writer():
    pack = template()
    del pack["spelling_conventions"][0]["writer_language"]
    assert any("writer_language" in e for e in validate_pack(pack))
