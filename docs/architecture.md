Data-Flow architecture
======================

Desktop: Windows, Python, Eel, HTML/CSS/JavaScript. Automation: Playwright. Local data: SQLite. Cloud control plane: FastAPI and PostgreSQL. Redis is optional for cache, rate limiting, and queues when measured demand justifies it.

The desktop is an untrusted client. Never embed database credentials or license-signing private keys in the EXE. The cloud API is authoritative for identity, tenant membership, subscription status, device activation, and audit events. It issues short-lived signed license leases verified by a public key in the desktop. Revocation takes effect on the next successful check or lease expiry; instant remote shutdown is impossible while a device is offline.

Every cloud-owned business record is tenant-scoped. Tenant scope comes from authenticated server-side identity, not a client-supplied tenant ID. Billing webhooks must be signature-verified and idempotent. Passwords require modern password hashing; sessions require short-lived access tokens and refresh-token rotation.

Workflow: sign in and activate device; import XLSX/CSV; select sheet and header row; map columns to web form fields; validate mapping; execute rows through Playwright; record row outcomes; sync minimal usage telemetry and job summaries.

Suggested cloud entities: tenants, users, tenant memberships, plans, subscriptions, devices, license activations, license leases, automation profiles, usage events, audit logs, billing webhook events.

Distribution: publish a versioned, code-signed Windows build. Provision customer entitlements server-side. Store local user data in a per-user application data directory. Do not treat the installer directory as writable data storage.

SQLite is per-installation local storage, not the global SaaS database. Scale FastAPI and PostgreSQL independently. Add Redis, workers, queues, read replicas, and horizontal replicas only when workload measurements justify them. Capacity claims require reproducible load tests.