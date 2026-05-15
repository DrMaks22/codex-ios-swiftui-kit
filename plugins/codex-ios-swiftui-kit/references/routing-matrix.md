# Skill Routing Matrix

Use this matrix to pick the right skill first and avoid overlap.

| User/task signal | Use this skill | Do not use this skill when | Expected output |
|---|---|---|---|
| New screen design, visual tone, anti-generic feel, token strategy | `swiftui-design-direction` | The code is already implemented and stable | Design direction, token schema, hierarchy, accessibility constraints, implementation handoff |
| Feature shape is clear and needs view code | `ios-swiftui` | You are deciding ownership/boundaries first | SwiftUI structure, state ownership table, navigation model, file-level plan |
| Multi-screen, shared state, service layer, testability concern | `ios-architecture` | Single screen with local state only | Ownership map, module boundaries, dependency map |
| Need VoiceOver, Dynamic Type, color contrast, motion, target controls review | `ios-accessibility` | You only need a visual design critique | Impact-ordered accessibility findings and concrete edits |
| Suspected jank, list rebuilds, large body work, identity churn | `ios-performance` | Performance is obviously fine or out of scope | Evidence-based findings, hot-path map, measurement plan |
| Need final quality gate with severity and code actionability | `swiftui-expert-review` | You only need a draft review without final judgment | Severity-ranked findings, patch order, verdict |

## Trigger words and phrases

- `swiftui-design-direction`
  - "design direction", "visual style", "iPhone layout", "screen concept", "brand system", "anti-slop"
- `ios-swiftui`
  - "implement", "build SwiftUI", "navigation", "view tree", "animation", "sheet", "alert", "preview"
- `ios-architecture`
  - "feature architecture", "state ownership", "boundary", "module split", "DI", "dependency injection"
- `ios-accessibility`
  - "VoiceOver", "Dynamic Type", "touch target", "contrast", "reduced motion", "focus", "screen reader"
- `ios-performance`
  - "scroll", "jank", "lag", "identity", "body", "body churn", "instruments", "invalidation"
- `swiftui-expert-review`
  - "final review", "severity", "release gate", "pass/fix/revision", "must fix"

## Overlap rules

- `ios-swiftui` handles implementation mechanics: container structure, navigation primitives, presentation state, transitions, and animation wiring.
- `ios-architecture` handles feature-level ownership, dependency injection, boundaries, and test seams.
- `swiftui-expert-review` owns severity ranking, final verdict, and concrete fix ordering.

When signals overlap:

- If a request includes both implementation and ownership questions, run `ios-architecture` first only when the feature spans multiple screens/services/shared state.
- If a request includes implementation and accessibility concerns, run `ios-swiftui` then `ios-accessibility`.
- If a request includes performance concerns and implementation changes are already known, run `ios-performance` then `swiftui-expert-review`.
