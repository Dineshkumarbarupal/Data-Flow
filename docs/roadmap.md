Data-Flow roadmap
=================

Phase 1: modular desktop shell; SQLite schema/migrations; workbook import/preview; column mapping and validation; Playwright browser lifecycle and configurable form workflow; cloud sign-in, tenant model, device activation, subscription status, signed license lease; usage history; Windows packaging; automated tests.

Phase 2: payment provider and verified webhooks; admin portal; tenant/plan/invoice/license management; background jobs, retries, observability, and support tooling.

Phase 3: SSO/MFA, granular RBAC, audit exports, tenant-isolation testing, queue-backed execution, metrics/tracing, backup and disaster recovery.

Phase 4: multi-region deployment, regional data strategy, global routing, event-driven integrations, and tested recovery objectives. Microservices and distributed databases only when independently justified.

A feature is complete only after implementation, tests, UI verification, and documentation. Capacity claims require reproducible load-test evidence.