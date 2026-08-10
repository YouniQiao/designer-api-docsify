# offLocationChange

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## offLocationChange

```TypeScript
function offLocationChange(callback?: Callback<Location>): void
```

Unsubscribe location changed.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn since version 26.0.0; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 23 - 24: ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function offLocationChange(callback?: Callback<Location>): void--><!--Device-geoLocationManager-function offLocationChange(callback?: Callback<Location>): void-End-->

**System capability:** 
- API version 23 and later: SystemCapability.Location.Location.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Location&gt; | No | Indicates the callback for reporting the location result.<br>**Since:** 23 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Failed to call \\${geoLocationManager.offLocationChange} due to limited device capabilities.<br>**Applicable version:** 23 and later |
| 201 | Permission verification failed. The application does not have the permission required to call the API. Introduced in API 9 and will not be threw above API 24.<br>**Applicable version:** 23 - 24 |
| 3301000 | The location service is unavailable.<br>**Applicable version:** 23 and later |

