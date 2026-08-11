# constructTCPSocketServerInstance

## Modules to Import

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## constructTCPSocketServerInstance

```TypeScript
function constructTCPSocketServerInstance(): TCPSocketServer
```

Creates a TCPSocketServer object.

**Since:** 24

<!--Device-socket-function constructTCPSocketServerInstance(): TCPSocketServer--><!--Device-socket-function constructTCPSocketServerInstance(): TCPSocketServer-End-->

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TCPSocketServer](arkts-network-socket-tcpsocketserver-i.md) |

## Examples

```TypeScript
import { socket } from '@kit.NetworkKit';
let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
```
