# CallingInfo

```TypeScript
class CallingInfo
```

Defines the IPC context, including the PID and UID, local and remote device IDs, and whether the API is invoked on the same device.

**Since:** 23

**System capability:** SystemCapability.Communication.IPC.Core

## Modules to Import

```TypeScript
import { rpc } from '@kit.IPCKit';
```

## callerPid

```TypeScript
readonly callerPid: number
```

PID of the caller, which is valid only in the IPC scenario.

**Type:** number

**Default:** -1

**Since:** 23

**Model restriction:** This API can be used in both the stage model and FA model.

**System capability:** SystemCapability.Communication.IPC.Core

## callerTokenId

```TypeScript
readonly callerTokenId: number
```

Token ID of the caller, which is valid only in the IPC scenario.

**Type:** number

**Default:** -1

**Since:** 23

**Model restriction:** This API can be used in both the stage model and FA model.

**System capability:** SystemCapability.Communication.IPC.Core

## callerUid

```TypeScript
readonly callerUid: number
```

UID of the caller, which is valid only in the IPC scenario.

**Type:** number

**Default:** -1

**Since:** 23

**Model restriction:** This API can be used in both the stage model and FA model.

**System capability:** SystemCapability.Communication.IPC.Core

## isLocalCalling

```TypeScript
readonly isLocalCalling: boolean
```

Whether the peer end of the current communication is a process on the local device. The value **true** indicates that the local and peer processes are on the same device (IPC scenario), and the value **false** indicates that they are not on the same device (RPC scenario).

**Type:** boolean

**Default:** true

**Since:** 23

**Model restriction:** This API can be used in both the stage model and FA model.

**System capability:** SystemCapability.Communication.IPC.Core

## localDeviceId

```TypeScript
readonly localDeviceId: string
```

Local device ID. This parameter is valid only in RPC scenarios.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used in both the stage model and FA model.

**System capability:** SystemCapability.Communication.IPC.Core

## remoteDeviceId

```TypeScript
readonly remoteDeviceId: string
```

Remote device ID. This parameter is valid only in RPC scenarios.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used in both the stage model and FA model.

**System capability:** SystemCapability.Communication.IPC.Core
