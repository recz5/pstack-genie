# Bug-fix playbook

1. Describe expected and actual behavior; identify a reliable reproduction.
2. Isolate the first causal mismatch rather than patching symptoms.
3. Capture a failing test or safe observable baseline.
4. Implement the smallest correct fix in an allowed environment.
5. Run the targeted test, related regression tests, and a diff review.
6. State which checks ran and which did not; include rollback notes if consequential.

Do not reproduce a risky production incident by changing production data.
