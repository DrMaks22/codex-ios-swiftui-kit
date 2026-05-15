# Dependency Injection

Inject what the feature needs, not the entire world.

## Guidance

- pass dependencies in at the boundary where the feature starts
- keep concrete dependencies close to where they are used
- prefer simple protocol or value injection when it keeps the feature testable
- do not add indirection unless it makes a real change easier

## Common mistakes

- reaching into globals
- passing the same dependencies through many unrelated views
- creating abstractions before the shape of the feature is clear
- hiding side effects behind overly broad interfaces
