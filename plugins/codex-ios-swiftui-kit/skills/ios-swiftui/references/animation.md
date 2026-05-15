# SwiftUI Animation

Use animation to explain change, not to decorate the screen.

## Guidance

- Animate only the state transitions that help the user understand what changed.
- Keep spring values conservative unless the product needs a stronger feel.
- Respect reduced motion.
- Prefer explicit transitions when content enters or leaves.
- Keep animation responsibility close to the state change that causes it.

## Common mistakes

- animating every property change
- making motion compete with content
- using motion where spacing or hierarchy would be clearer
- forgetting accessibility preferences
