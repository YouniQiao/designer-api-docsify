# exitMasterProcessRole

## Modules to Import

```TypeScript
import { application } from 'kits/@kit.AbilityKit';
```

## exitMasterProcessRole

```TypeScript
export function exitMasterProcessRole(): Promise<void>
```

Relinquishes the [master-process](../../../application-models/ability-terminology.md#master-process) role from the current process. This API uses a promise to return the result. This API can be properly called only on 2-in-1 devices and tablets. If it is called on other device types, error code 801 is returned.

**Since:** 21

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [16000118](../errorcode-ability.md#16000118-process-is-not-the-master-process) |
| [16000119](../errorcode-ability.md#16000119-pending-request-exists) |
