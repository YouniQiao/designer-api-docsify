# onDeviceConfigChange (System API)

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
import { wifiManagerExt } from '@kit.ConnectivityKit';
```

## onDeviceConfigChange

```TypeScript
function onDeviceConfigChange(callback: Callback<int>): void
```

Subscribe Wi-Fi device config change events.

**Since:** 23

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function onDeviceConfigChange(callback: Callback<int>): void--><!--Device-wifiManager-function onDeviceConfigChange(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | Yes | the callback of on, 0: config is added, 1: config is changed, 2: config is removed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | System API is not allowed called by Non-system application. |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) | Operation failed. |

