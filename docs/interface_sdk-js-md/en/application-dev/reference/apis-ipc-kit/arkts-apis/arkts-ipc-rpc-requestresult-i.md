# RequestResult

发送请求的响应结果。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-rpc-interface RequestResult--><!--Device-rpc-interface RequestResult-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## Modules to Import

```TypeScript
import { rpc } from 'kits/@kit.IPCKit';
```

## code

```TypeScript
code: int
```

消息代码。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RequestResult-code: int--><!--Device-RequestResult-code: int-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## data

```TypeScript
data: MessageSequence
```

发送给对端进程的MessageSequence对象。

**Type:** [MessageSequence](arkts-ipc-rpc-messagesequence-c.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RequestResult-data: MessageSequence--><!--Device-RequestResult-data: MessageSequence-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## errCode

```TypeScript
errCode: int
```

错误码。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RequestResult-errCode: int--><!--Device-RequestResult-errCode: int-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## reply

```TypeScript
reply: MessageSequence
```

对端进程返回的MessageSequence对象。

**Type:** [MessageSequence](arkts-ipc-rpc-messagesequence-c.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RequestResult-reply: MessageSequence--><!--Device-RequestResult-reply: MessageSequence-End-->

**System capability:** SystemCapability.Communication.IPC.Core

