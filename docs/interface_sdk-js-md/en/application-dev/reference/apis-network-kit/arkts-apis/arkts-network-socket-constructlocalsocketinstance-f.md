# constructLocalSocketInstance

## Modules to Import

```TypeScript
import { socket } from 'kits/@kit.NetworkKit';
```

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
| [LocalSocket](arkts-network-socket-localsocket-i.md) | the LocalSocket of the constructLocalSocketInstance. |

## Examples

```TypeScript
import { socket } from '@kit.NetworkKit';
let client: socket.LocalSocket = socket.constructLocalSocketInstance();
```

