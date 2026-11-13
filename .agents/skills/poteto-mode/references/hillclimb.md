# Hillclimb workflow

Use this workflow for sustained improvement of one measurable outcome through repeated experiments. Use Performance for diagnosing or fixing one performance issue; use Hillclimb only when the requested work is an optimization loop.

1. Define the realistic workload, one metric, the direction that is better, a regression gate, and a checkable stop predicate. When the user did not supply a target, establish a bounded experimental target rather than inventing a product requirement.
2. Build or identify one repeatable measurement command. Prove the harness can distinguish meaningfully different cases, report errors and work performed, choose a sampling rule appropriate to the noise, then freeze the harness for the run.
3. Record a baseline metric and a passing regression gate before the first candidate.
4. Open [Show me your work](show-me-your-work.md) and record every attempt with its canonical TSV columns: put the attempt in `phase`, the mechanism-based hypothesis and change in `decision` and `why`, the before, after, delta, and regression pointers in `evidence`, and the `kept`, `reverted`, or `INCONCLUSIVE` verdict in `result`. Keep the trail outside shipped source unless it is itself a requested deliverable.
5. Test one candidate at a time. Measure with the frozen harness and run the regression gate. Keep a candidate only when improvement clears observed noise and behavior remains correct; otherwise revert it fully.
6. Use native parallel workers only when the runtime exposes them, the user authorizes parallel work, candidates have isolated write scopes, and the root agent reviews every diff and result. Otherwise run candidates sequentially. Never claim independent review that did not occur.
7. On a plateau, change hypothesis category or revisit the architecture and measurement sensitivity. Stop at the predicate, the agreed experiment bound, or when remaining candidates are not worth their cost. Never relax the predicate after seeing results.

Report the metric and workload, baseline and final values with units, sampling method, attempts kept and reverted, regression evidence, final predicate state, and the best remaining hypothesis. Do not commit, push, open a pull request, deploy, or publish without explicit authorization.
