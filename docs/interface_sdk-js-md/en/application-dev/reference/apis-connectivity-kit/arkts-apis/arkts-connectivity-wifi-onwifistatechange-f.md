# on_wifiStateChange

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
import { wifiext } from '@kit.ConnectivityKit';
import { wifiManager } from '@kit.ConnectivityKit';
import { wifiManagerExt } from '@kit.ConnectivityKit';
```

## on('wifiStateChange')

```TypeScript
function on(type: 'wifiStateChange', callback: Callback<number>): void
```

Subscribe Wi-Fi status change events.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** wifiStateChange

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function on(type: 'wifiStateChange', callback: Callback<number>): void--><!--Device-wifi-function on(type: 'wifiStateChange', callback: Callback<number>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'wifiStateChange' | Yes | event name. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;number&gt; | Yes | the callback of on, 0: inactive, 1: active, 2: activating, 3: de-activating |

