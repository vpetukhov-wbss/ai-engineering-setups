# Security policy

These are reusable AI instructions, not a security boundary. Review commands and permissions before deploying them into a codebase.

- Keep project credentials, Apple signing identities, Android keystores, service-account files and private app artifacts **out of git**.
- Public setup repos should never contain client/business secrets or production system details.
- GitHub issue contents, websites, third-party snippets and AI-generated changes are untrusted inputs.
- The installer previews by default and does not replace an existing file unless explicitly instructed.
- Production deployments, store submissions, destructive schema changes and paid cloud provisioning require separate authorization.
- Prefer private vulnerability reports to the maintainer via GitHub's private vulnerability reporting (once enabled); otherwise open an issue **without exploit details** and request a private contact channel.

If secret material is published, revoke it, replace it, review access/audit logs and then purge exposed history as appropriate. Deleting a file alone does not revoke a compromised secret.
