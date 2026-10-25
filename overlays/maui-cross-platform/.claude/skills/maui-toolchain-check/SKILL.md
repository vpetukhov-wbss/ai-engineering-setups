---
name: maui-toolchain-check
description: "Diagnose .NET MAUI Android iOS Mac Catalyst and Windows workloads, SDK/Xcode/JDK compatibility, and blocked builds."
---

# maui-toolchain-check

## Procedure
1. Collect actual OS/CPU and local availability: `dotnet --info`, `dotnet workload list`, `dotnet --list-sdks`; inspect project target frameworks and `global.json`.
2. On macOS inspect `xcode-select -p`, `xcodebuild -version` and compatible Xcode; on Android inspect SDK and Java location **without printing secrets**.
3. On Windows validate Windows SDK/WinUI/MSBuild and intended packaged/unpackaged build path; do not claim WinUI builds on macOS.
4. Consult current Microsoft version/release matrix for matching Xcode, Android SDK/JDK, workload and target API. Treat mismatches as blockers rather than guessing flags.
5. Propose minimal, reversible setup steps; request approval before workload installation, system changes or elevation.
6. Run non-destructive restore/build only when available and authorized. Collect actual command outputs and return codes.

## Output
Per-target matrix: `Ready / Needs setup / Cannot validate here`, exact detection commands, evidence, remedial steps and remaining signing/device needs.

## Reference
`knowledge/MAUI_SOURCES.md`.
