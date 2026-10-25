---
paths:
  - "**/*.csproj"
  - "**/*.props"
  - "**/*.targets"
  - "**/.github/workflows/**"
  - "**/azure-pipelines*.yml"
---

# maui-tests-and-distribution

- Inspect project target TFMs, installed SDKs and workloads before proposing build CLI commands.
- Pure unit tests can run on general .NET runners; Android needs Android SDK/JDK, iOS/Mac Catalyst need macOS/Xcode, and Windows WinUI builds need Windows tooling.
- Do not check in `.p12`, `.mobileprovision`, `.keystore`, store-service credentials or public signed artifacts with confidential data.
- Distinguish signed Release package from `dotnet build` and from `dotnet publish`. Never claim store release without proof.
- PR jobs must never access production signing secrets; protected jobs and approval gates perform signing and upload.
- Test upgrade, logout/local data, push/deep links, permission denial, offline, background and accessibility on target OS.
