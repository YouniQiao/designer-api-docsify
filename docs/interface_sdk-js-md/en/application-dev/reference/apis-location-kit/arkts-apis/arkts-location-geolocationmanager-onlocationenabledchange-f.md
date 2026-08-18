# onLocationEnabledChange

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## onLocationEnabledChange

```TypeScript
function onLocationEnabledChange(callback: Callback<boolean>): void
```

Subscribe location switch changed.

**Since:** 23

<!--Device-geoLocationManager-function onLocationEnabledChange(callback: Callback<boolean>): void--><!--Device-geoLocationManager-function onLocationEnabledChange(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;boolean&gt; | Yes | Indicates the callback for reporting the location switch status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call \\${geoLocationManager.onLocationEnabledChange} due to limited device capabilities. |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) | The location service is unavailable. |

