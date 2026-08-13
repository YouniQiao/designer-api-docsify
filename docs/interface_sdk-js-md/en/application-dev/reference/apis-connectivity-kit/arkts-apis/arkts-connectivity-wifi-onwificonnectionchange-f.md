# on_wifiConnectionChange

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
```

## on_wifiConnectionChange

```TypeScript
function on(type: 'wifiConnectionChange', callback: Callback<number>): void
```

Subscribe Wi-Fi connection change events.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** wifiConnectionChange

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function on(type: 'wifiConnectionChange', callback: Callback<number>): void--><!--Device-wifi-function on(type: 'wifiConnectionChange', callback: Callback<number>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'wifiConnectionChange' | Yes | event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | Yes | the callback of on, 0: disconnected, 1: connected |

