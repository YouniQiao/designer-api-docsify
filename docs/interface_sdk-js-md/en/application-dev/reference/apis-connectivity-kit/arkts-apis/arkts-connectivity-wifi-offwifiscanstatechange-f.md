# off_wifiScanStateChange

## Modules to Import

```TypeScript
import { wifi } from 'wifi';
```

## off_wifiScanStateChange

```TypeScript
function off(type: 'wifiScanStateChange', callback?: Callback<number>): void
```

Unsubscribe Wi-Fi scan status change events. &lt;p&gt;All callback functions will be deregistered If there is no specific callback parameter.&lt;/p&gt;

**Since:** 7

**Deprecated since:** 9

**Substitutes:** wifiScanStateChange

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function off(type: 'wifiScanStateChange', callback?: Callback<number>): void--><!--Device-wifi-function off(type: 'wifiScanStateChange', callback?: Callback<number>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'wifiScanStateChange' | Yes | event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No | the callback of on, 0: scan fail, 1: scan success |

**Examples**

```TypeScript
import wifi from '@ohos.wifi';

let recvWifiScanStateChangeFunc = (result:number) => {
    console.info("Receive Wifi scan state change event: " + result);
}

// Register an event.
wifi.on("wifiScanStateChange", recvWifiScanStateChangeFunc);

// Unregister an event.
wifi.off("wifiScanStateChange", recvWifiScanStateChangeFunc);
```

