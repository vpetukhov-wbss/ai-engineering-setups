# Create a public GitHub repository

**Owner:** `vpetukhov-wbss`

**Repository name:** `ai-engineering-setups`

**Description (GitHub About):**

> Reusable Claude Code engineering setups, AI agents, skills and playbooks for .NET, C#, Blazor, MAUI, architecture, testing, security and DevOps.

**Suggested topics:** `claude-code`, `ai-agents`, `dotnet`, `csharp`, `maui`, `blazor`, `clean-architecture`, `software-architecture`, `devops`, `developer-tools`, `ai-engineering`

**Visibility:** Public.

**Initialize with README:** No (the ZIP contains the complete root README already).

**Initialize with .gitignore or license:** No (both are included).

## Publish from an extracted ZIP

```bash
cd /path/to/ai-engineering-setups
git init -b main
git add .
git commit -m "feat: initial reusable AI engineering setups and MAUI profile"
git remote add origin https://github.com/vpetukhov-wbss/ai-engineering-setups.git
git push -u origin main
```

First create the blank public repository under the GitHub account, then run the commands above. This repository is not created automatically by the ZIP. Review staged files with `git diff --cached --stat` and `git diff --cached` before committing; never commit private client documents, tokens or signing keys.
