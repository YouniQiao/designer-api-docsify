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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-geoLocationManager-function isGeocoderAvailable(): boolean--><!--Device-geoLocationManager-function isGeocoderAvailable(): boolean-End-->

**System capability:** SystemCapability.Location.Location.Geocoder

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Failed to call \\${geoLocationManager.isGeocoderAvailable} due to limited device capabilities. |
| [3301000](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-location-kit/errorcode-geoLocationManager.md#3301000-location-service-unavailable) | The location service is unavailable. |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  let isAvailable = geoLocationManager.isGeocoderAvailable();
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```

