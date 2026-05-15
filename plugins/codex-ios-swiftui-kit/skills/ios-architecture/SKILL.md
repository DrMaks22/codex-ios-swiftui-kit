---
name: ios-architecture
description: Use when a SwiftUI feature needs clearer state ownership, dependency injection, feature boundaries, or module-level structure.
---

# iOS Architecture

## Overview

This skill keeps a SwiftUI feature from becoming a pile of shared state and accidental dependencies. It is for ownership, boundaries, and practical modularity.

## Use this skill when

- a feature spans several views or services
- state ownership is unclear
- a screen feels hard to test or hard to change
- you need to decide whether a boundary belongs in the feature, a view model, or a shared layer

## Workflow

1. Map the responsibilities in the feature.
2. Identify the one owner for each piece of mutable state.
3. Decide which dependencies are local and which should be injected.
4. Draw the smallest useful feature boundary.
5. Remove abstractions that do not earn their keep.

## What to output

Return:

- ownership map for the feature state
- boundary recommendations
- dependency injection points
- any over-abstraction or coupling risks

## Rules

- One piece of mutable state should have one clear owner.
- Keep dependencies as local as possible.
- Inject only what the feature actually needs.
- Do not create layers that only mirror existing UIKit or service structures.
- Split modules when the boundaries improve comprehension or testing.
- Prefer a smaller, explicit architecture over a clever but hidden one.

## References

- [`state-ownership.md`](references/state-ownership.md)
- [`module-boundaries.md`](references/module-boundaries.md)
- [`dependency-injection.md`](references/dependency-injection.md)
