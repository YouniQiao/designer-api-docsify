# constructTCPSocketInstance

## Modules to Import

```TypeScript
import { socket } from '@kit.NetworkKit';
```

## constructTCPSocketInstance

```TypeScript
function constructTCPSocketInstance(): TCPSocket
```

Creates a TCPSocket object.

**Since:** 10

<!--Device-socket-function constructTCPSocketInstance(): TCPSocket--><!--Device-socket-function constructTCPSocketInstance(): TCPSocket-End-->

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TCPSocket](arkts-network-socket-tcpsocket-i.md) |

## Examples

```TypeScript
import { socket } from '@kit.NetworkKit';
let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
```
