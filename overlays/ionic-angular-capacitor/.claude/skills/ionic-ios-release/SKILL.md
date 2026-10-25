---
name: ionic-ios-release
description: "Xcode archive, App Store policy and TestFlight release workflow."
---

# ionic-ios-release

1. Verify Mac/Xcode version compatible with installed Capacitor, Apple deployment target, bundle ID, signing team, provisioning and schemes.
2. Run npm ci, web production build and npx cap sync ios; inspect native project changes and build/archive with Xcode.
3. Review Info.plist purpose strings, Associated Domains, push/background entitlements, required privacy manifests and data collection labels.
4. Run simulator and physical-device tests of permissions, Universal Links, app resume, camera, auth and offline behavior.
5. Prepare TestFlight first; keep certificates/private keys out of git and obtain explicit approval before App Store submission.

## Proof of completion
Provide changed files, exact commands/results, platforms verified, platforms NOT TESTED, risks, and human approvals still needed. Never claim a device or App Store submission was tested if it was not.
