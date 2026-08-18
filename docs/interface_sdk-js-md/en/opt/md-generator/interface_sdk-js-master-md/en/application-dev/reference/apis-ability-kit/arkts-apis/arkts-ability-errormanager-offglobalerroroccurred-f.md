# off_globalErrorOccurred

## Modules to Import

```TypeScript
```

## off_globalErrorOccurred

```TypeScript
function off(type: 'globalErrorOccurred', observer?: GlobalObserver): void
```

Unregisters a global error observer. Once unregistered, global listening cannot be implemented. If the observer passed in is not in the observer queue registered via the **on** API, error code 16300004 is thrown. Therefore, you are advised to handle this using **try-catch** logic.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-errorManager-function off(type: 'globalErrorOccurred', observer?: GlobalObserver): void--><!--Device-errorManager-function off(type: 'globalErrorOccurred', observer?: GlobalObserver): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'globalErrorOccurred' | Yes |
| [observer](../../apis-arkui/arkts-apis/arkts-arkui-viewmodel-observer-i.md) | [GlobalObserver](arkts-ability-errormanager-globalobserver-t.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16200001](../errorcode-ability.md#16200001-caller-released) |
| [16300004](../errorcode-ability.md#16300004-observer-does-not-exist) |

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
  errorManager.off('globalErrorOccurred', errorFunc)
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`error: ${code}, ${message}`);
}
```
