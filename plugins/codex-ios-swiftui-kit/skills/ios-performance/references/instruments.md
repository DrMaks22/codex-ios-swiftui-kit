# Instruments

Use Instruments when runtime symptoms are not obvious from source inspection.

## Good moments to measure

- scrolling feels uneven
- launch time is too slow
- memory climbs while navigating
- animations hitch when state changes

## Measurement table

| Symptom | Tool | Scenario | Expected signal | Likely code fix |
|---|---|---|---|---|
| Scroll hitch | Core Animation, Time Profiler | open list + fast scroll | spikes in body rendering and layout | cache data, stable ids, split heavy rows |
| Startup lag | Instruments launch + Time Profiler | cold start of target screen | excessive startup work in `init`/onAppear | defer non-critical initialization |
| Memory growth | Allocations + Leaks | repeated entry/exit | growing allocation footprint | optimize image decode and avoid repeated object churn |
| Transition stutter | Time Profiler + Core Animation | button trigger + animated route | delayed transitions and dropped frames | reduce animation scope and state fan-out |

## Reporting rule

- For each finding, include:
  - what to measure
  - what signal indicates risk
  - likely code change
