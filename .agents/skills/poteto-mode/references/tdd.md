# TDD workflow

Use this workflow when the user explicitly requests TDD or a regression test, or when a defect has an obvious, cheap local test target. Do not force it when the only path needs broad harness setup, brittle mocks, slow infrastructure, production-only state, or unrelated fixture churn.

1. State intended behavior, current behavior, and the smallest observable reproduction.
2. Choose the narrowest existing test level that exercises the behavior.
3. Add a focused behavioral regression test before changing production code.
4. Run that test and confirm it fails for the intended reason. If it passes or fails for another reason, correct the test or reproduction first.
5. Make the smallest production change that fixes the root cause without weakening valid assertions.
6. Rerun the regression test, then the nearest related checks.
7. Report the failing-before evidence, passing-after evidence, and checks not run.

If a failing automated test is impractical, do not add a bad test. Use the closest executable check, such as a targeted script, safe manual reproduction, snapshot, log assertion, or focused integration check, and state why failing-before test evidence was unavailable.
