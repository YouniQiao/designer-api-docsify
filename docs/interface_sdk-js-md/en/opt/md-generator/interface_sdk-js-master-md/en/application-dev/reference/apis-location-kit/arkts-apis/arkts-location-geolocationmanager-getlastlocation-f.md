# getLastLocation

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## getLastLocation

```TypeScript
function getLastLocation(): Location
```

Obtain last known location.

**Since:** 9

**Required permissions:** ohos.permission.APPROXIMATELY_LOCATION

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-geoLocationManager-function getLastLocation(): Location--><!--Device-geoLocationManager-function getLastLocation(): Location-End-->

**System capability:** SystemCapability.Location.Location.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Location](arkts-location-geolocationmanager-location-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [3301200](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-location-kit/errorcode-geoLocationManager.md#3301200-failed-to-obtain-the-positioning-result) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [3301000](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-location-kit/errorcode-geoLocationManager.md#3301000-location-service-unavailable) |
| [3301100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-location-kit/errorcode-geoLocationManager.md#3301100-positioning-failed-because-the-location-switch-is-turned-off) |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  let location = geoLocationManager.getLastLocation();
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```
