# acquireFormData (System API)

## Modules to Import

```TypeScript
```

## acquireFormData

```TypeScript
function acquireFormData(formId: string, callback: AsyncCallback<Record<string, Object>>): void
```

Requests data from the widget provider. This API uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.REQUIRE_FORM

**Model restriction:** This API can be used only in the stage model.

<!--Device-formHost-function acquireFormData(formId: string, callback: AsyncCallback<Record<string, Object>>): void--><!--Device-formHost-function acquireFormData(formId: string, callback: AsyncCallback<Record<string, Object>>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, Object&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
| [16500060](../errorcode-form.md#16500060-service-connection-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16500100](../errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) |


## acquireFormData

```TypeScript
function acquireFormData(formId: string): Promise<Record<string, Object>>
```

Requests data from the widget provider. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.REQUIRE_FORM

**Model restriction:** This API can be used only in the stage model.

<!--Device-formHost-function acquireFormData(formId: string): Promise<Record<string, Object>>--><!--Device-formHost-function acquireFormData(formId: string): Promise<Record<string, Object>>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;{ [key: string]: Object |
| Promise&lt;[Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, Object&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
| [16500060](../errorcode-form.md#16500060-service-connection-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16500100](../errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) |
