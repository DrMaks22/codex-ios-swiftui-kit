# Performance Finding Format

## Finding template

| Severity | Symptom | Likely Cause | Evidence | Fix | Measurement Needed |
|---|---|---|---|---|---|

### Good finding

- Symptom: "List row body recomputes all content on each scroll event"
- Likely Cause: state object mutated at list parent level
- Evidence: diff shows all row IDs re-evaluated in 16ms+ frames
- Fix: move immutable payload into row-level structs and stable `id`
- Measurement Needed: Instruments scroll trace before and after

### Bad finding

- "Use a lighter color." (no evidence, no severity, no code target)
