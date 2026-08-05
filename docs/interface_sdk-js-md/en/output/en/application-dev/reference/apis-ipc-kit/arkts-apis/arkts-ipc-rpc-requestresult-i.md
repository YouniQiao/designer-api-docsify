# RequestResult

Defines the response to the request.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-rpc-interface RequestResult--><!--Device-rpc-interface RequestResult-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## code

```TypeScript
code: int
```

Message code.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RequestResult-code: int--><!--Device-RequestResult-code: int-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## data

```TypeScript
data: MessageSequence
```

**MessageSequence** object sent to the remote process.

**Type:** MessageSequence

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RequestResult-data: MessageSequence--><!--Device-RequestResult-data: MessageSequence-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## errCode

```TypeScript
errCode: int
```

Error code.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RequestResult-errCode: int--><!--Device-RequestResult-errCode: int-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## reply

```TypeScript
reply: MessageSequence
```

**MessageSequence** object returned by the remote process.

**Type:** MessageSequence

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RequestResult-reply: MessageSequence--><!--Device-RequestResult-reply: MessageSequence-End-->

**System capability:** SystemCapability.Communication.IPC.Core

