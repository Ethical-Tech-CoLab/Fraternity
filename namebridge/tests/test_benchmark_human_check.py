import json

import pytest

from namebridge.benchmark.human_check import STRATA, compare, sample, write
from namebridge.benchmark.queries import build
from namebridge.benchmark.world import PARAMS


@pytest.fixture(scope="module")
def built(tmp_path_factory):
    out = tmp_path_factory.mktemp("bench")
    build(json.loads(PARAMS.read_text(encoding="utf-8")), out, people=8000)
    return out


def test_sample_is_dev_only_stratified_and_reproducible(built, tmp_path):
    pairs = sample(built)
    assert pairs == sample(built)
    counts = {s: sum(p["stratum"] == s for p in pairs) for s in STRATA}
    for s, n in STRATA.items():  # look-alikes are capped by how many the dev split holds
        assert counts[s] == n or (s == "lookalike" and 0 < counts[s] < n)
    split = {}
    for line in (built / "gold" / "people.jsonl").read_text(encoding="utf-8").splitlines():
        p = json.loads(line)
        split[p["id"]] = p["split"]
    for p in pairs:
        ids = p.get("people") or [p["person"]]
        assert all(split[i] == "dev" for i in ids)


def test_page_holds_no_answers(built, tmp_path):
    pairs = sample(built)
    write(pairs, tmp_path)
    shown = json.loads((tmp_path / "pairs.json").read_text(encoding="utf-8"))
    text = json.dumps(shown)
    for word in ("stratum", "answer", "person", "gold", "written_by", "writer", "errors", "lookalike"):
        assert f'"{word}' not in text
    html = (tmp_path / "pair-check.html").read_text(encoding="utf-8")
    assert "__PAIRS__" not in html
    assert html.count('"pair_id"') == len(pairs)


def test_compare(built, tmp_path):
    pairs = sample(built)
    write(pairs, tmp_path)
    (tmp_path / "answers").mkdir()
    for p in pairs[:3]:
        (tmp_path / "answers" / f"{p['pair_id']}.json").write_text(json.dumps({"answer": p["answer"]}))
    other = "different" if pairs[3]["answer"] == "same" else "same"
    (tmp_path / "answers" / f"{pairs[3]['pair_id']}.json").write_text(json.dumps({"answer": other, "note": "x"}))
    res = compare(tmp_path / "key.jsonl", tmp_path)
    assert res["per_stratum"]["all"]["agree"] == 3 and res["per_stratum"]["all"]["disagree"] == 1
    assert len(res["to_review"]) == 1
