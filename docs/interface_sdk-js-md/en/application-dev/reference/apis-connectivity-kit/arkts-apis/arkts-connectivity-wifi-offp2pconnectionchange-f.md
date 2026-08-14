# off_p2pConnectionChange

## Modules to Import

```TypeScript
import { wifi } from 'wifi';
```

## off_p2pConnectionChange

```TypeScript
function off(type: 'p2pConnectionChange', callback?: Callback<WifiP2pLinkedInfo>): void
```

Unsubscribe P2P connection change events.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** p2pConnectionChange

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function off(type: 'p2pConnectionChange', callback?: Callback<WifiP2pLinkedInfo>): void--><!--Device-wifi-function off(type: 'p2pConnectionChange', callback?: Callback<WifiP2pLinkedInfo>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'p2pConnectionChange' | Yes | event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;WifiP2pLinkedInfo&gt; | No | the callback of on |

## Examples

```TypeScript
import wifi from '@ohos.wifi';

let recvP2pConnectionChangeFunc = (result:wifi.WifiP2pLinkedInfo) => {
    console.info("Receive p2p connection change event: " + result);
}

// Register an event.
wifi.on("p2pConnectionChange", recvP2pConnectionChangeFunc);

// Unregister an event.
wifi.off("p2pConnectionChange", recvP2pConnectionChangeFunc);
```

