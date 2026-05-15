# SwiftUI Navigation

Navigation should be explicit, predictable, and easy to review.

## Guidance

- Use `NavigationStack` for most modern flows.
- Keep route data simple and inspectable.
- Model sheets, full-screen covers, popovers, and alerts as deliberate presentation state.
- Prefer one navigation style per feature unless there is a strong reason to mix them.
- Make deep links and selection state visible in the data model when needed.

## Common mistakes

- hiding navigation inside helper methods
- using multiple overlapping presentation mechanisms
- making the back path unclear
- coupling screen identity too tightly to transient view state
