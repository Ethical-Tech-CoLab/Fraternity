# NameBridge

Cross-border name intelligence for missing-person search: a sourced name
knowledge graph, probabilistic entity resolution and human review.

**Status:** research prototype. Offline, synthetic data only, no live case
decisions. Scope, users and prohibited uses: [`../docs/SCOPE.md`](../docs/SCOPE.md).
Design: [`../docs/CONCEPT-IDEA.md`](../docs/CONCEPT-IDEA.md). Plan:
[`../docs/TIMETABLE.md`](../docs/TIMETABLE.md).

## Layout

- `src/namebridge/` — the package
  - `schema/` — schemas and validators: public name graph, protected case
    graph, CPIMS+ ingestion allowlist, language-pack template (week 3);
    plain-language version in `../docs/SCHEMA.md`
  - `similarity.py` — Jaro-Winkler on folded forms
- `tests/` — the regression suite: every change must pass it before it is
  committed
- `data/` — the public name graph and language packs (CC BY 4.0)

## Set-up

```sh
cd namebridge
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip   # Python 3.9's bundled pip can't do editable installs
.venv/bin/pip install -e '.[dev]'
.venv/bin/pytest
```

Validate the data in the repo:

```sh
.venv/bin/python -m namebridge.schema.name_graph data/graph
.venv/bin/python -m namebridge.schema.pack data/packs/*.json
```

Load the packs into the graph (re-run after changing a pack):

```sh
.venv/bin/python -m namebridge.packs data/packs/*.json
.venv/bin/python -m namebridge.crosspack data/crosspack/*.json
.venv/bin/python -m namebridge.places data/places/*.json
.venv/bin/python -m namebridge.variants data/variants/*.json
```

Resolve a place name both ways in time (old → new, new → old), with the path that explains each candidate:

```sh
.venv/bin/python -m namebridge.resolve_place Kamenge
.venv/bin/python -m namebridge.resolve_place Butanyerera
```

`scripts/burundi_crosswalk.py` rebuilds the Burundi old → new commune table from public boundary data (inputs and method in its docstring).

## Licences

- Code: [Apache-2.0](LICENSE)
- Name graph and packs (`data/`): [CC BY 4.0](data/LICENSE)

Query the name graph (names only, never people): the typed paths from a name to its variants, with confidence, sources and review status; negative constraints remove a variant and are reported:

```sh
.venv/bin/python -m namebridge.graph_api "Yohana"
.venv/bin/python -m namebridge.graph_api "Ishimwe" --min-confidence 0.3
```

Review graph edges (people with a role only; decisions are kept in `data/reviews/reviews.jsonl` and re-applied on every reload):

```sh
.venv/bin/python -m namebridge.review queue --limit 20
.venv/bin/python -m namebridge.review record <edge-id> reviewed --by "<name>" --role linguist --note "<reason>"
```

Rebuild the source and licence register after adding a source (a test fails if an edge cites an unregistered source):

```sh
.venv/bin/python scripts/build_source_register.py data/register/sources.json
```
