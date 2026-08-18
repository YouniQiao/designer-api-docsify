# constructMulticastSocketInstance

## Modules to Import

```TypeScript
```

## constructMulticastSocketInstance

```TypeScript
function constructMulticastSocketInstance(): MulticastSocket
```

Creates a MulticastSocket object.

**Since:** 12

<!--Device-socket-function constructMulticastSocketInstance(): MulticastSocket--><!--Device-socket-function constructMulticastSocketInstance(): MulticastSocket-End-->

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MulticastSocket](arkts-network-socket-multicastsocket-i.md) |

**Examples**

```TypeScript
import { socket } from '@kit.NetworkKit';
let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
```
