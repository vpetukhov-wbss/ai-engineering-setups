---
description: "Secure mobile identity and offline storage"
paths:
  - "**/*.ts"
  - "**/*.html"
  - "**/*.scss"
  - "**/*.css"
  - "**/capacitor.config.*"
  - "**/ios/**"
  - "**/android/**"
---

# ionic-auth-storage

- Never commit credentials, app-store keys, sensitive certificates, client secrets or private user data.
- Native public OAuth clients use PKCE, callback validation, Keychain/Keystore-backed secure token storage and server-authorized actions.
- Preferences is not a credential vault or durable database; SQLite or equivalent for transactional offline records.
- Document offline migrations, queue operation IDs, server idempotency, revision conflicts and account deletion.
- Assess WebView origins, CORS/CSRF, XSS/CSP, plugin security and privacy declarations.
