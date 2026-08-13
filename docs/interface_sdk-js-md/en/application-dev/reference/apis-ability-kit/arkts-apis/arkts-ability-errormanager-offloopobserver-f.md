# off_loopObserver

## Modules to Import

```TypeScript
import { errorManager } from '@kit.AbilityKit';
```

## off_loopObserver

```TypeScript
function off(type: 'loopObserver', observer?: LoopObserver): void
```

Unregisters an observer for the message processing duration of the main thread. This API can only be used in the main thread. If a thread error occurs, an error code is thrown. You are advised to handle it with try-catch logic.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-errorManager-function off(type: 'loopObserver', observer?: LoopObserver): void--><!--Device-errorManager-function off(type: 'loopObserver', observer?: LoopObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'loopObserver' | Yes | Event type. It is fixed at **'loopObserver'**, indicating an observer for the message processing duration of the main thread. |
| observer | LoopObserver | No | Observer to unregister. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
import { errorManager } from '@kit.AbilityKit';

errorManager.off("loopObserver");
```

