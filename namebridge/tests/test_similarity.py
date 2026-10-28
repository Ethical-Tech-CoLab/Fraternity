from namebridge.similarity import fold, jaro_winkler


def test_known_value():
    assert round(jaro_winkler("MARTHA", "MARHTA"), 4) == 0.9611  # Winkler's example


def test_fold_ignores_case_and_accents():
    assert fold("Ndáyishimíye") == "ndayishimiye"
    assert jaro_winkler("NDAYISHIMIYE", "ndayishimiye") == 1.0


def test_unrelated_names_score_low():
    assert jaro_winkler("Jean", "Hamisi") < 0.8
