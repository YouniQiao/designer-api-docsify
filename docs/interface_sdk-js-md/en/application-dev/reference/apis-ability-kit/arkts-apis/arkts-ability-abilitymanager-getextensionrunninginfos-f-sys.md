# getExtensionRunningInfos (System API)

## Modules to Import

```TypeScript
import { abilityManager } from '@kit.AbilityKit';
```

## getExtensionRunningInfos

```TypeScript
function getExtensionRunningInfos(upperLimit: number): Promise<Array<ExtensionRunningInfo>>
```

Obtains the ExtensionAbility running information. This API uses a promise to return the result.

**Since:** 9

**Required permissions:** ohos.permission.GET_RUNNING_INFO

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| upperLimit | number | Yes | Maximum number of messages that can be obtained. The maximum value is 2&lt;sup&gt;31&lt;/sup&gt;-1. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;ExtensionRunningInfo&gt;&gt; | Promise used to return the API call result and the ExtensionAbility running information. You can perform error handling or other custom processing. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |

**Examples**

```TypeScript
import { abilityManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let upperLimit = 10;

try {
  abilityManager.getExtensionRunningInfos(upperLimit).then((data: Array<abilityManager.ExtensionRunningInfo>) => {
    console.info(`getExtensionRunningInfos success, data: ${JSON.stringify(data)}`);
  }).catch((err: BusinessError) => {
    console.error(`getExtensionRunningInfos fail, err: ${JSON.stringify(err)}`);
  });
} catch (paramError) {
  let code: number = (paramError as BusinessError).code;
  let message: string = (paramError as BusinessError).message;
  console.error(`error.code: ${code}, error.message: ${message}`);
}
```


## getExtensionRunningInfos

```TypeScript
function getExtensionRunningInfos(upperLimit: number, callback: AsyncCallback<Array<ExtensionRunningInfo>>): void
```

Obtains the ExtensionAbility running information. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.GET_RUNNING_INFO

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| upperLimit | number | Yes | Maximum number of messages that can be obtained. The maximum value is 2&lt;sup&gt;31&lt;/sup&gt;-1. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;ExtensionRunningInfo&gt;&gt; | Yes | Callback used to return the result. If the API call is successful, **err** is **undefined** and **data** is the ExtensionAbility running information obtained. Otherwise, **err** is an error object. You can perform error handling or other custom processing. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |

**Examples**

```TypeScript
import { abilityManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let upperLimit = 10;

try {
  abilityManager.getExtensionRunningInfos(upperLimit, (err: BusinessError, data: Array<abilityManager.ExtensionRunningInfo>) => {
    if (err) {
      console.error(`getExtensionRunningInfos fail, err: ${JSON.stringify(err)}`);
    } else {
      console.info(`getExtensionRunningInfos success, data: ${JSON.stringify(data)}`);
    }
  });
} catch (paramError) {
  let code: number = (paramError as BusinessError).code;
  let message: string = (paramError as BusinessError).message;
  console.error(`error.code: ${code}, error.message: ${message}`);
}
```
