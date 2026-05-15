---
name: ios-architecture
description: Use for SwiftUI feature architecture: state ownership, dependency injection, boundaries, and test seams before or after implementation.
---

# iOS SwiftUI Feature Architecture

Use this skill for feature-level architecture decisions, not as a generic architecture doctrine.

## Use this skill when

- feature spans multiple screens/services/shared state
- state ownership is duplicated or unclear
- boundaries, DI, or testability are blocking progress
- implementation already needs refactor before reliable review

## Do not use this skill when

- request is only visual direction
- request is only straightforward single-view implementation

## Codex behavior

- Explicitly mark pass type: pre-implementation or refactor/audit.
- Recommend architecture only at feature granularity unless there is evidence for extraction.
- Reference `../../../references/swiftui-state-ownership.md` as source of truth for state placement.

## Workflow

1. Map feature responsibilities and dependencies.
2. Assign one owner per mutable state.
3. Define feature entry point and DI injection model.
4. Confirm shared boundaries and anti-abstraction candidates.
5. Add test and preview seams.
6. Return compact handoff contract to implementation.

## Required output

## Responsibility Map
| Responsibility | Owner | Notes |
|---|---|---|
## State Ownership
| State | Owner | Mutators | Readers | Lifetime |
|---|---|---|---|---|
## Dependency Map
| Dependency | Injected At | Used By | Reason |
|---|---|---|---|
## Boundary Decision
- Keep inside feature:
- Extract to shared:
- Do not abstract yet:
## Test Seams
- Unit-testable logic:
- Preview/sample data:
- Integration risks:
## Handoff
- Implementation constraints:
- Risks to review later:

## Rules

- Do not mandate Clean Architecture, MVVM, or TCA.
- One owner per mutable state is mandatory.
- Inject at feature boundary first, not globally.
- Avoid modules with no measurable comprehension benefit.
- Prefer one clear architecture pass over repeated rewrites.

## References

- [`state-ownership.md`](references/state-ownership.md)
- [`module-boundaries.md`](references/module-boundaries.md)
- [`dependency-injection.md`](references/dependency-injection.md)
- [`feature-boundaries.md`](references/feature-boundaries.md)
