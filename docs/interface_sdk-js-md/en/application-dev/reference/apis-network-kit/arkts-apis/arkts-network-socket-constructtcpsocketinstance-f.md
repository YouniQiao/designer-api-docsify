# constructTCPSocketInstance

## Modules to Import

```TypeScript
import { socket } from 'socket';
```

## constructTCPSocketInstance

```TypeScript
function constructTCPSocketInstance(): TCPSocket
```

Creates a TCPSocket object.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-socket-function constructTCPSocketInstance(): TCPSocket--><!--Device-socket-function constructTCPSocketInstance(): TCPSocket-End-->

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| Type | Description |
| --- | --- |
| TCPSocket | the TCPSocket of the constructTCPSocketInstance. |

## Examples

```TypeScript
import { socket } from '@kit.NetworkKit';
let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
```

