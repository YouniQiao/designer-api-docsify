# isPoiServiceSupported

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## isPoiServiceSupported

```TypeScript
function isPoiServiceSupported(): boolean
```

Check whether the POI service is supported.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-geoLocationManager-function isPoiServiceSupported(): boolean--><!--Device-geoLocationManager-function isPoiServiceSupported(): boolean-End-->

**System capability:** SystemCapability.Location.Location.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

let poiServiceState = geoLocationManager.isPoiServiceSupported();
console.info("poiServiceState:" + poiServiceState);
```
