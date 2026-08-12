# getProcessRunningInformation (System API)

## getProcessRunningInformation

```TypeScript
function getProcessRunningInformation(): Promise<Array<ProcessRunningInfo>>
```

Obtains information about the running processes. This API uses a promise to return the result.

> This API is deprecated since API version 9. You are advised to use
> [appManager.getRunningProcessInformation](arkts-ability-appmanager-getrunningprocessinformation-f.md#getRunningProcessInformation)
> instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getRunningProcessInformation](ohos.app.ability.appManager:appManager#getRunningProcessInformation)

**Required permissions:** 
- API version 8 - 10: ohos.permission.GET_RUNNING_INFO

<!--Device-appManager-function getProcessRunningInformation(): Promise<Array<ProcessRunningInfo>>--><!--Device-appManager-function getProcessRunningInformation(): Promise<Array<ProcessRunningInfo>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[ProcessRunningInfo](arkts-ability-processrunninginfo-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |


## getProcessRunningInformation

```TypeScript
function getProcessRunningInformation(callback: AsyncCallback<Array<ProcessRunningInfo>>): void
```

Obtains information about the running processes. This API uses an asynchronous callback to return the result.

> This API is deprecated since API version 9. You are advised to use
> [appManager.getRunningProcessInformation]{
> @link @ohos.app.ability.appManager:appManager.getRunningProcessInformation()} instead.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getRunningProcessInformation](ohos.app.ability.appManager:appManager#getRunningProcessInformation)

**Required permissions:** 
- API version 8 - 10: ohos.permission.GET_RUNNING_INFO

<!--Device-appManager-function getProcessRunningInformation(callback: AsyncCallback<Array<ProcessRunningInfo>>): void--><!--Device-appManager-function getProcessRunningInformation(callback: AsyncCallback<Array<ProcessRunningInfo>>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[ProcessRunningInfo](arkts-ability-processrunninginfo-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
