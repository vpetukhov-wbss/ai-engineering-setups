---
name: angular-ssr-performance
description: "Choose Angular SSR/SSG/CSR and diagnose hydration, bundle size, change detection and web vitals."
---

# angular-ssr-performance

## Procedure
1. Inspect actual Angular version and enabled render modes; define route SEO/indexing, freshness, personalization and latency needs.
2. Distinguish CSR, SSG, SSR and route-level hybrid. Respect platform checks for DOM/window and hydration differences.
3. Evaluate lazy routes, @defer, image optimizations, bundle budgets, caching, signals, stable tracking and zoneless compatibility.
4. Measure LCP/INP/CLS with repeatable environment; profile before modifying hot paths.
5. Verify authenticated content is not leaked via shared caching or SSR serialization, then document tradeoffs.

## Deliverables
Summarize scope and choices, changed files, verified commands/results, evidence, risks and required human approvals.

## References
`knowledge/ANGULAR_PLAYBOOK.md`, `knowledge/SOURCES.md`.
