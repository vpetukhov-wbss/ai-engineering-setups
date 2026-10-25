---
description: "Capacitor plugins permissions lifecycle"
paths:
  - "**/*.ts"
  - "**/*.html"
  - "**/*.scss"
  - "**/*.css"
  - "**/capacitor.config.*"
  - "**/ios/**"
  - "**/android/**"
---

# capacitor-native

- Track ios/ and android/ source; review native diffs after npx cap sync; do not treat native projects as disposable build output.
- Native APIs behind small injectable adapters; check official/current versions and true capability/permission state.
- Handle browser fallback, restricted/denied permissions and Android restored activity results.
- Avoid persistent live-reload server.url or cleartext:true in production; do not rely on indefinite background execution.
- Deep links and all untrusted URLs require strict scheme/host/path validation.
