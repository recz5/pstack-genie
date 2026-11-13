# Multi-phase plan workflow

Use this workflow only when the user asks for a plan and the work has multiple dependent phases. For a small change with an obvious path, explain that a multi-phase plan would add overhead and provide the smaller next step instead.

The plan is the deliverable. Do not implement it until the user explicitly asks execution to begin.

1. Inspect the current architecture, conventions, entry points, tests, and operational constraints.
2. Resolve factual questions with safe investigation or a minimal non-production prototype. Ask only for product or preference decisions evidence cannot settle.
3. Define the target outcome, non-goals, acceptance criteria, security boundaries, and assumptions.
4. Split the work into ordered phases that each leave the system in a verifiable state. Name dependencies and safe parallel work without assuming agents are available.
5. For every phase, record the outcome, affected files or interfaces, implementation steps, behavioral verification, failure or rollback path, and completion evidence.
6. Identify cross-phase risks, migration or compatibility constraints, deployment requirements, and decisions that need explicit approval.
7. Write the plan to the user-requested path, or under `docs/` when a durable repository artifact is requested and no path is given. Otherwise return it in the response.
8. Hand back the plan and stop. Execution begins only on the user's explicit go.

Tests alone may be insufficient for phases that change a live interface or operation. Match verification to the actual surface, use only available authorized tools, and name any live or performance evidence that remains unavailable.
