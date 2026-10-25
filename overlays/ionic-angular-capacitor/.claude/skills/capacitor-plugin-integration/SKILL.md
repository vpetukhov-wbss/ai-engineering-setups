---
name: capacitor-plugin-integration
description: "Evaluate and integrate native Capacitor APIs, permissions and fallbacks."
---

# capacitor-plugin-integration

1. Compare web API, official Capacitor plugin, maintained community package and custom native plugin; check compatibility with installed Capacitor major.
2. Review exact plugin version, license, security, native SDK requirements, iOS Info.plist/entitlements, Android manifest, privacy implications and browser support.
3. Hide plugin behind a small typed injectable port with a mock; distinguish native unavailable, granted, denied and restricted permissions.
4. Handle asynchronous failures and Android restored activity results where plugins invoke external activities.
5. Review tracked ios/ and android/ after cap sync, run native debug builds and test permissions on real targets; never quietly use production cleartext/live reload.

## Proof of completion
Provide changed files, exact commands/results, platforms verified, platforms NOT TESTED, risks, and human approvals still needed. Never claim a device or App Store submission was tested if it was not.
