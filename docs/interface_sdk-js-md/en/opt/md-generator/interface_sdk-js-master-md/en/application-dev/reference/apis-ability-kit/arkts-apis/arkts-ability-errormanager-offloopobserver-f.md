# off_loopObserver

## Modules to Import

```TypeScript
```

## off_loopObserver

```TypeScript
function off(type: 'loopObserver', observer?: LoopObserver): void
```

Unregisters an observer for the message processing duration of the main thread. This API can only be used in the main thread. If a thread error occurs, an error code is thrown. You are advised to handle it with try-catch logic.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-errorManager-function off(type: 'loopObserver', observer?: LoopObserver): void--><!--Device-errorManager-function off(type: 'loopObserver', observer?: LoopObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'loopObserver' | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [LoopObserver](arkts-ability-loopobserver-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

**Examples**

```TypeScript
import { errorManager } from '@kit.AbilityKit';

errorManager.off("loopObserver");
```
