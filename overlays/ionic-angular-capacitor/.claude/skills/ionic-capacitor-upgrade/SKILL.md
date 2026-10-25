---
name: ionic-capacitor-upgrade
description: "Safely upgrade Angular Ionic Capacitor and native plugin majors."
---

# ionic-capacitor-upgrade

1. Inventory current Node, Angular, TypeScript, Ionic, Capacitor core/cli/ios/android versions, plugins, Gradle, Xcode and SDK.
2. Check official migration guides and compatibility; never run unreviewed @latest upgrades or delete ios/android to make builds pass.
3. Plan staged migration and backup, including offline DB schema and platform signing changes.
4. Review lockfile, capacitor.config, native project diff, permissions, routing and standalone imports.
5. Verify unit/browser/native builds and physical device smoke tests; document migration and rollback evidence.

## Proof of completion
Provide changed files, exact commands/results, platforms verified, platforms NOT TESTED, risks, and human approvals still needed. Never claim a device or App Store submission was tested if it was not.
