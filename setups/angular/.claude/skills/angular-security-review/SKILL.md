---
name: angular-security-review
description: "Review Angular browser security, auth boundaries, SSR and token/session handling."
---

# angular-security-review

## Procedure
1. Map trust boundaries: browser, API, identity provider, SSR/proxy and third-party scripts.
2. Review XSS sinks and bypassSecurityTrust*, unsafe DOM/innerHTML, CSP/Trusted Types, URL handling and supply-chain exposure.
3. Verify server-side authorization; guards/interceptors are UX controls only.
4. Review cookie/SameSite/XSRF/CORS strategy, OAuth/OIDC PKCE or BFF, storage choices and logout semantics.
5. Report severity, evidence, reproduction and safe fixes. Never exfiltrate or print credentials.

## Deliverables
Summarize scope and choices, changed files, verified commands/results, evidence, risks and required human approvals.

## References
`knowledge/ANGULAR_PLAYBOOK.md`, `knowledge/SOURCES.md`.
