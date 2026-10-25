---
name: maui-device-test
description: "Build risk-based unit, integration, Appium UI and real-device test matrices for .NET MAUI targets."
---

# maui-device-test

## Procedure
1. Identify supported Android/iOS/Mac/Windows OS versions, phones/tablets/device capacities, integrations and release-critical user journeys.
2. Separate generic .NET tests (domain/ViewModel) from platform builds, Appium UI tests, OS permissions, security and real-device exploratory tests.
3. Include first install, upgrade, session expiry, deep links, denied/revoked permissions, airplane mode/reconnect, background/process kill, localization and accessibility.
4. Use automation IDs and stable navigation contracts, not brittle hard-coded pixel positions.
5. Set up CI job ownership per OS and measure flaky-test retries; do not treat automatic retries as proof the test is reliable.
6. Execute only available tests, preserve exit codes/outputs, record actual device + OS + SDK, and mark unavailable tests NOT RUN.

## Output
Populated target matrix, test instructions/scripts, result evidence, blockers and clear ship/no-ship recommendation.

## Reference
`knowledge/MAUI_TEST_MATRIX.md`.
