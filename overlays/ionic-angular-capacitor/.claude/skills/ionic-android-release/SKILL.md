---
name: ionic-android-release
description: "Signed Android AAB, Play Console review and staged deployment."
---

# ionic-android-release

1. Verify pinned Capacitor/Android/Gradle/SDK/JDK compatibility, app ID, versionCode, target API policy and native permission declarations.
2. Run npm ci, project web production build and npx cap sync android; inspect Gradle and manifest diff.
3. Build debug, test emulator and actual device; then prepare signed AAB with safely stored upload key and Play App Signing.
4. Verify Data safety, store listing, service credentials, Android App Links, notification/camera/background use and internal testing track.
5. Do not submit production without approval; record AAB hash/version, staged rollout, crash monitoring and recovery strategy.

## Proof of completion
Provide changed files, exact commands/results, platforms verified, platforms NOT TESTED, risks, and human approvals still needed. Never claim a device or App Store submission was tested if it was not.
