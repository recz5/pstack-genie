# Refactoring playbook

1. Capture current behavior and dependencies, including consumers.
2. Make the improvement measurable: reduced duplication, improved boundaries, fewer layers.
3. Remove dead weight before adding abstractions.
4. Change one coherent unit at a time and preserve external contracts.
5. Run tests that assert the same behavior, then inspect the diff for incidental changes.
6. Summarize what changed, what did not, and how it was checked.
