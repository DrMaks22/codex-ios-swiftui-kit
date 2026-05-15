# SwiftUI Layout

Use the smallest layout structure that can express the screen clearly.

## Guidance

- Prefer `VStack`, `HStack`, `ZStack`, `ScrollView`, `List`, and `Grid` before custom layout code.
- Keep spacing intentional and consistent.
- Use containers to group related content and preserve hierarchy.
- Let the parent own the large-scale arrangement and the child own local details.
- Respect safe area, compact width, and long localized strings.

## Common mistakes

- nesting too many container views
- using frame tweaks to compensate for missing hierarchy
- building a layout that only works at one size
- letting every card, section, and row look equally important

## Good output

- one-sentence layout summary
- main containers in order
- notes on spacing, alignment, and adaptive behavior
