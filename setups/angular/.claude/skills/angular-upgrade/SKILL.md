---
name: angular-upgrade
description: "Plan risk-controlled Angular/TypeScript/Node migration without unsupported assumptions."
---

# angular-upgrade

## Procedure
1. Discover exact versions, package manager, Node support, breaking library dependencies, styles and test tooling.
2. Consult official Angular update guide for source and destination versions; prefer incremental migrations and schematics on clean branch.
3. Identify standalone adoption, deprecated APIs, Angular compiler/strict templates, zoneless/ZoneJS and runner differences.
4. Prepare reversible increments with tests and benchmark baselines; keep private forks/dependencies visible as blockers.
5. Never change all dependencies in one unreviewable commit or promise compatibility without running build/tests.

## Deliverables
Summarize scope and choices, changed files, verified commands/results, evidence, risks and required human approvals.

## References
`knowledge/ANGULAR_PLAYBOOK.md`, `knowledge/SOURCES.md`.
