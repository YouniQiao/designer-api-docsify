# off_p2pDiscoveryChange

## Modules to Import

```TypeScript
import { wifi } from 'wifi';
```

## off_p2pDiscoveryChange

```TypeScript
function off(type: 'p2pDiscoveryChange', callback?: Callback<number>): void
```

Unsubscribe P2P discovery events.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** p2pDiscoveryChange

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function off(type: 'p2pDiscoveryChange', callback?: Callback<number>): void--><!--Device-wifi-function off(type: 'p2pDiscoveryChange', callback?: Callback<number>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'p2pDiscoveryChange' | Yes | event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No | the callback of on |

**Examples**

```TypeScript
import wifi from '@ohos.wifi';

let recvP2pDiscoveryChangeFunc = (result:number) => {
    console.info("Receive p2p discovery change event: " + result);
}

// Register an event.
wifi.on("p2pDiscoveryChange", recvP2pDiscoveryChangeFunc);

// Unregister an event.
wifi.off("p2pDiscoveryChange", recvP2pDiscoveryChangeFunc);
```

