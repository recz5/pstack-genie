# Orchestrate workflow

Use this workflow for a program with multiple independently verifiable work units that cannot reasonably be completed as one ordinary task. One bounded task driven to a predicate is Autonomous run; iterative metric optimization is Hillclimb; work that fits one focused implementation run should use its ordinary primary playbook.

## Scope the program

1. Define the program outcome, trust boundaries, dependency graph, shared-state risks, and completion evidence before assigning work.
2. Split work into units with one owner, explicit allowed and forbidden paths or actions, dependencies, and a command or observable artifact that proves completion. Start with one representative unit before widening concurrency.
3. Use only collaboration tools actually exposed by the current runtime. If no authorized worker mechanism exists, execute the units sequentially and report that fallback. Never invent workers, status, or independent verdicts.

## Coordinate execution

- Keep a coordinator-owned ledger of each unit's owner, state, dependencies, evidence, and disposition. The coordinator remains accountable for the program even when a worker implements a unit.
- Isolate concurrent writers by non-overlapping files or supported workspaces. Never assign multiple writers to the same state without an explicit serialization rule.
- Give each worker the goal, required context, write scope, prohibited actions, acceptance evidence, and handoff format. Do not pass secrets or broader permissions than the unit needs.
- Review the produced diff or artifact and rerun relevant evidence; a worker summary or green status alone is not a verdict. Use an independent verifier only when one actually runs, and identify it accurately.
- Retry by cause with a smaller scope or corrected context. After two failed retries for the same cause, replan, absorb the unit, or report it as blocked rather than looping.
- Ask the user only for an irreversible action, unavailable permission, product decision that evidence cannot settle, or a genuine blocker. Production writes, permission changes, deployments, commits, pushes, and external publication remain separately approval-gated.

Report program progress against the outcome, every unit's disposition and evidence, what was retried or dropped and why, which work ran concurrently or sequentially, and decisions still requiring the user.
