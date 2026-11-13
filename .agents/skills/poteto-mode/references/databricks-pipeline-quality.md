# Data pipeline quality

- Confirm the source system of record, incremental watermark, replay strategy, and idempotent merge key.
- Validate schema evolution and nullable fields on incoming events.
- Check duplicate handling, late arrivals, and malformed rows with explicit disposition.
- Compare raw source totals and transformed totals on equivalent grains, date windows, and filters.
- Test Gold rollups using independently derived SQL rather than repeating production transformation code.
- Monitor freshness, reconciliation drift, job error rate, runtime, and compute spend.
- Do not publish data with a degraded quality test without disclosing the exception.
