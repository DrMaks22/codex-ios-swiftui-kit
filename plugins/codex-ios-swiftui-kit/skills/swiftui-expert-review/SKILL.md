---
name: swiftui-expert-review
description: Use for final SwiftUI quality review, severity-ranked defects, and concrete fixes across state, architecture, accessibility, performance, navigation, and availability.
---

# iOS SwiftUI Quality Review

Use this as the final review gate after implementation and targeted audits.

## Use this skill when

- a SwiftUI feature is implemented and needs final release-quality review
- you need severity-ranked findings and clear patch order
- architecture, accessibility, and performance handoffs are already present

## Do not use this skill when

- design direction has not been agreed and implementation is still exploratory
- the request is only for a single-file micro-optimization without context

## Codex behavior

- do not invent findings; only report what code/path evidence supports
- prioritize findings by severity and user impact
- use severity mapping from `../../references/review-severity.md`
- include concrete region/pattern-level fixes and residual risk

## Required output

## Review Verdict
Status: Pass / Pass with fixes / Needs revision
## Findings
### 1. [Severity] Title
- Region / pattern:
- Why it matters:
- Concrete fix:
- Residual risk:
## What Is Already Strong
- ...
## Patch Order
1. ...
2. ...
3. ...
## Final Handoff
- Must fix before shipping:
- Optional polish:
- Follow-up checks:

## Rules

- Keep iOS 26+ API usage behind availability checks.
- Keep severity visible in order.
- Mention what is already strong before broad recommendations.
- Only report issues with evidence and fix path.

## References

- [`review-checklist.md`](references/review-checklist.md)
- [`state-ownership.md`](references/state-ownership.md)
- [`performance.md`](references/performance.md)
- [`accessibility.md`](references/accessibility.md)
- [`availability.md`](references/availability.md)
- [`../../references/review-severity.md`](../../references/review-severity.md)
- [`handoff-contract.md`](../../references/handoff-contract.md)
