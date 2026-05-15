# SwiftUI State Ownership (Shared Contract)

Use this as the single source for state ownership across skills.

## State levels

| Level | What it is | Typical container | Lifetime |
|---|---|---|---|
| View-local transient state | Immediate UI interaction state | Single view or leaf | current interaction |
| Presentation state | Sheet, cover, alert, confirmation, focus state | Parent owning route/presentation lifecycle | usually screen session |
| Feature state | Domain values and actions for a feature | Feature root or coordinator | feature session or feature scope |
| Shared app state | User profile, auth, global settings | App-level state owner | app lifetime |
| External/service-backed state | Results loaded from services | Data layer owner | network/session/cache lifecycle |

## Decision tree

1. Is the value derived from another value?
   - Yes -> derived property/state; do not store independently.
   - No -> continue.
2. Does it survive screen dismissal or back-navigation?
   - Yes -> feature state, shared app state, or service-backed state.
   - No -> maybe view-local or presentation state.
3. Who mutates it?
   - A single owner only -> keep that owner local to mutate.
   - Multiple owners -> move upward to shared owner first.
4. Who observes it?
   - 1 view -> local.
   - Multiple siblings or distant descendants -> feature/shared owner.
5. Is it UI-only or behavior-critical?
   - UI-only -> view-local or presentation.
   - Behavior-critical -> feature state or shared state.

## SwiftUI implementation mapping

- View-local transient: `@State`, local bindings.
- Shared feature state: `@StateObject`, environment-owned source-of-truth, observation (`@Observable`) at feature boundary.
- Presentation: explicit route/presentation flags and enums, not implicit side effects.
- Derived values: computed properties, memoized selectors, not stored as separate mutable state.
- External state: injected services/repositories, async flows, and explicit cache invalidation.

## Output table (use with all implementation and review tasks)

| State | Owner | Mutators | Readers | Lifetime | Notes |
|---|---|---|---|---|---|
| replace with actual state names | |

Use one row per meaningful piece of mutable state.
