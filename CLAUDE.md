# Fraternity — working rules for Claude

- **Gates first.** Before starting any NameBridge task, read the "⛔ Gates" table in `docs/TIMETABLE.md`.
  - If the task is listed under "Blocks" for an **open ⛔ hard gate**, do not do it. Tell the user which gate blocks it, who must decide, and by when.
  - For an open **⚠ soft gate**, warn the user, state the default in use, and say what may need redoing.
  - Proceed with blocked work only if the user explicitly overrides. Then record the override in `docs/RESEARCH_LOG.md` (date, gate, reason, what may need redoing).
- **Raise new gates.** When a new decision comes up that someone other than the user must make (the professor, the IRB, a partner) and it would change how we work, add it to the gates table before continuing.
- **Close gates explicitly.** When the professor or IRB answers, close the gate in the table with the date and the decision, and update the affected documents.
- **Mark early progress.** When research finishes a task planned for a later week, mark it ◐ (partly done) or ✔ (done) in that week of `docs/TIMETABLE.md`, and add it to the Progress section.
- **Sources.** Every claim gets a source and a date; conflicting sources stay side by side; single-sourced claims are flagged. Research uses Tavily (the claude.ai connector works when the local MCP key fails).
- **Cross-cutting rules.** `docs/NAME_CHANGE.md` and the prohibited uses in `docs/SCOPE.md` §4 apply in every context.
- **Commit and push** after each change set (remote: `origin`). Docs are in English; explain to the user in English.
