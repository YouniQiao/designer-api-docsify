# destroyStream (System API)

## Modules to Import

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
```

## destroyStream

```TypeScript
function destroyStream(streamId: int): void
```

Destroy the Stream.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityConnectionManager-function destroyStream(streamId: int): void--><!--Device-abilityConnectionManager-function destroyStream(streamId: int): void-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamId | int | Yes | Indicates the ID of a transport stream. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system App. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

