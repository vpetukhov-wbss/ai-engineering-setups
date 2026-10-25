# Merge into the existing project CLAUDE.md — Ionic Angular + Capacitor

This overlay augments the Angular (or .NET + Angular) baseline. The installer does **not** append automatically.

- Target platforms: iOS/iPadOS and Android native via Capacitor; browser/PWA only when requested. Windows desktop/macOS desktop are NOT native Capacitor targets.
- Check installed package versions, lockfile, capacitor.config, ios/, android/, SDKs, native plugins and project build scripts before implementation.
- Prefer feature-first Angular and separate TS/HTML/SCSS/spec files, standalone Ionic imports when appropriate, KISS/DRY/YAGNI.
- Use Ionic router outlet, correct tabs/back stack and ionViewWillEnter/Leave; do not assume ngOnInit/ngOnDestroy runs on every navigation.
- Native API boundary through injectable capability adapters with permission denial, errors, Android process restoration and Web fallback.
- Mobile auth with PKCE/system browser/verified app links, native secure token storage and server authorization. No embedded secrets.
- Offline preferences ≠ transactional database ≠ secure vault. Define idempotent sync, migrations, conflicts and logout/wipe.
- Web build -> cap sync -> platform build -> device tests -> staged store testing; report NOT TESTED rather than inventing PASS.
- Human approval required for real store submission, signing changes, irreversible operations and production spend.

Preferred skills: /ionic-app-architecture /ionic-feature /ionic-navigation-lifecycle /capacitor-plugin-integration /ionic-device-testing.
