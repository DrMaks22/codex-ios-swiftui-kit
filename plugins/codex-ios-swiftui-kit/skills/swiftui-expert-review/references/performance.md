# Performance Review (Review only)

- body work still heavy in frequently rendered views
- unstable IDs or unstable `ForEach` identity
- broad state invalidation
- image decoding or formatting in visible hot paths

## Severity mapping

- High: clear evidence of jank/hitch in primary flow
- Medium: avoidable heavy work with simple refactor
- Low: micro-optimization after functional risks are closed

## Reference

- detailed optimization patterns: `../../../ios-performance/references/swiftui-performance.md`
