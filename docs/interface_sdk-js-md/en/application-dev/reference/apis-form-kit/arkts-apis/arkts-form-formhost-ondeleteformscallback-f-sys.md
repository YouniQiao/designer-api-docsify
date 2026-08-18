# onDeleteFormsCallback (System API)

## Modules to Import

```TypeScript
import { formHost } from '@kit.FormKit';
import { formHost } from '@kit.FormKit';
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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | formInfo.DeleteFormsCallback | Yes | Identifies the callback for deleting forms. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permissions denied. |
| [16500050](../errorcode-form.md#16500050-ipc-failure) | IPC connection error. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not a system application. |

