---
name: maui-ui-quality
description: "Audit and improve MAUI UI for VoiceOver TalkBack Narrator accessibility, responsive layout, performance and design consistency."
---

# maui-ui-quality

## Procedure
1. List supported phone/tablet/desktop sizes, DPI, orientation, theme, font scale and input methods.
2. Inspect screen reader semantics, labels, navigation order, touch target sizes, headings, contrast, loading/error announcements and dynamic type.
3. Inspect typed bindings, `CollectionView` virtualization and layout nesting; do not refactor without reproduction or measurement.
4. Test desktop hover/focus/keyboard, mobile gestures/IME overlap, safe areas and accessibility across actual target devices.
5. Include screenshots/recordings and profiling baselines only if actually produced; separate design review from functional UI tests.
6. Recommend small, testable changes and distinguish automatic lint/compile checks from human accessibility audits.

## Output
Severity-ranked accessibility defects, device matrix, before/after metrics (when available), proposed fixes and residual risk.

## References
`knowledge/MAUI_CROSS_PLATFORM.md`, `knowledge/MAUI_TEST_MATRIX.md`.
