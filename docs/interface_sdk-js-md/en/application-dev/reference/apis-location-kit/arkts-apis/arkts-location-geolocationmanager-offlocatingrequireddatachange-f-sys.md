# offLocatingRequiredDataChange (System API)

## Modules to Import

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## offLocatingRequiredDataChange

```TypeScript
function offLocatingRequiredDataChange(callback?: Callback<Array<LocatingRequiredData>>): void
```

Stop WiFi/BT scanning and unsubscribe from WiFi/BT scanning information changes.

**Since:** 23

**Required permissions:** ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function offLocatingRequiredDataChange(callback?: Callback<Array<LocatingRequiredData>>): void--><!--Device-geoLocationManager-function offLocatingRequiredDataChange(callback?: Callback<Array<LocatingRequiredData>>): void-End-->

**System capability:** SystemCapability.Location.Location.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[LocatingRequiredData](arkts-location-geolocationmanager-locatingrequireddata-i-sys.md)&gt;&gt; | No | Indicates the callback for reporting WiFi/BT scan info. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call \\${geoLocationManager.offLocatingRequiredDataChange} due to limited device capabilities. |

