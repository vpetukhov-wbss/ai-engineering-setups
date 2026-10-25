# Golden Claude Code prompts

## Product design
```text
/ionic-app-architecture
Design a multi-role production/order app for customer, storekeeper, production and admin using Ionic Angular + Capacitor on iOS, Android and optional PWA. ASP.NET Core owns authorization and business rules. Produce architecture/ADR, routes, typed API contracts, local storage strategy, native plugin choices, permission matrix, device tests and staged release gates. KISS/DRY/YAGNI.
```

## Native camera
```text
/capacitor-plugin-integration
Implement a customer cake image upload with permission-denied UX, browser fallback and Android activity restoration. Preserve the installed Capacitor version; run verified test commands and label unavailable native tests NOT TESTED.
```

## Offline work
```text
/ionic-offline-sync
Design offline production status changes with server idempotency, ETag/revision conflicts, queue retries and recovery after process kill. Compare SQLite and preferences; never put credentials in Preferences.
```

## App release
```text
/ionic-device-testing
Audit signed Android and iOS readiness and produce a PASS/FAIL/NOT TESTED matrix with exact environments, privacy declarations, device evidence, missing entitlements and explicit production approval requirements.
```
