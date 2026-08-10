# createWebSocketServer

## 导入模块

```TypeScript
import { webSocket } from 'kits/@kit.NetworkKit';
```

## createWebSocketServer

```TypeScript
function createWebSocketServer(): WebSocketServer
```

Creates a web socket Server.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-webSocket-function createWebSocketServer(): WebSocketServer--><!--Device-webSocket-function createWebSocketServer(): WebSocketServer-End-->

**系统能力：** SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WebSocketServer](arkts-network-websocket-websocketserver-i.md) | the WebSocketServer Object. |

## 示例

```TypeScript
let ws: webSocket.WebSocketServer = webSocket.createWebSocketServer();
```

