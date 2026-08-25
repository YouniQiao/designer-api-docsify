# WebSocketMessage

从指定客户端接收到的消息，包括客户端的信息和数据。

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { webSocket } from '@kit.NetworkKit';
```

## clientConnection

```TypeScript
clientConnection: WebSocketConnection
```

客户端信息，包括客户端的ip地址和端口号port。

**类型：** [WebSocketConnection](arkts-network-websocket-websocketconnection-i.md)

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.NetStack

## data

```TypeScript
data: string | ArrayBuffer
```

接收到的客户端发的消息数据。

**类型：** string \| ArrayBuffer

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.NetStack
