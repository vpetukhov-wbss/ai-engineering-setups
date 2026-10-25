---
name: maui-ios-release
description: "Prepare iOS/iPadOS MAUI app signing, provisioning, TestFlight, privacy review and App Store release handoff."
---

# maui-ios-release

## Procedure
1. Inspect target TFM, Mac host/Xcode and workload compatibility, bundle ID, minimum iOS version and runtime identifiers.
2. Confirm Apple Developer signing/provisioning/entitlements availability without exporting private credentials to chat or source control.
3. Verify iPhone/iPad layouts, system auth callbacks, push notifications, privacy strings/manifests, permissions, background behavior and deep links.
4. Build/publish `.ipa` in appropriate Release context only on a provisioned Mac, record output and codesign results.
5. Recommend TestFlight first; store metadata, screenshot matrix and App Review concerns are explicit owner tasks.
6. Require human approval for TestFlight/App Store upload; report tested vs not-tested physical devices, crash monitoring and roll-forward plan.

## Output
Signed package evidence or blockers, release checklist, actual test matrix, approval-required steps.

## Reference
`knowledge/MAUI_RELEASE_PLAYBOOK.md`.
