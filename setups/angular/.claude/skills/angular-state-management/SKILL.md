---
name: angular-state-management
description: "Choose Angular signals, RxJS or a state library based on observed state complexity and ownership."
---

# angular-state-management

## Procedure
1. Inventory all state and its true owner (component, URL, server or shared feature).
2. Prefer local signals/computed for synchronous UI state; use RxJS for streams and cancellation; avoid effects as generalized event buses.
3. Define loading/error/refetch, deduplication, stale data, optimistic update and invalidation behavior.
4. Only recommend centralized libraries for justified cross-feature coordination; avoid conflicting stores.
5. Write tests for racing requests, cancellation, stale responses and navigation teardown.

## Deliverables
Summarize scope and choices, changed files, verified commands/results, evidence, risks and required human approvals.

## References
`knowledge/ANGULAR_PLAYBOOK.md`, `knowledge/SOURCES.md`.
