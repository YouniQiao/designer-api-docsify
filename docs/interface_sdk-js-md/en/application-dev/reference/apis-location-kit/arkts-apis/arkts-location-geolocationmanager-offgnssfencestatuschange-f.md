# offGnssFenceStatusChange

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## offGnssFenceStatusChange

```TypeScript
function offGnssFenceStatusChange(request: GeofenceRequest, want: WantAgent): void
```

Remove a geofence and unsubscribe geofence status changed.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Deprecated since:** -1

<!--Device-geoLocationManager-function offGnssFenceStatusChange(request: GeofenceRequest, want: WantAgent): void--><!--Device-geoLocationManager-function offGnssFenceStatusChange(request: GeofenceRequest, want: WantAgent): void-End-->

**System capability:** SystemCapability.Location.Location.Geofence

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| request | GeofenceRequest | Yes | Indicates the Geofence configuration parameters. |
| want | [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-depr-t.md) | Yes | Indicates which ability to start when the geofence event is triggered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call \\${geoLocationManager.offGnssFenceStatusChange} due to limited device capabilities. |
| [3301600](../errorcode-geoLocationManager.md#3301600-geofence-operation-failed) | Failed to operate the geofence. |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) | The location service is unavailable. |
| [3301100](../errorcode-geoLocationManager.md#3301100-positioning-failed-because-the-location-switch-is-turned-off) | The location switch is off. |

