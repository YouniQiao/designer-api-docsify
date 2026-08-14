# updateSurfaceParam (System API)

## Modules to Import

```TypeScript
import { abilityConnectionManager } from 'abilityConnectionManager';
```

## updateSurfaceParam

```TypeScript
function updateSurfaceParam(streamId: int, param: SurfaceParam): void
```

Update surface parameters.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityConnectionManager-function updateSurfaceParam(streamId: int, param: SurfaceParam): void--><!--Device-abilityConnectionManager-function updateSurfaceParam(streamId: int, param: SurfaceParam): void-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| streamId | int | Yes | Stream ID. |
| param | [SurfaceParam](arkts-distributedservice-abilityconnectionmanager-surfaceparam-i-sys.md) | Yes | Surface Parameters |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system App. |

