# on_loopObserver

## Modules to Import

```TypeScript
import { errorManager } from '@kit.AbilityKit';
```

## on_loopObserver

```TypeScript
function on(type: 'loopObserver', timeout: number, observer: LoopObserver): void
```

Registers an observer for the message processing duration of the main thread. After the registration, the execution time of a message processed by the main thread of the application can be captured. This API can only be used in the main thread. If a thread error occurs, an error code is thrown. You are advised to handle it with try-catch logic.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-errorManager-function on(type: 'loopObserver', timeout: number, observer: LoopObserver): void--><!--Device-errorManager-function on(type: 'loopObserver', timeout: number, observer: LoopObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'loopObserver' | Yes |
| timeout | number | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [LoopObserver](arkts-ability-loopobserver-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## Examples

```TypeScript
import { errorManager } from '@kit.AbilityKit';

let observer: errorManager.LoopObserver = {
  onLoopTimeOut(timeout: number) {
    console.info('Duration timeout: ' + timeout);
  }
};

errorManager.on("loopObserver", 1, observer);
```
