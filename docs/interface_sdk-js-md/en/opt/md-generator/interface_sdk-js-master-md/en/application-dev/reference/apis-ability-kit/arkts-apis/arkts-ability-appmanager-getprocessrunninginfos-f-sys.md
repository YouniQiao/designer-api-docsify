# getProcessRunningInfos (System API)

## Modules to Import

```TypeScript
import { appManager } from '@kit.AbilityKit';
```

## getProcessRunningInfos

```TypeScript
function getProcessRunningInfos(): Promise<Array<ProcessInformation>>
```

Obtains information about the running processes of the current application. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [getRunningProcessInformation](arkts-ability-appmanager-getrunningprocessinformation-f.md#getRunningProcessInformation)

**Required permissions:** 
- API version 9 - 10: ohos.permission.GET_RUNNING_INFO

<!--Device-appManager-function getProcessRunningInfos(): Promise<Array<ProcessInformation>>--><!--Device-appManager-function getProcessRunningInfos(): Promise<Array<ProcessInformation>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;ProcessInformation & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |


## getProcessRunningInfos

```TypeScript
function getProcessRunningInfos(callback: AsyncCallback<Array<ProcessInformation>>): void
```

Obtains information about the running processes of the current application. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [getRunningProcessInformation](arkts-ability-appmanager-getrunningprocessinformation-f.md#getRunningProcessInformation)

**Required permissions:** 
- API version 9 - 10: ohos.permission.GET_RUNNING_INFO

<!--Device-appManager-function getProcessRunningInfos(callback: AsyncCallback<Array<ProcessInformation>>): void--><!--Device-appManager-function getProcessRunningInfos(callback: AsyncCallback<Array<ProcessInformation>>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;ProcessInformation&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
