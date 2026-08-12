# constructMulticastSocketInstance

## Modules to Import

```TypeScript
import { socket } from '@kit.NetworkKit';
```

## constructMulticastSocketInstance

```TypeScript
function constructMulticastSocketInstance(): MulticastSocket
```

Creates a MulticastSocket object.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-socket-function constructMulticastSocketInstance(): MulticastSocket--><!--Device-socket-function constructMulticastSocketInstance(): MulticastSocket-End-->

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| Type | Description |
| --- | --- |
| [MulticastSocket](arkts-network-socket-multicastsocket-i.md) | the MulticastSocket of the constructMulticastSocketInstance. |

## Examples

```TypeScript
import { socket } from '@kit.NetworkKit';
let multicast: socket.MulticastSocket = socket.constructMulticastSocketInstance();
```

