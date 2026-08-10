# LocationRequest

Configuring parameters in location requests.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-geoLocationManager-export interface LocationRequest--><!--Device-geoLocationManager-export interface LocationRequest-End-->

**System capability:** SystemCapability.Location.Location.Core

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## distanceInterval

```TypeScript
distanceInterval?: double
```

Location report distance interval.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LocationRequest-distanceInterval?: double--><!--Device-LocationRequest-distanceInterval?: double-End-->

**System capability:** SystemCapability.Location.Location.Core

## maxAccuracy

```TypeScript
maxAccuracy?: double
```

Accuracy requirements for reporting locations.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LocationRequest-maxAccuracy?: double--><!--Device-LocationRequest-maxAccuracy?: double-End-->

**System capability:** SystemCapability.Location.Location.Core

## priority

```TypeScript
priority?: LocationRequestPriority
```

Priority of the location request.

**Type:** [LocationRequestPriority](arkts-location-geolocation-locationrequestpriority-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LocationRequest-priority?: LocationRequestPriority--><!--Device-LocationRequest-priority?: LocationRequestPriority-End-->

**System capability:** SystemCapability.Location.Location.Core

## scenario

```TypeScript
scenario?: LocationRequestScenario
```

User scenario of the location request.

**Type:** [LocationRequestScenario](arkts-location-geolocationmanager-locationrequestscenario-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LocationRequest-scenario?: LocationRequestScenario--><!--Device-LocationRequest-scenario?: LocationRequestScenario-End-->

**System capability:** SystemCapability.Location.Location.Core

## timeInterval

```TypeScript
timeInterval?: int
```

Location report interval.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LocationRequest-timeInterval?: int--><!--Device-LocationRequest-timeInterval?: int-End-->

**System capability:** SystemCapability.Location.Location.Core

