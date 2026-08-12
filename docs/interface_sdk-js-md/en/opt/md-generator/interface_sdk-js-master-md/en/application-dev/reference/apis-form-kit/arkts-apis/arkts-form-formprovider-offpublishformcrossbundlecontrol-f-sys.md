# offPublishFormCrossBundleControl (System API)

## Modules to Import

```TypeScript
import { formProvider } from '@kit.FormKit';
```

## offPublishFormCrossBundleControl

```TypeScript
function offPublishFormCrossBundleControl(callback?: formInfo.PublishFormCrossBundleControlCallback): void
```

Unsubscribes from controls on cross-bundle widget addition to the home screen. This API uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.PUBLISH_FORM_CROSS_BUNDLE_CONTROL

**Model restriction:** This API can be used only in the stage model.

<!--Device-formProvider-function offPublishFormCrossBundleControl(callback?: formInfo.PublishFormCrossBundleControlCallback): void--><!--Device-formProvider-function offPublishFormCrossBundleControl(callback?: formInfo.PublishFormCrossBundleControlCallback): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | formInfo.PublishFormCrossBundleControlCallback | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [16500050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500050-ipc-failure) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
