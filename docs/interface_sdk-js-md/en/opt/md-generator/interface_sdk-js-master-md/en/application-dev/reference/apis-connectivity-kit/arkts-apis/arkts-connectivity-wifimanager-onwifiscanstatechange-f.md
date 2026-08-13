# onWifiScanStateChange

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## onWifiScanStateChange

```TypeScript
function onWifiScanStateChange(callback: Callback<number>): void
```

Subscribe Wi-Fi scan status change events.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManager-function onWifiScanStateChange(callback: Callback<int>): void--><!--Device-wifiManager-function onWifiScanStateChange(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) |
