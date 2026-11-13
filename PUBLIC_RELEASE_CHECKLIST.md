# Public release checklist

`pstack-genie` is an independent, public, community-maintained project designed for Genie Code web and CLI. Publishing this source does **not** publish or configure any Databricks workspace.

Before making the GitHub repository public:

- [ ] Confirm the code may legally be published and retain upstream license and copyright notices.
- [ ] Review **all committed files and full Git history** for credentials, company or customer data, private schemas, internal links, and proprietary configurations. `.gitignore`.
- [ ] Run `python scripts/validate_repo.py`, `python scripts/check_public_release.py`, and `python -m unittest discover -s tests -v`.
- [ ] Scan the **complete Git history** with a dedicated secret-scanning tool, such as Gitleaks, not only the working tree.
- [ ] If importing upstream pstack, inspect `vendor/pstack/` for release suitability, retain original licenses/attribution, and record the upstream revision.
- [ ] Do not commit `.env`, `.databrickscfg`, tokens, local Genie profiles, workspace exports, logs, or company-specific code/data.
- [ ] Verify the README accurately describes what works and what remains unported; do not suggest endorsement by Databricks or Cursor.
- [ ] Configure GitHub branch protection or rulesets, required checks, and pull request reviews as appropriate.
- [ ] Review the GitHub Actions workflow for least privilege and security before allowing outside contributions.
- [ ] Enable private vulnerability reporting, set up an appropriate security contact, and review public issues before discussing sensitive bugs.

## Publishing a new public GitHub repository

1. On GitHub, create a new repository named **`pstack-genie`** in the intended account or organization. Choose **Public** visibility, if authorized.
2. Create it **empty** (do not initialize a README, `.gitignore`, or license), because these files already exist locally.
3. After reviewing the local files and Git history, run:

   ```bash
   git init
   git add .
   git commit -m "Initial public pstack-genie starter"
   git branch -M main
   git remote add origin https://github.com/<YOUR_USERNAME>/pstack-genie.git
   git push -u origin main
   ```

4. Verify the public repository from an unauthenticated browser and inspect visible Actions logs and repository contents for sensitive material.
5. On GitHub, configure **Settings → Rules → Rulesets** or branch protection, Actions permissions, and security features appropriate for a public repository.

## Switching an existing GitHub repository to public

Open the repository's **Settings → General → Danger Zone → Change repository visibility**, select **Public**, and confirm. Review all history, releases, Actions artifacts and logs before switching. Organization policy may restrict changes.

Reference: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility
