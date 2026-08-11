# onFreeze

## Modules to Import

```TypeScript
import { errorManager } from 'kits/@kit.AbilityKit';
```

## onFreeze

```TypeScript
function onFreeze(observer: FreezeObserver): void
```

Register an observer for freeze event.This function can only be called from main thread.Please note that each process only supports registering one observer.If you register multiple times, the later one will overwrite the previous one.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-errorManager-function onFreeze(observer: FreezeObserver): void--><!--Device-errorManager-function onFreeze(observer: FreezeObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observer | [FreezeObserver](arkts-ability-errormanager-freezeobserver-t.md) | Yes | The freeze event observer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16200001](../errorcode-ability.md#16200001-caller-released) | If the caller is invalid. |

