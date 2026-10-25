---
description: "Ionic Capacitor version-aware dependency policy"
paths:
  - "**/*.ts"
  - "**/*.html"
  - "**/*.scss"
  - "**/*.css"
  - "**/capacitor.config.*"
  - "**/ios/**"
  - "**/android/**"
---

# ionic-dependency-policy

- Always inspect actual lockfile and compatible Ionic Angular Capacitor Node Xcode Gradle SDK versions.
- Keep @capacitor/core/cli/ios/android majors consistent; validate each plugin's platform and major support.
- Avoid @latest, large rewrites, unsupported native packages or automatic upgrades absent a clear request.
- Record ADR for switching critical plugins, auth architecture, database or offline sync strategy.
