# Interrogate workflow

Use this workflow for an adversarial review, challenge, stress test, or blind-spot search over a named change, design, or plan. Findings survive only when reproduced against accessible evidence. Report findings; do not apply fixes unless the user separately requests a fix workflow.

## Frame the review

1. Use the scope the user names. Otherwise inspect the branch diff from its merge base through the working tree when Git and the base are available; if not, state the narrower accessible scope.
2. Restate the intended behavior and trust boundaries from the request, change history, and documentation. Ask only when ambiguity prevents deciding whether evidence violates the intent.
3. Define adversarial lenses appropriate to the change, such as correctness, boundary inputs, failure recovery, concurrency, authorization, compatibility, or operational safety. Do not manufacture a fixed reviewer count when fewer lenses cover the risk.

## Challenge and verify

- Give every pass the same scope, intent, prohibited actions, and evidence rule: a finding needs a failing test, reproduction command, prototype, or artifact that shows actual behavior differs from required behavior.
- Use independent native workers only when the runtime exposes them and their read or write scopes can be isolated. Otherwise run the adversarial lenses sequentially. Never describe a sequential self-review as multi-agent or independent review.
- Keep reproduction artifacts local and reversible. Do not change production code, commit, push, deploy, publish, or perform production writes while interrogating.
- Rerun each proposed finding against the reviewed state. Keep it only when the evidence reproduces and the mismatch breaks the stated intent. Drop style preferences, speculation, future-only risks, and failures inherited from outside the reviewed scope unless the change newly exposes them.
- Merge findings with the same root cause. No verified findings is a valid result.

Report the intent and scope, each verified finding with its exact command or artifact, observed result, required result, and impact, then summarize dropped candidates and why. Identify which native workers actually ran, if any.
