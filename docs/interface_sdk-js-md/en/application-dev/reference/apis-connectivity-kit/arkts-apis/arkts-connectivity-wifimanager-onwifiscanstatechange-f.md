# onWifiScanStateChange

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
import { wifiManagerExt } from '@kit.ConnectivityKit';
```

## onWifiScanStateChange

```TypeScript
function onWifiScanStateChange(callback: Callback<int>): void
```

Subscribe Wi-Fi scan status change events.

**Since:** 23

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function onWifiScanStateChange(callback: Callback<int>): void--><!--Device-wifiManager-function onWifiScanStateChange(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | Yes | the callback of on, 0: scan fail, 1: scan success |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) | Operation failed. |

