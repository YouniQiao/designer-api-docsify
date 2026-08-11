# getPublishedRunningFormInfos

## Modules to Import

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## getPublishedRunningFormInfos

```TypeScript
function getPublishedRunningFormInfos(): Promise<Array<formInfo.RunningFormInfo>>
```

Obtains information about all widgets that have been added to the home screen. This API uses a promise to return the result.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-formProvider-function getPublishedRunningFormInfos(): Promise<Array<formInfo.RunningFormInfo>>--><!--Device-formProvider-function getPublishedRunningFormInfos(): Promise<Array<formInfo.RunningFormInfo>>-End-->

**System capability:** SystemCapability.Ability.Form

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;formInfo.RunningFormInfo&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [16500100](../errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) |

## Examples

```TypeScript
import { formInfo, formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  formProvider.getPublishedRunningFormInfos().then((data: formInfo.RunningFormInfo[]) => {
    console.info(`formProvider getPublishedRunningFormInfos, data: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`promise error, code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```
