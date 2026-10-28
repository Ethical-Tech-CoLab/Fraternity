from pathlib import Path

from namebridge.schema import name_graph as ng

DATA = Path(__file__).resolve().parents[1] / "data" / "graph"

NODES = [
    {"id": "nf:jean", "type": "NameForm", "text": "Jean", "script": "Latn"},
    {"id": "nf:yohana", "type": "NameForm", "text": "Yohana", "script": "Latn"},
    {"id": "rule:married", "type": "Rule", "description": "a general naming rule"},
]


def edge(**overrides):
    e = {
        "id": "e1", "from": "nf:jean", "to": "nf:yohana", "relation_type": "historical_cognate_of",
        "source_name": "A sourced reference", "source_url": "https://example.org/ref",
        "source_excerpt_or_locator": "p. 12", "source_language": "fr", "applicable_languages": ["sw", "fr"],
        "applicable_regions": ["CD"], "confidence": 0.9, "confidence_basis": "attested",
        "reversible": True, "review_status": "reviewed", "reviewer_role": "linguist", "license": "CC-BY-4.0",
    }
    e.update(overrides)
    return e


def test_repo_graph_is_valid():
    assert ng.validate_dir(DATA) == []


def test_valid_cognate_edge():
    assert ng.validate_graph(NODES, [edge()]) == []


def test_adopted_name_is_not_a_variant():
    errors = ng.validate_graph(NODES, [edge(relation_type="adopted_name_of")])
    assert any("NAME_CHANGE.md rule 1" in e for e in errors)


def test_restricted_layer_never_in_public_graph():
    errors = ng.validate_graph(NODES, [edge(layer="restricted")])
    assert any("restricted layer" in e for e in errors)


def test_generated_edge_stays_proposed():
    errors = ng.validate_graph(NODES, [edge(confidence_basis="generated")])
    assert any("generated edge" in e for e in errors)
    assert ng.validate_graph(NODES, [edge(confidence_basis="generated", review_status="proposed")]) == []


def test_reviewed_edge_needs_reviewer_and_source():
    errors = ng.validate_graph(NODES, [edge(reviewer_role=None, source_excerpt_or_locator="")])
    assert len(errors) == 2


def test_every_edge_needs_a_source():
    errors = ng.validate_graph(NODES, [edge(review_status="proposed", source_name="", source_url="")])
    assert any("needs a source" in e for e in errors)


def test_confidence_range():
    assert ng.validate_graph(NODES, [edge(confidence=1.2)])
    assert ng.validate_graph(NODES, [edge(confidence=True)])


def test_missing_node_and_self_loop():
    assert any("does not exist" in e for e in ng.validate_graph(NODES, [edge(to="nf:missing")]))
    assert any("two different nodes" in e for e in ng.validate_graph(NODES, [edge(to="nf:jean")]))


def test_married_form_only_as_general_rule():
    errors = ng.validate_graph(NODES, [edge(relation_type="married_or_previous_form_of")])
    assert any("Rule node" in e for e in errors)
    assert ng.validate_graph(NODES, [edge(relation_type="married_or_previous_form_of", to="rule:married")]) == []


def test_ethnicity_attribute_refused_on_nodes_and_edges():
    nodes = NODES + [{"id": "nf:x", "type": "NameForm", "text": "X", "script": "Latn", "ethnicity": "any"}]
    assert any("forbidden attribute 'ethnicity'" in e for e in ng.validate_graph(nodes, []))
    assert any("forbidden attribute" in e for e in ng.validate_graph(NODES, [edge(notes={"clan": "any"})]))


def test_nameform_needs_script():
    assert ng.validate_node({"id": "nf:y", "type": "NameForm", "text": "Y", "script": "latin"})


def test_duplicate_ids():
    errors = ng.validate_graph(NODES + NODES[:1], [edge(), edge()])
    assert any("duplicate node" in e for e in errors)
    assert any("duplicate edge" in e for e in errors)


def form(nid, text, script="Latn"):
    return {"id": nid, "type": "NameForm", "text": text, "script": script}


def test_spelling_variant_must_look_alike():
    # Kinyarwanda by -> Kirundi vy (RESEARCH_LOG.md, Kirundi spelling rules)
    nodes = [form("nf:rw", "Habyarimana"), form("nf:bi", "Havyarimana")]
    assert ng.validate_graph(nodes, [edge(**{"from": "nf:rw", "to": "nf:bi"}, relation_type="orthographic_variant_of")]) == []


def test_unrelated_names_cannot_be_a_spelling_variant():
    nodes = [form("nf:jean", "Jean"), form("nf:hamisi", "Hamisi")]
    bad = edge(**{"from": "nf:jean", "to": "nf:hamisi"}, relation_type="orthographic_variant_of")
    assert any("NAME_CHANGE.md rule 1" in e for e in ng.validate_graph(nodes, [bad]))


def test_low_similarity_needs_reason_and_review():
    nodes = [form("nf:a", "Kakolele"), form("nf:b", "Ngolele")]
    low = edge(**{"from": "nf:a", "to": "nf:b"}, relation_type="phonetic_variant_of")
    assert ng.validate_graph(nodes, [low])  # similarity 0.78
    assert ng.validate_graph(nodes, [dict(low, low_similarity_reason="attested in source p. 3")]) == []
    unreviewed = dict(low, low_similarity_reason="x", review_status="proposed")
    assert ng.validate_graph(nodes, [unreviewed])


def test_real_variant_pairs_pass_the_threshold():
    # UN 1533 alias pair; Rw/Bi spelling; French tch and ou conventions (RESEARCH_LOG.md)
    from namebridge.similarity import jaro_winkler
    for a, b in [("Kakolele", "Kakorere"), ("Habyarimana", "Havyarimana"), ("Ciza", "Tchiza"), ("Rwanda", "Ruanda")]:
        assert jaro_winkler(a, b) >= ng.MIN_SPELLING_SIMILARITY, (a, b)


def test_cognates_may_differ_in_spelling():
    assert ng.validate_graph(NODES, [edge()]) == []  # Jean / Yohana as historical_cognate_of


def test_endpoint_types():
    nodes = NODES + [{"id": "m:imana", "type": "Morpheme"}]
    assert ng.validate_graph(nodes, [edge(relation_type="contains_morpheme", to="m:imana")]) == []
    assert any("cannot join" in e for e in ng.validate_graph(nodes, [edge(relation_type="contains_morpheme")]))


def test_transliteration_needs_two_scripts():
    errors = ng.validate_graph(NODES, [edge(relation_type="transliteration_of")])
    assert any("two different scripts" in e for e in errors)


def test_duplicate_triple_and_contradiction():
    errors = ng.validate_graph(NODES, [edge(), edge(id="e2")])
    assert any("already exists" in e for e in errors)
    neg = edge(id="e3", relation_type="not_equivalent_to")
    assert any("contradiction" in e for e in ng.validate_graph(NODES, [edge(), neg]))
    assert ng.validate_graph(NODES, [edge(review_status="deprecated", reviewer_role="linguist"), neg]) == []


def test_text_must_be_nfc():
    decomposed = "Ndaye\u0301"  # e + combining acute
    assert any("NFC" in e for e in ng.validate_node(form("nf:x", decomposed)))
