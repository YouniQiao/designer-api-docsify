# constructTLSSocketServerInstance

## Modules to Import

```TypeScript
import { socket } from '@kit.NetworkKit';
```

## constructTLSSocketServerInstance

```TypeScript
function constructTLSSocketServerInstance(): TLSSocketServer
```

Creates a TLSSocketServer object.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-socket-function constructTLSSocketServerInstance(): TLSSocketServer--><!--Device-socket-function constructTLSSocketServerInstance(): TLSSocketServer-End-->

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| Type | Description |
| --- | --- |
| [TLSSocketServer](arkts-network-socket-tlssocketserver-i.md) | the TLSSocketServer of the constructTLSSocketServerInstance. |

## Examples

```TypeScript
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tlsServer: socket.TLSSocketServer = socket.constructTLSSocketServerInstance();
```

