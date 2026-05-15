---
name: ios-accessibility
description: Use when auditing or implementing SwiftUI screens for VoiceOver, Dynamic Type, contrast, motion, and touch target accessibility.
---

# iOS Accessibility

## Overview

This skill checks whether a SwiftUI screen remains usable for VoiceOver users, people using larger text, and users who prefer reduced motion or stronger contrast.

## Use this skill when

- a SwiftUI screen is ready for accessibility review
- the layout or control hierarchy may be confusing to assistive technology
- text may wrap, scale, or truncate in risky ways
- motion, contrast, or touch target size could block real users

## Workflow

1. Inspect reading order and semantic labels first.
2. Check Dynamic Type behavior with longer and larger text.
3. Confirm color contrast and non-color cues.
4. Verify motion and focus behavior with accessibility preferences in mind.
5. Return a concrete list of fixes, not vague advice.

## What to output

Return:

- accessibility findings ordered by impact
- exact SwiftUI changes to make
- any labels, hints, values, or traits that should be added
- notes about Dynamic Type, motion, and contrast

## Rules

- Do not rely on color alone to communicate state.
- Prefer standard controls and semantics when they already match the job.
- Keep touch targets generous and predictable.
- Make the reading order match the visual order unless there is a strong reason not to.
- Respect reduced motion.
- Keep labels concise but meaningful.
- If the screen breaks at large text sizes, treat that as a design issue, not only an accessibility issue.

## References

- [`voiceover.md`](references/voiceover.md)
- [`dynamic-type.md`](references/dynamic-type.md)
- [`contrast-motion.md`](references/contrast-motion.md)
