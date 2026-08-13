# isGeocoderAvailable

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## isGeocoderAvailable

```TypeScript
function isGeocoderAvailable(): boolean
```

Obtain geocoding service status.

**Since:** 23

**Deprecated since:** -1

<!--Device-geoLocationManager-function isGeocoderAvailable(): boolean--><!--Device-geoLocationManager-function isGeocoderAvailable(): boolean-End-->

**System capability:** SystemCapability.Location.Location.Geocoder

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  let isAvailable = geoLocationManager.isGeocoderAvailable();
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```
