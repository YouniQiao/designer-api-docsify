# onHotspotStaJoin (System API)

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
import { wifiManagerExt } from '@kit.ConnectivityKit';
```

## onHotspotStaJoin

```TypeScript
function onHotspotStaJoin(callback: Callback<StationInfo>): void
```

Subscribe Wi-Fi hotspot sta join events.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_WIFI_HOTSPOT

<!--Device-wifiManager-function onHotspotStaJoin(callback: Callback<StationInfo>): void--><!--Device-wifiManager-function onHotspotStaJoin(callback: Callback<StationInfo>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;StationInfo&gt; | Yes | the callback of on |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | System API is not allowed called by Non-system application. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [2601000](../errorcode-wifi.md#2601000-hotspot-module-error) | Operation failed. |

