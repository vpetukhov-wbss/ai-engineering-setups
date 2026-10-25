---
paths:
  - "**/Platforms/iOS/**"
  - "**/Platforms/MacCatalyst/**"
  - "**/Info.plist"
  - "**/Entitlements.plist"
---

# maui-apple-platform

- iOS/iPadOS and Mac Catalyst require a compatible macOS/Xcode build and provisioning for release; inspect target workload.
- Keep App ID/bundle ID, entitlements, universal/deep links, APNs, privacy declarations and permission strings aligned.
- iOS background execution is constrained by the OS; do not simulate indefinite background workers as supported functionality.
- Mac Catalyst desktop behavior requires mouse/keyboard/windowing/file-selection tests; never assume all iOS APIs work identically.
- Certificates and profiles are secret operational assets. Store releases and direct Mac notarization require explicit approval.
