# setPublishFormResult (System API)

## Modules to Import

```TypeScript
import { formHost } from '@kit.FormKit';
```

## setPublishFormResult

```TypeScript
function setPublishFormResult(formId: string, result: formInfo.PublishFormResult): void
```

Sets the result for the operation of adding a widget to the home screen.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.REQUIRE_FORM

**Model restriction:** This API can be used only in the stage model.

<!--Device-formHost-function setPublishFormResult(formId: string, result: formInfo.PublishFormResult): void--><!--Device-formHost-function setPublishFormResult(formId: string, result: formInfo.PublishFormResult): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |
| result | formInfo.PublishFormResult | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16501001](../errorcode-form.md#16501001-widget-id-not-exist) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
| [16500060](../errorcode-form.md#16500060-service-connection-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
