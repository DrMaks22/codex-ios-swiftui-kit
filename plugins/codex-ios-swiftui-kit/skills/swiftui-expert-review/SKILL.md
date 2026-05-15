---
name: swiftui-expert-review
description: Use when reviewing or refining SwiftUI code for state ownership, modern APIs, accessibility, performance, and navigation correctness.
---

# SwiftUI Expert Review

## Overview

This skill is the final review gate for SwiftUI work. It checks correctness, polish, and implementation quality after design and build steps are done.

## Use this skill when

- a SwiftUI screen is already implemented and needs review
- you want a second pass on state, navigation, or view structure
- accessibility or performance issues may be hidden in the code
- availability-gated APIs or modern SwiftUI patterns need verification

## Workflow

1. Review the highest-risk issue first.
2. Check state ownership and view composition.
3. Check navigation, presentation, and API availability.
4. Check accessibility and performance.
5. Return findings in severity order, then provide corrected guidance or code.

## What to output

Return:

- review findings ordered by severity
- the exact code region or pattern causing each issue
- concrete fixes or refactor suggestions
- a short residual-risk note if needed

## Rules

- Prefer facts from the code over general advice.
- If the code is fine, say so and note any remaining risk.
- Treat state duplication, unstable identity, and hidden side effects as real review issues.
- Verify accessibility and performance instead of assuming them.
- Keep iOS 26+ or other newer APIs gated unless the target explicitly supports them.

## References

- [`review-checklist.md`](references/review-checklist.md)
- [`state-ownership.md`](references/state-ownership.md)
- [`performance.md`](references/performance.md)
- [`accessibility.md`](references/accessibility.md)
