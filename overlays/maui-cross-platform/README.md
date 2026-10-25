# MAUI Cross-Platform Engineering Profile

**Target:** `.NET MAUI` applications for **iOS/iPadOS, Android, macOS (Mac Catalyst), Windows (WinUI 3)**; choose XAML-native UI or Blazor Hybrid intentionally.

This **overlay augments** the core .NET setup. It is not a standalone compiled application, an SDK installer, or an automatic signing/deployment system.

## Install safely

From the repository root, preview, then copy to an existing app repo:

```bash
python3 scripts/install.py --preset dotnet-maui --target /path/to/app
python3 scripts/install.py --preset dotnet-maui --target /path/to/app --apply
```

Conflicts are skipped. Review `MAUI_CLAUDE_APPEND.md` and merge relevant facts into the app repo's `CLAUDE.md` manually.

## Skills

| Skill command | When to invoke |
| --- | --- |
| `/maui-app-architecture` | Choose MAUI native vs Blazor Hybrid and design target-aware boundaries. |
| `/maui-toolchain-check` | Diagnose dotnet workload, Xcode, JDK, Android SDK and target availability. |
| `/maui-feature` | Deliver XAML/MVVM features with tests and platform handling. |
| `/maui-blazor-hybrid` | Design Razor reuse with host/WebView security and native bridges. |
| `/maui-offline-sync` | Cache, local writes, idempotency, conflict resolution and sync UX. |
| `/maui-ui-quality` | Accessibility, theming, responsive/adaptive layouts, performance. |
| `/maui-device-test` | Device test matrix, Appium/UI smoke tests and lifecycle/permissions. |
| `/maui-android-release` | Build, sign and verify Android AAB/APK delivery plans. |
| `/maui-ios-release` | IPA signing, provisioning, TestFlight/App Store release planning. |
| `/maui-desktop-release` | Mac Catalyst and WinUI desktop packaging and update planning. |

## Architecture recommendation (not a mandatory scaffold)

```text
src/
  Sample.App/                      # MAUI entry, pages, platform glue
    Features/
      Orders/
        OrdersPage.xaml
        OrdersPage.xaml.cs
        OrdersViewModel.cs
    Platforms/
      Android/
      iOS/
      MacCatalyst/
      Windows/
    MauiProgram.cs
  Sample.Application/              # Use cases and interfaces when complexity warrants
  Sample.Domain/                   # Business invariants when warranted
tests/
  Sample.UnitTests/
  Sample.IntegrationTests/
  Sample.UiTests/                  # Optional Appium/device tests
```

Do **not** automatically create all these projects. Small MAUI apps can start with a single app project and well-organized feature folders. Split projects when you gain real domain complexity, shared logic, independent testing needs or separate deployment boundaries.

### UI strategy

- **XAML-native:** prefer when strongly native experiences, accessibility/animation, hardware integration or platform feel dominate. Keep `.xaml`, `.xaml.cs`, ViewModel and services separate.
- **Blazor Hybrid:** prefer when existing Razor components/shared web UI offer concrete reuse. Define a clear boundary between Razor and native APIs. Razor components have `.razor`, `.razor.cs`, `.razor.css`; MAUI hosts have `.xaml`, `.xaml.cs`.
- **Mixed:** supported technically, but justify the maintenance cost; do not accidentally duplicate entire screens in XAML and Razor.

### Target and release matrix

| Target | Build host | Smoke testing | Production packaging |
| --- | --- | --- | --- |
| Android | Android SDK/JDK compatible host | emulator + real device, multiple API levels | signed `.aab` for Google Play; APK for controlled side-load |
| iOS/iPadOS | **Mac + supported Xcode** | simulator + physical device, signing | signed `.ipa`, TestFlight and/or App Store |
| Mac Catalyst | **Mac + supported Xcode** | real Mac, both architectures as applicable | signed app/package, App Store or notarized distribution |
| Windows | **Windows + Windows SDK/WinUI tooling** | packaged/unpackaged on real Windows | MSIX or unpackaged installer, test upgrade paths |

Exact SDK/Xcode/JDK versions and minimum OS targets vary with MAUI workload. Inspect `dotnet --info`, `dotnet workload list`, project TFMs, Microsoft release matrix and locally installed tools. **Never invent a successful build.**

## Design and quality gates

1. Business use cases, UX acceptance criteria, target OS versions and privacy/data flow confirmed.
2. Responsive layout for phone/tablet/window resizes; accessibility with VoiceOver/TalkBack/Narrator.
3. MVVM commands are async/cancellable where appropriate; typed XAML bindings; correct DI lifetimes.
4. Native permissions requested at point of use; app never stores client secrets.
5. App lifecycle, resumed state, OS process death, offline mode and retry behavior tested.
6. Release build tested with trimming/AOT choices and packages, **not only Debug**.
7. Platform-specific tests reported separately; CI results include target, device/emulator and OS versions.
8. Signing/release credentials kept in appropriate secret storage; store submission requires explicit approval.

## Platform reference files

- [MAUI engineering guide](knowledge/MAUI_CROSS_PLATFORM.md)
- [Releases and CI/CD](knowledge/MAUI_RELEASE_PLAYBOOK.md)
- [Device test matrix](knowledge/MAUI_TEST_MATRIX.md)
- [Official source index](knowledge/MAUI_SOURCES.md)
- [Example screen architecture](examples/MAUI_APP_ARCHITECTURE.md)
- [MAUI workflow prompts](examples/MAUI_PROMPTS.md)

## Non-goals

No supported Linux MAUI desktop target is claimed. Experimental alternate backends must have their own compatibility investigation. This profile does not include Apple certificates, Android keystores, shipping production credentials, a paid build service or automatic store submissions.
