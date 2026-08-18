# on_globalUnhandledRejectionDetected

## Modules to Import

```TypeScript
import { errorManager } from '@kit.AbilityKit';
```

## on_globalUnhandledRejectionDetected('globalUnhandledRejectionDetected')

```TypeScript
function on(type: 'globalUnhandledRejectionDetected', observer: GlobalObserver): void
```

Registers a rejected promise observer with any thread in the process. Once registered, it can capture a rejected promise that is not captured in the current thread of the application.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-errorManager-function on(type: 'globalUnhandledRejectionDetected', observer: GlobalObserver): void--><!--Device-errorManager-function on(type: 'globalUnhandledRejectionDetected', observer: GlobalObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'globalUnhandledRejectionDetected' | Yes | Event type. It is fixed at **'globalUnhandledRejectionDetected'**, indicating an observer for the promise rejection. |
| observer | [GlobalObserver](arkts-ability-errormanager-globalobserver-t.md) | Yes | Observer to register. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16200001](../errorcode-ability.md#16200001-caller-released) | If the caller is invalid. |

**Examples**

```TypeScript
import { errorManager } from '@kit.AbilityKit';

function promiseFunc(observer: errorManager.GlobalError) {
  console.info("result name :" + observer.name);
  console.info("result message :" + observer.message);
  console.info("result stack :" + observer.stack);
  console.info("result instanceName :" + observer.instanceName);
  console.info("result instanceType :" + observer.instanceType);
}

errorManager.on("globalUnhandledRejectionDetected", promiseFunc);
// You are advised to use async to throw a promise exception.
async function throwError() {
  throw new Error("uncaught error");
}

let promise1 = new Promise<void>(() => {}).then(() => {
  throwError();
});
```

