# SwiftUI State

State should live where it is owned and no lower.

## Guidance

- Use local state for local interactions.
- Pass in data for read-only display whenever possible.
- Use observation and bindings for shared editable state.
- Avoid duplicating the same truth in multiple layers.
- Prefer a single source of truth for selection, loading, filtering, and presentation state.

## Review questions

- Who owns this data?
- Which view should react to changes?
- Does the state need to survive navigation or dismissal?
- Is this value derived or truly independent?

## Common mistakes

- copying the same model into several views
- storing derived values as separate mutable state
- making the parent own everything just because it is convenient
- mixing transient UI state with durable feature state
