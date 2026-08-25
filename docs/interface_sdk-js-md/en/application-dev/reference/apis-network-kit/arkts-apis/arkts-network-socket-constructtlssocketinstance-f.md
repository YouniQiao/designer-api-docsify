# constructTLSSocketInstance

## Modules to Import

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## constructTLSSocketInstance

```TypeScript
function constructTLSSocketInstance(): TLSSocket
```

Creates a **TLSSocket** object.

**Since:** 9

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TLSSocket](arkts-network-socket-tlssocket-i.md) |


## constructTLSSocketInstance

```TypeScript
function constructTLSSocketInstance(tcpSocket: TCPSocket): TLSSocket
```

Upgrades a **TCPSocket** connection to a **TLSSocket** connection.

> **NOTE：**&gt;
> Before calling **constructTLSSocketInstance**, ensure that a **TCPSocket** connection has been established and no
> data is transmitted. After a successful upgrade, you do not need to call the **close** API for the **TCPSocket**
> object.

**Since:** 12

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tcpSocket | [TCPSocket](arkts-network-socket-tcpsocket-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TLSSocket](arkts-network-socket-tlssocket-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2300002](../errorcode-net-socket.md#2300002-system-internal-error) |
| 2303601 |
| 2303602 |
