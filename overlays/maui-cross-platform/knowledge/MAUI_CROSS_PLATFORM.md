# .NET MAUI cross-platform engineering playbook

Updated 2026-10-25. Version-sensitive statements MUST be rechecked against current SDK, workload and target framework. Official references are in `MAUI_SOURCES.md`.

## 1. Requirements before architecture

Gather *personas / critical jobs / nonfunctional constraints / distribution channels / target OS versions / accessibility / regulatory privacy / offline and network assumptions / device capabilities / ownership of backend endpoints*. Explicitly ask which features are intended for phones, tablets, Windows desktops, and Macs; desktop != just a resized mobile app.

Evaluate native vs Blazor Hybrid with a decision table:

| Decision factor | XAML-native | Blazor Hybrid |
| --- | --- | --- |
| Native design behaviors and input | Strong default | Host APIs require explicit bridges |
| Existing Razor component reuse | Limited | Often compelling |
| Native camera/location/files/notifications | Direct | Via MAUI service bridge |
| UI testing | Appium, platform tests | Native shell + WebView DOM strategy |
| Performance & package size | Measure on device | Measure WebView and startup on device |
| Offline | Explicit local data strategy | Explicit local data strategy; WebView does not create sync automatically |

Do not recommend Hybrid just because the team knows C#, or native just because the app runs on a phone. Build a prototype for uncertain app constraints.

## 2. Architectural boundaries

Default to an **application with feature folders** and one primary view model per stateful screen. Extract application/domain assemblies only when invariants, reuse, tests or independent boundaries justify them. Do not force backend-style Clean Architecture layers into a three-screen client.

`View (XAML/Razor) -> ViewModel/presentation state -> use case/API client -> backend/domain`.

- View: binding, gestures, native UI concerns. No business transactions or direct data persistence.
- ViewModel: loading/error/empty states, async commands, cancellation, debouncing, composition of use cases; no UI `Page` dependency.
- Application services: business workflows and validation, testable independently from the UI.
- API client: typed DTOs, authentication, timeouts, status handling, idempotency and retry classification.
- Platform adapters: limited surface around microphone/camera/permissions/push/background operations; no giant generic `IPlatformService` or `IHelper`.
- Domain: invariants and meaningful use cases, only as needed.

Keep one meaningful type per file. If an API model is shared across transports, version contracts deliberately; do not reuse EF Core database entities in MAUI app code.

## 3. XAML, binding and MVVM correctness

- Prefer CommunityToolkit.Mvvm when accepted by the project; `[ObservableProperty]` and `[RelayCommand]` generators reduce boilerplate. Verify package version for the target SDK. Avoid pointless wrapper frameworks.
- Mark XAML pages and each `DataTemplate` with correct `x:DataType` for compiled bindings. Never silence a real binding problem with `x:DataType="x:Object"`.
- Use `AsyncRelayCommand` for I/O. `IsBusy`, `ErrorMessage`, `CanExecute`, cancellation and duplicate-tap behavior should reflect actual UX.
- Register dependencies in `MauiProgram`, avoid service-locator patterns and accidental singleton state leaks.
- Scope ViewModel lifetime to navigation where possible; cleanup subscriptions, timers, handlers, commands and event streams on disposal/navigation.
- Do not do synchronous network or expensive bitmap work on UI thread. Marshal only final UI changes to dispatcher/MainThread.
- Use semantic focus order, screen reader descriptions, text scaling, sufficient contrast and touch target size.

## 4. Navigation and state

- Shell routes and deep links require route allowlists, parameter validation and authorization checks; a deep link is untrusted input.
- Persist only restoration-critical state: selected item, pending form where justified, filter choice, not arbitrary live ViewModels.
- Back stack, modal dismissal, Android hardware/system back, iOS swipe-back, and desktop multi-window behave differently. Add behavior tests.
- Refresh or resubscribe on resume; pause work and unsubscribe on stop; do not assume `Stopped` is always followed by `Resumed` (process can be killed).

## 5. Network, offline and sync

- Define read-through cache TTL and invalidation; distinguish "offline by design" from "temporarily unavailable".
- Explicitly decide if writes are blocked, queued or optimistically reflected. Queued writes need durable ID, creation time, schema version, retries, backoff, server-side idempotency key and observable status.
- Define conflict resolution: server-authoritative, optimistic concurrency token + reconcile UI, or field-level merge where truly warranted. **Do not silently overwrite offline edits.**
- On login/logout/tenant switch remove or segregate sensitive caches and authentication state. Protect stored data per risk classification.
- Network indicators aren't guarantees of connectivity; handle HTTP timeouts/5xx, TLS failures, token expiration, captive portals and rate limits. Avoid blind automatic retries of non-idempotent POST requests.

## 6. Identity and security

- Mobile/desktop apps are public clients. **Never embed private keys, client secrets or trusted backend credentials** in code, assets, configuration, or pushed git history.
- For OAuth/OIDC use system browser/broker and PKCE where applicable, validate redirect URIs, state, issuer, scopes and token lifecycle; select platform-supported libraries. Auth is NOT handled by copying a website login into WebView.
- `ISecureStorage` is for small key/value secrets and may throw on backup/restore/corruption; catch and recover. It does not replace encrypted-at-rest design for a complete local database.
- Permissions: minimum set, request on use, explanatory UX, handle denial/revocation and "never ask again" state. Ensure accurate Info.plist/Android manifest descriptions and data privacy disclosures.
- Deep links, imported files and push payloads are untrusted; sanitize and validate before use. Avoid logging access tokens/PII.
- Plan OS transport security, certificate validation and acceptable debug-only overrides. Never ship disabled TLS validation.

## 7. Native platform differences

### iOS / iPadOS
- macOS + compatible Xcode mandatory for final iOS build/signing. Pair-to-Mac does not remove this requirement.
- Plan App ID / bundle ID, entitlements, provisioning, push APNs, Background Modes (if actually needed), Privacy Manifest and privacy descriptions.
- iOS may suspend background work; avoid promises of unrestricted always-on processes. Test actual device behavior, notifications, universal links, safe areas, keyboards, dynamic text, orientation and app review constraints.
- Support iPad layout and navigation only when product requires it; validate split view/multitasking on supported iPadOS versions.

### Android
- Identify target/minimum API levels from compatible workload and Play policy. Test several device density/screen sizes/API levels.
- Account for Android back navigation, activity recreations, rotation, doze/battery optimization, scoped storage, notifications permission and process termination.
- Keystore handling and AAB signing are release tasks; Play Console and Play App Signing configuration require trusted owner review.

### macOS (Mac Catalyst)
- Treat as desktop: menu/keyboard shortcuts, pointer/hover, focus, resize, title bar/window lifecycle, accessibility and file pickers.
- Not all iOS APIs translate directly to Mac Catalyst. Test real Mac behavior with correct entitlements and sandbox permissions.
- Distribution outside Mac App Store requires Developer ID signing and notarization; Store distribution uses separate identities/workflows.

### Windows (WinUI 3)
- Test keyboard shortcuts, mouse, focus, windowing, resize/minimize, scaling, touch vs pointer and file system permissions.
- Release with packaged MSIX or unpackaged installer deliberately; upgrades/uninstalls and certificate trust differ.
- Windows runners needed to validate WinUI release packaging. Do not claim Windows shipping readiness from a Mac build.

## 8. Blazor Hybrid bridge

- Razor components execute .NET code in the native process, rendering into a WebView; don't treat the WebView content as a remote browser-hosted SPA.
- Put native capabilities behind DI services with narrow contracts so Razor UI does not hard-code `DeviceInfo`/`Permissions` everywhere.
- Verify the target platform's WebView runtime and authentication story; do not leak bearer tokens into URLs, JS logs or localStorage without strong justification.
- Keep platform-native host lifecycle and API responsibilities outside reused Razor components where possible. Validate Razor routing, back button, keyboard/accessibility and WebView input behavior on every target.
- Full trimming and NativeAOT have constraints on dynamic features; check official docs before enabling. In .NET 10 some hybrid controls are disabled by default with full trimming.

## 9. Performance and reliability

Measure cold/warm startup, memory high-water mark, image decode and caching, CollectionView scrolling, native navigation transitions, DB operations and battery/network use on representative low-end devices. Use typed bindings and reduce nested layout depth only where profiling shows gain. Release/trimming can change behavior: compare Debug vs Release on all relevant targets.

## 10. Deliverable definition

A feature is not complete until: requirements and design tradeoffs are recorded; tests appropriate to risk ran; each applicable platform has known pass/fail/blocked status; accessibility and lifecycle cases are addressed; security/performance risks are documented; deployment changes have rollback and manual approval gates.
