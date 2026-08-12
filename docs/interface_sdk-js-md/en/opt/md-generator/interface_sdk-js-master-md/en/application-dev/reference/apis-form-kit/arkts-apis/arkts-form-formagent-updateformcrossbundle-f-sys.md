# updateFormCrossBundle (System API)

## Modules to Import

```TypeScript
import { formAgent } from '@kit.FormKit';
```

## updateFormCrossBundle

```TypeScript
function updateFormCrossBundle(formId: string, formBindingData: formBindingData.FormBindingData): Promise<void>
```

Updates a widget by cross bundle. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.UPDATE_FORM_CROSS_BUNDLE

**Model restriction:** This API can be used only in the stage model.

<!--Device-formAgent-function updateFormCrossBundle(formId: string, formBindingData: formBindingData.FormBindingData): Promise<void>--><!--Device-formAgent-function updateFormCrossBundle(formId: string, formBindingData: formBindingData.FormBindingData): Promise<void>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |
| [formBindingData](arkts-app-form-formbindingdata.md) | formBindingData.FormBindingData | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16501003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501003-widget-not-operatable) |
| [16501001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501001-widget-id-not-exist) |
| [16501000](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501000-internal-function-error) |
| [16501007](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501007-untrusted-widget) |
| [16500060](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500060-service-connection-failure) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [16500050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500050-ipc-failure) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
