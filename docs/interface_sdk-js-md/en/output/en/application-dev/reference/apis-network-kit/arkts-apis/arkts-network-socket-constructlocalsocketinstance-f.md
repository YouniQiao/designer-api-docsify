# constructLocalSocketInstance

## constructLocalSocketInstance

```TypeScript
function constructLocalSocketInstance(): LocalSocket
```

Creates a LocalSocket object.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-socket-function constructLocalSocketInstance(): LocalSocket--><!--Device-socket-function constructLocalSocketInstance(): LocalSocket-End-->

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the LocalSocket of the constructLocalSocketInstance. |

**Example**

```TypeScript
import { socket } from '@kit.NetworkKit';
let client: socket.LocalSocket = socket.constructLocalSocketInstance();
```

