# Angular Engineering Setup

Reusable Claude Code rules, agents, skills and practical playbooks for Angular + TypeScript (standalone or combined with ASP.NET Core).

**Presets:** `angular` (standalone) and `dotnet-angular` (.NET foundation + Angular-specific tools). A combined install deliberately retains the .NET `CLAUDE.md`; manually merge [ANGULAR_CLAUDE_APPEND.md](ANGULAR_CLAUDE_APPEND.md) into the application's existing instructions.

## Install

```bash
python3 scripts/install.py --preset angular --target /path/to/angular-app
python3 scripts/install.py --preset angular --target /path/to/angular-app --apply
# Or, for ASP.NET Core + Angular:
python3 scripts/install.py --preset dotnet-angular --target /path/to/fullstack-app --apply
```

Install is preview-first, skips conflicts, never downloads dependencies, and requires a preexisting target directory. Read the generated differences and merge project-specific instructions manually.

## What's included

- 12 skills: architecture, features, state, API, forms, auth/security, SSR/performance, accessibility, testing, CI/deployment, upgrade and independent review.
- 7 dedicated agents: architect, UI implementer, state/API engineer, accessibility expert, security reviewer, QA/E2E, performance & release engineer.
- Path-scoped rules for Angular, templates, TypeScript, API/auth, tests, SSR/CI and architecture.
- Evidence-oriented architecture decisions, feature specs, PR checklist, release checklist, source index and example task prompts.

## Defaults, not dogma

Check the actual versions of Angular, TypeScript, Node and build tooling before choosing APIs. Angular v21+ uses zoneless change detection by default, recent Angular CLI projects use Vitest, and official style guidance favors feature folders, `inject()` and one concept per file. Do not blindly modernize working legacy applications.

## Suggested quality check

Run the commands defined in the target application's `package.json`, typically `npm ci`, `npm run lint --if-present`, `npm test -- --watch=false`, `npm run build -- --configuration production` (adjust CLI flags to scripts). Inspect the emitted bundle; test auth, a11y and SSR on real routes rather than asserting success from a clean compile.

See the [architecture playbook](knowledge/ANGULAR_PLAYBOOK.md) and [official sources](knowledge/SOURCES.md).
