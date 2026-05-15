# Codex iOS SwiftUI Kit

Codex-native plugin bundle for premium iOS SwiftUI UX/UI work.

It packages:

- `swiftui-design-direction` for visual direction and design tokens
- `ios-swiftui` for layout, navigation, state, and animation implementation
- `ios-accessibility` for VoiceOver, Dynamic Type, contrast, and motion
- `ios-performance` for runtime and Instruments-minded optimization
- `ios-architecture` for state ownership and module boundaries
- `swiftui-expert-review` for final SwiftUI quality review

## Install into Codex

From this repository root:

```bash
python3 scripts/install_codex_ios_swiftui_kit.py
```

By default, the installer:

- copies the bundle to `~/plugins/codex-ios-swiftui-kit`
- updates `~/.agents/plugins/marketplace.json`
- validates the installed plugin structure

## Useful options

```bash
python3 scripts/install_codex_ios_swiftui_kit.py --dry-run
python3 scripts/install_codex_ios_swiftui_kit.py --force
python3 scripts/install_codex_ios_swiftui_kit.py --link
python3 scripts/install_codex_ios_swiftui_kit.py --target-root /custom/plugins
python3 scripts/install_codex_ios_swiftui_kit.py --marketplace-path /custom/.agents/plugins/marketplace.json
```

## What the installer changes

- installs the plugin bundle into the Codex-local plugin directory
- merges the plugin entry into the local marketplace without removing existing plugins
- keeps the plugin layout aligned with Codex plugin creator conventions

## Repo layout

- `plugins/codex-ios-swiftui-kit/` - the plugin bundle
- `scripts/install_codex_ios_swiftui_kit.py` - local installer
- `docs/superpowers/plans/2026-05-15-codex-ios-swiftui-kit.md` - implementation plan
