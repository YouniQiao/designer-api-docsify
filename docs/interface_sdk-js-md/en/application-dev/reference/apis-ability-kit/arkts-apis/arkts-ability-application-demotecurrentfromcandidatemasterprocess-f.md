# demoteCurrentFromCandidateMasterProcess

## Modules to Import

```TypeScript
import { application } from 'kits/@kit.AbilityKit';
```

## demoteCurrentFromCandidateMasterProcess

```TypeScript
export function demoteCurrentFromCandidateMasterProcess(): Promise<void>
```

Removes the current process from the candidate master process list. This API uses a promise to return the result. This API can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code 801 is returned. **System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Since:** 20

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
| [16000116](../errorcode-ability.md#16000116-process-is-already-a-master-process) |
| [16000117](../errorcode-ability.md#16000117-process-is-not-a-candidate-master-process) |
