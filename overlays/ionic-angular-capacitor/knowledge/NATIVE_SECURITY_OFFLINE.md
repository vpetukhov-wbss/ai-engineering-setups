# Security, storage, plugins and offline synchronization

## Evaluate every plugin
Capture exact name/version, Capacitor major, Android/iOS/Web support, maintenance and CVEs, license, native SDK implications, permissions, privacy/data access, process lifecycle and test evidence. Consider vetted community/plugin alternative only after official APIs.

## Security boundaries
A Capacitor app packages readable JavaScript. Never ship a client secret, signing key, production credential or encryption root key. Native OIDC uses Authorization Code+PKCE with system browser, state/nonce and checked callback. Prefer HTTPS Universal Links/App Links; validate host/scheme/path and register associated domain assets securely. Secure token storage should use approved Keychain/Keystore-backed solutions. Guard business permissions server-side. Audit WebView origins, CORS/CSRF, XSS sanitization, CSP and untrusted external links.

## Storage classes
- Preferences: lightweight, nonsensitive key/value settings; **not a database or secret vault**.
- Offline orders/production state: vetted SQLite/equivalent with migrations, transactions, querying and appropriate encryption.
- Files/media: explicit retention, size limits, storage and retry semantics.
- Credentials: securely managed device storage, clear on logout where appropriate.

## Durable synchronization
Represent each queued operation with unique ID, stable idempotency key, revision/ETag, payload, state, retry count and timestamps. Backend enforces idempotency, conflicts and authorization. Handle offline create/edit, retry, server rejection, app kill between send/ack, duplicate messages and logout data cleanup. Use backoff/reconnection/resume checks; connectivity is not backend reachability. iOS/Android can suspend background work at any time.

## Permissions and process death
Request narrowly at point of use; handle granted, denied, restricted, permanently denied and unsupported. Android camera/other external activities may return a restored result after app termination. Test both Web fallback and native happy/failure cases. Avoid logging PII or notification tokens.
