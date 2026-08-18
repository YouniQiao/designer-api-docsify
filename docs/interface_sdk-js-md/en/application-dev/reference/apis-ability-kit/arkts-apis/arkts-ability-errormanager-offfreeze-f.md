# offFreeze

## Modules to Import

```TypeScript
import { errorManager } from '@kit.AbilityKit';
```

## offFreeze

```TypeScript
function offFreeze(observer?: FreezeObserver): void
```

Unregister the observer for freeze event. This function can only be called from main thread.

**Since:** 24

<!--Device-errorManager-function offFreeze(observer?: FreezeObserver): void--><!--Device-errorManager-function offFreeze(observer?: FreezeObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observer | [FreezeObserver](arkts-ability-errormanager-freezeobserver-t.md) | No | The freeze event observer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16200001](../errorcode-ability.md#16200001-caller-released) | If the caller is invalid. |
| [16300004](../errorcode-ability.md#16300004-observer-does-not-exist) | If the observer does not exist. |

