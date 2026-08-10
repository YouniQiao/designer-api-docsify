# getLocationIconStatus (System API)

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## getLocationIconStatus

```TypeScript
function getLocationIconStatus(): LocationIconStatus
```

Get location icon status.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-geoLocationManager-function getLocationIconStatus(): LocationIconStatus--><!--Device-geoLocationManager-function getLocationIconStatus(): LocationIconStatus-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [LocationIconStatus](arkts-location-geolocationmanager-locationiconstatus-e-sys.md) | The location icon status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Failed to call \\${geoLocationManager.getLocationIconStatus} due to limited device capabilities. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 3301000 | The location service is unavailable. |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  let iconStatus = geoLocationManager.getLocationIconStatus();
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```

