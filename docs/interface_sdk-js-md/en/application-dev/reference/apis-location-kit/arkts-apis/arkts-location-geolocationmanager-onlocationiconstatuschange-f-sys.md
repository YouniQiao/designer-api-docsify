# onLocationIconStatusChange (System API)

## Modules to Import

```TypeScript
import { geoLocationManager } from 'geoLocationManager';
```

## onLocationIconStatusChange

```TypeScript
function onLocationIconStatusChange(callback: Callback<LocationIconStatus>): void
```

Subscribe location icon status changed.

**Since:** 23

<!--Device-geoLocationManager-function onLocationIconStatusChange(callback: Callback<LocationIconStatus>): void--><!--Device-geoLocationManager-function onLocationIconStatusChange(callback: Callback<LocationIconStatus>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[LocationIconStatus](arkts-location-geolocationmanager-locationiconstatus-e-sys.md)&gt; | Yes | Indicates the callback for reporting the location icon status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call \\${geoLocationManager.onLocationIconStatusChange} due to limited device capabilities. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) | The location service is unavailable. |

