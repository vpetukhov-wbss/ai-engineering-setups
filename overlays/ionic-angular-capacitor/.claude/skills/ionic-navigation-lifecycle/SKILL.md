---
name: ionic-navigation-lifecycle
description: "Navigation stacks, Ionic cached pages, deep links and back behavior."
---

# ionic-navigation-lifecycle

1. Inspect Angular Router, IonRouterOutlet, IonTabs, nested outlets, route guards, overlay handling and Android back.
2. Respect independent tab histories; nested outlets should normally be reserved for tabs. Ionic may cache routed views instead of destroying them.
3. Use ionViewWillEnter or ionViewDidEnter when revisiting must refresh; use ionViewWillLeave to suspend visible-only work. ngOnInit does NOT mean every entry.
4. Test modal dismissal, input keyboard and hardware back, resume, app kill and link open from closed app.
5. Validate Universal/App Link HTTPS scheme/host/path allowlist before navigation; account for Angular change detection in outlet ancestors.

## Proof of completion
Provide changed files, exact commands/results, platforms verified, platforms NOT TESTED, risks, and human approvals still needed. Never claim a device or App Store submission was tested if it was not.
