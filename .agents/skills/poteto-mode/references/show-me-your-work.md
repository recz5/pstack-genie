# Show-me-your-work workflow

Use this internal workflow when the user explicitly requests a decision trail, or when an authorized long-running or unattended workflow needs a reviewable record. Keep one canonical append-only TSV log. The trail records evidence; it does not replace verification.

## Format and location

Use this header exactly:

```text
ts\tphase\tdecision\twhy\tevidence\tresult
```

- `ts`: ISO 8601 timestamp.
- `phase`: phase, workstream, or `start` when a new run resumes an existing trail.
- `decision`: the concrete choice or action, on one line.
- `why`: the plain-language reason, on one line.
- `evidence`: a resolvable path, command output artifact, change identifier, or `file:line` pointer; never an unsupported claim or paragraph.
- `result`: the observable outcome or predicate state, such as `tests green`, `reverted`, `open`, or `INCONCLUSIVE`.

Default to an uncommitted working artifact at `decisions.tsv`, or `.audit/<task-slug>.tsv` for concurrent efforts. Create or modify the log only inside an authorized writable workspace. Do not commit, push, publish, or upload it without explicit user authorization.

## Logging rules

1. Append one row at a decision point or checkpoint: a chosen fork, completed unit and evidence, pivot, revert, blocker, or gate result. Skip trivial actions.
2. Keep every cell single-line. Strip tabs and newlines from generated or user-supplied cell values, and prefix a cell beginning with `=`, `+`, `-`, or `@` with a single quote to prevent spreadsheet formula execution.
3. Never edit or delete history. Correct a wrong row by appending a superseding row that names the correction and valid evidence.
4. When resuming an existing trail, read its last rows first and append a `start` row that identifies the new run and the earlier timestamp range it did not create.
5. Before handoff, audit this run's rows against evidence actually accessible in the current runtime. Do not search unrelated transcripts, user directories, or private chats. Confirm each evidence pointer resolves and append corrections for omissions or unsupported claims.
6. Request an independent trail review only when the runtime exposes an authorized distinct worker. Otherwise perform a clearly labeled self-audit and report that independent review was unavailable; never invent a reviewer or model name.

Report the trail path, timestamp range written by this run, verification status, corrections appended, and any attention items. Do not expose secrets or sensitive values in log cells.
