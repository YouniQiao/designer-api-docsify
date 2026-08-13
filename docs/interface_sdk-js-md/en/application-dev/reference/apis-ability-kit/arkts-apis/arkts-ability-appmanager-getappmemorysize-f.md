# getAppMemorySize

## Modules to Import

```TypeScript
import { appManager } from '@kit.AbilityKit';
```

## getAppMemorySize

```TypeScript
function getAppMemorySize(): Promise<int>
```

Obtains the maximum memory (RAM allocation) available to the current application. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-appManager-function getAppMemorySize(): Promise<int>--><!--Device-appManager-function getAppMemorySize(): Promise<int>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the maximum memory (RAM allocation) size, in MB. You can perform error processing or other custom processing based on the size. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |

## Examples

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

appManager.getAppMemorySize().then((data) => {
  console.info(`The size of app memory is: ${JSON.stringify(data)}`);
}).catch((error: BusinessError) => {
  console.error(`error: ${JSON.stringify(error)}`);
});
```


## getAppMemorySize

```TypeScript
function getAppMemorySize(callback: AsyncCallback<int>): void
```

Obtains the maximum memory (RAM allocation) available to the current application. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-appManager-function getAppMemorySize(callback: AsyncCallback<int>): void--><!--Device-appManager-function getAppMemorySize(callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | Yes | Callback used to return the result. If the API call is successful, **err** is **undefined** and **data** is the maximum memory (RAM allocation) available to the current application. Otherwise, **err** is an error object. You can perform error handling or other custom processing based on the return value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |

## Examples

```TypeScript
import { appManager } from '@kit.AbilityKit';

appManager.getAppMemorySize((err, data) => {
  if (err) {
    console.error(`getAppMemorySize fail, err: ${JSON.stringify(err)}`);
  } else {
    console.info(`The size of app memory is: ${JSON.stringify(data)}`);
  }
});
```

