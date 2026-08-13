# off_p2pStateChange

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
```

## off_p2pStateChange

```TypeScript
function off(type: 'p2pStateChange', callback?: Callback<number>): void
```

Unsubscribe P2P status change events.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** p2pStateChange

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function off(type: 'p2pStateChange', callback?: Callback<number>): void--><!--Device-wifi-function off(type: 'p2pStateChange', callback?: Callback<number>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'p2pStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | No |

## Examples

```TypeScript
import wifi from '@ohos.wifi';

let recvP2pStateChangeFunc = (result:number) => {
    console.info("Receive p2p state change event: " + result);
}

// Register an event.
wifi.on("p2pStateChange", recvP2pStateChangeFunc);

// Unregister an event.
wifi.off("p2pStateChange", recvP2pStateChangeFunc);
```
