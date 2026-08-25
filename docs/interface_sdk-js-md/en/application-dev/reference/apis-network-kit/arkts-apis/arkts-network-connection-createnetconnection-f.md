# createNetConnection

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## createNetConnection

```TypeScript
function createNetConnection(netSpecifier?: NetSpecifier, timeout?: number): NetConnection
```

Creates a **NetConnection** object, which can be used to listen for the network status. [netSpecifier](arkts-network-connection-netspecifier-i.md) specifies the network to be listened for, and **timeout** indicates the timeout duration (ms). **netSpecifier** is a mandatory parameter for **timeout**. If neither of them is present, the default network is used.

> **NOTE：**&gt;
> To listen for the network status, after creating a **NetConnection** object, you need to call
> [register](arkts-network-connection-netconnection-i.md#register) to register the notification of the specified network status
> change.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

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
