# getActiveGeoFences

## Modules to Import

```TypeScript
```

## getActiveGeoFences

```TypeScript
function getActiveGeoFences(): Promise<Map<number, Geofence>>
```

Get all active fences.

**Since:** 23

**Required permissions:** ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function getActiveGeoFences(): Promise<Map<int, Geofence>>--><!--Device-geoLocationManager-function getActiveGeoFences(): Promise<Map<int, Geofence>>-End-->

**System capability:** SystemCapability.Location.Location.Geofence

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Map & lt;number, Geofence & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |

**Examples**

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
