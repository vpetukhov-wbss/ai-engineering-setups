---
name: ionic-push-notifications
description: "Implement notifications with APNs, FCM, permission consent and token lifecycle."
---

# ionic-push-notifications

1. Confirm user value and lawful consent; document notification channel/category requirements.
2. Review @capacitor/push-notifications compatibility and configure APNs capabilities plus Android FCM server integration.
3. Register after appropriate permission, associate tokens with user/device on backend, handle rotation, reinstall, logout and revocation.
4. Handle foreground, background and terminated notification taps with validated deep links; don't trust notification body as business state.
5. Run real-device permission/token/delivery tests on both OSs, note simulator limits and test duplicated/late notifications.

## Proof of completion
Provide changed files, exact commands/results, platforms verified, platforms NOT TESTED, risks, and human approvals still needed. Never claim a device or App Store submission was tested if it was not.
