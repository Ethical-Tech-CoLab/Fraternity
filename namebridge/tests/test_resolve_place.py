from pathlib import Path

import pytest

from namebridge.resolve_place import PlaceIndex, fold

GRAPH = Path(__file__).resolve().parents[1] / "data" / "graph"


@pytest.fixture(scope="module")
def index():
    return PlaceIndex(GRAPH)


def names(rows, kind=None):
    return {r["name"] for r in rows if kind is None or r["kind"] == kind}


def test_fold_ignores_case_accents_hyphens_and_prefixes():
    assert fold("Nyanza-Lac") == fold("NYANZA LAC") == fold("Nyanza Lac")
    assert fold("Quartier Rohero") == fold("Rohero")
    assert fold("Province du Nord") == fold("Nord")
    assert fold("Élisabethville") == fold("Elisabethville")


def test_old_name_finds_the_new_one(index):
    # A child says the old province; records use the 2025 one.
    assert "Butanyerera" in names(index.resolve("Kayanza", "BI"), "later")


def test_new_name_finds_the_old_ones(index):
    rows = index.resolve("Butanyerera")
    assert {"Kayanza", "Kirundo", "Ngozi"} <= names(rows, "earlier")


def test_new_name_does_not_jump_to_siblings(index):
    # Kayanza -> Butanyerera must not continue back to Kirundo or Ngozi.
    assert not {"Kirundo", "Ngozi"} & names(index.resolve("Kayanza", "BI"))


def test_bujumbura_2010_commune_reaches_today(index):
    rows = index.resolve("Kamenge")
    assert {"Ntahangwa", "Bujumbura"} <= names(rows, "within")


def test_variant_spelling_finds_the_official_commune(index):
    rows = index.resolve("Nyanrusange")
    assert "Nyarusange" in names(rows, "match")
    assert "Gishubi" in names(rows, "later")
    assert next(r for r in rows if r["name"] == "Gishubi")["derived"]


def test_kinyarwanda_and_french_province_names(index):
    for spoken in ("Intara y'Amajyaruguru", "Province du Nord"):
        assert "Northern Province" in names(index.resolve(spoken), "match")


def test_one_name_many_places(index):
    # Cibitoke: an old province, a 2025 commune, and a zone of Bujumbura city.
    levels = {(r["level"], r["period"]) for r in index.resolve("Cibitoke", "BI") if r["kind"] == "match"}
    assert {("province", "pre2025"), ("commune", "2025-"), ("commune", "2010")} <= levels


def test_colonial_city_names(index):
    assert "Lubumbashi" in names(index.resolve("Élisabethville"), "later")
    assert "Astrida" in names(index.resolve("Butare", "RW"), "earlier")


def test_country_filter(index):
    # Muhanga is a Burundian commune and a Rwandan district.
    assert {r["country"] for r in index.resolve("Muhanga")} >= {"BI", "RW"}
    assert {r["country"] for r in index.resolve("Muhanga", "BI")} == {"BI"}


def test_city_outranks_the_parts_of_its_split_province(index):
    # Bandundu city is in Kwilu; the old Bandundu province split into three.
    rows = {r["name"]: r for r in index.resolve("Bandundu")}
    assert rows["Kwilu"]["score"] == 1.0
    assert rows["Kwango"]["score"] < 1.0 and rows["Mai-Ndombe"]["score"] < 1.0


def test_split_parts_share_the_weight(index):
    scores = [r["score"] for r in index.resolve("Kivu") if r["kind"] == "later"]
    assert len(scores) == 3 and all(abs(s - 1 / 3) < 0.01 for s in scores)
