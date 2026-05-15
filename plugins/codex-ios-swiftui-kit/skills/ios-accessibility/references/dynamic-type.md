# Dynamic Type

Dynamic Type should be treated as a layout constraint, not a nice-to-have.

## Layout techniques

- Avoid fixed heights on containers with text.
- Use flexible stacks and `lineLimit(nil)` for meaningful copy.
- Prefer `minimumScaleFactor` only as a last option.
- Test with increased content sizes and long strings.
- Use `layoutPriority` to protect primary actions.

## Risky patterns

- Fixed width/height text containers.
- `lineLimit(1)` on critical labels.
- `frame(height:)` where content can grow.
- Icon-only buttons without accessible labels at large sizes.

## Common examples

```swift
Text(title)
  .lineLimit(1) // risk if title can grow

Text(title)
  .lineLimit(nil) // safer for scaling text
```

```swift
HStack(spacing: 8) {
  Text("Status")
  Text(status).font(.subheadline)
}
.fixedSize(horizontal: false, vertical: true)
```

## Common mistakes

- clipping text with fixed frames
- shrinking text to force it to fit
- making large text break the primary action path
