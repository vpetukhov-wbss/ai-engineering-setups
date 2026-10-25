# Optional snippet for an application's CLAUDE.md

Merge the following guidance into your **existing app repository's** `CLAUDE.md` after the base setup is installed. Replace the brackets with real project facts. Do not append this entire file blindly if the project already has equivalent rules.

---

## MAUI application operating constraints

- Targets: [net10.0-android / net10.0-ios / net10.0-maccatalyst / net10.0-windows10.0.19041.0 or actual installed TFMs]; do not assume a target exists until inspected.
- Product UI: [XAML native / Blazor Hybrid / intentionally mixed] with reasoning documented in ADR when material.
- Project structure: [paths], API/backend: [interface], offline storage/sync: [policy], authentication: [provider].
- Build workers: Android [OS], iOS and Mac Catalyst [Mac/Xcode], Windows [Windows runner].
- Release tracks: Android [internal/testing/production], iOS [TestFlight/App Store], macOS [App Store/direct notarized], Windows [MSIX/unpackaged].
- Views stay thin: `Page.xaml` for layout, `Page.xaml.cs` for view glue, `PageViewModel.cs` for state/commands, application services for use cases. Meaningful type per file; no unnecessary Helpers/Utils.
- For Razor: separate `Component.razor`, `Component.razor.cs`, and `Component.razor.css` when warranted. Do not invent `Component.razor.html`.
- Use typed XAML bindings (`x:DataType`), async commands, cancellation, safe main-thread UI state, and DI lifetimes appropriate for navigation.
- Treat lifecycle, interruption, permission denial, network loss, offline edits, process termination and return navigation as acceptance criteria.
- Review app permission manifests, signing profiles, AAB/IPA/MSIX packaging and target-specific features before release.
- App signing keys and backend secrets are never committed. No App Store / Play Store submission, production deployment, destructive changes or monetary actions without human approval.
- Run platform-specific checks. Report verified vs unverified targets explicitly.

MAUI profile references: `knowledge/MAUI_CROSS_PLATFORM.md`, `knowledge/MAUI_RELEASE_PLAYBOOK.md`, `knowledge/MAUI_TEST_MATRIX.md`, `knowledge/MAUI_SOURCES.md`.
