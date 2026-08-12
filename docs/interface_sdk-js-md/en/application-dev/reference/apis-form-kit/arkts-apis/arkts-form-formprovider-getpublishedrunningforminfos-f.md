# getPublishedRunningFormInfos

## Modules to Import

```TypeScript
import { formProvider } from '@kit.FormKit';
```

## getPublishedRunningFormInfos

```TypeScript
function getPublishedRunningFormInfos(): Promise<Array<formInfo.RunningFormInfo>>
```

Obtains information about all widgets that have been added to the home screen. This API uses a promise to return the result.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-formProvider-function getPublishedRunningFormInfos(): Promise<Array<formInfo.RunningFormInfo>>--><!--Device-formProvider-function getPublishedRunningFormInfos(): Promise<Array<formInfo.RunningFormInfo>>-End-->

**System capability:** SystemCapability.Ability.Form

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;formInfo.RunningFormInfo&gt;&gt; | Promise used to return the information about widgets that meet the requirements. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16501000](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501000-internal-function-error) | An internal functional error occurred. |
| [16500050](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500050-ipc-failure) | IPC connection error. |
| [16500100](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) | Failed to obtain the configuration information. |

## Examples

```TypeScript
import { formInfo, formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  formProvider.getPublishedRunningFormInfos().then((data: formInfo.RunningFormInfo[]) => {
    console.info(`formProvider getPublishedRunningFormInfos, data: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`promise error, code: ${error.code}, message: ${error.message})`);
  });
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
}
```

