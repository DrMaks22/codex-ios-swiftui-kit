# Codex iOS SwiftUI Kit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build one Codex-native plugin bundle for premium iOS SwiftUI UX/UI work that combines visual direction, native iOS implementation guidance, and SwiftUI review into a single maintainable package.

**Architecture:** A repo-local Codex plugin lives under `plugins/codex-ios-swiftui-kit/` and is discovered through `.agents/plugins/marketplace.json`. The plugin is intentionally split into multiple small skills instead of one large skill: one design-direction skill, four iOS foundation skills, and one SwiftUI review skill. Shared rules and upstream attribution live in compact reference files. Figma support remains optional and is wired only through a separate MCP config so the core bundle still works when Figma is absent.

**Tech Stack:** Codex plugin manifest, Agent Skills format, `agents/openai.yaml`, optional Figma MCP config, JSON/YAML validation, SwiftUI/iOS reference material, curated upstream skill content.

---

### Task 1: Scaffold the Codex plugin shell and marketplace entry

**Files:**
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/.codex-plugin/plugin.json`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/.agents/plugins/marketplace.json`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/references/codex-workflow.md`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/references/upstream-attribution.md`

- [ ] **Step 1: Create the plugin scaffold**

Run:

```bash
python3 /Users/lma/.codex/skills/.system/plugin-creator/scripts/create_basic_plugin.py codex-ios-swiftui-kit \
  --path /Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins \
  --with-marketplace \
  --with-skills \
  --with-assets
```

Expected:
- `plugins/codex-ios-swiftui-kit/.codex-plugin/plugin.json` exists
- `.agents/plugins/marketplace.json` exists with one local entry for `codex-ios-swiftui-kit`

- [ ] **Step 2: Replace the scaffold metadata with Codex-specific values**

Set the plugin metadata to make the bundle feel like one product instead of a generic prompt pack:
- plugin name: `codex-ios-swiftui-kit`
- display name: `Codex iOS SwiftUI Kit`
- short description: design, build, and review premium iOS SwiftUI UI
- interface default prompts: one design prompt, one implementation prompt, one review prompt
- category: `Productivity`
- skills path: `./skills/`
- keep the plugin manifest lean and avoid any Claude-only conventions

Example `defaultPrompt` shape:

```json
[
  "Design a premium iPhone SwiftUI screen with clear hierarchy and accessible spacing.",
  "Implement this design in SwiftUI with modern navigation and adaptive layout.",
  "Review my SwiftUI view for state, accessibility, and performance issues."
]
```

- [ ] **Step 3: Record the bundle workflow and attribution**

Write two short references:
- `codex-workflow.md` explains the bundle's internal ordering: design direction -> implementation -> accessibility/performance/architecture -> expert review
- `upstream-attribution.md` records the source repos and license notes for the imported skill material

Expected:
- the bundle has one clear operating model
- the imported material stays traceable and maintainable

- [ ] **Step 4: Validate the scaffold**

Run:

```bash
jq '.name, .interface.displayName, .skills' /Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/.codex-plugin/plugin.json
jq '.name, .plugins[0].name, .plugins[0].source.path' /Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/.agents/plugins/marketplace.json
```

Expected:
- plugin name and marketplace entry match
- the bundle is discoverable as a local Codex plugin

### Task 2: Build the design-direction skill

**Files:**
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/swiftui-design-direction/SKILL.md`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/swiftui-design-direction/agents/openai.yaml`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/swiftui-design-direction/references/anti-ai-slop.md`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/swiftui-design-direction/references/layout-patterns.md`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/swiftui-design-direction/references/typography-color.md`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/swiftui-design-direction/references/brand-assets.md`

- [ ] **Step 1: Scaffold the skill directory**

Run:

```bash
python3 /Users/lma/.codex/skills/.system/skill-creator/scripts/init_skill.py swiftui-design-direction \
  --path /Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills \
  --resources references,assets \
  --interface display_name="SwiftUI Design Direction" \
  --interface short_description="Premium iOS visual direction" \
  --interface default_prompt="Use \$swiftui-design-direction to design a distinctive iPhone SwiftUI screen."
```

Expected:
- `SKILL.md` exists with valid frontmatter
- `agents/openai.yaml` exists with skill UI metadata
- `references/` and `assets/` directories exist

- [ ] **Step 2: Replace the template with a tight design skill**

The skill should do three things only:
- choose or refine a visual direction
- produce usable design tokens and layout guidance
- reject generic AI slop patterns

The skill body should be short and opinionated:
- explain when to use it
- encode the anti-slop rules
- keep visual decisions grounded in iPhone-first SwiftUI
- avoid copying the full upstream README into the skill body

- [ ] **Step 3: Move the long-form guidance into references**

Split the long guidance into small files:
- `anti-ai-slop.md` for rules and anti-patterns
- `layout-patterns.md` for common iPhone screen structures
- `typography-color.md` for type scale, contrast, and palette logic
- `brand-assets.md` for brand integration and asset handling

Expected:
- `SKILL.md` stays compact
- the reference files carry the detailed material from the upstream design skill

- [ ] **Step 4: Validate the skill metadata**

Run:

```bash
python3 /Users/lma/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/swiftui-design-direction
```

Expected:
- frontmatter is valid
- `agents/openai.yaml` is consistent with the skill name and trigger language

### Task 3: Build the iOS foundation skill set

**Files:**
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/ios-swiftui/SKILL.md`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/ios-swiftui/agents/openai.yaml`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/ios-swiftui/references/layout.md`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/ios-swiftui/references/state.md`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/ios-swiftui/references/navigation.md`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/ios-swiftui/references/animation.md`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/ios-accessibility/SKILL.md`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/ios-accessibility/agents/openai.yaml`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/ios-accessibility/references/voiceover.md`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/ios-accessibility/references/dynamic-type.md`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/ios-accessibility/references/contrast-motion.md`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/ios-performance/SKILL.md`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/ios-performance/agents/openai.yaml`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/ios-performance/references/swiftui-performance.md`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/ios-performance/references/instruments.md`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/ios-architecture/SKILL.md`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/ios-architecture/agents/openai.yaml`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/ios-architecture/references/state-ownership.md`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/ios-architecture/references/module-boundaries.md`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/ios-architecture/references/dependency-injection.md`

- [ ] **Step 1: Scaffold the four skills as separate folders**

Run the initializer once per skill so each concern gets its own trigger and reference depth:

```bash
python3 /Users/lma/.codex/skills/.system/skill-creator/scripts/init_skill.py ios-swiftui \
  --path /Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills \
  --resources references \
  --interface display_name="iOS SwiftUI" \
  --interface short_description="SwiftUI layout and composition" \
  --interface default_prompt="Use \$ios-swiftui to implement a polished iPhone UI in SwiftUI."

python3 /Users/lma/.codex/skills/.system/skill-creator/scripts/init_skill.py ios-accessibility \
  --path /Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills \
  --resources references \
  --interface display_name="iOS Accessibility" \
  --interface short_description="VoiceOver, Dynamic Type, contrast" \
  --interface default_prompt="Use \$ios-accessibility to audit a SwiftUI screen for accessibility."

python3 /Users/lma/.codex/skills/.system/skill-creator/scripts/init_skill.py ios-performance \
  --path /Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills \
  --resources references \
  --interface display_name="iOS Performance" \
  --interface short_description="SwiftUI runtime and Instruments" \
  --interface default_prompt="Use \$ios-performance to optimize a SwiftUI view for runtime cost."

python3 /Users/lma/.codex/skills/.system/skill-creator/scripts/init_skill.py ios-architecture \
  --path /Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills \
  --resources references \
  --interface display_name="iOS Architecture" \
  --interface short_description="State ownership and module boundaries" \
  --interface default_prompt="Use \$ios-architecture to structure a SwiftUI feature cleanly."
```

Expected:
- each skill is a separate folder with its own `SKILL.md` and `agents/openai.yaml`
- the skill names are small, stable, and easy for Codex to trigger from context

- [ ] **Step 2: Write the `ios-swiftui` skill**

This skill should cover:
- layout systems
- state ownership
- navigation
- sheets, alerts, and overlays
- animation patterns

Keep it focused on implementation, not design taste. The design taste belongs in `swiftui-design-direction`.

- [ ] **Step 3: Write the `ios-accessibility` skill**

This skill should cover:
- VoiceOver labels and rotor-friendly order
- Dynamic Type and text scaling
- contrast and color safety
- reduced motion and focus behavior
- accessible tap targets

It should read like a checklist Codex can apply during implementation and review.

- [ ] **Step 4: Write the `ios-performance` skill**

This skill should cover:
- SwiftUI body cost and view identity
- scrolling and list performance
- Instruments usage
- memory and launch-time pressure
- animation overhead

The output should favor concrete fixes over generic advice.

- [ ] **Step 5: Write the `ios-architecture` skill**

This skill should cover:
- state ownership
- feature boundaries
- dependency injection
- module boundaries
- when to introduce abstraction versus keep the feature local

Keep architecture guidance practical so the plugin does not drift into over-engineering.

- [ ] **Step 6: Validate each skill independently**

Run the validator once per skill:

```bash
python3 /Users/lma/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/ios-swiftui
python3 /Users/lma/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/ios-accessibility
python3 /Users/lma/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/ios-performance
python3 /Users/lma/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/ios-architecture
```

Expected:
- every skill has valid frontmatter and metadata
- no skill description overlaps enough to cause noisy triggering

### Task 4: Build the SwiftUI expert review skill

**Files:**
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/swiftui-expert-review/SKILL.md`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/swiftui-expert-review/agents/openai.yaml`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/swiftui-expert-review/references/review-checklist.md`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/swiftui-expert-review/references/state-ownership.md`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/swiftui-expert-review/references/performance.md`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/swiftui-expert-review/references/accessibility.md`

- [ ] **Step 1: Scaffold the review skill**

Run:

```bash
python3 /Users/lma/.codex/skills/.system/skill-creator/scripts/init_skill.py swiftui-expert-review \
  --path /Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills \
  --resources references \
  --interface display_name="SwiftUI Expert Review" \
  --interface short_description="Review and refine SwiftUI code" \
  --interface default_prompt="Use \$swiftui-expert-review to review SwiftUI code for correctness and polish."
```

Expected:
- the review skill is clearly distinct from the design and implementation skills
- the prompt asks for review, refactor, and correction instead of new design direction

- [ ] **Step 2: Encode the review contract**

The skill should enforce:
- correct property-wrapper choice
- predictable state ownership
- modern APIs where appropriate
- accessibility as a review gate, not an afterthought
- performance checks on expensive views and lists

This is where the bundle gets its final quality pass.

- [ ] **Step 3: Keep iOS 26+ features gated**

If the review skill mentions Liquid Glass or other iOS 26+ APIs, it must treat them as optional and availability-gated rather than as the default path for every SwiftUI view.

This prevents the plugin from overfitting to the newest APIs when the product target is older.

- [ ] **Step 4: Validate the review skill**

Run:

```bash
python3 /Users/lma/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/skills/swiftui-expert-review
```

Expected:
- the skill reads as a reviewer, not a second design skill

### Task 5: Add the optional Figma bridge behind a separate config

**Files:**
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/.mcp.json`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/references/figma-bridge.md`

- [ ] **Step 1: Keep Figma optional**

The plugin should work without any Figma setup. Only add MCP config when the project actually has Figma files or a design system that should be read as source of truth.

Expected:
- the core bundle is still fully usable when no Figma account or file is present

- [ ] **Step 2: Use the official Figma server only**

Wire the official Figma MCP endpoint and avoid third-party bridge packages for the core bundle. The bridge note should say that Figma is for extracting variables, components, and layout data, not for replacing the plugin’s own design workflow.

Expected:
- the plugin gets design context from Figma when needed
- the bundle remains safe and simple by default

- [ ] **Step 3: Document the bridge usage**

`figma-bridge.md` should explain:
- when to use Figma context
- when to keep working from the local design system
- why the bridge is optional and not part of the core plugin identity

### Task 6: Polish the bundle and prove it works with real prompts

**Files:**
- Modify: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/.codex-plugin/plugin.json`
- Modify: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/.agents/plugins/marketplace.json`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/assets/icon.png`
- Create: `/Users/lma/Documents/Codex/2026-05-15/ux-ui-ios-swiftui-ios-swiftui/plugins/codex-ios-swiftui-kit/assets/logo.png`

- [ ] **Step 1: Create polished visual assets**

Make the plugin icon and logo look like a product, not a placeholder:
- restrained brand color
- simple layout or SwiftUI motif
- no generic rainbow gradient treatment

Expected:
- the plugin card is recognizable in Codex UI

- [ ] **Step 2: Tighten the plugin descriptions**

Refine the plugin-level description and each skill’s short description so they are all easy to scan and do not overlap too much.

Expected:
- the bundle reads as one coherent product
- the skills remain individually discoverable

- [ ] **Step 3: Run prompt-based acceptance checks**

Use the following prompt set and confirm the right skill family is chosen:
- a design-direction prompt should trigger `swiftui-design-direction`
- an implementation prompt should trigger `ios-swiftui`
- an accessibility prompt should trigger `ios-accessibility`
- a performance prompt should trigger `ios-performance`
- an architecture prompt should trigger `ios-architecture`
- a review prompt should trigger `swiftui-expert-review`

Expected:
- the plugin routes cleanly with minimal cross-trigger noise
- the output style matches the role of the skill

- [ ] **Step 4: Trim any overgrown content**

If any `SKILL.md` starts getting too large, move details into a reference file instead of expanding the skill body.

Expected:
- the bundle stays maintainable
- the context load stays lean

### Acceptance Criteria

- One Codex plugin exists at `plugins/codex-ios-swiftui-kit/`
- The marketplace file exposes the plugin as a local Codex bundle
- The bundle contains one design-direction skill, four iOS foundation skills, and one SwiftUI review skill
- The plugin works without Figma, with Figma only as an optional bridge
- Each skill has a short, explicit trigger and a short default prompt in `agents/openai.yaml`
- The long guidance lives in `references/`, not in bloated `SKILL.md` files
- The bundle’s prompts move in the correct order: design -> implementation -> accessibility/performance/architecture -> review
