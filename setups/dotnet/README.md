# .NET Engineering Intelligence — Claude Code setup

A project-agnostic, original synthesis of public engineering guidance from Milan Jovanović, Nick Chapsas, Anton Martyniuk, Derek Banas, Hassan Habib, and Microsoft Learn. Researched 2026-10-25. **Not a verbatim copy of copyrighted tutorials, paid courses or books.** It is a practical, opinionated starter system, not proof that every publication from all six authors was reviewed.

## Install in an existing repository
1. Unzip. Copy `CLAUDE.md`, `.claude/`, `knowledge/`, `templates/`, `scripts/`, and `examples/` into the repository root. **Review existing files before overwriting** any `.claude/` or `CLAUDE.md`.
2. Edit `CLAUDE.md` section **Project facts** with business domain, solution path, frameworks, tests and hosting. Keep it concise.
3. Read `.claude/settings.json` and confirm the deny rules suit the environment. Do not put secrets in Claude instructions.
4. From the repository root, launch `claude`, then use `/requirements-to-solution <business requirement>` or `/architecture-decision <problem>`; use `/code-review` after implementation.
5. After adopting, run `bash scripts/quality-gate.sh` and `python3 scripts/validate-setup.py`. Quality gate will skip non-existent solutions and tell you what was not checked.
6. For global, cross-project reuse copy the *generic* content to `~/.claude/` deliberately; keep project-specific files inside each repo.

## What lives where?
- `CLAUDE.md`: always-on compact operating contract, not a textbook.
- `.claude/rules/`: path-scoped language and framework rules.
- `.claude/skills/`: on-demand step-by-step playbooks invoked as `/skill-name`.
- `.claude/agents/`: optional delegated specialists (main Claude coordinates; no parallel agent requirement for simple work).
- `knowledge/`: detailed playbooks with source traceability.
- `templates/`: reusable business briefs, ADRs, plans, review and release evidence.
- `scripts/`: explicit deterministic checks (no unsafe post-edit execution installed by default).

## Async/await and concurrency guidance (2026-10-30)
- [Async/await, cancellation and bounded-concurrency playbook](knowledge/ASYNC_AWAIT_CONCURRENCY.md): original, source-checked synthesis of public Aram Tchekrekjian guidance and Microsoft .NET documentation. The specific new seven-point post is not quoted because its full text was not independently retrieved.
- [Path-scoped Claude rule](.claude/rules/dotnet-async-concurrency.md) applies to C#, Razor, MAUI code.
- Use `/async-concurrency-review` for fault, cancellation, EF Core parallelism, service-lifetime and background-work reviews.

## Typical lifecycle
**Business ask → clarify only critical unknowns → architecture options & tradeoffs → accepted decision/ADR → thin vertical slice → tests → quality gate → security/performance review → CI/CD & rollout → evidence-based completion.**

### Commands
- `/requirements-to-solution` — turn requirements into bounded use cases, quality attributes, acceptance criteria, and a proposal.
- `/architecture-decision` — compare architectural alternatives and draft an ADR.
- `/dotnet-feature` — implement an isolated slice with tests and guardrails.
- `/efcore-data` — review database schema, consistency, query plans and EF Core.
- `/blazor-ui` and `/maui-mobile` — framework-specific UI workflows.
- `/test-strategy` — tests by failure mode and layer.
- `/code-review` — prioritized evidence-based PR review, no editing.
- `/security-review`, `/performance-review`, `/delivery-infrastructure`, `/production-readiness` — specialized audit/planning.
- `/debug-incident` — systematic bug/production issue investigation.
- `/simplify-design` — KISS/DRY/YAGNI refactoring without cosmetic churn.

## Principles of arbitration
The authors are different voices, not one canon. For example Hassan Habib's The Standard prescribes Brokers → Services → Exposers; Milan and Anton often frame code as Clean Architecture / Vertical Slices. **Do not merge all layers indiscriminately**. Choose one primary organizing model and borrow cross-cutting ideas where compatible. See `knowledge/AUTHOR_COMPARISON.md`.

## Proof and limits
Source anchors: `knowledge/SOURCES.md`; rules and tradeoffs: `knowledge/`. Version-sensitive claims must be checked against the current SDK/repository during execution. Paid content is not included. No automatic production deploy, database migration, secret read, force push or infrastructure destroy is authorized.
