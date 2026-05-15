# State Ownership Review (Review only)

Focus on review red flags, not teaching.

- same mutable value duplicated across views
- local UI state hoisted without a reason
- hidden presentation flow state
- unstable owner for shared mutable values

## Severity mapping

- High: duplicated source of truth with user-visible drift
- Medium: over-specified state shape slowing maintenance
- Low: naming and organization risks

## Reference

- shared contract: `../../../references/swiftui-state-ownership.md`
