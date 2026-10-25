# MAUI release checklist

**App:** [ ]  **Commit SHA:** [ ]  **Version / build:** [ ]  **Date:** [ ]

## Baseline
- [ ] All planned TFMs and versions verified against supported workload/toolchain.
- [ ] Security review (auth, storage, transport, logging, permissions, privacy data).
- [ ] Unit, integration, API contract and UI tests recorded with actual results.
- [ ] Signed Release package smoke tested on supported OS targets.
- [ ] Upgrade from previous version validated without data loss.
- [ ] Roll-forward/disable plan and backend backwards compatibility documented.
- [ ] Monitoring and support owners assigned.

## Android
- [ ] Android API levels and Google Play target policy checked.
- [ ] `ApplicationId`, version/build and permissions reviewed.
- [ ] Signed AAB verified; keystore held outside repository.
- [ ] Internal testing and device coverage completed.
- [ ] Play store production promotion explicitly authorized.

## iOS/iPadOS
- [ ] Matching macOS + Xcode, iOS workload and provisioning confirmed.
- [ ] App ID, bundle identity, entitlements and privacy manifest reviewed.
- [ ] IPA signed and installed/tested; TestFlight smoke performed where applicable.
- [ ] App Store metadata/screenshots and review requirements checked.
- [ ] App Store submission explicitly authorized.

## Mac Catalyst
- [ ] Signed release tested on supported macOS versions and CPU architectures.
- [ ] App Store vs direct distribution selected.
- [ ] If direct: notarization and ticket/installer verified.
- [ ] Window, keyboard/pointer, file and accessibility smoke completed.

## Windows
- [ ] Windows runner with correct WinUI/SDK completed release build.
- [ ] MSIX/unpackaged installer path reviewed and signed as required.
- [ ] Fresh install, update and uninstall smoke completed.
- [ ] Keyboard, DPI, multiwindow, permissions and WebView (if Hybrid) tested.

## Release evidence
| Target | Runner/device/OS | Build result | UI smoke | Artifact | Blockers |
| --- | --- | --- | --- | --- | --- |
| Android | | NOT RUN | NOT RUN | | |
| iOS | | NOT RUN | NOT RUN | | |
| Mac Catalyst | | NOT RUN | NOT RUN | | |
| Windows | | NOT RUN | NOT RUN | | |

**Approved by:** [ ] **Deployment / store track:** [ ] **Result:** [ ]
