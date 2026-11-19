# getRunningProcessInformation

## Modules to Import

```TypeScript
import { appManager } from '@kit.AbilityKit';
```

## getRunningProcessInformation

```TypeScript
function getRunningProcessInformation(): Promise<Array<ProcessInformation>>
```

Obtain information about application running processes. Use Promise asynchronous callbacks.

> **NOTE:** 
> 
> - For versions earlier than API version 11, you need to apply for the ohos.permission.GET_RUNNING_INFO permission to query the running process information of all applications.
> 
> - From API version 11, only the running process information of the caller is returned by default. If you have the ohos.permission.GET_RUNNING_INFO permission,You can query the running process information of all applications.

**Since:** 9

**Required permissions:** 
- API version 11 and later: N/A
- API versions 9 to 10: ohos.permission.GET_RUNNING_INFO

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-appManager-function getRunningProcessInformation(): Promise<Array<ProcessInformation>>--><!--Device-appManager-function getRunningProcessInformation(): Promise<Array<ProcessInformation>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[ProcessInformation](arkts-ability-appmanager-processinformation-t.md)&gt;&gt; | Promise used to return the API call result and the process running information. You can perform error handling or custom processing in this callback. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |

**Examples**

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

appManager.getRunningProcessInformation().then((data) => {
  console.info(`The running process information is: ${JSON.stringify(data)}`);
}).catch((error: BusinessError) => {
  console.error(`code: ${error.code}, msg:${error.message}`);
});
```


## getRunningProcessInformation

```TypeScript
function getRunningProcessInformation(callback: AsyncCallback<Array<ProcessInformation>>): void
```

Obtain information about application running processes. Use callback asynchronous callback.

> **NOTE:** 
> 
> - For versions earlier than API version 11, you need to apply for the ohos.permission.GET_RUNNING_INFO permission to query the running process information of all applications.
> 
> - From API version 11, only the running process information of the caller is returned by default. If you have the ohos.permission.GET_RUNNING_INFO permission,You can query the running process information of all applications.

**Since:** 9

**Required permissions:** 
- API version 11 and later: N/A
- API versions 9 to 10: ohos.permission.GET_RUNNING_INFO

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-appManager-function getRunningProcessInformation(callback: AsyncCallback<Array<ProcessInformation>>): void--><!--Device-appManager-function getRunningProcessInformation(callback: AsyncCallback<Array<ProcessInformation>>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[ProcessInformation](arkts-ability-appmanager-processinformation-t.md)&gt;&gt; | Yes | Callback used to return the result. If the API call is successful, **err** is **undefined** and **data** is the information about the running processes. Otherwise, **err** is an error object. You can perform error handling or other custom processing. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;         2. Incorrect parameter types; 3. Parameter verification failed. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |

**Examples**

```TypeScript
import { appManager } from '@kit.AbilityKit';

appManager.getRunningProcessInformation((err, data) => {
  if (err) {
    console.error(`getRunningProcessInformation fail, code: ${err.code}, msg:${err.message}`);
  } else {
    console.info(`The running process information is: ${JSON.stringify(data)}`);
  }
});
```
