# Figma Bridge

Use Figma only when the project has an actual Figma file or design system that should remain the source of truth.

## Preferred setup

- Use the remote Figma MCP server first.
- The official remote endpoint is `https://mcp.figma.com/mcp`.
- Keep the bridge separate from the core bundle so the plugin still works without Figma.

## What to use it for

- extracting design tokens from a real file
- reading layout structure from a frame or selection
- aligning SwiftUI implementation to an existing design system
- verifying that brand assets and components match the file

## What not to use it for

- replacing the bundle's own design-direction skill
- guessing at design intent when no Figma file exists
- turning every UI task into a Figma task

## Rule

Treat Figma as a source of truth for existing design context, then let the bundle translate that context into SwiftUI.
