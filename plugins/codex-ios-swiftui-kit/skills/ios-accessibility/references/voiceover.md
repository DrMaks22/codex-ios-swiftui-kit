# VoiceOver

Use VoiceOver labels to make the screen understandable without looking at it.

Use concise and explicit semantics on real controls.

## Guidance

- Give every meaningful control a label, and add a hint only when the action is not obvious.
- Keep the reading order aligned with the visual hierarchy.
- Use values to convey state, progress, and selection when needed.
- Use traits only when they improve discovery.
- Prefer one clear semantic control over several decorative tap targets.

## Common mistakes

- unlabeled icon buttons
- reading order that jumps around the screen
- hints that repeat the label instead of adding value
- custom controls that are visually clear but semantically empty

## SwiftUI examples

```swift
Button("Send") {
  send()
}
.accessibilityLabel("Send message")
.accessibilityHint("Double tap to submit")
```

```swift
Toggle("Enable notifications", isOn: $isEnabled)
  .accessibilityValue(isEnabled ? "On" : "Off")
```

```swift
Text("5 messages").accessibilityLabel("5 unread messages")
```

## Custom control warning

- If a control is custom-drawn, provide the correct `.accessibilityElement`, label, value, and traits.
- Do not rely on visual-only semantics.
