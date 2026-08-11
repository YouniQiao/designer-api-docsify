# offLocationIconStatusChange (System API)

## Modules to Import

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## offLocationIconStatusChange

```TypeScript
function offLocationIconStatusChange(callback?: Callback<LocationIconStatus>): void
```

Unsubscribe location icon status changed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-geoLocationManager-function offLocationIconStatusChange(callback?: Callback<LocationIconStatus>): void--><!--Device-geoLocationManager-function offLocationIconStatusChange(callback?: Callback<LocationIconStatus>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;LocationIconStatus&gt; | No | Indicates the callback for reporting the location icon status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Failed to call \\${geoLocationManager.offLocationIconStatusChange} due to limited device capabilities. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [3301000](../errorcode-geoLocationManager.md#3301000-location-service-unavailable) | The location service is unavailable. |

