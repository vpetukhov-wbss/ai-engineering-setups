---
name: ionic-device-testing
description: "Test Ionic Web, Android, iOS and native permission/lifecycle behavior."
---

# ionic-device-testing

1. Inspect actual package.json scripts and installed test runners. Execute typecheck, lint, unit, web E2E and prod build when available.
2. Mock Capacitor adapters for deterministic unit tests; run real emulators/devices for native permissions, push, deep links, camera, filesystem and app lifecycle.
3. Test airplane mode, backend unreachable, resume, process death, offline queue, auth callback and notification tap.
4. Separate browser PASS from Android/iOS PASS; browser E2E never proves a native plugin works.
5. Report matrix with command, hardware/OS, screenshots/logs, PASS/FAIL/NOT TESTED and reasons; release blocking checks must be explicit.

## Proof of completion
Provide changed files, exact commands/results, platforms verified, platforms NOT TESTED, risks, and human approvals still needed. Never claim a device or App Store submission was tested if it was not.
