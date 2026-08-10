# CachedGnssLocationsRequest

Parameters for requesting to report cache location information.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-geoLocationManager-export interface CachedGnssLocationsRequest--><!--Device-geoLocationManager-export interface CachedGnssLocationsRequest-End-->

**系统能力：** SystemCapability.Location.Location.Gnss

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## reportingPeriodSec

```TypeScript
reportingPeriodSec: int
```

GNSS cache location report period.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-CachedGnssLocationsRequest-reportingPeriodSec: int--><!--Device-CachedGnssLocationsRequest-reportingPeriodSec: int-End-->

**系统能力：** SystemCapability.Location.Location.Gnss

## wakeUpCacheQueueFull

```TypeScript
wakeUpCacheQueueFull: boolean
```

Indicates whether to wake up the listener when the GNSS cache location queue is full.

**类型：** boolean

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-CachedGnssLocationsRequest-wakeUpCacheQueueFull: boolean--><!--Device-CachedGnssLocationsRequest-wakeUpCacheQueueFull: boolean-End-->

**系统能力：** SystemCapability.Location.Location.Gnss

