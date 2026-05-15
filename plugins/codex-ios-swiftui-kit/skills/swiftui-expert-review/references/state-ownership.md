# State Ownership Review

Look for state that is stored in the wrong place or copied too widely.

## Red flags

- the same truth exists in multiple layers
- local UI state is hoisted without a reason
- bindings are passed deeper than needed
- presentation state is hidden behind side effects
