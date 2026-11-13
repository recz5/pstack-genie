# Databricks deployment safety

- Identify the target workspace and catalog from actual configuration, not environment labels alone.
- Use a least-privilege deployment identity; no hard-coded PATs, tokens, hostnames containing secrets, or credentials in Git.
- Prefer source-controlled Declarative Automation Bundles, tests, and reviewable changes.
- Require a dev/test dry run and diff of resource identities, root paths, ownership, grants, warehouses, and jobs.
- Distinguish code deployment from executing jobs or triggering pipelines. Treat either as consequential if production data is impacted.
- Block accidental catalog replacement or cross-environment overwrite with explicit environment guards.
- Confirm whether a resource uses embedded credentials; evaluate least privilege and sharing implications.
- Do not run DROP, TRUNCATE, DELETE, OVERWRITE, schema migration, permission grant/revoke, or production deploy without user approval of the exact effect and destination.
- Include rollback or forward-fix, backup/time-travel assumptions, and downstream dashboard validation in the deployment report.
