# Feature Boundaries

Use these checks before creating or removing feature boundaries.

- Create a feature boundary when:
  - 3+ screens share behavior/state
  - feature logic is reused in production tasks
  - test/data fixtures become difficult to share
- Do not create one when:
  - there is only one screen and one owner
  - behavior is temporary and highly specific

## Signals of bad boundary

- Comprehension drops when reading one file.
- Coupling leaks into unrelated screens.
- Feature has one mutable state owner but 3+ abstractions.

## Boundary quality checks

- Testability: can core logic be unit tested?
- Comprehension: does structure reduce or increase cognitive load?
- Locality: can contributors find the entrypoint quickly?
