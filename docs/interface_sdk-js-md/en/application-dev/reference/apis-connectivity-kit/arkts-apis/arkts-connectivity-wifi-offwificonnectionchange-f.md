# off_wifiConnectionChange

## Modules to Import

```TypeScript
import { wifi } from 'wifi';
```

## off_wifiConnectionChange

```TypeScript
function off(type: 'wifiConnectionChange', callback?: Callback<number>): void
```

Unsubscribe Wi-Fi connection change events. &lt;p&gt;All callback functions will be deregistered If there is no specific callback parameter.&lt;/p&gt;

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** wifiConnectionChange

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function off(type: 'wifiConnectionChange', callback?: Callback<number>): void--><!--Device-wifi-function off(type: 'wifiConnectionChange', callback?: Callback<number>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'wifiConnectionChange' | Yes | event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No | the callback of on, 0: disconnected, 1: connected |

## Examples

```TypeScript
import wifi from '@ohos.wifi';

let recvWifiConnectionChangeFunc = (result:number) => {
    console.info("Receive wifi connection change event: " + result);
}

// Register an event.
wifi.on("wifiConnectionChange", recvWifiConnectionChangeFunc);

// Unregister an event.
wifi.off("wifiConnectionChange", recvWifiConnectionChangeFunc);
```

