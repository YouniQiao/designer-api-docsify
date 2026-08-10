# removeGnssGeofence

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## removeGnssGeofence

```TypeScript
function removeGnssGeofence(geofenceId: int): Promise<void>
```

Remove a geofence.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 12 - 24: ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function removeGnssGeofence(geofenceId: int): Promise<void>--><!--Device-geoLocationManager-function removeGnssGeofence(geofenceId: int): Promise<void>-End-->

**System capability:** SystemCapability.Location.Location.Geofence

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| geofenceId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the ID of geofence. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 3301602 | Failed to delete a geofence due to an incorrect ID. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call \\${geoLocationManager.removeGnssGeofence} due to limited device capabilities. |
| 201 | Permission verification failed. The application does not have the permission required to call the API.<br>**Applicable version:** 12 - 24 |
| 3301000 | The location service is unavailable. |

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

