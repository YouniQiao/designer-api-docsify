# WebSocketMessage

Info about the message received from a specific client.

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

<!--Device-webSocket-export interface WebSocketMessage--><!--Device-webSocket-export interface WebSocketMessage-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { webSocket } from 'kits/@kit.NetworkKit';
```

## clientConnection

```TypeScript
clientConnection: WebSocketConnection
```

The connection where the message comes from.

**类型：** [WebSocketConnection](arkts-network-websocket-websocketconnection-i.md)

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

<!--Device-WebSocketMessage-clientConnection: WebSocketConnection--><!--Device-WebSocketMessage-clientConnection: WebSocketConnection-End-->

**系统能力：** SystemCapability.Communication.NetStack

## data

```TypeScript
data: string | ArrayBuffer
```

Content of the message.

**类型：** string \| ArrayBuffer

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

<!--Device-WebSocketMessage-data: string | ArrayBuffer--><!--Device-WebSocketMessage-data: string | ArrayBuffer-End-->

**系统能力：** SystemCapability.Communication.NetStack

