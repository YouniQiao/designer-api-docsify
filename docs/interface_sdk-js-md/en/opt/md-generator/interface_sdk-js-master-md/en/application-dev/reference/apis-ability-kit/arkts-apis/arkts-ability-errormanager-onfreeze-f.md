# onFreeze

## Modules to Import

```TypeScript
import { errorManager } from '@kit.AbilityKit';
```

## onFreeze

```TypeScript
function onFreeze(observer: FreezeObserver): void
```

Register an observer for freeze event. This function can only be called from main thread. Please note that each process only supports registering one observer. If you register multiple times, the later one will overwrite the previous one.

**Since:** 24

**Deprecated since:** -1

<!--Device-errorManager-function onFreeze(observer: FreezeObserver): void--><!--Device-errorManager-function onFreeze(observer: FreezeObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [FreezeObserver](arkts-ability-errormanager-freezeobserver-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |
