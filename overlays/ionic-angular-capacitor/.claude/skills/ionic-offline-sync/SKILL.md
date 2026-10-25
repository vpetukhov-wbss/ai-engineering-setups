---
name: ionic-offline-sync
description: "Persistent offline entities and conflict-safe sync with backend."
---

# ionic-offline-sync

1. Classify preferences, structured offline records, media cache and credentials separately.
2. Use @capacitor/preferences only for small nonsensitive values; choose maintained SQLite or equivalent for durable transactional offline data, OS vault for auth credentials.
3. Design local schema migrations, immutable command IDs, idempotent server endpoints, queue states, retry/backoff, revision/ETag conflicts and user-visible resolution.
4. On reconnect or resume, verify server reachability and sync; do not assume background execution runs continuously on iOS/Android.
5. Test write/read offline, restart/process kill, partial upload, duplicate request, server rejection, logout/wipe and conflict recovery.

## Proof of completion
Provide changed files, exact commands/results, platforms verified, platforms NOT TESTED, risks, and human approvals still needed. Never claim a device or App Store submission was tested if it was not.
