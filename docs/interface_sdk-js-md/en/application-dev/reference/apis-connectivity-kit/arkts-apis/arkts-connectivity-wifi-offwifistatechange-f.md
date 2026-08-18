# off_wifiStateChange

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
import { wifiext } from '@kit.ConnectivityKit';
import { wifiManager } from '@kit.ConnectivityKit';
import { wifiManagerExt } from '@kit.ConnectivityKit';
```

## off_wifiStateChange('wifiStateChange')

```TypeScript
function off(type: 'wifiStateChange', callback?: Callback<number>): void
```

Unsubscribe Wi-Fi status change events. &lt;p&gt;All callback functions will be deregistered If there is no specific callback parameter.&lt;/p&gt;

**Since:** 7

**Deprecated since:** 9

**Substitutes:** wifiStateChange

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function off(type: 'wifiStateChange', callback?: Callback<number>): void--><!--Device-wifi-function off(type: 'wifiStateChange', callback?: Callback<number>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'wifiStateChange' | Yes | event name. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;number&gt; | No | the callback of on, 0: inactive, 1: active, 2: activating, 3: de-activating |

**Examples**

```TypeScript
import wifi from '@ohos.wifi';

let recvPowerNotifyFunc = (result:number) => {
    console.info("Receive power state change event: " + result);
}

// Register an event.
wifi.on("wifiStateChange", recvPowerNotifyFunc);

// Unregister an event.
wifi.off("wifiStateChange", recvPowerNotifyFunc);
```

