# Figma Bridge (Optional)

Do not use Figma unless a Figma file, frame, or explicit request is provided.

### Rule

- Do not use Figma for generic design tasks.
- Use Figma only when user explicitly asks or provides a valid source selection.
- Keep the plugin useful without Figma.

## What we use Figma for

- token extraction from selected frames/components
- frame structure and spacing/radius/type notes
- design-to-code mapping where a source exists
- component and asset dependency list

## Extraction contract

- frame name
- dimensions
- token candidates
- component names
- spacing/radius/type observations
- asset dependencies
- what could not be extracted
- SwiftUI translation notes

## Preferred setup

- official endpoint: `https://mcp.figma.com/mcp`
- keep `.mcp.json` at root of plugin and treat it as optional integration

## Not suitable without Figma

- new feature design with no source file
- tasks that are implementation-only
- review/audit tasks without source requirement
