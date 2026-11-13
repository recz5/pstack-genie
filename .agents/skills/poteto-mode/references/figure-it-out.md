# Figure it out

Use this internal workflow when no narrower playbook fits, or when one ambitious cross-cutting run needs a bespoke, auditable workflow. It does not create another exposed skill.

## Frame

Before implementation, state a falsifiable definition of done, quantified scope, known blockers, and a proportional rigor level. Identify one-way doors and consequential actions; reversible local investigation may proceed, but deployments, publication, permission changes, production writes, and destructive actions still require explicit approval.

## Design the workflow

Write an ordered phase list before code. Decompose work into independently verifiable units, sequence the riskiest unknown first, and build or identify the verification harness before feature work. Capture a pre-change baseline when one exists. Parallelize only across clean seams and only with collaboration tools actually exposed by the runtime; otherwise work sequentially.

## Run the hypothesis loop

For each unit:

1. State the hypothesis and the observation that would falsify it.
2. Make the smallest reversible change or investigation.
3. Measure the real artifact against the definition of done.
4. Record a verdict of `VERIFIED`, `NOT VERIFIED`, or `INCONCLUSIVE`.
5. Keep an advancing change; revert or revise a non-advancing local change when safe. Never treat `INCONCLUSIVE` as a pass.

Verify each unit before beginning the next. If a gate passes suspiciously easily, inspect the observation method before trusting the result.

## Keep a local decision trail

Maintain a concise trail with the phase, hypothesis or decision, evidence, verdict, and next step. Store it in an existing task artifact when appropriate, or include it in the handoff. Do not commit, push, publish, or create external records unless the user explicitly requests and approves that action.

## Verify and hand back

Check the whole result against the original predicate on the real artifact, not only the harness. Encode recurring corrections in a focused test or validation rule when justified. Report the designed playbook, rigor level, decision-trail location or summary, verified outcomes, open items, and risks.
