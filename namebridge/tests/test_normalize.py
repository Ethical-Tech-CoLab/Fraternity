import unicodedata

from namebridge.normalize import fold, forms


def test_original_is_kept_exactly():
    f = forms("  NSHIMIRIMANA  Belyse ")
    assert f["original"] == "  NSHIMIRIMANA  Belyse "
    assert f["folded"] == "nshimirimana belyse"


def test_composed_and_decomposed_spellings_are_equal():
    composed = "Désiré"
    decomposed = unicodedata.normalize("NFD", composed)
    assert composed != decomposed
    assert forms(composed)["nfc"] == forms(decomposed)["nfc"]
    assert fold(composed) == fold(decomposed) == "desire"


def test_preserving_form_keeps_accents_folded_form_drops_them():
    f = forms("Ishímwe")
    assert f["preserving"] == "ishímwe"
    assert f["folded"] == "ishimwe"


def test_letters_without_decomposition_are_mapped_not_dropped():
    # The old place fold turned these into nothing (ASCII conversion with errors ignored).
    assert fold("Mɛsɛ") == "mese"
    assert fold("Mbɔ́ngɔ") == "mbongo"
    assert fold("Ŋoma") == "ngoma"
    assert fold("Ŵanthu") == "wanthu"


def test_hyphen_and_apostrophe_give_split_and_joined_forms():
    f = forms("Jean-Marie Vianney")
    assert f["folded"] == "jean marie vianney"
    assert "jeanmarie vianney" in f["variants"]
    g = forms("N’uko")
    assert g["folded"] == "n uko"
    assert "nuko" in g["variants"]


def test_particles_give_a_form_without_them():
    assert "gahungu bucumi" in forms("Gahungu mwene Bucumi")["variants"]
    assert "mpolondo mukamba mutombo" in forms("Mpolondo Mukamba wa Mutombo")["variants"]


def test_every_change_is_logged_in_order():
    steps = [s["step"] for s in forms("  Mɛ́sɛ-Ŋoma ")["path"]]
    assert steps == ["casefold_and_spaces", "remove_accents_and_tone_marks", "map_special_letters", "apostrophes_and_hyphens_to_spaces"]


def test_unchanged_name_has_empty_path():
    assert forms("mugisha")["path"] == []


def test_fold_is_idempotent():
    for name in ("Jean-Marie Vianney", "Mɛsɛ", "N’uko", "Désiré  NDAYISHIMIYE"):
        assert fold(fold(name)) == fold(name)
