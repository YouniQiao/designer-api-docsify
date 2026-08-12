# setFontWeightScale

## Modules to Import

```TypeScript
import { uiAppearance } from '@kit.ArkUI';
```

## setFontWeightScale

```TypeScript
function setFontWeightScale(fontWeightScale: number): Promise<void>
```

Sets the system font weight scale.

**Permission required**: ohos.permission.UPDATE_CONFIGURATION

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-uiAppearance-function setFontWeightScale(fontWeightScale: number): Promise<void>--><!--Device-uiAppearance-function setFontWeightScale(fontWeightScale: number): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.UiAppearance

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fontWeightScale | number | Yes | indicates the font-weight-scale to set |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [500001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkui/errorcode-uiappearance.md#500001-internal-error) | Internal error. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
import { uiAppearance } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let fontWeightScale = 1;

try {
    uiAppearance.setFontWeightScale(fontWeightScale).then(() => {
      console.info('Set fontWeightScale successfully.');
    }).catch((error:Error) => {
      console.error('Set fontWeightScale failed, ' + error.message);
    });
} catch (error) {
    let message = (error as BusinessError).message;
    console.error('Set fontWeightScale failed, ' + message);
}
```

