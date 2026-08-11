# constructTLSSocketServerInstance

## Modules to Import

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

## constructTLSSocketServerInstance

```TypeScript
function constructTLSSocketServerInstance(): TLSSocketServer
```

Creates a TLSSocketServer object.

**Since:** 24

<!--Device-socket-function constructTLSSocketServerInstance(): TLSSocketServer--><!--Device-socket-function constructTLSSocketServerInstance(): TLSSocketServer-End-->

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TLSSocketServer](arkts-network-socket-tlssocketserver-i.md) |

## Examples

```TypeScript
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
```
