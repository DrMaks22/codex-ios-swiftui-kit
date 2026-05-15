# Skill Handoff Contracts

The bundle uses deterministic handoffs. Use these templates verbatim when passing between skills.

## Design Direction Handoff

### Inputs
- brief, user goals
- constraints: platform, screen density, language, brand tones
- existing style source (optional Figma/design tokens)

### Outputs
- distinct lane + mood
- token schema (color, type, spacing, shape, motion, surfaces)
- compact-width layout hierarchy and interaction rhythm
- accessibility constraints
- implementation handoff fields (containers, custom components, state implications, performance risks)

### Quality gates
- compact iPhone-first layout is explicit
- at least one non-color communication cue
- state implications are listed
- anti-slop score defined (see `anti-ai-slop.md`)

### Handoff template
```markdown
## Visual Direction
- Lane:
- Product mood:
- One-sentence concept:
- Distinctive detail:
## Tokens
| Role | Token | Light | Dark | SwiftUI mapping | Notes |
## Layout Hierarchy
1.
2.
3.
## Accessibility Constraints
- Dynamic Type:
- VoiceOver:
- Contrast:
- Touch targets:
## Implementation Handoff
- Primary screen pattern:
- Required SwiftUI containers:
- Required custom components:
- State implied by design:
- Performance risks:
```

## Architecture Handoff

### Inputs
- feature scope and screen graph
- ownership questions
- service or network boundaries

### Outputs
- responsibility map
- state ownership map
- dependency map with injection points
- boundary decision and test seams

### Quality gates
- one mutable owner per state
- dependencies injected at feature boundaries
- avoid global state as default choice

### Handoff template
```markdown
## Responsibility Map
| Responsibility | Owner | Notes |
## State Ownership
| State | Owner | Mutators | Readers | Lifetime |
## Boundary Decision
- Keep in feature:
- Extract to shared:
- Do not abstract yet:
```

## SwiftUI Implementation Handoff

### Inputs
- approved design direction
- architecture notes
- existing file context and constraints

### Outputs
- view-tree with container/sections/leafs
- state ownership table with owner/binding/lifetime
- explicit navigation and presentation model
- previewability impact and file-level patch plan

### Quality gates
- no invented components without a clear implementation plan
- navigation model has one clear mechanism
- safe-area, compact-width, dynamic type handled

### Handoff template
```markdown
## View Tree
- Container:
- Sections:
- Leaf components:
## State Ownership
| State | Owner | Binding? | Lifetime | Reason |
## Navigation and Presentation
- Navigation model:
- Routes:
- Sheets/covers/popovers:
- Dismissal behavior:
## Adaptive Layout
- Compact width:
- Dynamic Type:
- Safe areas:
## Implementation Plan
- Files to edit:
- New files:
- Preview/sample impact:
```

## Accessibility Handoff

### Inputs
- concrete SwiftUI code or screen context
- any previous design/accessibility assumptions

### Outputs
- impact-ordered issues with evidence
- exact code changes
- residual risks and deferred follow-up

### Quality gates
- critical production blockers are explicit
- no color-only state communication
- reduced-motion behavior is explicit

### Handoff template
```markdown
## Accessibility Findings
| Impact | Issue | Evidence | Fix |
## VoiceOver
- Reading order:
- Labels/values/hints/traits:
## Dynamic Type
- Risk areas:
- Layout fixes:
## Contrast and Non-color cues
- Contrast:
- State cues:
## Motion and Focus
- Reduced motion:
- Focus behavior:
## Handoff
- Required code changes:
- Residual risks:
```

## Performance Handoff

### Inputs
- implementation or modified SwiftUI view
- previous behavior assumptions
- expected scenario (scrolling, launch, media, animation)

### Outputs
- evidence-backed findings table
- hot path and identity/invalidation notes
- measurement plan when needed
- explicit follow-up

### Quality gates
- avoid speculative fixes
- each fix mapped to a symptom or signal
- measurement planned unless issue is obvious bug

### Handoff template
```markdown
## Performance Findings
| Severity | Symptom | Likely Cause | Evidence | Fix | Measurement Needed |
## Hot Path
- Frequently recomputed views:
- Scrolling/list risks:
- Image or formatting work:
## Measurement Plan
- Tool:
- Scenario:
- Expected signal:
## Handoff
- Code changes:
- Measurement follow-up:
```

## Expert Review Handoff

### Inputs
- completed implementation + audit results
- optional architecture notes

### Outputs
- severity-ranked findings
- patch order
- final verdict:
- what is already strong

### Quality gates
- no invented findings
- explicit residual risk labels
- release readiness is clear

### Handoff template
```markdown
## Review Verdict
Status: Pass / Pass with fixes / Needs revision
## Findings
### 1. [Severity] Title
- Region/pattern:
- Why it matters:
- Concrete fix:
- Residual risk:
## Patch Order
1. ...
## Final Handoff
- Must fix before shipping:
- Optional polish:
```
