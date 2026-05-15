# Dependency Injection

Inject what the feature needs, not the entire world.

## Guidance

- inject dependencies at feature boundary
- keep dependencies concrete and close to usage
- prefer simple protocols/closures only if testability improves
- avoid passing through unrelated views

## Examples

- Inject service at feature entry:

```swift
struct ConversationFeature: View {
  let service: ConversationService
}
```

- Use value/closure injection when lightweight:

```swift
struct ConversationRow: View {
  let onTap: () -> Void
}
```

- Avoid globals:
- Avoid globals
- Avoid protocol trees for one consumer

### What to avoid

- passing the same dependency through multiple unrelated views
- creating abstractions before shape is stable
- hiding side effects behind broad dependency contracts

## Common mistakes

- reaching into globals
- passing the same dependencies through many unrelated views
- creating abstractions before the shape of the feature is clear
- hiding side effects behind overly broad interfaces
