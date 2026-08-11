# getRunningFormInfoById (System API)

## Modules to Import

```TypeScript
import { formObserver } from 'kits/@kit.FormKit';
```

## getRunningFormInfoById

```TypeScript
function getRunningFormInfoById(formId: string): Promise<formInfo.RunningFormInfo>
```

Obtains the RunningFormInfo object by formId.

**Since:** 10

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

**Model restriction:** This API can be used only in the stage model.

<!--Device-formObserver-function getRunningFormInfoById(formId: string): Promise<formInfo.RunningFormInfo>--><!--Device-formObserver-function getRunningFormInfoById(formId: string): Promise<formInfo.RunningFormInfo>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;formInfo.RunningFormInfo&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16500100](../errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) |


## getRunningFormInfoById

```TypeScript
function getRunningFormInfoById(formId: string, isUnusedIncluded: boolean): Promise<formInfo.RunningFormInfo>
```

Obtains the RunningFormInfo object by formId.

**Since:** 11

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

**Model restriction:** This API can be used only in the stage model.

<!--Device-formObserver-function getRunningFormInfoById(formId: string, isUnusedIncluded: boolean): Promise<formInfo.RunningFormInfo>--><!--Device-formObserver-function getRunningFormInfoById(formId: string, isUnusedIncluded: boolean): Promise<formInfo.RunningFormInfo>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |
| isUnusedIncluded | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;formInfo.RunningFormInfo&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16500100](../errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) |


## getRunningFormInfoById

```TypeScript
function getRunningFormInfoById(formId: string, callback: AsyncCallback<formInfo.RunningFormInfo>): void
```

Obtains the RunningFormInfo object by formId.

**Since:** 10

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

**Model restriction:** This API can be used only in the stage model.

<!--Device-formObserver-function getRunningFormInfoById(formId: string, callback: AsyncCallback<formInfo.RunningFormInfo>): void--><!--Device-formObserver-function getRunningFormInfoById(formId: string, callback: AsyncCallback<formInfo.RunningFormInfo>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;formInfo.RunningFormInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16500100](../errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) |


## getRunningFormInfoById

```TypeScript
function getRunningFormInfoById(
    formId: string,
    isUnusedIncluded: boolean,
    callback: AsyncCallback<formInfo.RunningFormInfo>
  ): void
```

Obtains the RunningFormInfo object by formId.

**Since:** 11

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

**Model restriction:** This API can be used only in the stage model.

<!--Device-formObserver-function getRunningFormInfoById(    formId: string,    isUnusedIncluded: boolean,    callback: AsyncCallback<formInfo.RunningFormInfo>  ): void--><!--Device-formObserver-function getRunningFormInfoById(    formId: string,    isUnusedIncluded: boolean,    callback: AsyncCallback<formInfo.RunningFormInfo>  ): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |
| isUnusedIncluded | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;formInfo.RunningFormInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16500100](../errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) |
