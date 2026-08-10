# getRunningFormInfosByFilter (System API)

## Modules to Import

```TypeScript
import { formObserver } from 'kits/@kit.FormKit';
```

## getRunningFormInfosByFilter

```TypeScript
function getRunningFormInfosByFilter(
    formProviderFilter: formInfo.FormProviderFilter
  ): Promise<Array<formInfo.RunningFormInfo>>
```

Obtains the RunningFormInfo objects by FormProviderFilter.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

**Model restriction:** This API can be used only in the stage model.

<!--Device-formObserver-function getRunningFormInfosByFilter(    formProviderFilter: formInfo.FormProviderFilter  ): Promise<Array<formInfo.RunningFormInfo>>--><!--Device-formObserver-function getRunningFormInfosByFilter(    formProviderFilter: formInfo.FormProviderFilter  ): Promise<Array<formInfo.RunningFormInfo>>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formProviderFilter | formInfo.FormProviderFilter | Yes | Indicates the form provider app info. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;formInfo.RunningFormInfo&gt;&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16501000 | An internal functional error occurred. |
| 201 | Permissions denied. |
| 16500050 | IPC connection error. |
| 202 | The application is not a system application. |
| 16500100 | Failed to obtain the configuration information. |


## getRunningFormInfosByFilter

```TypeScript
function getRunningFormInfosByFilter(
    formProviderFilter: formInfo.FormProviderFilter,
    callback: AsyncCallback<Array<formInfo.RunningFormInfo>>
  ): void
```

Obtains the RunningFormInfo objects by FormProviderFilter.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

**Model restriction:** This API can be used only in the stage model.

<!--Device-formObserver-function getRunningFormInfosByFilter(    formProviderFilter: formInfo.FormProviderFilter,    callback: AsyncCallback<Array<formInfo.RunningFormInfo>>  ): void--><!--Device-formObserver-function getRunningFormInfosByFilter(    formProviderFilter: formInfo.FormProviderFilter,    callback: AsyncCallback<Array<formInfo.RunningFormInfo>>  ): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formProviderFilter | formInfo.FormProviderFilter | Yes | Indicates the form provider app info. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;formInfo.RunningFormInfo&gt;&gt; | Yes | The callback of getFormInstancesByFilter. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16501000 | An internal functional error occurred. |
| 201 | Permissions denied. |
| 16500050 | IPC connection error. |
| 202 | The application is not a system application. |
| 16500100 | Failed to obtain the configuration information. |

