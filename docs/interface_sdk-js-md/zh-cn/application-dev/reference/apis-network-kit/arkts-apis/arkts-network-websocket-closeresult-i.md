# CloseResult

The result for closing a WebSocket connection.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-webSocket-export interface CloseResult--><!--Device-webSocket-export interface CloseResult-End-->

**系统能力：** SystemCapability.Communication.NetStack

## 导入模块

```TypeScript
import { webSocket } from 'kits/@kit.NetworkKit';
```

## code

```TypeScript
code: int
```

Error code.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CloseResult-code: int--><!--Device-CloseResult-code: int-End-->

**系统能力：** SystemCapability.Communication.NetStack

## reason

```TypeScript
reason: string
```

Error cause.

**类型：** string

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-CloseResult-reason: string--><!--Device-CloseResult-reason: string-End-->

**系统能力：** SystemCapability.Communication.NetStack

