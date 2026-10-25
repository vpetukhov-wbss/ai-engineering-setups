# Cross-platform .NET MAUI CI/CD and release playbook

*Rules:* no secret material in repos or logs; no automatic production releases without authorization; verify each target separately. Version-sensitive flags below are **illustrative**, not universal defaults. Run only after matching installed SDK/workload, target RID and official guidance.

## CI stages and ownership

1. **PR checks** (no signing keys): restore, static analyzers, formatting, independent domain/ViewModel/API tests, generated XAML compilation for relevant targets, optional dependency/security scans, smoke package checks where agents support them.
2. **Integration**: real backend/test containers as appropriate, API contracts, local DB/migration and sync cases, mocked notification service. Avoid using production endpoints.
3. **Platform smoke**: Android emulator + device, iOS simulator + physical device, Windows VM/host, Mac Catalyst physical Mac. Schedule resource-intensive device tests when runners exist.
4. **Signed candidate** (restricted branch/manual gate): secure signing identity, deterministic version/build number, release package, installer/update checks, crash and network verification.
5. **Distribution**: Android internal track, iOS TestFlight, macOS beta/notarized package, Windows test ring. Confirm test feedback before production promotion.
6. **Post-release**: crash-free sessions, ANRs, memory, login failure, network failure, sync queue age and platform-specific rollback/roll-forward.

### Runner matrix

| Job | Host | Caveat |
| --- | --- | --- |
| `dotnet-unit` | Linux/Windows/macOS | Pure libraries and ViewModels are broadly testable without mobile workloads. |
| `android-build` | Runner with Android SDK, JDK & workload | Verify exact workload/API/JDK support; run emulator tests separately. |
| `ios-build` | macOS + **compatible Xcode** | Signing and physical-device UI smoke need Apple provisioning/devices. |
| `maccatalyst-build` | macOS + Xcode | Validate Intel/Apple Silicon RIDs as applicable. |
| `windows-build` | Windows + WinUI/Windows SDK | Verify MSIX/unpackaged paths separately. |

### Android

- Verify correct package/application ID, `ApplicationDisplayVersion` and monotonic `ApplicationVersion`/versionCode.
- Run `dotnet publish <app.csproj> -f net10.0-android -c Release` only after inspecting actual target framework and package settings. Default Play release artifact is **AAB**, not arbitrary APK. Use a dedicated Android keystore and store passwords in CI secret vault.
- Validate signed artifact, icon/splash, network/permissions, ABI/device coverage, min/target API/Play policy and manifest/permissions.
- Upload to **internal testing first** with an explicitly authorized service account and approved release job. Production Play deployment is separate approval.

### iOS/iPadOS

- Mac build host with matching Xcode, .NET iOS workload, available Apple Developer identity, App ID/bundle ID, signing certificate and provisioning profile.
- Choose `net10.0-ios` only if the project targets it; use target-specific runtime identifier for intended device/architecture and publish `.ipa` following SDK docs.
- Confirm entitlements, privacy strings/manifests, push capabilities, app icon/screenshots, app version/build number, target device compatibility and full Release/trimming behavior.
- Use TestFlight beta rollout before App Store; submission requires explicit approval. Never commit `.p12`, `.mobileprovision`, private keys or Apple credentials.

### Mac Catalyst

- Build with matching Xcode/macOS targets; desktop interaction tests on real Mac.
- Determine **Mac App Store** vs **outside store** before generating signing configuration. For direct distribution, verify Developer ID and **notarization** (including optional ticket stapling) per official documentation.
- Check installer/uninstaller, file opening, deep links, keyboard shortcuts, resizing, multiwindow and sandbox behaviors.

### Windows

- Build on Windows for WinUI 3 target using compatible workload/Windows SDK. `dotnet publish <app.csproj> -f <actual-windows-tfm> -c Release` is a starting point, not evidence of a working installer.
- Choose packaged **MSIX** or unpackaged distribution. Validate publisher certificate trust, package identity, runtime dependencies, install/upgrade/uninstall, user data migration and app activation.
- For Hybrid, ensure installed Windows WebView runtime is supported on target machines.

## Security and release controls

- CI uses least-privileged service accounts and environments. Protect approvals for signing secrets and target stores. Never run untrusted PR code with release secrets.
- Restrict stores, backend environments, DNS changes and destructive migrations behind manual gates; dry-run for infrastructure changes.
- Signed artifacts are immutable and traceable to commit SHA, build ID, package ID and release notes. Track provenance/checksum where possible.
- Mobile app rollback is limited: app stores and installed devices cannot be "undeployed" instantly. Prefer backwards-compatible API contracts, staged rollout, server-side feature flags and controlled roll-forward.
- After rollback, validate old app versions against the current backend; data schema backward compatibility matters.

## Acceptance evidence template

```text
Target / TFM / device / OS / architecture:
SDK workload / Xcode or Android SDK / tool versions:
Build command + exit code:
Test command + results:
Release package + signing verification:
Permissions / auth / offline / lifecycle smoke:
Known warnings and skipped checks:
Version + SHA + build number:
Deployment track + approval + rollback/roll-forward plan:
```
