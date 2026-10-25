# Ionic Angular + Capacitor Engineering Profile

Reusable Claude Code engineering overlay for **Ionic Angular on iOS, Android and Web/PWA**. It adds mobile architecture, native plugins, routing, offline sync, auth, push, testing, signing and store release instructions to the [base Angular setup](../../setups/angular/). It is **not** a replacement for the .NET MAUI profile and does **not** claim native Windows/macOS support.

## Install

```bash
git clone https://github.com/vpetukhov-wbss/ai-engineering-setups.git
cd ai-engineering-setups

# Angular + Ionic Capacitor project
python3 scripts/install.py --preset ionic-angular --target /path/to/ionic-app
python3 scripts/install.py --preset ionic-angular --target /path/to/ionic-app --apply

# ASP.NET Core + Angular Ionic Capacitor full-stack repository
python3 scripts/install.py --preset dotnet-ionic-angular --target /path/to/fullstack-app --apply
```

The installer copies instructions, **not an Ionic app or SDKs**. It previews first and does not overwrite existing CLAUDE.md without explicit flag. Review [IONIC_CLAUDE_APPEND.md](IONIC_CLAUDE_APPEND.md), merging it into your project's CLAUDE.md manually.

## Start a new application (optional)

```bash
npm install -g @ionic/cli
ionic start my-app tabs --type=angular
# choose Standalone if prompted
cd my-app
ionic serve
ionic build
npx cap add android  # only if not already present
npx cap add ios      # only if not already present, requires macOS/Xcode
npx cap sync
```

For existing apps, inspect actual versions and do not recreate native projects. As checked 2026-10-25, official docs show **Ionic 9** and **Capacitor 8**; Capacitor 8 requires Node 22+ and compatible platform SDKs. Framework versions update separately. Follow your locked project's compatibility matrix.

## 13 specialized skills

| Command | Scope |
|---|---|
| `/ionic-app-architecture` | Requirements, architecture and native capability matrix |
| `/ionic-feature` | Feature-first Ionic UI, state and error handling |
| `/ionic-navigation-lifecycle` | Tabs, cached routes, hardware back and deep links |
| `/capacitor-plugin-integration` | Official/community/custom native plugin decisions |
| `/ionic-offline-sync` | SQLite strategies, queue/idempotency/conflicts |
| `/ionic-auth-and-deep-links` | OIDC PKCE, universal/app links, secure session |
| `/ionic-push-notifications` | APNs, FCM, permission/token lifecycle |
| `/ionic-performance-a11y` | Startup, accessibility, keyboard and safe areas |
| `/ionic-device-testing` | Web, emulator and real device quality matrix |
| `/ionic-android-release` | Android AAB, Play internal release |
| `/ionic-ios-release` | Xcode archive, TestFlight, App Store |
| `/ionic-pwa-release` | Browser/PWA offline assets and updates |
| `/ionic-capacitor-upgrade` | Angular/Ionic/Capacitor upgrades and native diffs |

6 specialist agents, 5 mobile rules and focused knowledge/templates are included. Standard Angular skills for typed forms, state, HTTP APIs, security, accessibility and tests remain available.

## Definition of done
- UI: mobile and tablet layout, touch/screen reader, safe areas and keyboard handling.
- Native: plugin permissions, unavailable/fallback states, app resume and process restoration.
- Data: backend authority, token safety, offline retry/duplicate/conflict tests as applicable.
- Delivery: browser checks + **separate iOS/Android builds and real device testing** for native features.
- Stores: separate signed Android AAB and iOS Xcode/TestFlight reviews, with explicit human approval.

A web build cannot certify mobile device behavior. Skills guide an agent; they do not automatically sign or publish apps.

## References
See [MOBILE_ARCHITECTURE.md](knowledge/MOBILE_ARCHITECTURE.md), [NATIVE_SECURITY_OFFLINE.md](knowledge/NATIVE_SECURITY_OFFLINE.md), [RELEASE_TEST_MATRIX.md](knowledge/RELEASE_TEST_MATRIX.md) and [SOURCES.md](knowledge/SOURCES.md).
