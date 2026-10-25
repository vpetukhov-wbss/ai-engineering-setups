---
name: angular-architecture
description: "Design Angular application architecture from business requirements, API boundary, render strategy and delivery constraints."
---

# angular-architecture

## Procedure
1. Discover repo versions, domain model, user journeys, target devices and nonfunctional requirements.
2. Compare feature-oriented standalone SPA, SSR/hybrid, monorepo and module federation only where necessary; choose the least complex fitting model.
3. Draw boundaries: routes/features, domain-facing services, DTOs, state ownership, backend authority, authentication, shared UI/design system.
4. Describe data flows, error states, caching, delivery and tests; record major choices as ADR with alternatives and migration plan.
5. Propose staged implementation with acceptance criteria and measurable performance/accessibility gates.

## Deliverables
Summarize scope and choices, changed files, verified commands/results, evidence, risks and required human approvals.

## References
`knowledge/ANGULAR_PLAYBOOK.md`, `knowledge/SOURCES.md`.
