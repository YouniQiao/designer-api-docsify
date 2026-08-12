# createNetConnection

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## createNetConnection

```TypeScript
function createNetConnection(netSpecifier?: NetSpecifier, timeout?: number): NetConnection
```

Create a network connection with optional netSpecifier and timeout.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-connection-function createNetConnection(netSpecifier?: NetSpecifier, timeout?: int): NetConnection--><!--Device-connection-function createNetConnection(netSpecifier?: NetSpecifier, timeout?: int): NetConnection-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| netSpecifier | [NetSpecifier](arkts-network-connection-netspecifier-i.md) | No |
| timeout | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [NetConnection](arkts-network-connection-netconnection-i.md) |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';

// Example 1: Only the default network is concerned. You do not need to specify the netSpecifier parameter. If the timeout parameter is not passed, the timeout interval is not used. In this case, the value of timeout is 0.
let netConnection = connection.createNetConnection();

// Example 2: Only the cellular network is concerned. You need to specify the network type to cellular.
let timeout = 1000;
let netConnectionCellular = connection.createNetConnection({
  netCapabilities: {
    bearerTypes: [connection.NetBearType.BEARER_CELLULAR]
  }
}, timeout);

// Example 3: Both the cellular and Wi-Fi networks are concerned. You need to specify the network type to cellular and Wi-Fi.
let netConnectionCellularAndWifi = connection.createNetConnection({
  netCapabilities: {
    bearerTypes: [connection.NetBearType.BEARER_CELLULAR,
      connection.NetBearType.BEARER_WIFI]
  }
});
```
