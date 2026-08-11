# getAppMemorySize

## getAppMemorySize

```TypeScript
function getAppMemorySize(): Promise<number>
```

Obtains the maximum memory (RAM allocation) available to the current application. This API uses a promise to return  the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.app.ability.appManager/appManager#getAppMemorySize

<!--Device-appManager-function getAppMemorySize(): Promise<number>--><!--Device-appManager-function getAppMemorySize(): Promise<number>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

## Examples

```TypeScript
import appManager from '@ohos.application.appManager';
import { BusinessError } from '@ohos.base';

appManager.getAppMemorySize().then((data) => {
  console.info(`The size of app memory is: ${JSON.stringify(data)}`);
}).catch((error: BusinessError) => {
  console.error(`error: ${JSON.stringify(error)}`);
});
```


## getAppMemorySize

```TypeScript
function getAppMemorySize(callback: AsyncCallback<number>): void
```

Obtains the maximum memory (RAM allocation) available to the current application. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.app.ability.appManager/appManager#getAppMemorySize

<!--Device-appManager-function getAppMemorySize(callback: AsyncCallback<number>): void--><!--Device-appManager-function getAppMemorySize(callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## Examples

```TypeScript
import appManager from '@ohos.application.appManager';

appManager.getAppMemorySize((error, data) => {
  if (error && error.code !== 0) {
    console.error(`getAppMemorySize fail, error: ${JSON.stringify(error)}`);
  } else {
    console.info(`The size of app memory is: ${JSON.stringify(data)}`);
  }
});
```
