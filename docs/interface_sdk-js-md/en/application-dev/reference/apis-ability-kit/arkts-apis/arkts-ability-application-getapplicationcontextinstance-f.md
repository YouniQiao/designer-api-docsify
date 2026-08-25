# getApplicationContextInstance

## Modules to Import

```TypeScript
import { application } from 'kits/@kit.AbilityKit';
```

## getApplicationContextInstance

```TypeScript
export function getApplicationContextInstance(): ApplicationContext
```

Obtains the application context. This API provides context access independent of the base class **Context**. Repeated calls to this API obtain the same ApplicationContext instance.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ApplicationContext](arkts-ability-applicationcontext-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
