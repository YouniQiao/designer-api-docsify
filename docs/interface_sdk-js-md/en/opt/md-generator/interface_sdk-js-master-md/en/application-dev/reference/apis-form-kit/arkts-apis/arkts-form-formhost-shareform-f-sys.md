# shareForm (System API)

## Modules to Import

```TypeScript
```

## shareForm

```TypeScript
function shareForm(formId: string, deviceId: string, callback: AsyncCallback<void>): void
```

Shares a specified widget with a remote device. This API uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.REQUIRE_FORM and ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-formHost-function shareForm(formId: string, deviceId: string, callback: AsyncCallback<void>): void--><!--Device-formHost-function shareForm(formId: string, deviceId: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |
| deviceId | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16501003](../errorcode-form.md#16501003-widget-not-operatable) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16501001](../errorcode-form.md#16501001-widget-id-not-exist) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |


## shareForm

```TypeScript
function shareForm(formId: string, deviceId: string): Promise<void>
```

Shares a specified widget with a remote device. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.REQUIRE_FORM and ohos.permission.DISTRIBUTED_DATASYNC

<!--Device-formHost-function shareForm(formId: string, deviceId: string): Promise<void>--><!--Device-formHost-function shareForm(formId: string, deviceId: string): Promise<void>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |
| deviceId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16501003](../errorcode-form.md#16501003-widget-not-operatable) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16501001](../errorcode-form.md#16501001-widget-id-not-exist) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
