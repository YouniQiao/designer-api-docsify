# createWebSocketServer

## Modules to Import

```TypeScript
import { webSocket } from '@kit.NetworkKit';
```

## createWebSocketServer

```TypeScript
function createWebSocketServer(): WebSocketServer
```

Creates a **WebSocketServer** object, which provides methods to start or stop the WebSocketServer service, send data over the connection, close the connection, list all connections, and enable or disable listening for the **open**, **close**, **message**, and **error** events.

> **NOTE：**&gt;
> Supported on all devices since API version 23. In earlier versions, this method is supported only on TV devices.

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WebSocketServer](arkts-network-websocket-websocketserver-i.md) |

**Examples**

```TypeScript
let ws: webSocket.WebSocketServer = webSocket.createWebSocketServer();
```
