# constructUDPSocketInstance

## Modules to Import

```TypeScript
import socket from '@kit.NetworkKit';
```

## constructUDPSocketInstance

```TypeScript
function constructUDPSocketInstance(): UDPSocket
```

Creates a **UDPSocket** object.

**Since:** 7

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| Type | Description |
| --- | --- |
| [UDPSocket](arkts-network-connection-udpsocket-t.md) | UDPSocket** object. |

**Examples**

```TypeScript
import { socket } from '@kit.NetworkKit';
let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
```
