# setDefaultFreezeObserver

## Modules to Import

```TypeScript
import { errorManager } from 'kits/@kit.AbilityKit';
```

## setDefaultFreezeObserver

```TypeScript
function setDefaultFreezeObserver(defaultObserver?: FreezeObserver) : FreezeObserver
```

设置默认冻屏观测器。此函数将在通过errorManager.on注册的回调函数执行后立即执行。可用于替代errorManager.on实现链式调用。如果为某个模块设置空观测器，将导致调用链中断。

此API必须在主线程中调用。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-errorManager-function setDefaultFreezeObserver(defaultObserver?: FreezeObserver) : FreezeObserver--><!--Device-errorManager-function setDefaultFreezeObserver(defaultObserver?: FreezeObserver) : FreezeObserver-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| defaultObserver | [FreezeObserver](arkts-ability-errormanager-freezeobserver-t.md) | No | 默认冻屏观测器。 |

**Return value:**

| Type | Description |
| --- | --- |
| [FreezeObserver](arkts-ability-errormanager-freezeobserver-t.md) | 返回原来的默认冻屏观测器。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16000205 | API未在主线程中调用。 |

