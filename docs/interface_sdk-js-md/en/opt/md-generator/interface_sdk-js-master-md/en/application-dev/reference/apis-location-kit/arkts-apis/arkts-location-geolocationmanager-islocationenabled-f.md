# isLocationEnabled

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## isLocationEnabled

```TypeScript
function isLocationEnabled(): boolean
```

Obtain current location switch status.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-geoLocationManager-function isLocationEnabled(): boolean--><!--Device-geoLocationManager-function isLocationEnabled(): boolean-End-->

**System capability:** SystemCapability.Location.Location.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  let locationEnabled = geoLocationManager.isLocationEnabled();
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```
