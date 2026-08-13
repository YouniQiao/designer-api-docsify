# createWebSocketServer

## Modules to Import

```TypeScript
import { webSocket } from '@kit.NetworkKit';
```

## createWebSocketServer

```TypeScript
function createWebSocketServer(): WebSocketServer
```

Creates a web socket Server.

**Since:** 23

**Deprecated since:** -1

<!--Device-webSocket-function createWebSocketServer(): WebSocketServer--><!--Device-webSocket-function createWebSocketServer(): WebSocketServer-End-->

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WebSocketServer](arkts-network-websocket-websocketserver-i.md) |

## Examples

```TypeScript
let ws: webSocket.WebSocketServer = webSocket.createWebSocketServer();
```
