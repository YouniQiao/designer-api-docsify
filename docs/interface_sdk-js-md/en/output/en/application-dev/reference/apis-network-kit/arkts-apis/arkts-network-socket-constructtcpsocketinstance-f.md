# constructTCPSocketInstance

## constructTCPSocketInstance

```TypeScript
function constructTCPSocketInstance(): TCPSocket
```

Creates a TCPSocket object.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-socket-function constructTCPSocketInstance(): TCPSocket--><!--Device-socket-function constructTCPSocketInstance(): TCPSocket-End-->

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the TCPSocket of the constructTCPSocketInstance. |

**Example**

```TypeScript
import { socket } from '@kit.NetworkKit';
let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
```

