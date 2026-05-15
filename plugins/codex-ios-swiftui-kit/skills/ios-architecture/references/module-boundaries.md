# Module Boundaries

Use boundaries to protect the parts of the feature that should not know about each other.

## Guidance

- group code by feature, not by random technical layer alone
- keep view-specific logic close to the view when it is not shared
- split out shared behavior only when it is truly shared
- use boundaries to reduce coupling and simplify review

## Common signs a boundary is wrong

- too many imports for a simple screen
- code that changes for unrelated reasons
- a feature that is impossible to understand without reading the whole app
- modules that expose more than the feature needs
