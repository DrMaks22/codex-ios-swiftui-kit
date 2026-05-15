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

- installs globally into `~/plugins/codex-ios-swiftui-kit`
- updates `~/.agents/plugins/marketplace.json`
- validates the installed plugin structure

## Codex Self-Install

If you are using Codex, you can ask it to install this plugin directly from this README.
Use the command that matches where you want the plugin available.

Global install:

```bash
python3 scripts/install_codex_ios_swiftui_kit.py --scope global
```

Local install into a specific workspace:

```bash
python3 scripts/install_codex_ios_swiftui_kit.py --scope local --workspace-root /path/to/your/workspace
```

If you omit `--workspace-root`, the installer uses the current git top-level directory, or the current directory when no git repo is present.

Suggested prompt for Codex:

```text
Install the Codex iOS SwiftUI Kit for me.
Use global scope if I want it in my personal Codex profile.
Use local scope if I want it in a specific workspace.
When using local scope, install into the workspace root I provide and update that workspace's marketplace.
```

## Useful options

```bash
python3 scripts/install_codex_ios_swiftui_kit.py --scope local --workspace-root /path/to/workspace
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
- supports both global and workspace-local installs

## Repo layout

- `plugins/codex-ios-swiftui-kit/` - the plugin bundle
- `scripts/install_codex_ios_swiftui_kit.py` - local installer
- `docs/superpowers/plans/2026-05-15-codex-ios-swiftui-kit.md` - implementation plan
