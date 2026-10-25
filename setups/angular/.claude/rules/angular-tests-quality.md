---
paths:
  - "**/*.spec.ts"
  - "**/*.test.ts"
  - "**/e2e/**"
  - "**/playwright.config.*"
---
# Tests
- Use the project's installed runner; recent CLI projects default to Vitest, older projects may use Karma/Jasmine or Jest.
- Test observable user behavior and state transitions, not private implementation details or mocked internals without value.
- Include empty/loading/error/permission and accessibility states, cancel/retry flows, malformed API responses and race conditions.
- E2E should use stable accessibility selectors and hermetic test accounts/data. Never point destructive tests at production.
- Report exact runner version, command, passed/failed counts and skipped checks.
