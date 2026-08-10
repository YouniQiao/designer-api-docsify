# WebSocketCloseOptions

Defines the optional parameters carried in the request for closing a WebSocket connection.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-webSocket-export interface WebSocketCloseOptions--><!--Device-webSocket-export interface WebSocketCloseOptions-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { webSocket } from 'kits/@kit.NetworkKit';
```

## code

```TypeScript
code?: int
```

Error code.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebSocketCloseOptions-code?: int--><!--Device-WebSocketCloseOptions-code?: int-End-->

**系统能力：** SystemCapability.Communication.NetStack

## reason

```TypeScript
reason?: string
```

Error cause.

**类型：** string

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-WebSocketCloseOptions-reason?: string--><!--Device-WebSocketCloseOptions-reason?: string-End-->

**系统能力：** SystemCapability.Communication.NetStack

