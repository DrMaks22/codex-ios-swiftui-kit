---
name: ios-swiftui
description: Use when turning an iPhone UI concept into SwiftUI layout, state, navigation, presentation, or animation code.
---

# iOS SwiftUI

## Overview

This skill turns a design direction into a correct SwiftUI structure. It is for layout, data flow, navigation, sheets, alerts, and animation choices.

## Use this skill when

- you already know the screen shape and need SwiftUI code
- a view tree feels too deep, too tangled, or too stateful
- navigation, sheet, or alert behavior needs to be planned
- you need a clean first pass before accessibility and performance review

## Workflow

1. Identify the smallest view structure that can support the screen.
2. Decide which state belongs locally and which state should be passed in.
3. Build the hierarchy from container to leaf views.
4. Add presentation and navigation explicitly, not implicitly.
5. Check the resulting body for clarity, reuse, and unnecessary branching.

## What to output

Return:

- the proposed SwiftUI view tree
- state ownership decisions
- navigation and presentation plan
- adaptive layout notes
- a concise code sketch if useful

## Rules

- Prefer small, focused view types.
- Keep state as close to its owner as possible.
- Use SwiftUI primitives before reaching for UIKit bridges.
- Keep `body` readable; move repeated logic into helpers or subviews.
- Treat presentation state as explicit data, not hidden side effects.
- Use the simplest navigation model that fits the product.
- Keep the layout resilient to compact width, dynamic type, and long text.

## References

- [`layout.md`](references/layout.md)
- [`state.md`](references/state.md)
- [`navigation.md`](references/navigation.md)
- [`animation.md`](references/animation.md)
