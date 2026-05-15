# SwiftUI iPhone Layout Patterns

Choose one pattern first, then simplify to compact-width structure.

## Conversational assistant
- Use when:
  - chat, operator, or request/response work
- Layout grammar:
  - anchored composer, reverse chronological stream, context-aware affordance bar
- Avoid:
  - fixed multi-column history, heavy card borders, status noise above message flow

## Calm productivity dashboard
- Use when:
  - daily status, key metrics, quick triage
- Layout grammar:
  - hero insight first, compact list or stack, two-level actions
- Avoid:
  - dense grids, inconsistent spacing, oversized secondary cards

## Dense pro utility
- Use when:
  - task-heavy workflows, tables, filtered lists, quick actions
- Layout grammar:
  - strong primary section, sticky controls, compact scannable rows
- Avoid:
  - decorative depth, weak typography contrast, ambiguous row hierarchy

## Editorial detail
- Use when:
  - narrative content, review, deep read
- Layout grammar:
  - title block, structured metadata, body typography scale, minimal control intrusion
- Avoid:
  - competing gradients, oversized action density, tiny caption-only guidance

## Control surface
- Use when:
  - configuration, permissions, settings, toggles
- Layout grammar:
  - labeled sections, direct controls, inline explanatory subtitle
- Avoid:
  - mixed control density in one section, unlabeled switches, vague labels

## Object detail / action sheet
- Use when:
  - deep object drill-down with secondary actions
- Layout grammar:
  - object header, key info stack, one primary action row, optional confirmatory sheet
- Avoid:
  - burying critical action in menu, stacked modals, excessive nested actions

## iPhone guardrails

- Prefer vertical rhythm over horizontal noise.
- Keep touch targets generous.
- Parent owns arrangement; leafs own local detail.
- If text density rises, convert decoration into whitespace and structure.
