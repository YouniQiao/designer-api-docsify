# constructLocalSocketServerInstance

## constructLocalSocketServerInstance

```TypeScript
function constructLocalSocketServerInstance(): LocalSocketServer
```

Creates a LocalSocketServer object.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-socket-function constructLocalSocketServerInstance(): LocalSocketServer--><!--Device-socket-function constructLocalSocketServerInstance(): LocalSocketServer-End-->

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the LocalSocketServer of the constructLocalSocketServerInstance. |

**Example**

```TypeScript
import { socket } from '@kit.NetworkKit';
let server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
```

