# offGnssFenceStatusChange

## offGnssFenceStatusChange

```TypeScript
function offGnssFenceStatusChange(request: GeofenceRequest, want: WantAgent): void
```

Remove a geofence and unsubscribe geofence status changed.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

<!--Device-geoLocationManager-function offGnssFenceStatusChange(request: GeofenceRequest, want: WantAgent): void--><!--Device-geoLocationManager-function offGnssFenceStatusChange(request: GeofenceRequest, want: WantAgent): void-End-->

**System capability:** SystemCapability.Location.Location.Geofence

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| request | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates the Geofence configuration parameters. |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates which ability to start when the geofence event is triggered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported.Failed to call \_\_\_ESCAPED\_DOLLAR\_\_\_{geoLocationManager.offGnssFenceStatusChange} due to limited device capabilities. |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) | The location service is unavailable. |
| [3301100](../errorcode-geoLocationManager.md#3301100-positioning-failed-because-the-location-switch-is-turned-off) | The location switch is off. |
| [3301600](../errorcode-geoLocationManager.md#3301600-geofence-operation-failed) | Failed to operate the geofence. |

