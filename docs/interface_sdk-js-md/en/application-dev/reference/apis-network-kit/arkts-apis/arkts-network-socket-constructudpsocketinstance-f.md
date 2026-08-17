# constructUDPSocketInstance

## Modules to Import

```TypeScript
import { socket } from 'socket';
```

## constructUDPSocketInstance

```TypeScript
function constructUDPSocketInstance(): UDPSocket
```

Creates a UDPSocket object.

**Since:** 10

<!--Device-socket-function constructUDPSocketInstance(): UDPSocket--><!--Device-socket-function constructUDPSocketInstance(): UDPSocket-End-->

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| Type | Description |
| --- | --- |
| UDPSocket | the UDPSocket of the constructUDPSocketInstance. |

**Examples**

```TypeScript
import { socket } from '@kit.NetworkKit';
let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
```

