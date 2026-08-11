# onDeleteFormsCallback (System API)

## Modules to Import

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## onDeleteFormsCallback

```TypeScript
function onDeleteFormsCallback(callback: formInfo.DeleteFormsCallback): void
```

Register the callback for deleting forms.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

<!--Device-formHost-function onDeleteFormsCallback(callback: formInfo.DeleteFormsCallback): void--><!--Device-formHost-function onDeleteFormsCallback(callback: formInfo.DeleteFormsCallback): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | formInfo.DeleteFormsCallback | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { formHost, formInfo } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  const callback = (formIds: string[]): void => {
    console.info(`onDeleteFormsCallback formIds length: ${formIds.length}`);
    for (let formId of formIds) {
      console.info(`deleted formId: ${formId}`);
    }
  };
  formHost.onDeleteFormsCallback(callback);
  console.info(`onDeleteFormsCallback success`);
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```
