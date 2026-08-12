# offTemplateFormDetailInfoChange (System API)

## Modules to Import

```TypeScript
import { formHost } from '@kit.FormKit';
```

## offTemplateFormDetailInfoChange

```TypeScript
function offTemplateFormDetailInfoChange(callback?: formInfo.TemplateFormDetailInfoCallback): void
```

Unsubscribes from changes in the static configuration information of template widgets. This API uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

<!--Device-formHost-function offTemplateFormDetailInfoChange(callback?: formInfo.TemplateFormDetailInfoCallback): void--><!--Device-formHost-function offTemplateFormDetailInfoChange(callback?: formInfo.TemplateFormDetailInfoCallback): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | formInfo.TemplateFormDetailInfoCallback | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [16500050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500050-ipc-failure) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { formHost } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  formHost.offTemplateFormDetailInfoChange();
  console.info(`offTemplateFormDetailInfoChange success`);
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```
