# Instruments

Use Instruments when the problem is not obvious from code review alone.

## Good moments to measure

- scrolling feels uneven
- launch time is too slow
- memory climbs while navigating
- animations hitch when state changes

## What to look for

- repeated work in frequently rendered views
- large diff churn from identity problems
- expensive allocations or image decoding
- too many updates caused by one state change

## Reporting rule

- mention what to measure
- mention what you expect to see
- mention what code change is likely to help
