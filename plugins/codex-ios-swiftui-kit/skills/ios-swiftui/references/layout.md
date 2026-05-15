# SwiftUI Layout

Start from a minimal view tree and keep hierarchy obvious.

## Parent/child contract

- Parent owns broad arrangement.
- Child owns local detail.
- A single parent should declare section order and cross-section spacing.
- Avoid building visual intent with ad-hoc frame hacks.

## Compact width and previewability

- Prefer vertical stacks and single column for compact width.
- Never assume landscape or regular size at first draft.
- Ensure preview uses realistic strings and dynamic type scale.

## View-tree thinking

- Container stack
  - section block
    - row/block
    - control
    - secondary info

If this hierarchy needs manual `frame` alignment at each level, it is likely the wrong tree.

## Tiny example

1. `NavigationStack`
2. `ScrollView`
3. `VStack(spacing: 16)`
4. `HeaderView`, `PrimaryList`, `ComposerBar`
5. `FooterAction`

## Good output

- concise layout summary
- main containers in order
- spacing and alignment decisions
- adaptive behavior for compact width and long text
