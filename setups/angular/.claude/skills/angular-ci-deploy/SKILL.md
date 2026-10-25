---
name: angular-ci-deploy
description: "Build secure Angular CI/CD plan for static SPA and SSR/Node deployments."
---

# angular-ci-deploy

## Procedure
1. Inspect scripts, lockfiles, Node/Angular support range, hosting and production runtime (static CDN vs SSR Node).
2. Define dependency caching and `npm ci`, lint, type check, unit tests, build budgets, optional E2E/a11y and audit policy.
3. For SPA set rewrite fallback and immutable hashed asset caching; for SSR configure trusted proxy headers, health/observability and isolation.
4. Provide staging smoke, rollback/versioning, secrets via CI vault and supply chain review.
5. Never commit deployment credentials or submit live production deploy without approval; report what actually ran.

## Deliverables
Summarize scope and choices, changed files, verified commands/results, evidence, risks and required human approvals.

## References
`knowledge/ANGULAR_PLAYBOOK.md`, `knowledge/SOURCES.md`.
