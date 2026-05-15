---
name: ios-accessibility
description: Use for VoiceOver, Dynamic Type, contrast, motion, and touch-target accessibility audit and implementation fixes in SwiftUI.
---

# iOS Accessibility

## Use this skill when

- a SwiftUI screen is ready for accessibility review
- the layout or control hierarchy may be confusing to assistive technology
- text may wrap, scale, or truncate in risky ways
- motion, contrast, or touch target size could block real users

## Do not use this skill when

- there are no concrete screens or code contexts to review
- performance-only optimizations are requested

## Codex behavior

- Return findings in impact order.
- Require exact SwiftUI edits, not generic guidance.
- Link issues to code region/pattern so fixes are actionable.
- Use provided existing screen or files as primary evidence.
- Call out `anti-accessibility theater`: a fix that is visible in screenshots but not real usability improvement.

## Workflow

1. Inspect reading order and semantic labels first.
2. Check Dynamic Type behavior with larger scales.
3. Verify contrast, non-color cues, and state communication.
4. Validate reduced-motion and focus behavior.
5. Verify touch targets and control density.
6. Run a compact test matrix and return exact fixes.

## What to output

## Accessibility Findings
| Impact | Issue | Evidence | Fix |
|---|---|---|---|
## VoiceOver
- Reading order:
- Labels:
- Values:
- Hints:
- Traits:
## Dynamic Type
- Risk areas:
- Layout fixes:
## Contrast and Non-Color Cues
- Contrast:
- State communication:
## Motion and Focus
- Reduced motion:
- Focus behavior:
## Touch Targets
- Primary actions:
- Secondary controls:
## Handoff
- Required code changes:
- Residual risks:

## Rules

- Do not rely on color alone to communicate state.
- Prefer standard controls and semantics when they already match the job.
- Keep touch targets generous and predictable.
- Make the reading order match the visual order unless there is a strong reason not to.
- Respect reduced motion.
- Keep labels concise but meaningful.
- If the screen breaks at large text sizes, treat that as a design issue, not only an accessibility issue.
- Require severity ordering and explicit remaining risk.
- Add contrast and motion checks before finishing.
- Include anti-accessibility-theater examples: "looks fixed but still unusable".

## References

- [`voiceover.md`](references/voiceover.md)
- [`dynamic-type.md`](references/dynamic-type.md)
- [`contrast-motion.md`](references/contrast-motion.md)
- [`accessibility-test-matrix.md`](references/accessibility-test-matrix.md)
