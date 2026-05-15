# State Ownership

State should have one owner and one clear mutation path.

## Guidance

- local UI state stays in the smallest possible view
- shared feature state belongs higher only when multiple children need it
- derived values should be computed, not stored twice
- presentation state should be explicit and easy to trace

## Questions to ask

- Who owns the truth?
- Who is allowed to mutate it?
- Which views should observe it?
- What breaks if this moves one level up or down?
