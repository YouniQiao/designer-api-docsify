# createWebSocket

## Modules to Import

```TypeScript
import { webSocket } from '@kit.NetworkKit';
```

## createWebSocket

```TypeScript
function createWebSocket(): WebSocket
```

Creates a **WebSocket** object, which provides methods to create or close a WebSocket connection, send data over the connection, and enable or disable listening for the **open**, **close**, **message**, and **error** events.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WebSocket](arkts-network-websocket-websocket-i.md) |

**Examples**

```TypeScript
let ws: webSocket.WebSocket = webSocket.createWebSocket();
```
