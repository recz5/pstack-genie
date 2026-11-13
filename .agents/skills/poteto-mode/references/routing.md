# Playbook routing

Match intent, not keywords. Select a single starting playbook and read its full file:

| Task intent | Playbook |
| --- | --- |
| Understand existing behavior, architecture, or tradeoffs without writing | [Investigation](investigation.md) |
| Diagnose a defect or incident | [Bug fix](bug-fix.md) |
| Add new behavior, pipeline, or capability | [Feature](feature.md) |
| Change internal structure while keeping behavior | [Refactoring](refactoring.md) |
| Review architecture or choose among designs | [Architecture](architecture.md) |
| Check a diff, pull request, or safety of a change | [Review](review.md) |
| Adversarially challenge a change or design and keep only reproduced findings | [Interrogate](interrogate.md) |
| Explain or improve measured performance or cost | [Performance](performance.md) |
| Drive one bounded task autonomously to a checkable predicate | [Autonomous run](autonomous-run.md) |
| Improve one measured outcome through repeated controlled experiments | [Hillclimb](hillclimb.md) |
| Coordinate a multi-unit program with explicit ownership and evidence | [Orchestrate](orchestrate.md) |
| Diagnose a symptom in a currently running process from captured live evidence | [Runtime forensics](runtime-forensics.md) |
| Diagnose an existing profile, trace, heap snapshot, or spindump without recapturing it | [Trace forensics](trace-forensics.md) |
| Design one auditable run for ambitious cross-cutting work or a requirement no narrower playbook fits | [Figure it out](figure-it-out.md) |

Apply these internal workflows in addition to the primary playbook only when their trigger matches:

| Trigger | Internal workflow |
| --- | --- |
| The user explicitly requests TDD or a regression test, or a bug has an obvious cheap local test target | [TDD](tdd.md) |
| The user asks for a plan for work that genuinely spans multiple dependent phases | [Multi-phase plan](multi-phase-plan.md) |
| The user explicitly asks to pause, stop, or leave a resumable checkpoint | [Pause safely](pause-safely.md) |
| The user requests a decision trail, or an authorized long-running run needs one | [Show me your work](show-me-your-work.md) |

Prefer investigation first when the request is ambiguous but evidence can resolve it. Never invent hidden subagent execution.

Runtime forensics and trace forensics return a diagnosis, not a fix. Once the cause is known, start a separate Bug fix or Performance run if the user asked for remediation.
