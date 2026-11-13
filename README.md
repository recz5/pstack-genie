# pstack-genie

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Lauren Tan's [pstack](https://github.com/cursor/plugins/tree/main/pstack) is an opinionated engineering skill stack built around rigorous, verifiable agent workflows. **pstack-genie brings that approach to Databricks Genie Code**, with a shared skill layout for **Genie Code in the workspace** and **Genie Code CLI**.

Tell `poteto-mode` what you want to accomplish. It chooses an investigation, design, implementation, or verification workflow based on your task, then consults Databricks-specific references when the work calls for them. **There is only one installable skill and one entry point: `poteto-mode`.** The goal is the same whether you're reviewing a GitHub Actions workflow or a Delta Lake model: **understand the system, make the smallest useful change, and verify the outcome**.

This is a community-maintained project, not an official Databricks, Cursor, or Lauren Tan release.

> **Project status — starter adaptation.** The skills in this repository are working **independent adaptations** for Genie Code, not a complete port of upstream pstack. The included importer can bring the original source into `vendor/pstack/` for review. Cursor-specific subagents, hooks, and model orchestration are not enabled just by importing it. See [Port status](#port-status).

## Built for Genie Code

The same `.agents/skills/` directory is the source of truth for both runtimes:

| | Genie Code in the Databricks workspace | Genie Code CLI |
| --- | --- | --- |
| **Install** | Register the Git-backed skills folder in Genie Code Settings | Open the repository in Genie Code CLI, or install skills to `~/.genie/skills/` |
| **Invoke** | Mention `@poteto-mode` in a conversation | Ask for `poteto-mode` by name or select the skill using the CLI's available interface |
| **Best for** | Working with authorized workspace objects, SQL, data, and notebooks | Local repositories, code review, development workflows, and authorized Databricks resources |
| **Skill source** | `.agents/skills/` | `.agents/skills/` |

Genie Code supports [custom agent skills in the workspace](https://docs.databricks.com/aws/en/genie-code/skills/) and [local or project-level skills in the CLI](https://docs.databricks.com/aws/en/genie-code/genie-code-cli). Availability of individual tools and permissions still depends on your environment.

## Install

<details>

<summary><strong>Genie Code (Databricks workspace)</strong></summary>

1. Publish this repository to GitHub, then add it as a **Databricks Git folder** in your workspace.

2. Open **Genie Code → Settings → Skills**.

3. Add the path to the **parent skills folder**, not to an individual `SKILL.md`, for example:

   ```text
   /Workspace/Users/<your-user>/pstack-genie/.agents/skills
   ```

   Use the actual path of your Databricks Git folder.

4. Enable `poteto-mode`. No additional skills are required for Databricks tasks.

5. Start a fresh Genie Code conversation and try:

   ```text
   @poteto-mode Review this data pipeline's design and identify any correctness risks.
   ```

The repository is public, but the skills don't grant anyone access to your Databricks data. Genie Code only has the permissions configured for your own workspace session.

[Databricks: extend Genie Code with agent skills](https://docs.databricks.com/aws/en/genie-code/skills/)

</details>

<details>

<summary><strong>Genie Code CLI</strong></summary>

Clone the repository and run Genie Code CLI from the project root:

```bash
git clone https://github.com/<YOUR_USERNAME>/pstack-genie.git
cd pstack-genie
python scripts/validate_repo.py
genie
```

Genie Code CLI discovers skills from the repository's `.agents/skills/` directory. Ask it to use `poteto-mode` for the task.

To use the skills in **other** projects, optionally copy them to your personal Genie Code CLI skills directory:

```bash
python scripts/install_cli.py --dry-run
python scripts/install_cli.py
```

The installer will not overwrite existing skills unless explicitly given `--force`. Open a new CLI session after installing or updating them.

[Databricks: Genie Code CLI](https://docs.databricks.com/aws/en/genie-code/genie-code-cli)

</details>

## Getting started

Use `poteto-mode` whenever a task deserves a structured engineering workflow. In the workspace, mention `@poteto-mode` at the start of your prompt:

```text
@poteto-mode Find out why this Gold fact table duplicates sessions after a join.
Reproduce the issue with read-only SQL, explain the cause, and propose a fix.
```

Or use it for general engineering work:

```text
@poteto-mode Review our GitHub Actions workflow for accidental production deployments.
Explain the risks before suggesting changes.
```

For a task involving Databricks, `poteto-mode` loads its own [Databricks references](.agents/skills/poteto-mode/references/databricks.md). For unrelated software engineering tasks, it stays general-purpose.

### Just use `poteto-mode`

`poteto-mode` is the main entry point. You describe the problem; it selects a playbook, investigates the available evidence, and reports what was changed or verified.

The starter currently includes these primary playbooks and triggered internal workflows:

| Playbook | When to use it |
| --- | --- |
| **Investigation** | Understand an existing system, behavior, or design without making changes. |
| **Bug fix** | Reproduce a defect, find the cause, and verify a correction. |
| **Feature** | Design and implement a bounded new capability with tests. |
| **Refactoring** | Improve structure without changing external behavior. |
| **Architecture** | Assess tradeoffs and review a technical design. |
| **Review** | Inspect code, pull requests, and deployment safety. |
| **Performance** | Diagnose measured latency, cost, or throughput issues. |
| **TDD** | Add a focused failing regression before a small fix when the test path is practical. |
| **Multi-phase plan** | Produce an evidence-driven, ordered plan without starting implementation. |
| **Pause safely** | Leave an explicit, durable checkpoint that a cold-start agent can resume. |
| **Runtime forensics** | Diagnose a live symptom from authorized runtime evidence without silently fixing it. |
| **Trace forensics** | Diagnose an existing profiling artifact as a fixed dataset. |
| **Figure it out** | Design an auditable hypothesis-driven run when no narrower playbook fits. |
| **Autonomous run** | Drive one bounded task to a fixed, checkable predicate through evidence-based iterations. |
| **Hillclimb** | Improve one measured outcome with a frozen harness and keep-or-revert experiments. |
| **Orchestrate** | Coordinate a multi-unit program with explicit ownership, isolation, and verified evidence. |
| **Interrogate** | Challenge a change or design adversarially and retain only reproduced findings. |
| **Show me your work** | Keep an append-only, evidence-linked decision trail for reviewable long runs. |

These are the **eighteen workflows implemented in this starter**, not the full set of upstream pstack workflows. You can find their instructions in [the poteto-mode references](.agents/skills/poteto-mode/references/).

## One skill, one entry point

[`poteto-mode`](.agents/skills/poteto-mode/SKILL.md) is the **only skill** installed by this project. Its playbooks cover general engineering; domain-specific guidance lives in its own `references/` folder and loads only when relevant.

```text
@poteto-mode Explain how this API handles failed requests and retries.
@poteto-mode Review the grain, keys, and aggregations in these Gold tables.
@poteto-mode Review this Databricks Asset Bundle for deployment safety.
Do not deploy anything.
```

No second command or skill is needed. Databricks expertise is a set of optional reference checklists within `poteto-mode`.

## Make it yours

This project is designed to be customized. Keep the general-purpose workflow intact, and add domain-specific references or playbooks **under `.agents/skills/poteto-mode/references/`**, not as separate discoverable skills. For example, a team could add ETL quality guidance, dashboard validation checklists, or coding standards.

Keep private workspace details in private configuration, not in a public fork. Never commit personal access tokens, connection profiles, customer data, internal source code, or exported production metadata to this repository.

### Rename the skill

You can rename the single installed skill without changing its internal workflows. Use `scripts/rename_skill.py` from the repository root; it accepts a destination name, an optional current name, and an `--apply` flag. **The default is a dry run**, so you can review the changes before applying them.

For example, to rename the current `poteto-mode` skill to `mango-mode`:

```bash
# Preview the rename (no files changed)
python scripts/rename_skill.py mango-mode --from poteto-mode
# Apply after reviewing the preview
python scripts/rename_skill.py mango-mode --from poteto-mode --apply
```

The script renames the folder under `.agents/skills/`, updates the `SKILL.md` metadata and maintained references in the repository, and leaves `vendor/pstack/` and `port-validation/` untouched. It **does not** commit or push changes, rename the GitHub repository, or update separately installed Genie Code skills.

After renaming, review and validate the changes:

```bash
git status --short
git diff HEAD --stat
git diff HEAD --check
python -m unittest discover -s tests -v
python scripts/validate_repo.py
python scripts/check_public_release.py
```

Refresh any separately installed CLI skill or Databricks workspace skill, remove the old installed name if necessary, and start a new Genie Code session to confirm the new name is recognized. Keep **only one exposed skill**.

### Import the upstream pstack source

If you want to examine and gradually port the original pstack implementation, run:

```bash
python scripts/import_upstream.py
```

This fetches upstream [cursor/plugins/pstack](https://github.com/cursor/plugins/tree/main/pstack) into `vendor/pstack/`, preserves its license, and records the upstream revision. It **does not replace or activate** the Genie Code skills automatically. Review each upstream component and port it into the supported Genie Code skill format deliberately.

## Port status

The goal is to make pstack's rigorous workflows usable in both Genie Code environments while preserving its general-purpose character. Today, this repository provides a small, portable foundation—not feature parity with upstream.

| Capability | Status |
| --- | --- |
| General-purpose `poteto-mode` skill | Included in starter |
| Fourteen primary playbooks and four triggered workflows | Included in starter |
| Databricks-specific references inside poteto-mode | Included in starter (not a separate skill) |
| Shared web + CLI skill source | Included; runtime setup still needs live validation |
| Upstream pstack source import | Available via script, not pre-imported |
| Original Cursor subagents, model routing, hooks, and `/loop` | Not ported |
| Native custom `/poteto-mode` command on both Genie Code interfaces | Not verified; use supported skill invocation instead |

The compatibility rules are documented in [runtime guidance](.agents/skills/poteto-mode/references/runtime.md). Nothing in the starter should claim that a missing tool, subagent, or test actually ran.

## Data handling

`pstack-genie` is a set of skill instructions and local scripts. **This repository does not provide a hosted service or a telemetry endpoint.** When a skill asks Genie Code to inspect source code, tables, or logs, those requests are handled by your configured Genie Code environment and the applicable Databricks services and policies—not by a server operated by this repository.

Be mindful of what you expose to an AI assistant. Use least-privilege workspace access, avoid putting secrets in prompts or files, and require explicit approval for consequential production changes. The skills default to read-only exploration for data and infrastructure tasks.

## Validate

Before opening a pull request or releasing a public version, run:

```bash
python scripts/validate_repo.py
python scripts/check_public_release.py
python -m unittest discover -s tests -v
```

The GitHub Actions workflow runs the same checks. They are starter checks, **not** a replacement for reviewing your Git history and running a dedicated secret scanner before public release. See the [public release checklist](PUBLIC_RELEASE_CHECKLIST.md).

## Contributing

Issues, playbook improvements, compatibility fixes, documentation updates, and new references within `poteto-mode` are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidance and [SECURITY.md](SECURITY.md) for how to handle security-sensitive reports.

## License and acknowledgments

`pstack-genie` is released under the [MIT License](LICENSE). It is a community adaptation inspired by Lauren Tan's [original pstack](https://github.com/cursor/plugins/tree/main/pstack), which is also MIT-licensed (© 2026 Lauren Tan). Any upstream material imported into `vendor/pstack/` retains its original license and copyright notices. Attribution and reuse must follow those license terms.

Not affiliated with, sponsored by, or endorsed by Databricks or Cursor.
