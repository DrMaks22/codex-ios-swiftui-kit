# Contrast and Motion

Good accessibility means the screen is still legible and calm when contrast and motion preferences change.

## Guidance

- keep text and icon contrast strong enough for real environments
- use semantic colors for success, warning, and destructive states
- reduce motion when the user prefers it
- avoid blur-heavy or translucent surfaces that harm legibility
- make focus states obvious

## Non-color cues

- add iconography and text labels for critical states
- use shape, position, or weight to signal change
- avoid color-only indicators for selected, locked, error, and success states

## Common mistakes

- low-contrast gray on gray UI
- state communicated only through animation
- decorative motion that fights comprehension
- using blur as a substitute for hierarchy

## Reduced motion example

```swift
@Environment(\.accessibilityReduceMotion) private var reduceMotion

var body: some View {
  HStack {
    if isBusy {
      ProgressView()
        .scaleEffect(reduceMotion ? 1 : 1.2)
      Text("Loading")
    }
  }
}
```
