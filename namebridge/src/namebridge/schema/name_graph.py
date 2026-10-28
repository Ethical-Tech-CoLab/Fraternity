"""Public Name Knowledge Graph: schema and validator (CONCEPT-IDEA.md §5.1A).

Cultural and linguistic knowledge only, never case-person data. Stored as
JSON Lines: data/graph/nodes.jsonl and data/graph/edges.jsonl.

Run: python -m namebridge.schema.name_graph [graph_dir]
"""

import json
import re
import sys
from pathlib import Path

from namebridge.schema import forbidden_keys

NODE_TYPES = {"NameForm", "NameConcept", "Morpheme", "Script", "Language", "Locale", "Region", "Rule", "Source"}

# Name-to-name relations are variants only. There is deliberately no type for
# an adopted or changed name: rule 1 of NAME_CHANGE.md (no edge between
# unrelated names). The restricted name-change layer (G5, approved with
# conditions on 28 Oct 2026) is not part of the public graph.
EDGE_TYPES = {
    "transliteration_of",
    "romanization_variant_of",
    "orthographic_variant_of",
    "phonetic_variant_of",
    "nickname_of",
    "formal_form_of",
    "historical_cognate_of",
    "etymologically_derived_from",
    "contains_morpheme",
    "inflected_form_of",
    "married_or_previous_form_of",  # general rule only, never a person-specific fact
    "commonly_confused_with",
    "not_equivalent_to",  # negative constraint
}

REQUIRED_EDGE_FIELDS = (
    "id", "from", "to", "relation_type",
    "source_name", "source_url", "source_excerpt_or_locator",
    "source_language", "applicable_languages", "applicable_regions",
    "confidence", "confidence_basis", "reversible", "review_status", "license",
)
CONFIDENCE_BASES = {"attested", "statistical", "expert", "generated", "disputed"}
REVIEW_STATUSES = {"proposed", "reviewed", "deprecated"}
REVIEWER_ROLES = {"linguist", "community_expert", "investigator", "data_steward"}
REVERSIBLE = {True, False, "unknown"}

_BCP47 = re.compile(r"^[a-z]{2,3}(-[A-Za-z0-9]{2,8})*$")
_ISO15924 = re.compile(r"^[A-Z][a-z]{3}$")


def validate_node(node):
    errors = []
    nid = node.get("id")
    if not nid:
        errors.append("node without id")
    if node.get("type") not in NODE_TYPES:
        errors.append(f"node {nid}: unknown type {node.get('type')!r}")
    if node.get("type") == "NameForm":
        if not node.get("text"):
            errors.append(f"node {nid}: NameForm needs 'text'")
        if not _ISO15924.match(str(node.get("script", ""))):
            errors.append(f"node {nid}: NameForm needs an ISO 15924 'script' (e.g. Latn)")
    for key in forbidden_keys(node):
        errors.append(f"node {nid}: forbidden attribute {key!r} (no ethnicity, clan or religion; SCOPE.md §4)")
    return errors


def validate_edge(edge, nodes_by_id=None):
    eid = edge.get("id", "?")
    errors = [f"edge {eid}: missing {f!r}" for f in REQUIRED_EDGE_FIELDS if f not in edge]
    if errors:
        return errors

    rel = edge["relation_type"]
    if rel not in EDGE_TYPES:
        errors.append(
            f"edge {eid}: unknown relation_type {rel!r}. Adopted or changed names are not variants "
            "and never enter the public graph (NAME_CHANGE.md rule 1)"
        )
    if edge.get("layer", "public") != "public":
        errors.append(f"edge {eid}: only layer 'public' is allowed here; the restricted layer is separate (G5)")
    if edge["from"] == edge["to"]:
        errors.append(f"edge {eid}: an edge must join two different nodes")

    conf = edge["confidence"]
    if isinstance(conf, bool) or not isinstance(conf, (int, float)) or not 0 <= conf <= 1:
        errors.append(f"edge {eid}: confidence must be a number in [0, 1]")
    if edge["confidence_basis"] not in CONFIDENCE_BASES:
        errors.append(f"edge {eid}: unknown confidence_basis {edge['confidence_basis']!r}")
    if edge["reversible"] not in REVERSIBLE:
        errors.append(f"edge {eid}: reversible must be true, false or 'unknown'")
    status = edge["review_status"]
    if status not in REVIEW_STATUSES:
        errors.append(f"edge {eid}: unknown review_status {status!r}")

    # A generated edge never becomes authoritative on its own (§5.1A; DATA_RULES.md DR-1.5).
    if edge["confidence_basis"] == "generated" and status != "proposed":
        errors.append(f"edge {eid}: a generated edge can only be 'proposed'")
    if status == "reviewed":
        if edge.get("reviewer_role") not in REVIEWER_ROLES:
            errors.append(f"edge {eid}: a reviewed edge needs a reviewer_role")
        for f in ("source_name", "source_url", "source_excerpt_or_locator", "license"):
            if not edge[f]:
                errors.append(f"edge {eid}: a reviewed edge needs a non-empty {f!r}")
    elif not edge["source_name"] and not edge["source_url"]:
        errors.append(f"edge {eid}: every edge needs a source, even when proposed")

    for f in ("source_language",):
        if not _BCP47.match(str(edge[f])):
            errors.append(f"edge {eid}: {f} must be a BCP-47 tag")
    for lang in edge["applicable_languages"]:
        if not _BCP47.match(str(lang)):
            errors.append(f"edge {eid}: applicable_languages entry {lang!r} is not BCP-47")
    if not isinstance(edge["applicable_regions"], list):
        errors.append(f"edge {eid}: applicable_regions must be a list")

    if nodes_by_id is not None:
        for end in ("from", "to"):
            if edge[end] not in nodes_by_id:
                errors.append(f"edge {eid}: {end} node {edge[end]!r} does not exist")
        if rel == "married_or_previous_form_of" and not any(
            nodes_by_id.get(edge[end], {}).get("type") == "Rule" for end in ("from", "to")
        ):
            errors.append(f"edge {eid}: married_or_previous_form_of must attach to a Rule node (general rule only)")

    for key in forbidden_keys(edge):
        errors.append(f"edge {eid}: forbidden attribute {key!r}")
    return errors


def validate_graph(nodes, edges):
    errors, nodes_by_id = [], {}
    for node in nodes:
        errors.extend(validate_node(node))
        if node.get("id") in nodes_by_id:
            errors.append(f"duplicate node id {node['id']!r}")
        nodes_by_id[node.get("id")] = node
    seen = set()
    for edge in edges:
        errors.extend(validate_edge(edge, nodes_by_id))
        if edge.get("id") in seen:
            errors.append(f"duplicate edge id {edge['id']!r}")
        seen.add(edge.get("id"))
    return errors


def read_jsonl(path):
    path = Path(path)
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def validate_dir(graph_dir):
    graph_dir = Path(graph_dir)
    return validate_graph(read_jsonl(graph_dir / "nodes.jsonl"), read_jsonl(graph_dir / "edges.jsonl"))


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "data/graph"
    problems = validate_dir(target)
    print("\n".join(problems) or f"{target}: valid")
    sys.exit(1 if problems else 0)
