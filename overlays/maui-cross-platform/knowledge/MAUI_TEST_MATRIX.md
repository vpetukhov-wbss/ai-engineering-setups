# MAUI verification and device test matrix

Replace example cells with real devices/OS versions from the product support matrix. Tests without devices/appropriate runners are **NOT RUN**, never PASS.

## Functional behaviors to cover

| Scenario | Android | iOS | Windows | Mac Catalyst |
| --- | --- | --- | --- | --- |
| Cold start, first install | Emulator + real device | Simulator + real device | Fresh installer/clean profile | Fresh installer/clean profile |
| Account sign-in/sign-out/token expiry | Browser callback and back | System auth session and resume | Redirect/app activation | Redirect/app activation |
| Deep links, guarded navigation | Activity/intent and back | Universal/custom schemes | Protocol activation | URL scheme |
| Network loss/recovery | Airplane mode, captive portal | Airplane mode, captive portal | Offline ethernet/Wi-Fi | Offline ethernet/Wi-Fi |
| Background/foreground/process death | Background, OS kill | Background, OS kill | Minimize/close/reopen | Minimize/close/reopen |
| Local writes + conflict resolution | Queue/duplicate replay | Queue/duplicate replay | Local DB / app restart | Local DB / app restart |
| Permissions and revocation | Settings revoke and retry | Settings revoke and retry | OS privacy settings | OS privacy settings |
| Accessibility | TalkBack & large font | VoiceOver & Dynamic Type | Narrator / keyboard-only | VoiceOver / keyboard-only |
| Display & input | Phones/tablets, rotation | iPhone/iPad, multitasking | Mouse/keyboard/touch, high DPI | Pointer/keyboard, multiple windows |
| Locale & theme | Language, RTL if required, dark mode | Same | Same | Same |
| Signed release | APK/AAB installed | IPA/TestFlight | MSIX/unpackaged | App package/notarization |
| Upgrade & persisted state | Install n → n+1 | Install n → n+1 | Installer upgrade | Installer upgrade |

## Automated test pyramid

1. Pure .NET unit tests for domain and ViewModels (commands, errors, validation, concurrency, cancellation). Run on any compatible .NET test runner.
2. Integration tests for typed API clients, local SQLite (if used), idempotency, conflict handling and resilient HTTP. Use isolated test resources, not production.
3. Contract tests for REST/JSON and versioned endpoints; do not silently deserialize malformed or breaking payloads.
4. UI smoke with Appium or an explicitly selected supported framework for login, primary business flow and navigation. Use accessibility IDs/automation IDs rather than brittle pixel coordinates where possible.
5. Target-specific manual exploratory tests for OS dialogs, camera, audio, deep links, notifications, multi-window and battery constraints.

## Release-gate requirements

- Unit tests with pass/fail counts and coverage of high-risk domain logic; coverage percentage alone is not a quality signal.
- Integration/contract tests for remote dependencies and offline persistence when feature requires them.
- Accessibility checks for supported assistive technology, supported text sizes and keyboard interactions.
- At least one signed Release smoke per shipping platform plus representative devices and OS versions; no shipping decision based solely on Debug.
- Document memory/performance baseline, app package size/startup, crash reporting and analytics privacy.
- Record actual builds and test provenance; a template or CLI command does not prove successful execution.

## Example evidence (fill in, do not fabricate)

```markdown
| Platform | Build | Unit | Device smoke | Release package | Blockers |
| --- | --- | --- | --- | --- | --- |
| Android | NOT RUN | NOT RUN | NOT RUN | NOT RUN | Runner not configured |
| iOS | NOT RUN | NOT RUN | NOT RUN | NOT RUN | Xcode/signing needed |
| Windows | NOT RUN | NOT RUN | NOT RUN | NOT RUN | Windows runner needed |
| Mac Catalyst | NOT RUN | NOT RUN | NOT RUN | NOT RUN | Mac release runner needed |
```
