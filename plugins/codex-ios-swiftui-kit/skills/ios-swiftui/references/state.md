# SwiftUI State (Implementation-level)

Use `@State`, `@Binding`, `@Observed`, and observation types at implementation level only.

## Preferred primitives

- `@State`: local, non-shared interaction state.
- `@Binding`: editable state owned elsewhere.
- `@Observable` / `@StateObject` / model objects: shared feature-level mutable state.
- Derived values: computed properties, not stored as separate mutable fields.
- Presentation state: explicit `@State`/bindings for sheets, alerts, full-screen covers.

## Decision guide

- Read-only data for child display -> pass by value.
- Shared editable data -> inject owner and binding.
- Derived state -> compute, do not duplicate.
- Multi-view presentation coordination -> centralize in parent container.

## Shared contract

- Use [`../../../references/swiftui-state-ownership.md`](../../../references/swiftui-state-ownership.md) to classify every mutable value before implementing.
- Architecture-level ownership questions are handled by `ios-architecture`.

## Common mistakes

- duplicating the same mutable truth across siblings
- passing derived values through state bindings
- storing ephemeral UI flags in persistent feature state
- treating transient focus/sheet state as app-level state
