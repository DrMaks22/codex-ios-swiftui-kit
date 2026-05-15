# Availability Review

Always check API usage against known deployment target.

- Identify minimum target first.
- Use `if #available` checks for newer SwiftUI APIs.
- Do not assume iOS 26+ APIs unless target supports them.
- Replace unknown APIs with fallback paths in reviews and findings.
- Include compile impact when API availability is wrong.
