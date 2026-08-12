# getPublishedRunningFormInfoById

## Modules to Import

```TypeScript
import { formProvider } from '@kit.FormKit';
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
| [16501003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501003-widget-not-operatable) | The form cannot be operated by the current application. |
| [16501001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501001-widget-id-not-exist) | The ID of the form to be operated does not exist. |
| [16501000](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501000-internal-function-error) | An internal functional error occurred. |
| [16500050](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500050-ipc-failure) | IPC connection error. |
| [16500100](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) | Failed to obtain the configuration information. |

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

