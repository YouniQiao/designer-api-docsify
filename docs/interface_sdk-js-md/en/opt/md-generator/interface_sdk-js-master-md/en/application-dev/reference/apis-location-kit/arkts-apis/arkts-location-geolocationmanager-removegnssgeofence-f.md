# removeGnssGeofence

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## removeGnssGeofence

```TypeScript
function removeGnssGeofence(geofenceId: number): Promise<void>
```

Remove a geofence.

**Since:** 12

**Required permissions:** 
- API version 12 - 24: ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function removeGnssGeofence(geofenceId: int): Promise<void>--><!--Device-geoLocationManager-function removeGnssGeofence(geofenceId: int): Promise<void>-End-->

**System capability:** SystemCapability.Location.Location.Geofence

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| geofenceId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [3301602](../errorcode-geoLocationManager.md#3301602-failed-to-delete-a-geofence-due-to-an-incorrect-id) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) |

## Examples

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
import { BusinessError } from '@kit.BasicServicesKit';
// fenceId is obtained after geoLocationManager.addGnssGeofence is successfully executed.
let fenceId = 1;
try {
  geoLocationManager.removeGnssGeofence(fenceId).then(() => {
    console.info("removeGnssGeofence success fenceId:" + fenceId);
  }).catch((error: BusinessError) => {
    console.error("removeGnssGeofence: error=" + JSON.stringify(error));
  });
} catch (error) {
  console.error("removeGnssGeofence: error=" + JSON.stringify(error));
}
```
