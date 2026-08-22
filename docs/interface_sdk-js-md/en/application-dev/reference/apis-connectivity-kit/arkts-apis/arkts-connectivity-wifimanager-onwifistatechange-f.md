# onWifiStateChange

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
import { wifiManagerExt } from '@kit.ConnectivityKit';
```

## onWifiStateChange

```TypeScript
function onWifiStateChange(callback: Callback<int>): void
```

Subscribe Wi-Fi status change events.

**Since:** 23

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function onWifiStateChange(callback: Callback<int>): void--><!--Device-wifiManager-function onWifiStateChange(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | Yes | the callback of on, 0: inactive, 1: active, 2: activating, 3: de-activating |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) | Operation failed. |

