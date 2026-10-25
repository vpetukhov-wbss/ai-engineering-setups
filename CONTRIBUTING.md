# Contributing

Thanks for helping improve AI Engineering Setups.

## Scope

- Prefer small, justified changes that solve a real engineering or workflow problem.
- Add official references and dates for version-sensitive .NET, Apple, Android and Claude features.
- Explain tradeoffs rather than adding universal rules that conflict with other architectures.
- Keep the base `.NET` contract concise; prefer scoped rules or skills for specialist content.
- Do not duplicate purchased books, proprietary course chapters, internal company standards, or personal data.

## Workflow

1. Open an issue describing the scenario, the current failure and expected behavior.
2. Make a narrow PR and include an example prompt or reproducible validation case.
3. Run `python3 scripts/validate-repository.py` and report any platform checks you did not run.
4. Update `README.md` and source indexes when changing commands or version-sensitive advice.
5. Disclose if a change would widen Claude's permissions or enable potentially destructive commands.

## Public-repository safety

Never commit API tokens, signing certificates, provisioning profiles, private key material, production environment files, user addresses, account identifiers or customer code. Use deliberately fake identifiers in examples. If you accidentally expose a secret, rotate/revoke it **before** removing it from git history and follow SECURITY.md.
