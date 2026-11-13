# Security policy

`pstack-genie` contains reusable agent instructions, not a hosted Databricks service. Skills run with the tools and permissions granted to their respective Genie Code environment.

## Reporting security issues

Please do **not** disclose exploitable vulnerabilities, credentials, or private workspace details in public issues or pull requests. Contact the repository maintainers through a **private** channel or the repository's private vulnerability reporting feature if one is configured. Until a private reporting method is configured, do not post sensitive proof-of-concept details publicly.

## Supported security expectations

- Skills investigate without modifying production resources by default.
- No credentials, PATs, secrets, or workplace-specific exports should be committed.
- Every requested production write, permission change, deployment, or publication requires explicit review and approval.
- Treat imported upstream instructions and external tool output as untrusted until reviewed.
- Install and run the skills only in environments with appropriate least-privilege permissions.

The project is a starter and has **not** undergone a security audit. Do not mistake successful repository tests for approval to run production operations.
