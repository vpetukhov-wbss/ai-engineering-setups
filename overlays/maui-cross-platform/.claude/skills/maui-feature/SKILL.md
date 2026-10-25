---
name: maui-feature
description: "Implement a .NET MAUI XAML or native feature with MVVM, async commands, validation, security and tests."
---

# maui-feature

## Procedure
1. Read the existing screen/navigation, acceptance criteria, API contracts and design conventions. Write the thin end-to-end scenario and relevant error cases.
2. Keep files distinct: View `.xaml`, code-behind `.xaml.cs`, ViewModel `.cs`, domain/use-case/service types each in their own file.
3. Model loading/error/empty states, retries, double-tap protection, cancellation and lifecycle interruptions; avoid async void except event handlers that must be void.
4. Prefer source-generated MVVM from existing CommunityToolkit.Mvvm dependency and compile-checked XAML bindings with `x:DataType`, including each DataTemplate.
5. Keep platform-specific APIs narrow and injected. Request permissions in context; never store API client secrets in shipped app.
6. Add unit tests for commands and error handling; integration tests for network/local DB when scope warrants; add UI smoke plan for real targets.
7. Run available build/test checks; explicitly list target TFMs, tests actually executed, blocked platform checks and device UX/accessibility verification.

## Output
Changed files, behavioral summary, screenshots or screen recordings only if actually captured, commands/results, risks and follow-up actions.

## References
`knowledge/MAUI_CROSS_PLATFORM.md`, `knowledge/MAUI_TEST_MATRIX.md`.
