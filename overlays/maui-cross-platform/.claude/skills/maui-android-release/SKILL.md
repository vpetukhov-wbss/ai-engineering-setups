---
name: maui-android-release
description: "Prepare and verify Android APK/AAB signing, Play Console internal testing, manifest permissions and release safety."
---

# maui-android-release

## Procedure
1. Check target `net*-android` TFM, application ID, version/build counter, API levels and Google Play submission policy.
2. Verify compatible Android SDK/JDK and signing material **exists in secret store**, without reading/printing secret values.
3. Run build/publish only with explicit project path and user-approved environment; verify signed AAB for Google Play or APK for approved side-load scenario.
4. Check Play privacy data safety, runtime permissions, third-party SDK declarations, icons/screenshots, links, deep links and migration/upgrades.
5. Stage artifact to internal testing only after approval. Never auto-publish to production.
6. Record SHA/build number, signer identification without secrets, smoke device matrix, crash monitoring and staged-rollout plan.

## Output
Release checklist, actual commands and results, signed artifact verification or a BLOCKED status, store submission handoff.

## Reference
`knowledge/MAUI_RELEASE_PLAYBOOK.md`.
