# on_loopObserver

## Modules to Import

```TypeScript
import { errorManager } from '@kit.AbilityKit';
import { errorManager } from '@kit.AbilityKit';
```

## on_loopObserver

```TypeScript
function on(type: 'loopObserver', timeout: number, observer: LoopObserver): void
```

Registers an observer for the message processing duration of the main thread. After the registration, the execution time of a message processed by the main thread of the application can be captured. This API can only be used in the main thread. If a thread error occurs, an error code is thrown. You are advised to handle it with try-catch logic.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-errorManager-function on(type: 'loopObserver', timeout: number, observer: LoopObserver): void--><!--Device-errorManager-function on(type: 'loopObserver', timeout: number, observer: LoopObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'loopObserver' | Yes | Event type. It is fixed at **'loopObserver'**, indicating an observer for the message processing duration of the main thread. |
| timeout | number | Yes | Event execution threshold, in milliseconds. The value must be greater than **0**.The unit is milliseconds(ms). |
| observer | LoopObserver | Yes | Observer to register. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Examples**

```TypeScript
import { errorManager } from '@kit.AbilityKit';

let observer: errorManager.LoopObserver = {
  onLoopTimeOut(timeout: number) {
    console.info('Duration timeout: ' + timeout);
  }
};

errorManager.on("loopObserver", 1, observer);
```

