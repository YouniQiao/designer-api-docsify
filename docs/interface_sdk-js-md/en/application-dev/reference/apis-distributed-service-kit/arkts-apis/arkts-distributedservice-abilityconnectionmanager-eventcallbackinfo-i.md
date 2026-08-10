# EventCallbackInfo

回调方法的接收信息。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-abilityConnectionManager-interface EventCallbackInfo--><!--Device-abilityConnectionManager-interface EventCallbackInfo-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## Modules to Import

```TypeScript
import { abilityConnectionManager } from 'kits/@kit.DistributedServiceKit';
```

## data

```TypeScript
data?: ArrayBuffer
```

表示接收的字节流。

**Type:** ArrayBuffer

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EventCallbackInfo-data?: ArrayBuffer--><!--Device-EventCallbackInfo-data?: ArrayBuffer-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## msg

```TypeScript
msg?: string
```

表示接收的消息。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EventCallbackInfo-msg?: string--><!--Device-EventCallbackInfo-msg?: string-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## reason

```TypeScript
reason?: DisconnectReason
```

表示断连原因。

**Type:** [DisconnectReason](arkts-distributedservice-abilityconnectionmanager-disconnectreason-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EventCallbackInfo-reason?: DisconnectReason--><!--Device-EventCallbackInfo-reason?: DisconnectReason-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## sessionId

```TypeScript
sessionId: int
```

表示当前事件对应的协同会话ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EventCallbackInfo-sessionId: int--><!--Device-EventCallbackInfo-sessionId: int-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

