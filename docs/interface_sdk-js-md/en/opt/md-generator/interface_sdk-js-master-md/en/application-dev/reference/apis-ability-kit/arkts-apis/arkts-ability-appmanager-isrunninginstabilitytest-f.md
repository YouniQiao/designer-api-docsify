# isRunningInStabilityTest

## Modules to Import

```TypeScript
import { appManager } from '@kit.AbilityKit';
```

## isRunningInStabilityTest

```TypeScript
function isRunningInStabilityTest(callback: AsyncCallback<boolean>): void
```

Checks whether the system is undergoing a stability test. This API uses an asynchronous callback to return the result. > **NOTE：**> > A stability test scenario refers to a specific testing environment designed to verify application reliability > under complex, extreme, or long-term operating conditions.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-appManager-function isRunningInStabilityTest(callback: AsyncCallback<boolean>): void--><!--Device-appManager-function isRunningInStabilityTest(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |

## Examples

```TypeScript
import { appManager } from '@kit.AbilityKit';

appManager.isRunningInStabilityTest((err, flag) => {
  if (err) {
    console.error(`isRunningInStabilityTest fail, err: ${JSON.stringify(err)}`);
  } else {
    console.info(`The result of isRunningInStabilityTest is: ${JSON.stringify(flag)}`);
  }
});
```


## isRunningInStabilityTest

```TypeScript
function isRunningInStabilityTest(): Promise<boolean>
```

Checks whether the system is undergoing a stability test. This API uses a promise to return the result. > **NOTE：**> > A stability test scenario refers to a specific testing environment designed to verify application reliability > under complex, extreme, or long-term operating conditions.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-appManager-function isRunningInStabilityTest(): Promise<boolean>--><!--Device-appManager-function isRunningInStabilityTest(): Promise<boolean>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |

## Examples

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

appManager.isRunningInStabilityTest().then((flag) => {
  console.info(`The result of isRunningInStabilityTest is: ${JSON.stringify(flag)}`);
}).catch((error: BusinessError) => {
  console.error(`error: ${JSON.stringify(error)}`);
});
```
