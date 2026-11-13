# Contributing to pstack-genie

Thanks for your interest in improving portable `poteto-mode` workflows for Genie Code.

## Scope

Keep `poteto-mode` general-purpose. Databricks-specific guidance belongs in poteto-mode references, not in a second skill. Maintain compatibility with both Genie Code web and Genie Code CLI when possible. Clearly document environment-specific behavior; never silently assume Cursor tools are available.

## Change process

1. Open an issue or pull request explaining the problem, proposed behavior, and impact on both runtimes.
2. Make changes in a feature branch, preserving `SKILL.md` frontmatter and valid relative references.
3. Run `python scripts/validate_repo.py`, `python scripts/check_public_release.py`, and `python -m unittest discover -s tests -v`.
4. Add a test or an explicit manual test case for changed behavior, especially skill discovery and environment-specific orchestration.
5. Explain what was tested and what still requires live Genie Code verification.

Never submit credentials, workspace content, employer-private architecture, production dataset extracts, or copied materials without appropriate rights. Contributions incorporating upstream pstack files must retain required MIT license notices and source attribution. Follow the security reporting guidance in `SECURITY.md`.
