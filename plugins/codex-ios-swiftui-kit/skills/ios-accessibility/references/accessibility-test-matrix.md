# Accessibility Test Matrix

Use this matrix for required production checks.

| Area | What to test |
|---|---|
| VoiceOver reading order | Navigate in source order and ensure it matches visual order |
| labels/values/hints/traits | Validate semantics on all meaningful controls |
| Dynamic Type | Verify XL and XXL with long localized strings |
| Increased contrast | Test semantic states and icon/text contrast |
| Reduced motion | Ensure motion-sensitive transitions degrade safely |
| color-only state | Confirm every state has non-color cue |
| touch target size | Verify primary and secondary targets are at least 44x44 |
| focus behavior | Validate focus changes on appearance/disappearance of sheets |
