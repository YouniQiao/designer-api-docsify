# getLocationIconStatus (System API)

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## getLocationIconStatus

```TypeScript
function getLocationIconStatus(): LocationIconStatus
```

Get location icon status.

**Since:** 23

**Deprecated since:** -1

<!--Device-geoLocationManager-function getLocationIconStatus(): LocationIconStatus--><!--Device-geoLocationManager-function getLocationIconStatus(): LocationIconStatus-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [LocationIconStatus](arkts-location-geolocationmanager-locationiconstatus-e-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  let iconStatus = geoLocationManager.getLocationIconStatus();
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```
