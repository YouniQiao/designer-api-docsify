# SendRequestResult

发送请求的响应结果。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [rpc.RequestResult](arkts-ipc-rpc-requestresult-i.md)

<!--Device-rpc-interface SendRequestResult--><!--Device-rpc-interface SendRequestResult-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## Modules to Import

```TypeScript
import { rpc } from 'kits/@kit.IPCKit';
```

## code

```TypeScript
code: number
```

消息代码。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [rpc.RequestResult#code](arkts-ipc-rpc-requestresult-i.md#code)

<!--Device-SendRequestResult-code: number--><!--Device-SendRequestResult-code: number-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## data

```TypeScript
data: MessageParcel
```

发送给对端进程的MessageParcel对象。

**Type:** [MessageParcel](arkts-ipc-rpc-messageparcel-c.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [rpc.RequestResult#data](arkts-ipc-rpc-requestresult-i.md#data)

<!--Device-SendRequestResult-data: MessageParcel--><!--Device-SendRequestResult-data: MessageParcel-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## errCode

```TypeScript
errCode: number
```

错误码。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [rpc.RequestResult#errCode](arkts-ipc-rpc-requestresult-i.md#errcode)

<!--Device-SendRequestResult-errCode: number--><!--Device-SendRequestResult-errCode: number-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## reply

```TypeScript
reply: MessageParcel
```

对端进程返回的MessageParcel对象。

**Type:** [MessageParcel](arkts-ipc-rpc-messageparcel-c.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [rpc.RequestResult#reply](arkts-ipc-rpc-requestresult-i.md#reply)

<!--Device-SendRequestResult-reply: MessageParcel--><!--Device-SendRequestResult-reply: MessageParcel-End-->

**System capability:** SystemCapability.Communication.IPC.Core

