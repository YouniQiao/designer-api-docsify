# isPoiServiceSupported

## Modules to Import

```TypeScript
import { geoLocationManager } from 'geoLocationManager';
```

## isPoiServiceSupported

```TypeScript
function isPoiServiceSupported(): boolean
```

Check whether the POI service is supported.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-geoLocationManager-function isPoiServiceSupported(): boolean--><!--Device-geoLocationManager-function isPoiServiceSupported(): boolean-End-->

**System capability:** SystemCapability.Location.Location.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

let poiServiceState = geoLocationManager.isPoiServiceSupported();
console.info("poiServiceState:" + poiServiceState);
```

