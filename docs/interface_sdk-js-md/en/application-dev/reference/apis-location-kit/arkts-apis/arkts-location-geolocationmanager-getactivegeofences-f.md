# getActiveGeoFences

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## getActiveGeoFences

```TypeScript
function getActiveGeoFences(): Promise<Map<int, Geofence>>
```

Get all active fences.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function getActiveGeoFences(): Promise<Map<int, Geofence>>--><!--Device-geoLocationManager-function getActiveGeoFences(): Promise<Map<int, Geofence>>-End-->

**System capability:** SystemCapability.Location.Location.Geofence

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Map&lt;int, Geofence&gt;&gt; | The promise returned by the function. The key of the map represents the fence ID. The value of the map represents the detailed information of the fence. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call \\${geoLocationManager.getActiveGeoFences} due to limited device capabilities. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  geoLocationManager.getActiveGeoFences().then((res) => {
    if (res) {
      console.info("fence num:" + res.size);
      for (const item of res) {
        console.info("data=" + JSON.stringify(item));
      }
    }
  })
    .catch((error: BusinessError) => {
      console.error('promise, getActiveGeoFences: error=' + JSON.stringify(error));
    });
} catch (error) {
  console.error("getActiveGeoFences: errCode" + error.code + ", errMessage" + error.message);
}
```

