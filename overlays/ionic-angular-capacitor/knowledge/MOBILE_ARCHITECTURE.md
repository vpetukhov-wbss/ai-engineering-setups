# Ionic + Capacitor architecture playbook

## Choose deliberately
Choose Ionic+Capacitor when an Angular/Web UI is reusable and native integrations are bounded. Pure PWA is simpler when browser APIs suffice; MAUI/fully native may be better for extensive platform-specific UX, heavy graphics or background operations. Determine this from business constraints and device requirements, not enthusiasm for patterns.

## Feature-oriented code
```text
src/app/
  core/              # authentication/bootstrap only when genuinely cross-cutting
  features/
    orders/
      orders.routes.ts
      pages/order-list.page.{ts,html,scss,spec.ts}
      data/orders.api.ts
      state/orders.store.ts
    production/
      ...
  platform/
    camera/camera.port.ts
    camera/capacitor-camera.adapter.ts
  shared/ui/         # only truly reused UI
ios/                  # tracked native Xcode project
android/              # tracked native Android project
capacitor.config.ts
```
Adapt to existing conventions. No gratuitous repositories, generic Helpers/Utils or multiple unrelated classes per file.

## Navigation + lifecycle
Angular Router with IonRouterOutlet, optionally IonTabs. Pages can remain in the DOM when not active: ngOnInit runs once on creation, ngOnDestroy only on removal. Refresh on ionViewWillEnter/DidEnter and suspend screen-only work on ionViewWillLeave. Test independent tab stacks, Android back, overlays, soft keyboard, app foreground and kill/restart. Evaluate change detection assumptions around IonRouterOutlet on Angular 22+.

## Capability boundary
Prefer official Capacitor plugin when compatible; review native build requirements and permission purposes. Wrap plugin in minimal injectable adapter only if it improves testing or multi-platform support. Browser fallback is required only when Web/PWA is a supported target.

## Data and backend
Keep backend authoritative for money, permissions, state transitions and conflicts. Model typed DTOs, loading/empty/error states, offline queue and server idempotency. Signals for synchronous UI state; RxJS for async streams and cancellation; one source of truth.

## Decisions worth an ADR
PWA vs native; major plugin; authentication; database/encryption; push provider; OTA; high-risk release. State measurable quality gates and tradeoffs.
