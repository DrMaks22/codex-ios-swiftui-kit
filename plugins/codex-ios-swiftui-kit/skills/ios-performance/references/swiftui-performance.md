# SwiftUI Performance

Use this checklist when a screen feels heavy or scrolls poorly.

## Common issues

- unstable view identity
- too much work in `body`
- large lists that rebuild more than necessary
- expensive image or format work on the hot path
- state changes that invalidate more of the tree than needed

## Good fixes

- move repeated work out of hot render paths
- keep identity stable
- split expensive subtrees into smaller views
- avoid rendering data that is not visible yet
- simplify state so it invalidates only the views that need to change
