# CurrentLocationRequest

Configuring parameters in current location requests.

**Since:** 23

<!--Device-geoLocationManager-export interface CurrentLocationRequest--><!--Device-geoLocationManager-export interface CurrentLocationRequest-End-->

**System capability:** SystemCapability.Location.Location.Core

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## maxAccuracy

```TypeScript
maxAccuracy?: double
```

Accuracy requirements for reporting locations.

**Type:** double

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CurrentLocationRequest-maxAccuracy?: double--><!--Device-CurrentLocationRequest-maxAccuracy?: double-End-->

**System capability:** SystemCapability.Location.Location.Core

## priority

```TypeScript
priority?: LocationRequestPriority
```

Priority of the location request.

**Type:** LocationRequestPriority

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CurrentLocationRequest-priority?: LocationRequestPriority--><!--Device-CurrentLocationRequest-priority?: LocationRequestPriority-End-->

**System capability:** SystemCapability.Location.Location.Core

## scenario

```TypeScript
scenario?: LocationRequestScenario
```

User scenario of the location request.

**Type:** LocationRequestScenario

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CurrentLocationRequest-scenario?: LocationRequestScenario--><!--Device-CurrentLocationRequest-scenario?: LocationRequestScenario-End-->

**System capability:** SystemCapability.Location.Location.Core

## timeoutMs

```TypeScript
timeoutMs?: int
```

Timeout interval of a single location request.

**Type:** int

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CurrentLocationRequest-timeoutMs?: int--><!--Device-CurrentLocationRequest-timeoutMs?: int-End-->

**System capability:** SystemCapability.Location.Location.Core

