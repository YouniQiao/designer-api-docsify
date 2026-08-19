# onSatelliteStatusChange

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## onSatelliteStatusChange

```TypeScript
function onSatelliteStatusChange(callback: Callback<SatelliteStatusInfo>): void
```

Subscribe satellite status changed.

**Since:** 23

**Required permissions:** ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function onSatelliteStatusChange(callback: Callback<SatelliteStatusInfo>): void--><!--Device-geoLocationManager-function onSatelliteStatusChange(callback: Callback<SatelliteStatusInfo>): void-End-->

**System capability:** SystemCapability.Location.Location.Gnss

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SatelliteStatusInfo&gt; | Yes | Indicates the callback for reporting the satellite status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call \\${geoLocationManager.onSatelliteStatusChange} due to limited device capabilities. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) | The location service is unavailable. |
| [3301100](../errorcode-geoLocationManager.md#3301100-positioning-failed-because-the-location-switch-is-turned-off) | The location switch is off. |

