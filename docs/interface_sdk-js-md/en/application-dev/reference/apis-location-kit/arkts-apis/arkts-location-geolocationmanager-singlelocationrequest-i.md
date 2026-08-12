# SingleLocationRequest

Configuring parameters in single location requests.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-geoLocationManager-export interface SingleLocationRequest--><!--Device-geoLocationManager-export interface SingleLocationRequest-End-->

**System capability:** SystemCapability.Location.Location.Core

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## locatingPriority

```TypeScript
locatingPriority: LocatingPriority
```

Priority of the location request.

**Type:** [LocatingPriority](arkts-location-geolocationmanager-locatingpriority-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SingleLocationRequest-locatingPriority: LocatingPriority--><!--Device-SingleLocationRequest-locatingPriority: LocatingPriority-End-->

**System capability:** SystemCapability.Location.Location.Core

## locatingTimeoutMs

```TypeScript
locatingTimeoutMs: int
```

Timeout of a single location request, in milliseconds.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SingleLocationRequest-locatingTimeoutMs: int--><!--Device-SingleLocationRequest-locatingTimeoutMs: int-End-->

**System capability:** SystemCapability.Location.Location.Core

## needPoi

```TypeScript
needPoi?: boolean
```

Indicates whether to obtain POI information near the current location.

**Type:** boolean

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-SingleLocationRequest-needPoi?: boolean--><!--Device-SingleLocationRequest-needPoi?: boolean-End-->

**System capability:** SystemCapability.Location.Location.Core

