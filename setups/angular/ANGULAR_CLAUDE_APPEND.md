# Guidance to merge into an existing .NET application's CLAUDE.md

Do not overwrite existing instructions. Review actual Angular and ASP.NET Core project boundaries before adding the following.

- Angular frontend root: [relative path]; ASP.NET API root: [relative path]; contracts: [OpenAPI/other].
- Version-aware standalone Angular for new work; keep existing app patterns unless change is justified.
- Feature-first Angular layout, with separate `.ts`, `.html`, `.scss`/`.css`, `.spec.ts`; meaningful type/concept per file.
- Signals for local synchronous view state, RxJS where streams/cancellation matter; avoid redundant global stores and effect chains.
- Use typed API clients/contracts; backend verifies permissions and validation. Do not duplicate domain rules as competing authorities.
- Route guards do not confer authorization; no long-lived secrets or client-trusted roles. Review CORS, cookies, XSRF and OIDC session flow.
- SSR/hydration decisions are explicit. Protect browser-only APIs. Validate keyboard/screen-reader experience and Core Web Vitals.
- Verify Angular and API builds/tests independently, then execute cross-stack integration/contract/E2E scenarios.
- Never silently alter production data, release, merge or access credentials.

Reference: `knowledge/ANGULAR_PLAYBOOK.md` and `knowledge/SOURCES.md`.
