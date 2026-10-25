---
description: "Platform build tests delivery"
paths:
  - "**/*.ts"
  - "**/*.html"
  - "**/*.scss"
  - "**/*.css"
  - "**/capacitor.config.*"
  - "**/ios/**"
  - "**/android/**"
---

# ionic-platform-quality

- Build web app before npx cap sync; match capacitor.config webDir to actual output.
- Android release is a signed AAB with Play requirements; iOS requires macOS/Xcode, signing, TestFlight and App Store requirements.
- Browser-only test result does not satisfy native plugin acceptance; use explicit browser, emulator, physical-device matrices.
- No unattended signing, app-store submission, destructive migration, cloud expenditure or production release.
- Report exact commands, versions, evidence, limits, and unverified behavior.
