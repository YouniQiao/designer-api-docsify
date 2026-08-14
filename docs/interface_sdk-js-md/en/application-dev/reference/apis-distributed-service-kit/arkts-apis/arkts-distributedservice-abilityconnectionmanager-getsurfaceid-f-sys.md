# getSurfaceId (System API)

## Modules to Import

```TypeScript
import { abilityConnectionManager } from 'abilityConnectionManager';
```

## getSurfaceId

```TypeScript
function getSurfaceId(streamId: int, param: SurfaceParam): string
```

Obtains the transmission surface.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityConnectionManager-function getSurfaceId(streamId: int, param: SurfaceParam): string--><!--Device-abilityConnectionManager-function getSurfaceId(streamId: int, param: SurfaceParam): string-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamId | int | Yes | Indicates the ID of a transport stream. |
| param | [SurfaceParam](arkts-distributedservice-abilityconnectionmanager-surfaceparam-i-sys.md) | Yes | Surface Parameters |

**Return value:**

| Type | Description |
| --- | --- |
| string | Returns the ID of a surface. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system App. |

