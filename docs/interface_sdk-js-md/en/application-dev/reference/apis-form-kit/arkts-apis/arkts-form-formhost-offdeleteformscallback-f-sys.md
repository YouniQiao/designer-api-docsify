# offDeleteFormsCallback (System API)

## Modules to Import

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## offDeleteFormsCallback

```TypeScript
function offDeleteFormsCallback(callback?: formInfo.DeleteFormsCallback): void
```

Unregister the callback for deleting forms.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

<!--Device-formHost-function offDeleteFormsCallback(callback?: formInfo.DeleteFormsCallback): void--><!--Device-formHost-function offDeleteFormsCallback(callback?: formInfo.DeleteFormsCallback): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | formInfo.DeleteFormsCallback | No | Identifies the callback for deleting forms. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permissions denied. |
| 16500050 | IPC connection error. |
| 202 | The application is not a system application. |

## Examples

```TypeScript
import { formHost } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  formHost.offDeleteFormsCallback();
  console.info(`offDeleteFormsCallback success`);
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```

