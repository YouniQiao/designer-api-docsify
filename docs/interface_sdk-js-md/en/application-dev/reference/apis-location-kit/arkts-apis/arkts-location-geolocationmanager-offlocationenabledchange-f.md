# offLocationEnabledChange

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## offLocationEnabledChange

```TypeScript
function offLocationEnabledChange(callback?: Callback<boolean>): void
```

Unsubscribe location switch changed.

**Since:** 23

<!--Device-geoLocationManager-function offLocationEnabledChange(callback?: Callback<boolean>): void--><!--Device-geoLocationManager-function offLocationEnabledChange(callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | No | Indicates the callback for reporting the location switch status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call \\${geoLocationManager.offLocationEnabledChange} due to limited device capabilities. |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) | The location service is unavailable. |

