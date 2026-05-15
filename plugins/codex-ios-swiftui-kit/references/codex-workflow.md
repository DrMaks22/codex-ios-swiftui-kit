# Codex iOS SwiftUI Workflow

Use one stage at a time and keep the handoff contract explicit.

## Greenfield iPhone screen

1. `swiftui-design-direction`
   - Output: lane, tokens, hierarchy, implementation constraints.
2. `ios-architecture` (only if it spans screens, shared services, or shared state).
   - Output: ownership map + explicit boundaries + injection plan.
3. `ios-swiftui`
   - Output: file-aware SwiftUI view tree, navigation model, previews impact.
4. `ios-accessibility` (required for production)
   - Output: impact-ordered fixes and exact edits.
5. `ios-performance` (always considered, deep only when needed)
   - Output: evidence, severity, measurement need.
6. `swiftui-expert-review`
   - Output: final verdict and patch order.

## Existing screen review workflow

1. `swiftui-expert-review` for a fast baseline reading.
2. `ios-accessibility` if there are usability or AT risks.
3. `ios-performance` for hotspots and identity/invalidation issues.
4. `ios-swiftui` for concrete fixes.
5. Re-run `swiftui-expert-review` if implementation or state architecture changes.

## Figma-driven workflow

Use this flow only when source context exists in Figma and user explicitly asks.

1. `swiftui-design-direction` with `figma-bridge` extraction contract.
2. Optional `ios-architecture` if feature spans multiple screens/services.
3. `ios-swiftui` implementation.
4. `ios-accessibility`, `ios-performance`, `swiftui-expert-review` as in greenfield flow.

## Feature architecture workflow

Use before implementation when all apply:

- multi-screen feature
- service-backed state
- shared action state across 3+ views
- repeated cross-feature coupling

Output of this workflow is a concrete, minimal boundary plan and dependency map.

## Final review workflow

Before shipping, run `swiftui-expert-review` and require:

- severity-ranked findings
- exact region/pattern references
- concrete fixes
- verdict:
  - Pass / Pass with fixes / Needs revision

## Conditional notes

- `ios-architecture`:
  - Run **before implementation** when feature complexity justifies it.
  - Run **after implementation** only when refactor/audit is requested.
- `ios-performance`:
  - Always include basic perf awareness.
  - Run deep mode when there is feed/list scrolling, rich media, expensive rendering, launch concern, or animation hitch reports.
- `ios-accessibility`:
  - Required for any production UI.
- Always route results through the handoff contracts in `handoff-contract.md`.
