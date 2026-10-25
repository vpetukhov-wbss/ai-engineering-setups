# Ready-to-use MAUI prompts

## Architecture from product requirements

```text
/maui-app-architecture
Design an application for customers and production staff with order tracking,
barcode scans, status notifications and limited offline capability.
Support iOS, Android, Windows and macOS. Compare XAML-native vs Blazor Hybrid.
Prefer feature folders, KISS/DRY/YAGNI, one meaningful type per file,
and separate XAML + code-behind + ViewModel (or Razor markup + partial class + CSS).
Return ADR, repo structure, API contracts, device test matrix and staged delivery plan.
Do not invent SDK versions or claim completed builds.
```

## Implement one cross-platform slice

```text
/maui-feature
Implement the Orders list page. Provide search, refreshing, empty/error/offline
states, cancellable API calls and navigation. Add unit tests for ViewModel
and API failure handling. Check Android/iOS/desktop differences and accessible
names. Keep UI and ViewModel separate. Report actual builds and not-run targets.
```

## Offline production board

```text
/maui-offline-sync
Orders can be updated offline and synchronized when connectivity returns.
Design durable operation IDs, server idempotency, conflict handling, progress UI,
logout cache cleanup, retry limits and tests for duplicate/reordered submissions.
Do not assume unlimited background processing on iOS.
```

## Native vs Razor reusability

```text
/maui-blazor-hybrid
We already have Blazor admin components. Evaluate reuse for mobile and desktop
MAUI while keeping native barcode scanning, push notifications and secure auth.
Define service bridges, trust boundaries, WebView requirements and test strategy.
```

## Shipping without false positives

```text
/maui-device-test
Build a release candidate test matrix for Android, iOS, Windows and Mac Catalyst.
Verify what can actually run here; mark unavailable Xcode/Windows/physical-device
tests as NOT RUN. Produce evidence and a no-go/ship recommendation.
```

## Toolchain diagnosis on macOS

```text
/maui-toolchain-check
Investigate local `dotnet`, MAUI workloads, Xcode and Android toolchains.
I want to develop Android, iOS and Mac Catalyst from Mac, and Windows from
separate Windows CI. Inspect first; suggest only minimal fixes.
```
