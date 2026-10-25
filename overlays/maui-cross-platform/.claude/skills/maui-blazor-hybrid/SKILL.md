---
name: maui-blazor-hybrid
description: "Design and implement Blazor Hybrid Razor UI on MAUI with secure native services and explicit platform bridge."
---

# maui-blazor-hybrid

## Procedure
1. Confirm expected Razor reuse and supported desktop/mobile form factors; avoid Hybrid if it creates more duplicated UI.
2. Inspect target WebView requirements, Razor root components, DI scopes and host lifecycle.
3. Isolate native platform operations behind narrow C# services; never pass high-privilege tokens via URL or WebView JS state.
4. For nontrivial components use `.razor` + `.razor.cs` + `.razor.css`, maintain keyboard/touch/screen reader behavior and responsive layout.
5. Validate navigation/back, Android WebView behavior, iOS keyboard/safe areas, Windows/MacCatalyst resize and secure authentication redirect flow.
6. Check actual Release behavior with trimming/AOT constraints, component startup, memory and offline data needs.
7. Document which Razor components are truly shared with a separate web host and how platform-specific UX diverges.

## Output
Architecture and component boundaries, implementation/tests, per-platform risks and measured or unmeasured performance.

## References
`knowledge/MAUI_CROSS_PLATFORM.md`, `knowledge/MAUI_SOURCES.md`.
