# ContinuousLocationRequest

Configuring parameters in continuous location requests.

**Since:** 23

**Deprecated since:** -1

<!--Device-geoLocationManager-export interface ContinuousLocationRequest--><!--Device-geoLocationManager-export interface ContinuousLocationRequest-End-->

**System capability:** SystemCapability.Location.Location.Core

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## interval

```TypeScript
interval: number
```

Location report interval, in seconds.

**Type:** number

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ContinuousLocationRequest-interval: int--><!--Device-ContinuousLocationRequest-interval: int-End-->

**System capability:** SystemCapability.Location.Location.Core

## locationScenario

```TypeScript
locationScenario: UserActivityScenario | PowerConsumptionScenario
```

Location scenario. You can select a user activity scenario or power consumption scenario.

**Type:** [UserActivityScenario](arkts-location-geolocationmanager-useractivityscenario-e.md) \| [PowerConsumptionScenario](arkts-location-geolocationmanager-powerconsumptionscenario-e.md)

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ContinuousLocationRequest-locationScenario: UserActivityScenario | PowerConsumptionScenario--><!--Device-ContinuousLocationRequest-locationScenario: UserActivityScenario | PowerConsumptionScenario-End-->

**System capability:** SystemCapability.Location.Location.Core

## needPoi

```TypeScript
needPoi?: boolean
```

Indicates whether to obtain POI information near the current location.

**Type:** boolean

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ContinuousLocationRequest-needPoi?: boolean--><!--Device-ContinuousLocationRequest-needPoi?: boolean-End-->

**System capability:** SystemCapability.Location.Location.Core
