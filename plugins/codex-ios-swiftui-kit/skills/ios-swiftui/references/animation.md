# SwiftUI Animation

Use animation to explain change, not to decorate the screen.

## Guidance

- Animate only transitions the user can perceive as meaningful.
- Keep spring values conservative unless the product requires a stronger feel.
- Respect reduced motion.
- Prefer explicit transitions for enter/exit states.
- Keep animation responsibility near the state change that triggers it.

## Reduced-motion fallback

```swift
@Environment(\.accessibilityReduceMotion) private var reduceMotion

var body: some View {
  if reduceMotion {
    content
  } else {
    content.transition(.move(edge: .bottom).combined(with: .opacity))
  }
}
```

```swift
let duration = reduceMotion ? 0.0 : 0.25
```

## Common mistakes

- animating every property change
- making motion compete with content
- using motion where spacing or hierarchy would be clearer
- adding motion without user value

## Rule

- every animation should explain a state change
