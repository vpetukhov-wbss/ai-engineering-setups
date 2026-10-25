---
description: "Ionic layout router and lifecycle"
paths:
  - "**/*.ts"
  - "**/*.html"
  - "**/*.scss"
  - "**/*.css"
  - "**/capacitor.config.*"
  - "**/ios/**"
  - "**/android/**"
---

# ionic-ui-navigation

- Prefer standalone Ionic imports from @ionic/angular/standalone when app uses standalone Angular, and provideIonicAngular() as appropriate.
- Use IonApp and IonRouterOutlet, tabs' independent stacks, ion-header/ion-content and responsive safe areas.
- Cached routed pages may not call ngOnInit/ngOnDestroy on every navigation; handle ionViewWillEnter/ionViewWillLeave correctly.
- Respect keyboard, hardware back, dark mode, system text scale, orientation and accessible focus.
- Keep TS, HTML, SCSS/CSS and spec files separate; no generic helper grab bags.
- Verify Angular 22+ change detection assumptions near IonRouterOutlet.
