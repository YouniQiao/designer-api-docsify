# constructTCPSocketServerInstance

## Modules to Import

```TypeScript
import { socket } from '@kit.NetworkKit';
```

## constructTCPSocketServerInstance

```TypeScript
function constructTCPSocketServerInstance(): TCPSocketServer
```

Creates a TCPSocketServer object.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 24; ArkTS-Sta since version 26.0.0.

<!--Device-socket-function constructTCPSocketServerInstance(): TCPSocketServer--><!--Device-socket-function constructTCPSocketServerInstance(): TCPSocketServer-End-->

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| Type | Description |
| --- | --- |
| [TCPSocketServer](arkts-network-socket-tcpsocketserver-i.md) | the TCPSocketServer of the constructTCPSocketServerInstance. |

## Examples

```TypeScript
import { socket } from '@kit.NetworkKit';
let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
```

