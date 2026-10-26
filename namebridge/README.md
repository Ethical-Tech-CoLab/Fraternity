# NameBridge

Cross-border name intelligence for missing-person search: a sourced name
knowledge graph, probabilistic entity resolution and human review.

**Status:** research prototype. Offline, synthetic data only, no live case
decisions. Scope, users and prohibited uses: [`../docs/SCOPE.md`](../docs/SCOPE.md).
Design: [`../docs/CONCEPT-IDEA.md`](../docs/CONCEPT-IDEA.md). Plan:
[`../docs/TIMETABLE.md`](../docs/TIMETABLE.md).

## Layout

- `src/namebridge/` — the package
- `tests/` — the test suite (becomes the regression suite, week 3)
- `data/` — the public name graph and language packs (CC BY 4.0)

## Set-up

```sh
cd namebridge
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip   # Python 3.9's bundled pip can't do editable installs
.venv/bin/pip install -e '.[dev]'
.venv/bin/pytest
```

## Licences

- Code: [Apache-2.0](LICENSE)
- Name graph and packs (`data/`): [CC BY 4.0](data/LICENSE)
