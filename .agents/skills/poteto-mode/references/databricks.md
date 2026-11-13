# Databricks guidance for poteto-mode

Use this reference **only when the current task involves Databricks** (for example: Delta Lake, SQL/PySpark, medallion layers, Unity Catalog, Lakeflow, AI/BI dashboards, or Databricks deployment). For other work, remain general-purpose and do not load this reference.

This is not a separate skill or mode. Follow the active poteto-mode playbook, layering these considerations into its investigation, design, and verification steps.

## Investigate

1. Confirm accessible workspace, catalog, schema, environment, and privileges from real evidence; never guess.
2. Inspect relevant data sources, table definitions, Delta properties, pipelines, jobs, dashboards, and lineage using available read-only tools.
3. Document dataset grain, keys, deduplication, freshness assumptions, downstream consumers, and sensitivity.
4. For modeling or analytic correctness, read [data modeling](databricks-data-modeling.md). For ETL or pipeline work, read [pipeline quality](databricks-pipeline-quality.md).

## Design and implement

1. Evaluate Bronze, Silver, and Gold responsibilities based on actual contracts; naming alone proves nothing.
2. Specify incremental loading, late-arriving data, reprocessing behavior, idempotency, and schema compatibility.
3. Verify fact/dimension joins, row multiplication, event/session/user populations, and aggregation before recommending changes.
4. For Unity Catalog, production, and configuration changes, read [deployment safety](databricks-deployment-safety.md).
5. Stage changes in version control and verify them against a non-production environment when authorized.

## Verify and report

- Check uniqueness, nullability, reconciliation, temporal consistency, referential integrity, freshness, and metric invariants.
- Prefer bounded, read-only validation SQL; disclose cost before expensive workloads.
- Support performance claims with actual query or job evidence rather than SQL appearance alone.
- Distinguish proposed checks from executed tests, and disclose missing access and remaining uncertainty.
- Get explicit review and approval before consequential production writes, permission changes, or deployment.
