---
name: maui-offline-sync
description: "Design and implement offline-first MAUI data flows, local database queues, conflict handling and safe retries."
---

# maui-offline-sync

## Procedure
1. Identify offline reads vs writes, data sensitivity, local retention, tenancy and business consequences of stale data.
2. Define authoritative server state, cache strategy, local schema/migrations and access control. Choose SQLite or another store only if needed.
3. For queued writes design immutable operation ID, server-side idempotency, retry classification/backoff, attempt limit, ordering and user-visible sync status.
4. Define explicit optimistic concurrency/conflict behavior; preserve both versions when conflicts must be resolved by user.
5. Wire cancellation and app resume to reliable sync scheduling; do not assume unrestricted iOS background execution.
6. Validate sign-out and account/tenant switch wiping or partitioning; handle device restore, secure-storage failures and schema upgrades.
7. Test connectivity flapping, duplicate replay, server 409/429/500, token expiry, clock skew, partial multi-item failure and disk pressure.

## Output
State diagram, sync contract, failure matrix, migration plan, tests and data security notes.

## Reference
`knowledge/MAUI_CROSS_PLATFORM.md`.
