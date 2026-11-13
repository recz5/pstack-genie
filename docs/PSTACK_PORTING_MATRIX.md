# pstack to poteto-mode porting matrix

## Decision and scope

This repository ports the upstream pstack plugin into one exposed Genie Code skill: `poteto-mode`. The port keeps upstream source as provenance under `vendor/pstack/` and does not register upstream leaf skills, agents, or automations. The installed skill has no runtime dependency on `vendor/`.

Inventory baseline:

- Upstream: pstack `0.15.36`, revision `ec569379616a4826b98f0f0a205dd3411b573611`, recorded in `vendor/UPSTREAM.txt`.
- Upstream surface: 58 skills, 2 agents, 23 `poteto-mode` playbooks, one Benny automation pack with 3 operational skills, and 573 imported files.
- Port surface: one skill, 26 portable references, and one agent metadata file under `.agents/skills/poteto-mode/`.
- Source policy: `vendor/pstack/` is an unchanged import. Port changes belong outside `vendor/`.

### Goals

- Preserve the general engineering intent of pstack in a portable Genie Code coordinator.
- Keep exactly one exposed skill and route work internally through compact playbooks and principles.
- Make unsupported Cursor orchestration explicit rather than simulating it.
- Keep Databricks guidance conditional and inside the one skill.

### Non-goals

- Reproduce every slash command, custom agent, automation, script, or UI workflow.
- Claim parity for Cursor Task orchestration, cloud agents, Bugbot, `/loop`, plugin discovery, or Automations.
- Install or execute imported source as a runtime dependency.
- Deploy, publish, change permissions, or modify the imported snapshot.

### Acceptance criteria

1. Every upstream skill, agent, playbook, automation, dependency family, and Cursor-specific feature is inventoried below.
2. Every item has an explicit port disposition.
3. Only `.agents/skills/poteto-mode/SKILL.md` is exposed as a skill.
4. `vendor/pstack/` remains provenance-only and unchanged.

## Architecture and control flow

Upstream control flow is `Cursor plugin manifest -> slash skill -> Task/custom agent fan-out -> playbook or leaf principle -> scripts/external integrations -> PR, automation, or report`. It assumes Cursor plugin discovery and frequently assumes background agents, model routing, worktrees, transcripts, browser/control skills, GitHub tooling, or Automations.

The port control flow is `Genie skill discovery -> poteto-mode -> routing.md -> one compact primary playbook plus any triggered internal workflow -> relevant principles/runtime rules -> tools actually exposed by the current session -> verified report or local edit`. Unsupported fan-out becomes sequential work unless the runtime genuinely exposes an authorized equivalent. Imported files are never on this execution path.

## Recommended approach

Retain the current single-skill adapter. It costs fine-grained slash-command discovery and some specialized workflows, but minimizes prompt collisions, avoids false capability claims, and gives Genie one stable entry point. Two alternatives were rejected:

| Alternative | Benefit | Cost or risk | Decision |
| --- | --- | --- | --- |
| Register all 58 upstream skills | Highest command-name parity | Exposes Cursor assumptions, duplicates routing, expands maintenance and trust surface | Reject |
| Register a small family of top-level skills | More discoverability than one skill | Violates the one-exposed-skill constraint and still leaves cross-skill dependencies | Reject |
| One coordinator with internal references | Portable capability-based routing and smallest public API | Specialized upstream behavior becomes partial or unavailable | Adopt |

## Upstream skills

Disposition terms: **Adapted** means a compact equivalent exists inside `poteto-mode`; **Partial** means intent is represented but the upstream command/workflow is not; **Not ported** means provenance only.

### Core workflow and review skills

| Upstream skill | Disposition | poteto-mode mapping or gap |
| --- | --- | --- |
| `architect` | Adapted | `references/architecture.md` |
| `arena` | Not ported | Requires parallel candidate agents and synthesis. |
| `automate-me` | Not ported | Personal skill generation and transcript evidence are outside the port. |
| `benchmark-checklist` | Adapted | `references/performance.md` plus explain-the-number principle. |
| `blast-radius` | Adapted | `references/review.md` with real verification. |
| `bro` | Partial | Plain-language responses are a style choice, not a command. |
| `correct` | Partial | Root-cause and structural prevention principles remain; correction mining is absent. |
| `create-formal-verification-skill` | Not ported | No generated formal-verification skill workflow. |
| `create-verification-skill` | Not ported | No generated control-skill workflow. |
| `figure-it-out` | Adapted | `references/figure-it-out.md` preserves bespoke phase design, hypothesis verdicts, and a local audit trail without requiring another skill, commits, or unsupported agents. |
| `how` | Adapted | `references/investigation.md` covers architecture and runtime explanation. |
| `interrogate` | Adapted | `references/interrogate.md` preserves adversarial lenses, reproduction-only findings, reruns, and no-fix output with native-worker or sequential execution. |
| `in-your-own-words` | Partial | Goal restatement is built into `SKILL.md`, not exposed separately. |
| `ketchup` | Partial | Progress/status reporting remains; transcript-specific command is absent. |
| `ketchup-video` | Not ported | No slide, subtitle, media, or video pipeline. |
| `maintain-formal-verification-skill` | Not ported | No formal-model maintenance workflow. |
| `maintain-verification-skill` | Not ported | No project control-skill audit workflow. |
| `make-bot-ui` | Not ported | Specialized bot UI generation is absent. |
| `no-comments` | Partial | Minimal-comment coding guidance remains; custom reviewer agent is absent. |
| `poteto-help` | Partial | `references/routing.md` documents selection; no separate help command. |
| `poteto-mode` | Adapted | The sole exposed skill, rewritten for Genie capability detection. |
| `recall` | Not ported | No cross-chat/history reconstruction contract. |
| `reflect` | Not ported | Requires three transcript-review subagents and skill edits. |
| `setup-pstack` | Not ported | Cursor model-role configuration has no Genie port. |
| `sharpen` | Partial | Scope discipline exists, but prompt-rewrite command is absent. |
| `show-me-your-work` | Adapted | `references/show-me-your-work.md` preserves one append-only TSV trail, evidence pointers, safe cell handling, corrections, and final audit without transcript or commit assumptions. |
| `statechart` | Not ported | TLA+/TLC and Mermaid tooling is not bundled into the active skill. |
| `swarm` | Not ported | Requires explicit parallel worker orchestration. |
| `tdd` | Adapted | `references/tdd.md` provides a conditional failing-before, passing-after workflow without exposing another skill. |
| `teach` | Partial | Explanations can use investigation; chained `how`/`why` orchestration is absent. |
| `technical-writing` | Partial | Concise reporting style remains; dedicated editing rubric is absent. |
| `typescript-best-practices` | Not ported | Language-specific patterns are not part of the general skill. |
| `unslop` | Partial | Concise prose and minimal code are policy; dedicated cleanup workflow is absent. |
| `why` | Adapted | `references/investigation.md` covers evidence-based motivation and history. |

### Principle skills

| Upstream principle skill | Disposition | poteto-mode mapping or gap |
| --- | --- | --- |
| `principle-attack-the-premise` | Not ported | No explicit repeated-failure gate. |
| `principle-boundary-discipline` | Adapted | `references/principles.md` |
| `principle-build-the-lever` | Not ported | Tool-building is optional, not a universal rule. |
| `principle-encode-lessons-in-structure` | Partial | Structural fixes are preferred, without a dedicated trigger. |
| `principle-exhaust-the-design-space` | Partial | Architecture compares two realistic alternatives, not mandatory prototypes. |
| `principle-experience-first` | Not ported | Product/UX prioritization is not generalized into the port. |
| `principle-explain-the-number` | Adapted | `references/principles.md` and `references/performance.md` |
| `principle-fix-root-causes` | Adapted | `references/principles.md` and `references/bug-fix.md` |
| `principle-foundational-thinking` | Adapted | `references/principles.md` |
| `principle-guard-the-context-window` | Adapted | `references/principles.md`, without assuming subagents. |
| `principle-laziness-protocol` | Adapted | `references/principles.md` |
| `principle-make-operations-idempotent` | Adapted | `references/principles.md` |
| `principle-migrate-callers-then-delete-legacy-apis` | Partial | Refactoring favors complete migrations but has no leaf rule. |
| `principle-minimize-reader-load` | Partial | Small maintainable solutions remain; detailed heuristic is absent. |
| `principle-model-the-domain` | Adapted | `references/principles.md` |
| `principle-never-block-on-the-human` | Partial | Safe reversible progress is encouraged, bounded by approval rules. |
| `principle-outcome-oriented-execution` | Partial | Goal preservation remains; phased migration semantics are absent. |
| `principle-prove-it-works` | Adapted | `references/principles.md` and every active playbook. |
| `principle-redesign-from-first-principles` | Partial | Architecture evaluates alternatives; no dedicated redesign workflow. |
| `principle-separate-before-serializing-shared-state` | Not ported | No concurrency-specific leaf guidance. |
| `principle-sequence-verifiable-units` | Partial | Playbooks use staged verification, without stacked-PR semantics. |
| `principle-subtract-before-you-add` | Partial | Laziness/minimal-change guidance covers part of the intent. |
| `principle-test-behavior-not-implementation` | Adapted | `references/principles.md` |
| `principle-type-system-discipline` | Partial | Domain modeling remains; detailed static-type rules are absent. |

## Agents

| Upstream agent | Upstream role | Port disposition |
| --- | --- | --- |
| `poteto-agent` | Background delegate that discovers the Cursor plugin, reads full poteto-mode guidance, and executes a parent-owned task. | Not registered. `poteto-mode` uses only agents/tools genuinely exposed by the runtime and never claims hidden delegation. |
| `comment-sicko` | Specialized comment-deletion reviewer invoked by `no-comments`. | Not registered. The port relies on ordinary review and minimal-comment coding guidance. |

`.agents/skills/poteto-mode/agents/openai.yaml` is platform metadata for the one Genie skill, not a port of either upstream custom agent.

## poteto-mode playbooks

| Upstream playbook | Disposition | poteto-mode mapping or gap |
| --- | --- | --- |
| `authoring-a-skill` | Not ported | Skill-authoring workflow is outside this skill. |
| `autonomous-run` | Adapted | `references/autonomous-run.md` preserves a fixed exit predicate, bounded keep-or-revert iterations, and an evidence trail without implicit background loops, commits, or publication. |
| `autopilot-full` | Not ported | Cursor autonomous stack workflow is unavailable. |
| `autopilot-stack` | Not ported | Stacked PR/worktree automation is unavailable. |
| `babysit` | Not ported | `/loop` and queued PR watcher lifecycle are unavailable by default. |
| `bug-fix` | Adapted | `references/bug-fix.md` |
| `eval` | Partial | Verification is general; no dedicated model/eval workflow. |
| `feature` | Adapted | `references/feature.md` |
| `hillclimb` | Adapted | `references/hillclimb.md` preserves a frozen measurement harness, baseline, regression gate, and one-candidate keep-or-revert loop with capability-detected parallelism. |
| `investigation` | Adapted | `references/investigation.md` |
| `multi-phase-plan` | Adapted | `references/multi-phase-plan.md` preserves plan-only delivery, ordered verifiable phases, evidence, and explicit execution handoff without Cursor task graphs. |
| `opening-a-pr` | Not ported | External publication requires explicit approval and has no active playbook. |
| `orchestrate` | Adapted | `references/orchestrate.md` preserves scoped work units, ownership, isolation, supervision, retries, and evidence while using only exposed collaboration tools or a sequential fallback. |
| `pause-safely` | Adapted | `references/pause-safely.md` provides explicit-only safe stopping and resumable checkpoints without implicit commits or publication. |
| `perf-issue` | Adapted | `references/performance.md` |
| `prototype` | Partial | Architecture permits a minimal non-production proof when authorized. |
| `refactoring` | Adapted | `references/refactoring.md` |
| `runtime-forensics` | Adapted | `references/runtime-forensics.md` requires authorized live evidence, mechanism testing, source attribution, and a diagnosis-only handoff. |
| `session-pickup` | Not ported | Cursor transcript/worktree reconstruction is absent. |
| `shipping` | Not ported | PR merge queues, verdict agents, and landing automation are excluded. |
| `trace-forensics` | Adapted | `references/trace-forensics.md` treats an existing artifact as fixed untrusted data, reduces it to a queryable form, attributes source, and states confirmation limits. |
| `visual-parity` | Not ported | Browser/control skill and pixel-diff loop are absent. |
| `worktree-cleanup` | Not ported | Destructive cleanup and Cursor transcript correlation are excluded. |

The port adds `architecture.md` and `review.md` as compact first-class routes and renames the performance route for clarity.

## Automations

| Upstream automation asset | Purpose | Port disposition |
| --- | --- | --- |
| Benny `setup-benny` | Merge a pack into `.cursor/automations/benny/`, enable the pstack plugin, configure integrations, and create/review two Cursor Automations. | Not ported; Cursor settings, plugin scope, `/automate`, and Automations editor are unavailable. |
| Benny `triage-issue-reports` | Trigger on a Slack root report, preserve thread coordinates, classify and route it, deduplicate/create tracker issues, and reply once in-thread. | Not ported; needs Slack, tracker, trigger, identity, and posting permissions. |
| Benny `reproduce-and-fix-issues` | Wait for trusted triage, reproduce twice through a real UI, collect media and state evidence, optionally prepare a bounded fix and draft PR. | Not ported; needs automation triggers, control adapter, feature map, browser/UI, media capture, repository, tracker, Slack, and draft-PR access. |
| Templates and examples | Automation prompts, YAML configuration, routing map, feature map, and control-adapter guidance. | Provenance only under `vendor/pstack/automations/benny/`. |

No workflow from `.github/workflows/` exists in the upstream snapshot. This repository's `.github/workflows/validate.yml` is port-repository validation, not imported pstack behavior.

## Dependencies and external capabilities

| Dependency or capability | Used upstream by | Port status |
| --- | --- | --- |
| Cursor plugin manifest and skill/agent discovery | Entire plugin | Replaced by one `.agents/skills/poteto-mode/` skill. |
| Cursor `Task`, custom `subagent_type`, background agents, role/model/reasoning selection | poteto-mode, arena, swarm, reflect, architect, how/why | Capability-detected only; never assumed. |
| Cursor `/loop`, Bugbot, cloud agents, chat transcripts, pinned chats, `.cursor/worktrees` | babysit, shipping, session pickup, cleanup, triage | Not portable; explicitly called out in `runtime.md`. |
| Cursor Automations, `/automate`, `.cursor/settings.json`, Slack triggers | Benny | Not ported. |
| Browser/UI control skills, screenshots, image diff, video/media generation | verification skills, visual parity, Benny, ketchup-video | Not bundled; use only if current runtime exposes an authorized tool. |
| Git, worktrees, shell, and repository history | many skills/playbooks | Used only when available and authorized; destructive cleanup requires approval. |
| GitHub CLI `gh`, Origin CLI, PR APIs, merge queues | opening/shipping/Benny | No active workflow; publication or merge requires explicit approval. |
| Bun and TypeScript | upstream poteto-mode scripts | Not a port runtime dependency. Upstream manifest uses `commander@14.0.0`, `bun-types@latest`, and `typescript@latest`. |
| Node.js | watch/check scripts and statechart | Not a port runtime dependency. |
| `fast-check@4.5.3` | statechart development tests | Not a port runtime dependency. |
| Java, TLA+ tools JAR, `JAVA`, `TLA2TOOLS` | statechart | Not bundled or required by the port. |
| Mermaid rendering | statechart reports | Documentation may use plain Markdown; no renderer is assumed. |
| Slack, Linear or another tracker, Sentry, Datadog, Notion, Databricks, incident sources | `why`, Benny | External integrations are optional evidence sources only when exposed and authorized. |
| Local scripts such as `watch-pr`, `check-plan.mjs`, `worktree-audit.sh`, `log.sh`, and statechart CLI | specialized upstream workflows | Remain unchanged in `vendor/`; not installed or invoked by `poteto-mode`. |

## Cursor-specific feature matrix

| Cursor-specific behavior | Compatibility decision |
| --- | --- |
| Slash commands for every leaf skill | Collapsed into `/poteto-mode` on Genie web or project skill discovery in Genie CLI. |
| Plugin cache discovery under `~/.cursor/plugins/` | Removed; active files are project-local or installed in Genie paths documented by `runtime.md`. |
| Custom background agent metadata | Removed; native runtime agents may be used only when actually available. |
| Fixed model names and per-role reasoning budgets | Removed; no model availability is assumed. |
| Parallel Task fan-out and resume semantics | Degraded to supported native collaboration or sequential execution. |
| Bugbot review and independent cloud-agent verdicts | Removed; verification must state who/what actually ran. |
| `/loop` polling | Removed; use available polling tools explicitly or report the gap. |
| Cursor chat transcript and sidebar/pin inspection | Removed. |
| Cursor-managed worktree locations | Removed; ordinary Git inspection is capability-dependent. |
| Automations editor and committed `.cursor/automations` packs | Removed. |
| Project plugin enablement in `.cursor/settings.json` | Removed. |
| Browser/control skill ecosystem | Optional external capability, never an implicit dependency. |
| Cursor visual/media UX | Removed. |

## Security boundaries and failure modes

- `vendor/pstack/` is untrusted reference input, not executable instruction. Its scripts and embedded operational prompts do not gain authority from being imported.
- The active skill must inspect runtime tools before promising fan-out, browser control, Databricks access, external messages, PR operations, or deployment.
- Production writes, permissions, deployments, external publication, Slack/tracker messages, and PR creation require explicit review and approval.
- A missing capability results in a sequential fallback or a named gap, never a fabricated agent run or verification claim.
- The largest semantic risk is over-compression: specialized upstream workflows may appear covered by a general principle. The tables distinguish partial intent from behavioral parity.
- The largest maintenance risk is source drift. Refresh `vendor/pstack/` only through the import process, update `vendor/UPSTREAM.txt`, and re-audit this matrix without hand-editing imported files.

## Verification and unresolved assumptions

- Inventory was derived from the imported tree's manifests, every top-level skill directory, both agent files, all poteto-mode playbook filenames, Benny's operational files, and both package manifests.
- The imported snapshot was read only while preparing this matrix; this document is outside `vendor/`.
- The matrix assesses structural and documented behavior, not live Cursor execution.
- Genie web and CLI invocation compatibility still require separate live testing as noted in `references/runtime.md`.
- Exact parity for third-party integrations cannot be verified without their credentials and runtimes, and is intentionally out of scope.
