# offWifiScanStateChange

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## offWifiScanStateChange

```TypeScript
function offWifiScanStateChange(callback?: Callback<int>): void
```

Unsubscribe Wi-Fi scan status change events.All callback functions will be deregistered If there is no specific callback parameter.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function offWifiScanStateChange(callback?: Callback<int>): void--><!--Device-wifiManager-function offWifiScanStateChange(callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | No | the callback of off |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) | Operation failed. |

