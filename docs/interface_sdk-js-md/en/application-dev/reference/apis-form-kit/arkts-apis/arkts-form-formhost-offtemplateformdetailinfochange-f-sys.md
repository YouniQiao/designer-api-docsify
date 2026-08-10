# offTemplateFormDetailInfoChange (System API)

## Modules to Import

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## offTemplateFormDetailInfoChange

```TypeScript
function offTemplateFormDetailInfoChange(callback?: formInfo.TemplateFormDetailInfoCallback): void
```

Unsubscribes from changes in the static configuration information of template widgets. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

<!--Device-formHost-function offTemplateFormDetailInfoChange(callback?: formInfo.TemplateFormDetailInfoCallback): void--><!--Device-formHost-function offTemplateFormDetailInfoChange(callback?: formInfo.TemplateFormDetailInfoCallback): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | formInfo.TemplateFormDetailInfoCallback | No | Callback function used to listen for changes in the static configuration information of template widgets. |

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
  formHost.offTemplateFormDetailInfoChange();
  console.info(`offTemplateFormDetailInfoChange success`);
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```

