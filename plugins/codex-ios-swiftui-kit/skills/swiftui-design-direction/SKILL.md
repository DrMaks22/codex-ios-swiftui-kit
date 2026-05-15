---
name: swiftui-design-direction
description: Use when you need a premium iPhone SwiftUI visual direction, design tokens, layout rhythm, or a critique of a screen that feels generic or overdesigned.
---

# SwiftUI Design Direction

## Overview

This skill defines the visual language before code is written. It is for choosing a clear aesthetic lane, turning it into tokens, and rejecting generic AI-style UI.

## Use this skill when

- a new screen needs a visual system
- an existing view feels bland, noisy, or off-brand
- you need typography, color, spacing, and motion direction
- you want a design critique before implementation

## Workflow

1. Read the product brief and identify the primary user job.
2. Pick one visual lane and one supporting accent, not three competing ideas.
3. Define tokens for color, type, spacing, shape, and motion.
4. Describe the screen hierarchy from top to bottom on iPhone compact width.
5. Review the result for anti-slop issues before handing it to implementation.

## What to output

Return:

- the chosen visual lane
- a small token set
- layout hierarchy by section
- motion and interaction notes
- brand asset placement if needed
- one paragraph explaining why the design is distinctive

## Rules

- Start from iPhone compact width and scale up only if needed.
- Keep one dominant visual system per screen.
- Use typography and spacing as the main design tools.
- Use color sparingly and semantically.
- Avoid generic glass, neon, rainbow gradients, and random shadows.
- Keep the primary action obvious and reachable.
- Make dark mode and light mode both plausible.
- If the layout depends on brand assets, state the exact role of those assets.

## References

- [`anti-ai-slop.md`](references/anti-ai-slop.md)
- [`layout-patterns.md`](references/layout-patterns.md)
- [`typography-color.md`](references/typography-color.md)
- [`brand-assets.md`](references/brand-assets.md)
