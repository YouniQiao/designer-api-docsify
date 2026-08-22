# offLocationError

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## offLocationError

```TypeScript
function offLocationError(callback?: Callback<LocationError>): void
```

Unsubscribe continuous location error changed.

**Since:** 23

**Required permissions:** ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function offLocationError(callback?: Callback<LocationError>): void--><!--Device-geoLocationManager-function offLocationError(callback?: Callback<LocationError>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[LocationError](arkts-location-geolocationmanager-locationerror-e.md)&gt; | No | Indicates the callback for reporting the continuous location error. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call \\${geoLocationManager.offLocationError} due to limited device capabilities. |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) | The location service is unavailable. |

