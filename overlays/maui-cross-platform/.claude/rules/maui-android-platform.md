---
paths:
  - "**/Platforms/Android/**"
  - "**/*Android*.cs"
  - "**/AndroidManifest.xml"
---

# maui-android-platform

- Verify Android API target/minimum and toolchain rather than copying old manifest defaults.
- Handle denied/revoked permissions, system back/navigation, deep link intent validation, Android activity recreation, OS process death and notification permission.
- Avoid public shared file paths and accidental sensitive storage leaks; use platform storage as appropriate.
- Keep keystore passwords, private keys and package signing data out of repository and logs.
- Release to Google Play with signed AAB and explicit approval; record actual device tests and CI evidence.
