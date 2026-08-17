# CachedGnssLocationsRequest

Parameters for requesting to report cache location information.

**Since:** 23

<!--Device-geoLocationManager-export interface CachedGnssLocationsRequest--><!--Device-geoLocationManager-export interface CachedGnssLocationsRequest-End-->

**System capability:** SystemCapability.Location.Location.Gnss

## Modules to Import

```TypeScript
import { geoLocationManager } from 'geoLocationManager';
```

## reportingPeriodSec

```TypeScript
reportingPeriodSec: int
```

GNSS cache location report period.

**Type:** int

**Since:** 23

<!--Device-CachedGnssLocationsRequest-reportingPeriodSec: int--><!--Device-CachedGnssLocationsRequest-reportingPeriodSec: int-End-->

**System capability:** SystemCapability.Location.Location.Gnss

## wakeUpCacheQueueFull

```TypeScript
wakeUpCacheQueueFull: boolean
```

Indicates whether to wake up the listener when the GNSS cache location queue is full.

**Type:** boolean

**Since:** 23

<!--Device-CachedGnssLocationsRequest-wakeUpCacheQueueFull: boolean--><!--Device-CachedGnssLocationsRequest-wakeUpCacheQueueFull: boolean-End-->

**System capability:** SystemCapability.Location.Location.Gnss

