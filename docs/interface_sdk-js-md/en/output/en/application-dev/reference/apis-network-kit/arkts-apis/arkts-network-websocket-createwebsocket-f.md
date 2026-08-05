# createWebSocket

## createWebSocket

```TypeScript
function createWebSocket(): WebSocket
```

Creates a web socket connection.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-webSocket-function createWebSocket(): WebSocket--><!--Device-webSocket-function createWebSocket(): WebSocket-End-->

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | the WebSocket of the createWebSocket. |

**Example**

```TypeScript
let ws: webSocket.WebSocket = webSocket.createWebSocket();
```

