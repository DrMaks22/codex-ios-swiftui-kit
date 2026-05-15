# Typography and Color

Treat typography and color as semantic systems.

## Token naming examples

- `font-size/title`, `font-size/body`, `font-weight/primary`, `line-height/relaxed`
- `color/foregroundPrimary`, `color/foregroundSecondary`, `color/surface`, `color/neutralDivider`
- `color/accent`, `color/success`, `color/warning`, `color/error`
- `radius/std`, `spacing/screenSide`, `spacing/sectionGap`, `motion/standard`

## Semantic roles

- `foregroundPrimary` for main task and title
- `foregroundSecondary` for metadata and helper text
- `surface` for containers
- `surfaceElevated` for subtle elevation states
- `destructive`, `success`, `warning` for state and feedback
- `actionPrimary` for the main button

## SwiftUI mapping examples

- Font:
  - `Text(title).font(.system(.title3, weight: .semibold))`
  - `Text(body).font(.body)`
- Color:
  - `foregroundStyle(.primary)` mapped from `foregroundPrimary`
  - `foregroundStyle(Color.secondary)` mapped from `foregroundSecondary`
  - `background(Material.regularMaterial)` only when readability stays stable
- Spacing:
  - `padding(.horizontal, spacing.screenSide)`
  - `spacing(sectionGap)` in stacks
- Radius and surfaces:
  - `RoundedRectangle(cornerRadius: radius.std)`

## Practical checks

- One hierarchy by type size and weight, not by color alone.
- One neutral palette for most surfaces.
- Color is secondary to structure, not the structure itself.
- Screen should remain understandable in grayscale.
