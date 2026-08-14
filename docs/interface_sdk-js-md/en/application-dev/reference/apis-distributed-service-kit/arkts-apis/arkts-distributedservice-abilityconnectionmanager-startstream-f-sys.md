# startStream (System API)

## Modules to Import

```TypeScript
import { abilityConnectionManager } from 'abilityConnectionManager';
```

## startStream

```TypeScript
function startStream(streamId: int): void
```

Start Streaming

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityConnectionManager-function startStream(streamId: int): void--><!--Device-abilityConnectionManager-function startStream(streamId: int): void-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamId | int | Yes | Indicates the ID of a transport stream. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system App. |
| [32300002](../../apis-distributedservice-kit/errorcode-device-manager.md#32300002-stream-receive-end-not-started) | The stream at the receive end is not started. |

