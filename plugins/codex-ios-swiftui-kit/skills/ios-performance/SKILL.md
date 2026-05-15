---
name: ios-performance
description: Use when a SwiftUI screen needs runtime tuning, scrolling improvement, better identity handling, or Instruments-based performance review.
---

# iOS Performance

## Overview

This skill looks for SwiftUI runtime costs that hurt scrolling, responsiveness, launch time, or memory use.

## Use this skill when

- a SwiftUI view feels sluggish or overdrawn
- a list or feed stutters while scrolling
- body recomputation seems too expensive
- image loading, animation, or state changes may be too heavy

## Workflow

1. Identify the likely hot path.
2. Check view identity and invalidation behavior.
3. Inspect list, scroll, and image-loading patterns.
4. Look for expensive modifiers, repeated work, and unnecessary redraws.
5. Recommend concrete measurements or code changes.

## What to output

Return:

- performance findings ordered by impact
- the likely cause of each issue
- specific SwiftUI changes to make
- whether Instruments or another measurement step is warranted

## Rules

- Treat unnecessary body churn as a real bug.
- Keep identity stable.
- Avoid expensive work in paths that render often.
- Measure before and after if the fix is non-obvious.
- Favor simple, predictable view structures over clever abstractions.
- If a performance issue is caused by layout or state shape, fix the shape first.

## References

- [`swiftui-performance.md`](references/swiftui-performance.md)
- [`instruments.md`](references/instruments.md)
