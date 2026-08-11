# acquireFormState (System API)

## Modules to Import

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## acquireFormState

```TypeScript
function acquireFormState(want: Want, callback: AsyncCallback<formInfo.FormStateInfo>): void
```

Obtains the widget state. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.REQUIRE_FORM and ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-formHost-function acquireFormState(want: Want, callback: AsyncCallback<formInfo.FormStateInfo>): void--><!--Device-formHost-function acquireFormState(want: Want, callback: AsyncCallback<formInfo.FormStateInfo>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;formInfo.FormStateInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
| [16500060](../errorcode-form.md#16500060-service-connection-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16500100](../errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) |


## acquireFormState

```TypeScript
function acquireFormState(want: Want): Promise<formInfo.FormStateInfo>
```

Obtains the widget state. This API uses a promise to return the result.

**Since:** 9

**Required permissions:** ohos.permission.REQUIRE_FORM and ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-formHost-function acquireFormState(want: Want): Promise<formInfo.FormStateInfo>--><!--Device-formHost-function acquireFormState(want: Want): Promise<formInfo.FormStateInfo>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;formInfo.FormStateInfo&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
| [16500060](../errorcode-form.md#16500060-service-connection-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16500100](../errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) |
