# RequestResult

发送请求的响应结果。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.IPC.Core

## 导入模块

```TypeScript
import { rpc } from '@kit.IPCKit';
```

## code

```TypeScript
code: int
```

消息代码。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.IPC.Core

## data

```TypeScript
data: MessageSequence
```

发送给对端进程的MessageSequence对象。

**类型：** [MessageSequence](arkts-ipc-rpc-messagesequence-c.md)

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.IPC.Core

## errCode

```TypeScript
errCode: int
```

错误码。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.IPC.Core

## reply

```TypeScript
reply: MessageSequence
```

对端进程返回的MessageSequence对象。

**类型：** [MessageSequence](arkts-ipc-rpc-messagesequence-c.md)

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Communication.IPC.Core
