# Test and release matrix

| Case | Web/PWA | Android emulator | Android physical | iOS simulator | iOS physical |
|---|---|---|---|---|---|
| Navigation/route back | yes | yes | yes | yes | yes |
| API/forms/accessibility | yes | yes | yes | yes | yes |
| Permissions/camera | fallback | simulated | **required** | simulated | **required** |
| APNs/FCM push | conditional | limited | **required** | limited | **required** |
| Verified deep links | yes | yes | **required** | yes | **required** |
| Offline queue/restart | yes | yes | **required** | yes | **required** |
| Process kill/resume | n/a | yes | **required** | yes | **required** |
| Signed release | web publish | debug/AAB | AAB verify | Xcode archive | TestFlight |

**Build sequence:** locked npm install -> lint/type/unit -> production web build -> `npx cap sync android` / `ios` -> native compile -> emulator and real-device smoke -> stage signed release.

Native iOS requires compatible macOS+Xcode; Android needs SDK/Gradle. Keep `ios/` and `android/` tracked. Remove live reload server.url from production. On Android confirm app ID/versionCode, Play target SDK and Data Safety; produce signed AAB with secure upload key. On Apple confirm bundle ID, Team ID, provisioning, privacy strings/manifests, associated domains, build/archive and TestFlight. No secret material in repository and no store submission without explicit approval.

**Evidence template:** command | device and OS | result PASS/FAIL/NOT TESTED | artifact/log | limitation. Do not mark omitted device tests as passing.
