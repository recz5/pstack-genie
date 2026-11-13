# Engineering principles

These are a portable, concise adaptation of pstack's principles, not a verbatim reproduction of its upstream leaf skills.

- **Laziness protocol:** bias toward deletion and the smallest change that solves the problem.
- **Foundational thinking:** establish data shapes, constraints, and concurrency semantics before implementation.
- **Boundary discipline:** validate at trust boundaries; keep internal contracts explicit.
- **Model the domain:** encode important invariants in schemas, types, or well-defined structures.
- **Idempotent operations:** plan for retries and partial failures.
- **Prove it works:** require observable verification of the real artifact.
- **Fix root causes:** seek first causal mismatch rather than accumulating guards.
- **Test behavior:** preserve meaningful tests across internal refactors.
- **Explain the number:** require baselines and equivalent conditions for quantitative claims.
- **Guard context:** read only files necessary for the current step.

If original pstack content has been imported, consult `vendor/pstack/` through the repository only when the environment grants file access. Do not pretend that source is installed if absent.
