# on_globalErrorOccurred

## Modules to Import

```TypeScript
import { errorManager } from 'errorManager';
```

## on_globalErrorOccurred

```TypeScript
function on(type: 'globalErrorOccurred', observer: GlobalObserver): void
```

Registers a global error observer via the **errorManager.on** API within any thread of a process. Once registered, it can capture exceptions occurring in any thread across the entire process. When the observer captures such an exception, the application will not exit automatically. You are advised to add a synchronous exit operation after the callback function completes.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-errorManager-function on(type: 'globalErrorOccurred', observer: GlobalObserver): void--><!--Device-errorManager-function on(type: 'globalErrorOccurred', observer: GlobalObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'globalErrorOccurred' | Yes | Event type. It is fixed at **'globalErrorOccurred'**. |
| observer | [GlobalObserver](arkts-ability-errormanager-globalobserver-t.md) | Yes | Customized callback function for exception handling. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16200001](../errorcode-ability.md#16200001-caller-released) | If the caller is invalid. |

**Examples**

```TypeScript
import { errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

function errorFunc(observer: errorManager.GlobalError) {
    console.info("result name :" + observer.name);
    console.info("result message :" + observer.message);
    console.info("result stack :" + observer.stack);
    console.info("result instanceName :" + observer.instanceName);
    console.info("result instanceType :" + observer.instanceType);
}

try {
  errorManager.on('globalErrorOccurred', errorFunc);
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`error: ${code}, ${message}`);
}
```

