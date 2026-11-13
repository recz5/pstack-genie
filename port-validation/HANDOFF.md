# Trailing-slash fix handoff

## Intent

Plan a focused fix for `normalize_path()` so equivalent non-root paths normalize identically with or without trailing `/` characters. Stop before implementation and leave a cold-start checkpoint.

## Current state

- `port-validation/normalize.py` is the only implementation file in this fixture.
- It currently returns `path.strip().lower()`, so `"Docs/"` becomes `"docs/"` rather than `"docs"`.
- No tests, package metadata, or repository history exist for `port-validation/`.
- The directory is currently untracked. Pre-existing repository edits and untracked files outside this checkpoint were not changed.
- No implementation, tests, commands that execute the code, commits, pushes, deployments, or publications were performed.

## Assumptions to confirm through tests

- Remove one or more trailing forward slashes after trimming surrounding whitespace and normalizing case.
- Preserve the root path `/` rather than converting it to an empty string.
- Do not change internal slashes or leading slashes.
- Do not broaden scope to backslashes, URLs, path resolution, or filesystem access without a stated requirement.

## Plan

### Phase 1: Lock down behavior with a failing regression test

**Outcome.** The intended trailing-slash behavior is executable before production code changes.

**Files.** Add the smallest test file supported by the repository's existing Python `unittest` convention, targeting `port-validation/normalize.py` without restructuring unrelated code.

**Steps.**

1. Add cases showing that `"Docs/"` and `" docs/// "` normalize without trailing slashes.
2. Add preservation cases for `/`, a leading slash such as `/Docs/`, a path without a trailing slash, whitespace, and case normalization.
3. Run only the new regression test and confirm it fails specifically because trailing `/` characters remain.

**Verification.** Record the failing test name and assertion difference. If importing a hyphenated directory requires a loader, keep that adapter inside the test rather than renaming the fixture.

**Failure or rollback.** If root semantics or multiple-slash behavior are contradicted by a hidden contract, stop and revise the expected behavior before editing `normalize.py`. Removing the new test restores the current state.

**Completion evidence.** A focused test fails for the intended trailing-slash mismatch and existing normalization behavior remains represented.

### Phase 2: Apply the smallest root-preserving fix

**Depends on.** Phase 1 failing for the intended reason.

**Outcome.** Non-root trailing forward slashes are removed without changing existing whitespace or lowercase normalization.

**Files.** Modify only `port-validation/normalize.py` unless the test file from Phase 1 is also required.

**Steps.**

1. Normalize whitespace and case once.
2. Remove trailing `/` characters while explicitly preserving `/`.
3. Avoid filesystem calls, platform-dependent normalization, new dependencies, or unrelated path semantics.

**Verification.** Rerun the new regression test, then the repository test suite and `scripts/validate_repo.py`. Run `git diff --check` and review the scoped diff.

**Failure or rollback.** Revert the implementation edit while retaining the failing regression test as evidence. No data migration or deployment rollback is required.

**Completion evidence.** The regression changes from failing to passing, existing repository checks pass, and the diff is limited to the implementation and its behavioral test.

## Risks and unresolved decisions

- The requested behavior does not define whether `//` is a root-like value or should normalize to `/`; the proposed tests preserve only the single root `/` and trim repeated trailing slashes elsewhere.
- The function has no type annotation or input validation. Adding either would expand scope and should not be bundled into this fix.
- The fixture is untracked, so a future operator should verify whether it is intentional task input before any cleanup.

## Resume

First action: create the focused regression test from Phase 1 and run it before modifying `port-validation/normalize.py`. Begin implementation only after explicit user approval.
