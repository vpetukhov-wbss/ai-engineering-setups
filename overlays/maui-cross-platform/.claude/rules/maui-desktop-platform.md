---
paths:
  - "**/Platforms/Windows/**"
  - "**/Package.appxmanifest"
  - "**/Platforms/MacCatalyst/**"
---

# maui-desktop-platform

- Windows native MAUI UI uses WinUI 3; macOS standard target uses Mac Catalyst. Do not promise production Linux desktop target.
- Test resizing, keyboard navigation/shortcuts, pointer and high-DPI scaling, focus, multiwindow/activation and accessibility.
- For Windows choose MSIX vs unpackaged before describing install/update/uninstall; test release packages on Windows runners.
- For Mac Catalyst choose App Store vs notarized distribution before signing. Record build host and target RID.
- Never mark desktop ready based on Android/iOS Debug results.
