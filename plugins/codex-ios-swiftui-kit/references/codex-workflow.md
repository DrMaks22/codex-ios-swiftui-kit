# Codex iOS SwiftUI Kit Workflow

This bundle is intentionally layered so Codex can pick the right skill instead of dumping every concern into one prompt.

## Operating order

| Order | Skill | Use it for | Typical output |
|---|---|---|---|
| 1 | `swiftui-design-direction` | Visual direction, tone, layout rhythm, tokens | Design lane, token set, layout notes |
| 2 | `ios-swiftui` | Turning the design into SwiftUI | View hierarchy, state model, navigation choices |
| 3 | `ios-accessibility` | Accessibility pass | VoiceOver, Dynamic Type, contrast, motion fixes |
| 4 | `ios-performance` | Runtime cost pass | Hotspots, identity issues, list and scroll fixes |
| 5 | `ios-architecture` | Boundary and ownership pass | State ownership, DI, module boundaries |
| 6 | `swiftui-expert-review` | Final review and cleanup | Findings, corrections, refactor guidance |

## How to use the bundle

- Start with design direction when the screen still feels vague or generic.
- Jump straight to `ios-swiftui` when the shape is already known and you need correct SwiftUI structure.
- Run accessibility and performance as separate passes; they should not be hidden inside the implementation prompt.
- Use architecture review when the feature spans multiple views, models, or services.
- Use the expert review skill last, after the design and implementation are both stable.

## Bundle rules

- Keep one skill active at a time unless a task clearly needs two.
- Prefer iPhone-first composition and compact-width decisions.
- Treat Figma as an optional source of truth, not a required dependency.
- If the output starts sounding generic, return to `swiftui-design-direction` before polishing code.
