Client distribution
===================

1. Publish a versioned, code-signed Windows build from a controlled release pipeline.
2. Provision the customer tenant and user in the cloud admin system.
3. Assign the plan and subscription period based on verified payment state.
4. Customer installs the signed product and signs in.
5. Server issues a device-bound activation and short-lived signed license lease.
6. Client periodically renews the lease over HTTPS and records app/job usage.
7. When the subscription expires, the server stops renewing leases. Protected features are restricted when the current lease expires, subject to a bounded offline grace period.
8. After payment is confirmed, entitlement is restored and the desktop regains access after validation.

Immediate remote shutdown cannot be guaranteed while a device is offline. Keep account, export, and support access available where appropriate. Document data ownership, export, retention, and deletion terms.

Package Playwright browser dependencies deliberately, test on clean Windows machines, store user data under the per-user application-data directory, and sign installers/binaries with published checksums.
