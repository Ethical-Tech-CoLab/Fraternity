# NameBridge data

Public name knowledge only (`CONCEPT-IDEA.md` §5.1A). **No case data or
personal data about real people goes in this folder**, synthetic or not;
the synthetic benchmark lives elsewhere (week 6).

- `graph/` — the Name Knowledge Graph as JSON Lines: `nodes.jsonl` and
  `edges.jsonl` (empty until week 4). Schema and validator:
  `namebridge.schema.name_graph`.
- `packs/` — country/language packs (§11) as JSON. Start from
  `TEMPLATE.json`; validator: `namebridge.schema.pack`. `rw-kiny`,
  `bi-kirundi` and the DRC packs come in week 4.

The public graph holds **spelling variants only**: there is no edge type
for an adopted or changed name (`docs/NAME_CHANGE.md` rule 1), and no
ethnicity, clan or religion attribute on any node, edge or pack.

Every edge needs a source and a confidence level; nothing enters as
`reviewed` without one.

Licence: [CC BY 4.0](LICENSE). Third-party sources keep their own licences,
recorded per source in the source register (week 5).
