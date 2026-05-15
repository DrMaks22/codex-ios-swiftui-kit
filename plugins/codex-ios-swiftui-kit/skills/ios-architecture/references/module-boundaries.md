# Module Boundaries

Boundary intent: improve comprehension and reduce risk.

## Patterns

- Keep local:
  - screen-specific helpers used only inside one screen.
  - behavior tied to one flow and one owner.
- Feature boundary:
  - state and actions shared by several screens in same feature.
  - cohesive unit tests and shared preview fixtures.
- Shared module:
  - truly reusable behavior with multiple features.
  - behavior used in two+ features and stable over time.
- Avoid extracting yet:
  - premature abstraction for one-off screens
  - utilities with no observed reuse

## Signs boundary is wrong

- frequent imports from unrelated modules
- every change requires touching many layers
- module has no clear contract and no stable tests
