# createWebSocket

## 导入模块

```TypeScript
import { webSocket } from 'kits/@kit.NetworkKit';
```

## createWebSocket

```TypeScript
function createWebSocket(): WebSocket
```

Creates a web socket connection.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-webSocket-function createWebSocket(): WebSocket--><!--Device-webSocket-function createWebSocket(): WebSocket-End-->

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WebSocket](arkts-network-websocket-websocket-i.md) | the WebSocket of the createWebSocket. |

## 示例

```TypeScript
let ws: webSocket.WebSocket = webSocket.createWebSocket();
```

