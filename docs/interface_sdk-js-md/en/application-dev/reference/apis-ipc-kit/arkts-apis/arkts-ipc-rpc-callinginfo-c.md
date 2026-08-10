# CallingInfo

IPC上下文信息，包括PID和UID、本端和对端设备ID、检查接口调用是否在同一设备上。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-rpc-class CallingInfo--><!--Device-rpc-class CallingInfo-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## Modules to Import

```TypeScript
import { rpc } from 'kits/@kit.IPCKit';
```

## callerPid

```TypeScript
readonly callerPid: number
```

调用者的PID，仅IPC场景有效。

**Type:** number

**Default:** -1

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-CallingInfo-readonly callerPid: number--><!--Device-CallingInfo-readonly callerPid: number-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## callerTokenId

```TypeScript
readonly callerTokenId: number
```

调用者的TokenId，仅IPC场景有效。

**Type:** number

**Default:** -1

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-CallingInfo-readonly callerTokenId: number--><!--Device-CallingInfo-readonly callerTokenId: number-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## callerUid

```TypeScript
readonly callerUid: number
```

调用者的UID，仅IPC场景有效。

**Type:** number

**Default:** -1

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-CallingInfo-readonly callerUid: number--><!--Device-CallingInfo-readonly callerUid: number-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## isLocalCalling

```TypeScript
readonly isLocalCalling: boolean
```

当前通信对端是否为本设备进程。true：调用在同一台设备（IPC场景），false：调用未在同一台设备（RPC场景）。

**Type:** boolean

**Default:** true

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-CallingInfo-readonly isLocalCalling: boolean--><!--Device-CallingInfo-readonly isLocalCalling: boolean-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## localDeviceId

```TypeScript
readonly localDeviceId: string
```

本端设备的设备ID，仅RPC场景有效。

**Type:** string

**Default:** @syscap SystemCapability.Communication.IPC.Core @FaAndStageModel

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-CallingInfo-readonly localDeviceId: string--><!--Device-CallingInfo-readonly localDeviceId: string-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## remoteDeviceId

```TypeScript
readonly remoteDeviceId: string
```

对端设备的设备ID，仅RPC场景有效。

**Type:** string

**Default:** @syscap SystemCapability.Communication.IPC.Core @FaAndStageModel

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-CallingInfo-readonly remoteDeviceId: string--><!--Device-CallingInfo-readonly remoteDeviceId: string-End-->

**System capability:** SystemCapability.Communication.IPC.Core

