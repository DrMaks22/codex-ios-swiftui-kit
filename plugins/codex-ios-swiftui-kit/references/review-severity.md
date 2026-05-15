# SwiftUI Review Severity

Use this when scoring review findings in `swiftui-expert-review`.

## Severity definitions

### Critical
- User-critical failure.
- Build/regression blockers.
- Missing accessibility support that blocks primary flows.

### High
- Functional correctness is impaired but recoverable with fix.
- Significant accessibility or performance regressions with real user impact.

### Medium
- Correctness remains but quality, maintainability, or polish is materially reduced.
- Likely user-visible friction.

### Low
- Style, readability, micro-optimization, or refactor suggestions with low user impact.

## Example mapping

| Signal | Severity | Why |
|---|---|---|
| Compile break | Critical | Cannot build / impossible to ship |
| Unavailable API without target gates | Critical | Crash or compile fail on supported target |
| Broken primary user flow | Critical | Core task cannot complete |
| Inaccessible primary action | High | Users cannot complete main action with VoiceOver |
| Broken presentation lifecycle | High | Screens/flows get stuck or dismiss incorrectly |
| Duplicated source of truth without visible drift | Medium | Desync risk and maintainability cost |
| Duplicated source of truth with user-visible drift | High | Incorrect UI state or navigation/data mismatch |
| Dynamic Type failure in primary list or labels | High | Loss of content and likely interaction errors |
| Performance issue with clear evidence | High if visible | e.g. clear list hitches, main-thread churn |
| Visual polish issue only | Low | Improvement quality, not functional breakage |

## Verdict policy

- **Pass**
  - No blocking issues remain.
  - Non-blocking suggestions may still be noted.
- **Pass with fixes**
  - Minor but concrete fixes are required before shipping.
- **Needs revision**
  - One or more high/critical findings require remediation before release.

## Review output rule

- Rank by severity first, then by user impact.
- Include exact code region/pattern and concrete fix.
- Do not invent issues when the code region is already correct.
