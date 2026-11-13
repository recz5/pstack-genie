# Public release checklist

`pstack-genie` is an independent, public, community-maintained project designed for Genie Code web and CLI. Publishing this source does **not** publish or configure any Databricks workspace.

Before publishing or changing repository visibility:

- [ ] Confirm the code may legally be published, including any required employer or contributor approval, and retain upstream license and copyright notices.
- [ ] Review the files that will be public and **all Git history** for credentials, company or customer data, private schemas, internal links, and proprietary configurations. `.gitignore` does not remove files from existing commits.
- [ ] Run `python scripts/validate_repo.py`, `python scripts/check_public_release.py`, and `python -m unittest discover -s tests -v`.
- [ ] Scan the **complete Git history and current files** with a dedicated secret-scanning tool, such as Gitleaks. Record the tool and result; the repository check is not a substitute.
- [ ] If importing upstream pstack, inspect `vendor/pstack/` for release suitability, retain original licenses/attribution, and record the upstream revision.
- [ ] Do not commit `.env`, `.databrickscfg`, tokens, local Genie profiles, workspace exports, logs, or company-specific code/data.
- [ ] Verify the README accurately describes what works and what remains unported; do not suggest endorsement by Databricks or Cursor.
- [ ] Configure GitHub branch protection or rulesets, required checks, and pull request reviews as appropriate.
- [ ] Review the GitHub Actions workflow for least privilege and security before allowing outside contributions.
- [ ] Configure a private security reporting method and appropriate security contact before directing researchers to report sensitive issues.

## Publishing to a new GitHub repository

1. Confirm the intended owner and repository name. Create an empty repository on GitHub; do not initialize a README, `.gitignore`, or license because those files are already in this checkout.
2. From the repository root, confirm the branch, working tree, history, and remotes:

   ```bash
   git status --short --branch
   git log --oneline --decorate --all
   git remote -v
   ```

3. If this checkout has no remote, add the reviewed repository URL. If it already has a remote, verify that it points to the intended owner and repository; do not add a second `origin`.
4. After final review and authorization to publish, push the intended branch. Do not use `git init` on an already initialized checkout.
5. Verify the public repository from an unauthenticated browser and inspect visible Actions logs and repository contents for sensitive material.
6. On GitHub, configure **Settings → Rules → Rulesets** or branch protection, Actions permissions, and security reporting appropriate for a public repository.

This checkout already has a `main` branch and an `origin` tracking `origin/main`. Confirm the remote destination before pushing; the steps above are not a request to publish changes automatically.

## Switching an existing GitHub repository to public

Open the repository's **Settings → General → Danger Zone → Change repository visibility**, select **Public**, and confirm. Review all history, releases, Actions artifacts and logs before switching. Organization policy may restrict changes.

Reference: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility
