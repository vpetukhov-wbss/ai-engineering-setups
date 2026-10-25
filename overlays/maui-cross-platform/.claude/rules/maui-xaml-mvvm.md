---
paths:
  - "**/*.xaml"
  - "**/*.xaml.cs"
  - "**/*ViewModel.cs"
  - "**/MauiProgram.cs"
---

# maui-xaml-mvvm

- Use clear responsibility separation: `.xaml` for view structure, `.xaml.cs` for platform/view glue, ViewModel for screen state and commands, services for business and IO.
- For nontrivial bindings set `x:DataType` on pages and each DataTemplate; never silence incorrect bindings with `x:Object`.
- Prefer CommunityToolkit.Mvvm observable/command generators if compatible with existing dependencies; no unnecessary framework abstractions.
- Async commands must control reentrancy, error states, cancellations, and actual user feedback.
- Register page/ViewModel/service lifetimes intentionally in MauiProgram; no ambient global mutable state for user/tenant.
- Ensure UI updates run on main thread, respect reduced motion where applicable, dispose subscriptions and native handlers.
- Build keyboard/screen reader/touch accessibility and phone/tablet/window layouts from requirements, not post-release.
- Document which UI/performance assertions were actually measured on devices.
