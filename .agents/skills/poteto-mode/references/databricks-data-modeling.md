# Modeling checklist

- State fact table grain in one sentence and test candidate keys for duplicates.
- Verify how dimensions join; compare `COUNT(*)` before and after each join to find unexpected fanout.
- Separate event, session, user, and request metrics. These are not interchangeable populations.
- Distinguish ingestion timestamp from event timestamp and reporting date/timezone.
- Define whether historical corrections, late events, and slowly changing dimensions are supported.
- Ensure measures are additive, semi-additive, or non-additive as documented.
- Treat consent-based analytics as sampled/filtered observations of users who consented, not whole-site traffic.
- Identify dashboard contracts before schema changes.

For marketing analytics, validate attribution rules and user/session identifiers against actual instrumentation; never assume their definitions from names alone.
