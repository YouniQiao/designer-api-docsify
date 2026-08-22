# offHotspotStaLeave (System API)

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
import { wifiManagerExt } from '@kit.ConnectivityKit';
```

## offHotspotStaLeave

```TypeScript
function offHotspotStaLeave(callback?: Callback<StationInfo>): void
```

Unsubscribe Wi-Fi hotspot sta leave events.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_WIFI_HOTSPOT

<!--Device-wifiManager-function offHotspotStaLeave(callback?: Callback<StationInfo>): void--><!--Device-wifiManager-function offHotspotStaLeave(callback?: Callback<StationInfo>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;StationInfo&gt; | No | the callback of off |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | System API is not allowed called by Non-system application. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [2601000](../errorcode-wifi.md#2601000-hotspot-module-error) | Operation failed. |

