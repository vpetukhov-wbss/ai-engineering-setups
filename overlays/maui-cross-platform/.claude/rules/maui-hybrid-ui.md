---
paths:
  - "**/*.razor"
  - "**/*.razor.cs"
  - "**/*.razor.css"
  - "**/*BlazorWebView*"
---

# maui-hybrid-ui

- In Blazor Hybrid, Razor runs in native .NET process and renders through WebView; enforce native/WebView trust boundaries.
- Separate `.razor` markup, `.razor.cs` partial logic and `.razor.css` style for substantial components; never invent `.razor.html`.
- Keep device capabilities behind DI services, not direct platform API calls scattered across UI.
- Validate platform WebView runtime, authentication via secure system browser/broker, navigation/back button and OS keyboard/accessibility.
- Full trimming/NativeAOT can affect Hybrid WebView and reflection-based code. Test matching Release mode before enabling.
- Share Razor components only when semantics and UX work on touch and desktop; no forced reuse that harms usability.
