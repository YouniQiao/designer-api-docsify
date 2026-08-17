# on_error

## Modules to Import

```TypeScript
import { errorManager } from 'errorManager';
```

## on_error

```TypeScript
function on(type: 'error', observer: ErrorObserver): number
```

Registers an error observer. Once registered, it can capture JavaScript crashes occurring within the application, which are a type of application crash. When the observer captures such an exception, the application will not exit automatically. You are advised to add a synchronous exit operation after the callback function completes. This API can only be used in the main thread. If a thread error occurs, an error code is thrown. You are advised to handle it with try-catch logic.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-errorManager-function on(type: 'error', observer: ErrorObserver): number--><!--Device-errorManager-function on(type: 'error', observer: ErrorObserver): number-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'error' | Yes | Event type. It is fixed at **'error'**. |
| observer | ErrorObserver | Yes | Error observer instance. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Unique index of the observer, which corresponds one-to-one with the observer. This value can be used as the **observerId** parameter in the **errorManager.off** function. There is no specific unit. the returned result is observerId. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16000003](../errorcode-ability.md#16000003-id-does-not-exist) | The specified ID does not exist. |

**Examples**

```TypeScript
import { errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let observer: errorManager.ErrorObserver = {
  onUnhandledException(errorMsg) {
    console.info('onUnhandledException, errorMsg: ', errorMsg);
  },
  onException(errorObj) {
    console.info('onException, name: ', errorObj.name);
    console.info('onException, message: ', errorObj.message);
    if (typeof(errorObj.stack) === 'string') {
      console.info('onException, stack: ', errorObj.stack);
    }
  }
};
let observerId = -1;

try {
  observerId = errorManager.on('error', observer);
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`error: ${code}, ${message}`);
}
```

