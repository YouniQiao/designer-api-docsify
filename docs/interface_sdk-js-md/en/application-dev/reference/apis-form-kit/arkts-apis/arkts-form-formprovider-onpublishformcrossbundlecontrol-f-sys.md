# onPublishFormCrossBundleControl (System API)

## Modules to Import

```TypeScript
import { formProvider } from '@kit.FormKit';
```

## onPublishFormCrossBundleControl

```TypeScript
function onPublishFormCrossBundleControl(callback: formInfo.PublishFormCrossBundleControlCallback): void
```

Subscribes to controls on cross-bundle widget addition to the home screen. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.PUBLISH_FORM_CROSS_BUNDLE_CONTROL

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | formInfo.PublishFormCrossBundleControlCallback | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |

**Examples**

```TypeScript
import { formProvider, formInfo } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  formProvider.onPublishFormCrossBundleControl((info: formInfo.PublishFormCrossBundleInfo) => {
    return true;
  });
  console.info(`onPublishFormCrossBundleControl success`);
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
}
```
