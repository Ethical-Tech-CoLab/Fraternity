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

## Licences

- Code: [Apache-2.0](LICENSE)
- Name graph and packs (`data/`): [CC BY 4.0](data/LICENSE)
