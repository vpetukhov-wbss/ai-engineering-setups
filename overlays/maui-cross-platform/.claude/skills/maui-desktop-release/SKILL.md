---
name: maui-desktop-release
description: "Plan and verify .NET MAUI Windows WinUI MSIX/unpackaged and macOS Mac Catalyst signed/notarized desktop releases."
---

# maui-desktop-release

## Procedure
1. Distinguish Windows/WinUI 3 from macOS/Mac Catalyst and do not assume Linux production desktop support.
2. For Windows inspect target TFM and supported runner, choose MSIX vs unpackaged app, signing/publisher, WebView (if Hybrid), install/update/uninstall and certificate trust.
3. For Mac Catalyst inspect Xcode and signing identities, choose Mac App Store or Developer ID plus notarization for direct release; validate entitlements/sandbox and app lifecycle.
4. Verify keyboard/mouse/focus, resize, menus, multiwindow, file open, drag/drop (if product uses it), accessibility, deep links and high DPI.
5. Run Windows and Mac builds independently; cannot use one OS build as proof of the other. Record packaging command and exit status.
6. Never publish production packages without explicit approval; write update/migration and roll-forward strategy.

## Output
Separate Windows and Mac evidence, package/install checklist, blockers, owner approvals and store/direct distribution guidance.

## Reference
`knowledge/MAUI_RELEASE_PLAYBOOK.md`.
