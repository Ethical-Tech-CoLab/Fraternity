"""Every pack rule cited in docs/INTAKE_GUIDE.md must exist, so the guide never points at nothing."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PACKS = {"rw-kiny": "rw-kiny-2026.1", "bi-kirundi": "bi-kirundi-2026.1", "cd-swc-ln": "cd-swc-ln-2026.1"}


def _ids(pack):
    data = json.loads((ROOT / "namebridge" / "data" / "packs" / f"{pack}.json").read_text(encoding="utf-8"))
    return {e["id"] for v in data.values() if isinstance(v, list) for e in v if isinstance(e, dict) and "id" in e}


def test_cited_pack_rules_exist():
    text = (ROOT / "docs" / "INTAKE_GUIDE.md").read_text(encoding="utf-8")
    missing = []
    for ref in re.findall(r"`([^`]+)`", text):
        for part in re.split(r",\s*", ref):
            m = re.match(r"^(rw-kiny|bi-kirundi|cd-swc-ln):([a-z0-9-]+)$", part.strip())
            if m and m.group(2) not in _ids(PACKS[m.group(1)]):
                missing.append(part)
    # bare ids that follow a prefixed one in the same parenthesis, e.g. (`cd-swc-ln:a`, `b`)
    for prefix, rest in re.findall(r"`(rw-kiny|bi-kirundi|cd-swc-ln):[a-z0-9-]+`((?:,\s*`[a-z0-9-]+`)+)", text):
        for rid in re.findall(r"`([a-z0-9-]+)`", rest):
            if rid not in _ids(PACKS[prefix]):
                missing.append(f"{prefix}:{rid}")
    assert missing == [], missing
