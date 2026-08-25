# getRunningProcessInformation

## Modules to Import

```TypeScript
import { appManager } from 'kits/@kit.AbilityKit';
```

## getRunningProcessInformation

```TypeScript
function getRunningProcessInformation(): Promise<Array<ProcessInformation>>
```

Obtains information about the running processes of the current application. This API uses a promise to return the result.

> **NOTE：**&gt;
> - In versions earlier than API version 11, this API requires the ohos.permission.GET_RUNNING_INFO permission,
> which is available only for system applications.&gt;
> - Starting from API version 11, this API is used only to obtain the process information of the caller. No
> permission is required.

**Since:** 9

**Required permissions:** 
- API version 9 - 10: ohos.permission.GET_RUNNING_INFO

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;ProcessInformation & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |


## getRunningProcessInformation

```TypeScript
function getRunningProcessInformation(callback: AsyncCallback<Array<ProcessInformation>>): void
```

Obtains information about the running processes of the current application. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> - In versions earlier than API version 11, this API requires the ohos.permission.GET_RUNNING_INFO permission,
> which is available only for system applications.&gt;
> - Starting from API version 11, this API is used only to obtain the process information of the caller. No
> permission is required.

**Since:** 9

**Required permissions:** 
- API version 9 - 10: ohos.permission.GET_RUNNING_INFO

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;ProcessInformation&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
