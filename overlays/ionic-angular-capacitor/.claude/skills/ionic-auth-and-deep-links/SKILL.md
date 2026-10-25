---
name: ionic-auth-and-deep-links
description: "Secure public-client login, OIDC PKCE, auth callback and link handling."
---

# ionic-auth-and-deep-links

1. Identify IdP/backend, browser/native origins, app association domains and session policy.
2. Prefer Authorization Code + PKCE via system browser for native public clients; never place client secrets in app binaries or environment files.
3. Validate state, nonce, callback scheme/host/path, exact redirect URI and only allowlisted app routes. Prefer verified HTTPS Universal/App Links.
4. Use vetted Keychain/Keystore-backed storage for tokens; not localStorage or Capacitor Preferences; handle refresh rotation, app resume, cancellation and logout.
5. Authorize every sensitive action server-side. Test malicious callbacks, stale sessions, revoked credentials and browser/native CORS and cookie differences.

## Proof of completion
Provide changed files, exact commands/results, platforms verified, platforms NOT TESTED, risks, and human approvals still needed. Never claim a device or App Store submission was tested if it was not.
