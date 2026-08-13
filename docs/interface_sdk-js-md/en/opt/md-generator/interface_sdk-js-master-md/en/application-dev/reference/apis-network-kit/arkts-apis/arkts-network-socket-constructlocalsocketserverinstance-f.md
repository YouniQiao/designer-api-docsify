# constructLocalSocketServerInstance

## Modules to Import

```TypeScript
import { socket } from '@kit.NetworkKit';
```

## constructLocalSocketServerInstance

```TypeScript
function constructLocalSocketServerInstance(): LocalSocketServer
```

Creates a LocalSocketServer object.

**Since:** 12

**Deprecated since:** -1

<!--Device-socket-function constructLocalSocketServerInstance(): LocalSocketServer--><!--Device-socket-function constructLocalSocketServerInstance(): LocalSocketServer-End-->

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [LocalSocketServer](arkts-network-socket-localsocketserver-i.md) |

## Examples

```TypeScript
import { socket } from '@kit.NetworkKit';
let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
```
