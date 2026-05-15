# Codex iOS SwiftUI Kit

A Codex-native workflow bundle for iPhone-first SwiftUI UX/UI work.

## What this plugin is

This plugin turns SwiftUI UI work into a staged system:

- `swiftui-design-direction` creates visual direction and semantic tokens.
- `ios-architecture` defines feature boundaries and state ownership before or after implementation.
- `ios-swiftui` implements views, navigation, and interaction in SwiftUI.
- `ios-accessibility` runs an accessibility pass for production UI.
- `ios-performance` runs runtime checks with evidence.
- `swiftui-expert-review` runs final quality review with severity-ranked findings.

## What this plugin is not

- A simulator or build automation plugin.
- An automatic converter from screenshots.
- A replacement for design tools.
- An iOS project template.

The plugin does not require Figma, and install scripts are intentionally excluded from runtime usage.

## Install into Codex

From repository root:

```bash
python3 scripts/install_codex_ios_swiftui_kit.py --scope global
```

Global install does:

- copies the bundle to `~/plugins/codex-ios-swiftui-kit`
- merges the plugin entry into `~/.agents/plugins/marketplace.json`
- validates the installed plugin structure

To install into a workspace:

```bash
python3 scripts/install_codex_ios_swiftui_kit.py --scope local --workspace-root /path/to/workspace
```

Useful options:

```bash
python3 scripts/install_codex_ios_swiftui_kit.py --dry-run
python3 scripts/install_codex_ios_swiftui_kit.py --force
python3 scripts/install_codex_ios_swiftui_kit.py --link
python3 scripts/install_codex_ios_swiftui_kit.py --target-root /custom/plugins
python3 scripts/install_codex_ios_swiftui_kit.py --marketplace-path /custom/.agents/plugins/marketplace.json
```

## When to use which skill

- Start with `swiftui-design-direction` for new UX, unclear layouts, visual tone, or anti-slop guidance.
- Run `ios-architecture` before implementation for multi-screen features, shared state, or service-backed flows.
- Run `ios-swiftui` when implementation details are known and you need SwiftUI code.
- Run `ios-accessibility` for every production UI before shipping.
- Run `ios-performance` for scroll-heavy, media-heavy, animation-heavy, launch, or hitches workflows.
- Finish with `swiftui-expert-review` for severity-ranked go/no-go output and patch sequencing.

## Recommended workflow recipes

### 1) Greenfield premium iPhone screen

```text
Use swiftui-design-direction -> ios-swiftui -> ios-accessibility -> ios-performance -> swiftui-expert-review
```

### 2) Existing SwiftUI screen feels generic

```text
Use swiftui-expert-review -> swiftui-design-direction (if visual quality is low) -> ios-swiftui -> ios-accessibility -> swiftui-expert-review
```

### 3) Existing SwiftUI code needs full review

```text
Use swiftui-expert-review -> ios-accessibility -> ios-performance -> swiftui-expert-review
```

### 4) Multi-screen feature architecture

```text
Use ios-architecture -> ios-swiftui -> ios-accessibility -> ios-performance -> swiftui-expert-review
```

### 5) Figma to SwiftUI

```text
Use swiftui-design-direction (with figma bridge) -> ios-swiftui -> ios-accessibility -> ios-performance -> swiftui-expert-review
```

Use Figma only if you explicitly provide a frame selection, URL, or explicit Figma task.

## Example prompts

- Design direction:
  - `Use the Codex iOS SwiftUI Kit to create a premium iPhone-first design direction for ...`
- Implementation:
  - `Use the Codex iOS SwiftUI Kit to implement this approved direction in SwiftUI and keep the file layout clean.`
- Architecture:
  - `Use the Codex iOS SwiftUI Kit to define the feature ownership map and boundaries for this flow.`
- Accessibility:
  - `Use the Codex iOS SwiftUI Kit to audit this SwiftUI screen for VoiceOver, Dynamic Type, and reduced-motion safety.`
- Performance:
  - `Use the Codex iOS SwiftUI Kit to produce evidence-based SwiftUI performance findings with a measurement plan.`
- Expert review:
  - `Use the Codex iOS SwiftUI Kit to review these changed SwiftUI files and return severity-ranked fixes.`

## Notes for humans and Codex

- Runtime workflow should read `plugins/codex-ios-swiftui-kit/references/codex-workflow.md` first when you want staged execution.
- Figma is optional and explicit.
- Do not depend on install script behavior during day-to-day runtime usage.
- Plugin layout in this repository:
  - `plugins/codex-ios-swiftui-kit/.codex-plugin/plugin.json`
  - `plugins/codex-ios-swiftui-kit/skills/*`
  - `plugins/codex-ios-swiftui-kit/references/*`
  - `scripts/install_codex_ios_swiftui_kit.py` (install-time only)
