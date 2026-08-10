# offSatelliteStatusChange

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## offSatelliteStatusChange

```TypeScript
function offSatelliteStatusChange(callback?: Callback<SatelliteStatusInfo>): void
```

Unsubscribe satellite status changed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function offSatelliteStatusChange(callback?: Callback<SatelliteStatusInfo>): void--><!--Device-geoLocationManager-function offSatelliteStatusChange(callback?: Callback<SatelliteStatusInfo>): void-End-->

**System capability:** SystemCapability.Location.Location.Gnss

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SatelliteStatusInfo&gt; | No | Indicates the callback for reporting the satellite status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call \\${geoLocationManager.offSatelliteStatusChange} due to limited device capabilities. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

