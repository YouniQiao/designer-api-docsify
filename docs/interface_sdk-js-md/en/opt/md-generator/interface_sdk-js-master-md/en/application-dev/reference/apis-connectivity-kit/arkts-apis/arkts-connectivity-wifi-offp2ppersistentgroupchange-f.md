# off_p2pPersistentGroupChange

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
```

## off_p2pPersistentGroupChange

```TypeScript
function off(type: 'p2pPersistentGroupChange', callback?: Callback<void>): void
```

Unsubscribe P2P persistent group change events.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** p2pPersistentGroupChange

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function off(type: 'p2pPersistentGroupChange', callback?: Callback<void>): void--><!--Device-wifi-function off(type: 'p2pPersistentGroupChange', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'p2pPersistentGroupChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

## Examples

```TypeScript
import wifi from '@ohos.wifi';

let recvP2pPersistentGroupChangeFunc = (result:void) => {
    console.info("Receive p2p persistent group change event: " + result);
}

// Register an event.
wifi.on("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);

// Unregister an event.
wifi.off("p2pPersistentGroupChange", recvP2pPersistentGroupChangeFunc);
```
