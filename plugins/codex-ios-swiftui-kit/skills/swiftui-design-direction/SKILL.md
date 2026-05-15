---
name: swiftui-design-direction
description: Use for iPhone SwiftUI design direction, premium visual lanes, tokens, hierarchy, and anti-AI-slop treatment before implementation.
---

# SwiftUI Design Direction

Use this skill when a request includes: design concept, visual identity, screen concept, layout rhythm, anti-generic concerns, or any need to fix "AI-like" look.

## Use this skill when

- creating a new iPhone-first screen
- extracting a visual system from Figma or a brief
- improving a screen that looks generic or inconsistent
- checking accessibility-minded visual constraints before implementation

## Do not use this skill when

- implementation details are already fully decided and only SwiftUI code is requested
- architecture decisions are the main blocker
- user asks only for review of existing build quality

## Codex behavior

- Select a single visual lane and one accent logic.
- Keep compact-width iPhone as default.
- Return concise, copy-pastable artifacts that can be directly passed to `ios-swiftui`.
- If evidence suggests performance risk, call it out with a clear mitigation hint.
- Do not use Figma unless the user provides a Figma file, frame, selection, or explicitly asks for Figma.

## Workflow

1. Read the product brief and identify the primary user job.
2. Pick one design lane from `design-lanes.md`.
3. Define token schema for color, typography, spacing, shape, and motion.
4. Evaluate anti-slop score using `anti-ai-slop.md`.
5. Add accessibility and performance constraints.
6. Pass a structured handoff ready for `ios-swiftui`.

## What to output

Use this exact structure:

## Visual Direction
- Lane:
- Product mood:
- One-sentence screen concept:
- What makes it distinctive:
## Tokens
| Role | Token | Light | Dark | SwiftUI mapping | Notes |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |
## Layout Hierarchy
1.
2.
3.
## Interaction and Motion
- Primary interaction:
- Secondary interactions:
- Motion intent:
- Reduced-motion alternative:
## Accessibility Constraints
- Dynamic Type:
- VoiceOver:
- Contrast:
- Touch targets:
## Implementation Handoff
- Primary screen pattern:
- Required SwiftUI containers:
- Required custom components:
- Primary action placement:
- State implied by design:
- Assets:
- Performance risks:

## Rules

- Start from iPhone compact width and scale only with explicit reason.
- Keep one dominant visual system per screen.
- Use typography, spacing, and semantic color as core tools.
- Avoid generic glass, neon, rainbow gradients, and random shadows.
- Keep the primary action obvious and reachable.
- Make dark mode and light mode both plausible.
- If the layout depends on brand assets, state the exact role for each.
- Avoid inventing premium effects that cannot be implemented in plain SwiftUI without heavy GPU cost.

### Performance and accessibility guardrails

- For each major visual move, note a realistic performance risk.
- Do not output interactions that break Dynamic Type or VoiceOver semantics.
- If screen states are dense, prioritize readability over decorative depth.

## References

- [`anti-ai-slop.md`](references/anti-ai-slop.md)
- [`layout-patterns.md`](references/layout-patterns.md)
- [`design-lanes.md`](references/design-lanes.md)
- [`handoff-contract.md`](../../references/handoff-contract.md)
- [`swiftui-state-ownership.md`](../../references/swiftui-state-ownership.md)
- [`figma-bridge.md`](../../references/figma-bridge.md)
- [`typography-color.md`](references/typography-color.md)
- [`brand-assets.md`](references/brand-assets.md)
