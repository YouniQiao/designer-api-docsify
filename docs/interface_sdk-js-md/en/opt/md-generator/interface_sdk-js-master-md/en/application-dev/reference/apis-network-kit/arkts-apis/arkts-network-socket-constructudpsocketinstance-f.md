# constructUDPSocketInstance

## Modules to Import

```TypeScript
import { socket } from '@kit.NetworkKit';
```

## constructUDPSocketInstance

```TypeScript
function constructUDPSocketInstance(): UDPSocket
```

Creates a UDPSocket object.

**Since:** 10

**Deprecated since:** -1

<!--Device-socket-function constructUDPSocketInstance(): UDPSocket--><!--Device-socket-function constructUDPSocketInstance(): UDPSocket-End-->

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [UDPSocket](arkts-network-socket-udpsocket-i.md) |

## Examples

```TypeScript
import { socket } from '@kit.NetworkKit';
let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
```
