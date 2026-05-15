# Previewability

Keep previews useful, fast, and representative.

- Keep previews minimal and deterministic.
- Use fixtures for every model shown in preview.
- Avoid network/service calls in preview providers.
- Include separate preview variants for:
  - long content
  - empty states
  - loading states when relevant
- Add dark mode and Dynamic Type variants when visual hierarchy depends on size or contrast.
- Do not break existing previews when introducing new containers or route models.

### Preview checklist

- Can the view render with mock data only?
- Do previews respect compact width?
- Do they reveal layout breaks at larger text sizes?
- Are sheets and presentation states reachable in preview?
- Is no external service required at build time?
