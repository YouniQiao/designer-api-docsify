# getRunningFormInfosByFilter (System API)

## Modules to Import

```TypeScript
import { formObserver } from '@kit.FormKit';
```

## getRunningFormInfosByFilter

```TypeScript
function getRunningFormInfosByFilter(
    formProviderFilter: formInfo.FormProviderFilter
  ): Promise<Array<formInfo.RunningFormInfo>>
```

Obtains the RunningFormInfo objects by FormProviderFilter.

**Since:** 10

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

**Model restriction:** This API can be used only in the stage model.

<!--Device-formObserver-function getRunningFormInfosByFilter(    formProviderFilter: formInfo.FormProviderFilter  ): Promise<Array<formInfo.RunningFormInfo>>--><!--Device-formObserver-function getRunningFormInfosByFilter(    formProviderFilter: formInfo.FormProviderFilter  ): Promise<Array<formInfo.RunningFormInfo>>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formProviderFilter | formInfo.FormProviderFilter | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;formInfo.RunningFormInfo & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16501000](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501000-internal-function-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [16500050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500050-ipc-failure) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16500100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) |


## getRunningFormInfosByFilter

```TypeScript
function getRunningFormInfosByFilter(
    formProviderFilter: formInfo.FormProviderFilter,
    callback: AsyncCallback<Array<formInfo.RunningFormInfo>>
  ): void
```

Obtains the RunningFormInfo objects by FormProviderFilter.

**Since:** 10

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

**Model restriction:** This API can be used only in the stage model.

<!--Device-formObserver-function getRunningFormInfosByFilter(    formProviderFilter: formInfo.FormProviderFilter,    callback: AsyncCallback<Array<formInfo.RunningFormInfo>>  ): void--><!--Device-formObserver-function getRunningFormInfosByFilter(    formProviderFilter: formInfo.FormProviderFilter,    callback: AsyncCallback<Array<formInfo.RunningFormInfo>>  ): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formProviderFilter | formInfo.FormProviderFilter | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;formInfo.RunningFormInfo&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16501000](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501000-internal-function-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [16500050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500050-ipc-failure) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16500100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) |
