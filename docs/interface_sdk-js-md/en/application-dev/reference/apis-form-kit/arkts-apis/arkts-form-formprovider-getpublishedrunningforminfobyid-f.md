# getPublishedRunningFormInfoById

## Modules to Import

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## getPublishedRunningFormInfoById

```TypeScript
function getPublishedRunningFormInfoById(formId: string): Promise<formInfo.RunningFormInfo>
```

Obtains the information of a specified widget that has been added to the home screen. This API uses a promise to return the result.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-formProvider-function getPublishedRunningFormInfoById(formId: string): Promise<formInfo.RunningFormInfo>--><!--Device-formProvider-function getPublishedRunningFormInfoById(formId: string): Promise<formInfo.RunningFormInfo>-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formId | string | Yes | Widget ID. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;formInfo.RunningFormInfo&gt; | Promise used to return the information about the widgets that meet the requirements, including the widget name and dimension. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16501003 | The form cannot be operated by the current application. |
| 16501001 | The ID of the form to be operated does not exist. |
| 16501000 | An internal functional error occurred. |
| 16500050 | IPC connection error. |
| 16500100 | Failed to obtain the configuration information. |

## Examples

```TypeScript
import { formInfo, formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

const formId: string = '388344236';

try {
  formProvider.getPublishedRunningFormInfoById(formId).then((data: formInfo.RunningFormInfo) => {
    console.info(`formProvider getPublishedRunningFormInfoById, data: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`promise error, code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```

