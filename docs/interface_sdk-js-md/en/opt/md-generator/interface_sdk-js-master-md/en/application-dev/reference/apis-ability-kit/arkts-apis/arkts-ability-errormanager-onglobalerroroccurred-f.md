# on_globalErrorOccurred

## Modules to Import

```TypeScript
import { errorManager } from '@kit.AbilityKit';
```

## on_globalErrorOccurred

```TypeScript
function on(type: 'globalErrorOccurred', observer: GlobalObserver): void
```

Registers a global error observer via the **errorManager.on** API within any thread of a process. Once registered, it can capture exceptions occurring in any thread across the entire process. When the observer captures such an exception, the application will not exit automatically. You are advised to add a synchronous exit operation after the callback function completes.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-errorManager-function on(type: 'globalErrorOccurred', observer: GlobalObserver): void--><!--Device-errorManager-function on(type: 'globalErrorOccurred', observer: GlobalObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'globalErrorOccurred' | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [GlobalObserver](arkts-ability-errormanager-globalobserver-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |

## Examples

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
