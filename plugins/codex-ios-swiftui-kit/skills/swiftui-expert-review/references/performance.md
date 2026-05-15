# Performance Review

Look for patterns that make SwiftUI redraw too much or do too much work.

## Red flags

- heavy work in `body`
- unstable identity in lists or repeated content
- unnecessary redraws from broad state changes
- expensive image, formatting, or parsing work on the hot path
