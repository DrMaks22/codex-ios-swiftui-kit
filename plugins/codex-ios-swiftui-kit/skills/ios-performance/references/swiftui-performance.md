# SwiftUI Performance

Use this checklist when a screen feels heavy or scrolls poorly.

## Evidence-based anti-patterns

- unstable identity in list loops
- repeated expensive formatting inside `body`
- eager image decoding or resampling in scroll cells
- broad state updates that invalidate unrelated views
- expensive modifiers applied to large subtrees

## SwiftUI examples

```swift
ForEach(messages, id: \.id) { message in
  MessageRow(message: message) // stable id
}
```

```swift
// Weak example: unstable identity
ForEach(messages, id: \.self) { message in
  MessageRow(message: message)
}
```

```swift
Text(Date(), format: .dateTime) // avoid in hot body
```

```swift
// Move formatting to model or cache
let formattedDate = message.formatDate()
Text(formattedDate)
```

## Decision rule

- Do not optimize without evidence unless bug is obvious (e.g., compile error or guaranteed state corruption).

## Good fixes

- move repeated work out of hot render paths
- keep identity stable
- split expensive subtrees into smaller views
- avoid rendering data that is not visible yet
- simplify state so it invalidates only the views that need to change
