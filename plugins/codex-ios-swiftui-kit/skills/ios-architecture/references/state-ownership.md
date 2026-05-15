# State Ownership

State should have one owner and one clear mutation path.

## Guidance

Feature-level decisions should stay in architecture, not in each view.

- Start with `../../../references/swiftui-state-ownership.md`.
- local UI state stays in the smallest possible view.
- shared feature state belongs higher only when multiple children need it.
- derived values should be computed, not stored twice.
- presentation state should be explicit and easy to trace.

## Responsibility questions

- Who owns the truth for each mutable value?
- Which feature owns write access?
- Which screens only observe it?
- What breaks when ownership moves up or down?

## Decision notes

- local = local UI only
- feature = multi-screen shared behavior
- shared = app-level policy/state
- external/service-backed = cached and networked values
