---
name: ios-performance
description: Use for SwiftUI performance tuning, hotspot mapping, identity stability, and instrumentation-based verification.
---

# iOS SwiftUI Performance Audit

Use this skill when runtime behavior threatens smooth scrolling, responsiveness, or launch quality.

## Use this skill when

- a SwiftUI view stutters or feels heavy
- list/feed behavior is expensive
- body churn is visible or suspected
- image formatting, animation, or state invalidation is suspicious

## Do not use this skill when

- no implementation context exists
- only visual polish is requested without runtime concern

## Codex behavior

- Keep findings evidence-based.
- Avoid speculative optimization unless behavior is an obvious bug.
- Each finding must include measurable evidence, severity, and likely fix.
- Provide a short measurement plan where signal is uncertain.

## Required output

## Performance Findings
| Severity | Symptom | Likely Cause | Evidence | Fix | Measurement Needed |
|---|---|---|---|---|---|
## Hot Path
- Frequently recomputed views:
- Scrolling/list areas:
- Image or formatting work:
- Animation/layout risks:
## Identity and Invalidation
- Stable identity:
- Broad invalidation:
- State shape risks:
## Measurement Plan
- Tool:
- Scenario:
- Expected signal:
- Before/after comparison:
## Handoff
- Code changes:
- Measurement follow-up:

## Rules

- Treat unnecessary body churn as a bug.
- Keep identity stable across list and scroll contexts.
- Remove expensive formatting from hot render paths.
- If layout/state shape causes most churn, optimize state structure first.
- Do not optimize without evidence unless defect is obvious.

## References

- [`swiftui-performance.md`](references/swiftui-performance.md)
- [`instruments.md`](references/instruments.md)
- [`performance-finding-format.md`](references/performance-finding-format.md)
- [`handoff-contract.md`](../../references/handoff-contract.md)
