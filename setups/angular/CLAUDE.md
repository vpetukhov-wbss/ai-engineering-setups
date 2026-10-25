# Angular Engineering — Claude Code

> Use this file as a project baseline. Project-specific facts take priority when documented and reviewed.

## Mission
Translate verified business requirements into secure, accessible, testable, maintainable Angular applications. Avoid architecture theater. Preserve established project conventions before introducing new ones.

## Before changing code
1. Inspect `package.json`, lockfile, `angular.json`, TypeScript and lint configs, router, feature structure, test runner and node version. Never assume the framework version from this template.
2. Identify users, workflows, authorization boundaries, API contracts, acceptance criteria, performance budgets and deployment target.
3. For meaningful architectural tradeoffs, show 2 viable options and recommend the smallest safe option with an ADR.
4. Plan vertical feature slices and tests. Avoid massive unreviewable changes.

## Angular defaults (version aware)
- Prefer standalone components and feature-oriented folders for modern Angular; preserve NgModules in existing applications unless migration is justified.
- Prefer signals for local synchronous UI state, `computed()` for derived state; use RxJS for streams, cancellation and event composition where it provides value. Never implement the same source of truth twice.
- Angular v21+ defaults to zoneless; for earlier versions follow their documented change detection setup. Check compatibility rather than deleting `zone.js` blindly.
- Prefer `inject()` within supported injection contexts; typed forms and HttpClient with interceptors for shared transport concerns.
- Keep **meaningful** components in separate `.ts`, `.html`, `.scss`/`.css`, and `.spec.ts` files. One significant class or concern per file; no gratuitous `utils` or `helpers` files.
- Use `@if`, `@for` with stable tracking, `@switch` and lazy routes/defer where supported. Avoid expensive expressions or subscriptions in templates.
- Keep presentation thin; isolate backend integration and business use cases by feature. State libraries only when complexity supports them.
- No over-engineering: KISS/DRY/YAGNI, concise public APIs, predictable error/loading/empty states, and explicit cleanup.

## Security and correctness
- Treat all user-controlled data as untrusted. Never disable Angular sanitization casually, and do not use `bypassSecurityTrust*` without a documented, independently-reviewed need.
- Implement authorization on the **server**. Client guards improve UX but are not security boundaries.
- Use secure server-managed sessions / standards-based OIDC; never expose long-lived secrets, API keys, or privileged tokens in client bundles or tracked configuration.
- Respect XSRF/CSRF, CSP, Trusted Types, secure cookies and CORS according to the deployment architecture. Avoid direct DOM mutation and unsanitized HTML.
- Handle SSR/browser boundaries safely; guard access to window, document and storage. Design hydration and caching intentionally.

## Quality gates
- Execute available, repository-defined lint, format, TypeScript strict checks, tests, production build and accessibility/E2E checks, reporting exact command results.
- Angular CLI new project unit tests use Vitest in recent versions, but use the **installed** project's runner. Prefer component + service tests, Playwright/Cypress only if present or justified.
- Verify responsiveness, keyboard navigation, focus management, semantics, screen-reader labels, error states, browser compatibility, performance budgets and no client-side secret leaks.
- Never claim a deploy, Lighthouse score, vulnerability scan or E2E/device test happened unless actually run.
- Do not commit, publish, merge, change production infrastructure or incur costs unless explicitly authorized.

## Workflow routing
- New product/architecture: `/angular-architecture`
- Feature: `/angular-feature`
- State design: `/angular-state-management`
- API/auth: `/angular-api-integration`, `/angular-security-review`
- Rendering and speed: `/angular-ssr-performance`
- Accessibility: `/angular-accessibility`
- Tests: `/angular-test-strategy`
- Deploy: `/angular-ci-deploy`
- Review: `/angular-code-review`
- Migration: `/angular-upgrade`

See `knowledge/ANGULAR_PLAYBOOK.md`, `knowledge/SOURCES.md` and `templates/ANGULAR_FEATURE_SPEC.md`.
