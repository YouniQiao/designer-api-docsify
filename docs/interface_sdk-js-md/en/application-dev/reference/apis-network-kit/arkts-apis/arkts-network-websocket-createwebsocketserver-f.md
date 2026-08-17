# createWebSocketServer

## Modules to Import

```TypeScript
import { webSocket } from 'webSocket';
```

## createWebSocketServer

```TypeScript
function createWebSocketServer(): WebSocketServer
```

Creates a web socket Server.

**Since:** 23

<!--Device-webSocket-function createWebSocketServer(): WebSocketServer--><!--Device-webSocket-function createWebSocketServer(): WebSocketServer-End-->

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| Type | Description |
| --- | --- |
| [WebSocketServer](arkts-network-websocket-websocketserver-i.md) | the WebSocketServer Object. |

**Examples**

```TypeScript
let ws: webSocket.WebSocketServer = webSocket.createWebSocketServer();
```

