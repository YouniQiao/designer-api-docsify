# recoverForms (System API)

## Modules to Import

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## recoverForms

```TypeScript
function recoverForms(formIds: Array<string>): Promise<void>
```

Recovers recycled widgets and updates their status to non-recyclable, or updates the status of widgets to non- recyclable if the widgets are not recycled. This API uses a promise to return the result.

**Since:** 11

**Required permissions:** ohos.permission.REQUIRE_FORM

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formIds | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [16500060](../errorcode-form.md#16500060-service-connection-failure) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |


## recoverForms

```TypeScript
function recoverForms(formIds: Array<string>, callback: AsyncCallback<void>): void
```

Recovers widgets. This API uses an asynchronous callback to return the result.

**Since:** 11

**Required permissions:** ohos.permission.REQUIRE_FORM

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formIds | Array & lt;string & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [16500060](../errorcode-form.md#16500060-service-connection-failure) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
