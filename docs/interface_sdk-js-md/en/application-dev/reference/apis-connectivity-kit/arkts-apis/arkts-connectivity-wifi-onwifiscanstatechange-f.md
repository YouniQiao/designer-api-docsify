# on_wifiScanStateChange

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
import { wifiext } from '@kit.ConnectivityKit';
import { wifiManager } from '@kit.ConnectivityKit';
import { wifiManagerExt } from '@kit.ConnectivityKit';
```

## on_wifiScanStateChange('wifiScanStateChange')

```TypeScript
function on(type: 'wifiScanStateChange', callback: Callback<number>): void
```

Subscribe Wi-Fi scan status change events.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** wifiScanStateChange

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function on(type: 'wifiScanStateChange', callback: Callback<number>): void--><!--Device-wifi-function on(type: 'wifiScanStateChange', callback: Callback<number>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'wifiScanStateChange' | Yes | event name. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes | the callback of on, 0: scan fail, 1: scan success |

