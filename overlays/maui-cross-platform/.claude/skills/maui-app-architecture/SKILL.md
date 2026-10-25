---
name: maui-app-architecture
description: "Choose architecture for a new .NET MAUI app across iOS Android Windows and macOS, including XAML vs Blazor Hybrid."
---

# maui-app-architecture

## Input
Business brief, device capabilities, user journeys, target OS versions, offline and auth requirements, distribution channels, existing codebase.

## Procedure
1. Inspect existing `.csproj`, solution structure and target frameworks. If greenfield, write assumptions with confidence level.
2. Make explicit XAML-native / Blazor Hybrid / mixed decision with a short tradeoff matrix: UX, existing component reuse, native integrations, testability, performance, security, future cost.
3. Model user journeys and target-specific UX differences (phones, tablets, desktop windows, keyboard, pointer).
4. Identify domain invariants, API boundaries, ownership of app data, offline policy, auth and permissions. Start feature-folder-first; introduce projects/layers only if justified.
5. Sketch separate `.xaml`, `.xaml.cs`, ViewModel and use-case/service boundaries, or `.razor`, `.razor.cs`, `.razor.css` for Hybrid screens.
6. Define test pyramid, CI runner matrix and release delivery architecture for each selected platform.
7. Write an ADR using base `templates/ADR.md` when material; avoid microservices or generic Helpers without evidence.

## Output
Architecture decision, dependency diagram, selected platforms/TFMs **to verify**, project structure, risks, phased backlog, acceptance criteria and rollout approach.

## References
`knowledge/MAUI_CROSS_PLATFORM.md`, `knowledge/MAUI_RELEASE_PLAYBOOK.md`, `knowledge/MAUI_SOURCES.md`.
