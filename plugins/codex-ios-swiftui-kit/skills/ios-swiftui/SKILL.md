---
name: ios-swiftui
description: Use for iPhone SwiftUI implementation from approved design or architecture, including layout, state wiring, navigation, presentation, animation, and previews.
---

# iPhone SwiftUI Implementation

Use this skill when implementation is the target and visual direction is already defined.

## Use this skill when

- you need SwiftUI layout, composition, navigation, or animation implementation
- view code is too tangled or state handling is unclear
- preview/sample-data and API availability are part of the task
- you need a file-level concrete patch plan

## Do not use this skill when

- visual tone is still undecided
- feature-level ownership is unresolved across services or shared state
- only final review or performance-only audit is needed

## Codex behavior

- Inspect existing file context before proposing changes.
- Preserve established project patterns and naming unless there is a clear reason to change.
- Keep recommendations minimal, local, and compilable.
- Do not invent components unless they are explicitly proposed and linked to implementation files.
- Reference `../../references/swiftui-state-ownership.md` before state placement decisions.

## Workflow

1. Inspect relevant files for current structure and patterns.
2. Build the smallest working view tree from container to leaf.
3. Decide state ownership and API availability boundaries.
4. Define explicit navigation/presentation states.
5. Add previewable changes and avoid network-dependent preview logic.
6. Return a patch-oriented implementation contract.

## What to output

## Existing Context
- Files inspected:
- Existing patterns to preserve:
- Deployment target / API constraints, if known:
## View Tree
- Container:
- Sections:
- Leaf components:
- Extracted subviews and why:
## State Ownership
| State | Owner | Binding? | Lifetime | Reason |
|---|---|---|---|---|
## Navigation and Presentation
- Navigation model:
- Routes:
- Sheets/covers/popovers/alerts:
- Dismissal behavior:
## Adaptive Layout
- Compact width:
- Dynamic Type:
- Long text/localization:
- Safe areas:
## Implementation Plan
- Files to edit:
- New files/types:
- Preview/sample data impact:
## Code / Patch
- Concrete code sketch or patch steps

## Rules

- Prefer small, focused views and predictable composition.
- Keep state close to its owner and avoid copying mutable truth.
- Use SwiftUI primitives before UIKit bridging.
- Keep `body` readable, avoid heavy logic in deeply rendered closures.
- Make navigation and presentation explicit and inspectable.
- Respect compact width, Dynamic Type, and long text from the start.
- Verify API availability when using newer SwiftUI APIs.
- Keep one interaction model for navigation per feature.

## References

- [`layout.md`](references/layout.md)
- [`state.md`](references/state.md)
- [`navigation.md`](references/navigation.md)
- [`animation.md`](references/animation.md)
- [`previewability.md`](references/previewability.md)
- [`swiftui-state-ownership.md`](../../references/swiftui-state-ownership.md)
- [`handoff-contract.md`](../../references/handoff-contract.md)
