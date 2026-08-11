# setDefaultFreezeObserver

## Modules to Import

```TypeScript
import { errorManager } from 'kits/@kit.AbilityKit';
```

## setDefaultFreezeObserver

```TypeScript
function setDefaultFreezeObserver(defaultObserver?: FreezeObserver) : FreezeObserver
```

Set the default freeze observer, This function will be executed right after the callback function registered through errorManager.on is executed. You can use it to implement chain calls instead of errorManager.on.If an empty observer is set for a certain module, it will cause the call chain to be interrupted.This API must be called in the main thread.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-errorManager-function setDefaultFreezeObserver(defaultObserver?: FreezeObserver) : FreezeObserver--><!--Device-errorManager-function setDefaultFreezeObserver(defaultObserver?: FreezeObserver) : FreezeObserver-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| defaultObserver | [FreezeObserver](arkts-ability-errormanager-freezeobserver-t.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [FreezeObserver](arkts-ability-errormanager-freezeobserver-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [16000205](../errorcode-ability.md#16000205-api-not-called-in-main-thread) |
