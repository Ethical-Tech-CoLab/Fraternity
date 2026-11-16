import json

from namebridge.benchmark.realism import jsd, ngrams, run
from namebridge.benchmark.world import PARAMS


def test_jsd_properties():
    a = {"x": 1, "y": 1}
    assert jsd(a, a) == 0
    assert abs(jsd({"x": 1}, {"y": 1}) - 1.0) < 1e-9
    assert jsd({"x": 3, "y": 1}, {"x": 1, "y": 3}) == jsd({"x": 1, "y": 3}, {"x": 3, "y": 1})


def test_ngrams():
    assert ngrams(["kasongo"], 3, {"ong", "ngo"}) == {"ong": 1, "ngo": 1}


def test_realism_report_uses_the_fixed_limits():
    params = json.loads(PARAMS.read_text(encoding="utf-8"))
    result = run(params, people=3000)
    limits = params["realism_limits"]["checks"]
    assert set(result["fidelity"]) == set(limits)
    for key, check in result["fidelity"].items():
        assert check["limit"] == limits[key].get("limit", limits[key].get("limit_chars"))
    for origin in ("RW", "BI", "CD"):
        c = result["copy_test"][origin]
        assert 0 <= c["full_names_only_listed_elements"] <= 1 and 0 <= c["invented_element_rate"] <= 1
