# Autonomous run workflow

Use this workflow when the user explicitly asks the agent to keep driving one bounded task to a checkable outcome without routine approval pauses. It does not grant permission to commit, publish, deploy, change permissions, or perform production writes.

1. State one checkable exit predicate before the first iteration. Keep the user's predicate fixed; do not weaken it to declare success.
2. Identify the available wake mechanism. Use native runtime waiting or event tools only when they actually exist and are authorized. Otherwise iterate synchronously or tell the user which external wait cannot be performed; never pretend a background loop is armed.
3. Establish the baseline and the verification command or observable check before changing anything.
4. Run bounded iterations. Each iteration records the hypothesis, makes the smallest reversible change the evidence supports, runs the check, and either keeps the improvement or reverts that iteration completely. Do not retain speculative safeguards.
5. Address a discovered blocker only when it prevents the exit predicate. Keep unrelated findings as named follow-ups rather than expanding the run.
6. Checkpoint every iteration through [Show me your work](show-me-your-work.md), using its canonical TSV columns: put the iteration in `phase`, the hypothesis and change in `decision` and `why`, the verification pointer in `evidence`, and `kept`, `reverted`, or `INCONCLUSIVE` in `result`. Do not create commits unless the user explicitly requested them.
7. Stop when the predicate is met, the authorized time or iteration bound is reached, or a genuine blocker prevents useful progress. A plateau requires a changed hypothesis, not repeated identical attempts.

Report the exit predicate, iterations attempted, changes kept and discarded, final evidence, and any blocker. Distinguish `VERIFIED`, `NOT VERIFIED`, and `INCONCLUSIVE`.
