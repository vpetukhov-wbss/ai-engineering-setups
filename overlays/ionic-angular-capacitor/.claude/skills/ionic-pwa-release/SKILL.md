---
name: ionic-pwa-release
description: "Deploy Ionic Angular browser/PWA without pretending native API parity."
---

# ionic-pwa-release

1. Decide whether PWA is a supported product target or only development preview, and list unavailable native features and alternatives.
2. Configure manifest/icons/HTTPS/service worker according to installed Angular version; make hosted deep-link reloads work.
3. Separate cached static assets from personal/offline entity storage; do not cache private API responses indiscriminately.
4. Test installation, update migration, offline/online changes, responsive touch UX and browser permission behavior in Safari and Chromium.
5. Deliver PWA separately from native store releases, with explicit cache invalidation/rollback considerations.

## Proof of completion
Provide changed files, exact commands/results, platforms verified, platforms NOT TESTED, risks, and human approvals still needed. Never claim a device or App Store submission was tested if it was not.
