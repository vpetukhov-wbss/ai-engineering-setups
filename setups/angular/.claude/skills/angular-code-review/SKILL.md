---
name: angular-code-review
description: "Independent Angular PR review focusing on correctness, security, performance, testability and UX."
---

# angular-code-review

## Procedure
1. Read intent, diff, acceptance criteria and existing code conventions before evaluating design.
2. Rank functional/security issues first, then state/race/leaks, a11y, performance, tests and maintainability.
3. Flag over-engineering, arbitrary utils, broad shared state, duplication, unsafe casts and inaccessible custom controls.
4. Provide line-level, evidence-based blockers and actionable remediation, not stylistic churn.
5. Summarize executed checks and acknowledge tests not run.

## Deliverables
Summarize scope and choices, changed files, verified commands/results, evidence, risks and required human approvals.

## References
`knowledge/ANGULAR_PLAYBOOK.md`, `knowledge/SOURCES.md`.
