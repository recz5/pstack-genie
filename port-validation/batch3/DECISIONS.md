# Batch 3 controlled engineering assessment

## Verdict

**FAIL — one required correction before acceptance.**

Batch 3 is structurally valid, safely routed, and passes all repository checks, but it breaks the canonical decision-trail composition promised by Show Me Your Work. `autonomous-run.md` and `hillclimb.md` define parallel trail formats instead of routing checkpoints through the single canonical TSV trail.

## Scope and controls

- Reviewed commit: `67b15e8` against parent `60819e1`.
- Primary playbook: Orchestrate; internal workflows: Interrogate and Show Me Your Work.
- Trust boundary: repository files and local commands only.
- Allowed write: this file only.
- Prohibited: code changes, commits, deployments, production writes, permission changes, publication, and external actions.

## Work-unit ledger

| Unit | Owner | Evidence | Disposition |
| --- | --- | --- | --- |
| Representative fixture check | `/root/representative` | `python -B -m unittest discover -s port-validation -p 'test_normalize.py' -v` | PASS with stale-handoff caveat; not a batch-3 blocker |
| Upstream fidelity | `/root/upstream_fidelity` | `rg -n "iteration trail\|decision trail\|show-me-your-work\|ts\\tphase\|attempt, mechanism" ...` | FAIL; canonical-trail composition defect reproduced |
| Coverage and safety | `/root/coverage_safety` | focused/full skill tests, `python -B scripts/validate_repo.py`, link probe, reference count, `git diff --check` | PASS |
| Coordinator rerun | `/root` | same fidelity `rg` command and `git status --short` | Finding reproduced; workspace clean before this artifact |

## Verified finding

### Competing audit-trail contracts

- Required: Show Me Your Work states there is one canonical append-only TSV log with columns `ts`, `phase`, `decision`, `why`, `evidence`, and `result` at `.agents/skills/poteto-mode/references/show-me-your-work.md:3` and `.agents/skills/poteto-mode/references/show-me-your-work.md:10`.
- Upstream behavior: autonomous iterations and hillclimb attempts explicitly checkpoint through Show Me Your Work at `vendor/pstack/skills/poteto-mode/playbooks/autonomous-run.md:10` and `vendor/pstack/skills/poteto-mode/playbooks/hillclimb.md:9`.
- Observed: `.agents/skills/poteto-mode/references/autonomous-run.md:10` permits a response-only or artifact trail with a different schema; `.agents/skills/poteto-mode/references/hillclimb.md:8` defines another distinct schema.
- Impact: composed workflows can produce competing, noncanonical, or non-TSV records, so auditability depends on coordinator interpretation rather than the declared invariant.
- Required correction: route autonomous-run and hillclimb checkpoints through the active Show Me Your Work workflow, mapping workflow-specific details into its canonical columns instead of defining parallel trail formats.

## Dropped candidates

- Cursor `/loop`, fixed model families, commits, pull requests, and mandatory fan-out are intentional portability exclusions.
- Sequential orchestration fallback preserves ownership and evidence when native workers are unavailable.
- Textual workflow tests are appropriate for instruction artifacts; repository validation separately checks structure and links.
- The stale `port-validation/HANDOFF.md` narrative predates this batch and does not invalidate commit `67b15e8`.

## Validation evidence

- `python -B -m unittest tests.test_skills -v` — 14 tests passed.
- `python -B scripts/validate_repo.py` — passed in the independent coverage/safety unit.
- Markdown local-link probe — no broken links in the independent coverage/safety unit.
- `git diff --check 60819e1 67b15e8` — clean in the independent coverage/safety unit.
- Port reference count — 26, matching `docs/PSTACK_PORTING_MATRIX.md`.
- Coordinator fidelity rerun — reproduced the four active/upstream trail-contract lines cited above.

## Decision trail

```text
ts\tphase\tdecision\twhy\tevidence\tresult
2026-11-12T20:46:02-08:00\tstart\tAssess batch 3 with Orchestrate, Interrogate, and Show Me Your Work\tThe user requested bounded coordination, reproducible challenge, and one auditable artifact\t67b15e8\topen
2026-11-12T20:46:02-08:00\torchestrate\tRun one representative unit before widening concurrency\tThe orchestration workflow requires a representative unit before parallel review\tport-validation/HANDOFF.md:1\tPASS with caveat
2026-11-12T20:46:02-08:00\tinterrogate\tRetain the canonical-trail composition finding\tIndependent upstream-fidelity review and coordinator rerun reproduced the mismatch\t.agents/skills/poteto-mode/references/autonomous-run.md:10\tFAIL
2026-11-12T20:46:02-08:00\tverification\tAccept coverage and safety gates\tFocused and full tests, repository validation, links, count, and diff checks passed\ttests/test_skills.py:89\ttests green
2026-11-12T20:46:02-08:00\tverdict\tReject batch 3 pending one correction\tA declared single canonical trail is not consistently composed by two batch-3 workflows\t.agents/skills/poteto-mode/references/show-me-your-work.md:3\tFAIL
```

## Attention item

No production or external action was taken. No code was changed. Acceptance requires a separate authorized fix and rerun; this assessment does not authorize either.
