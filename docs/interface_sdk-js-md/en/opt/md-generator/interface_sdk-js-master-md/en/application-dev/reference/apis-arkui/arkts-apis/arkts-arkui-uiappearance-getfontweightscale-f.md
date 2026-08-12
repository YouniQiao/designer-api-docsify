# getFontWeightScale

## Modules to Import

```TypeScript
import { uiAppearance } from '@kit.ArkUI';
```

## getFontWeightScale

```TypeScript
function getFontWeightScale(): number
```

Obtains the current font weight scale factor.

&lt;!--Del--&gt;

> **NOTE：**

> This API is a system API in API version 19 and earlier. Using this API requires the
> [ohos.permission.UPDATE_CONFIGURATION](../../../security/AccessToken/permissions-for-system-apps.md#ohospermissionupdate_configuration)
> permission.

&lt;!--DelEnd--&gt;

**Since:** 20

**Required permissions:** 
- API version 12 - 19: ohos.permission.UPDATE_CONFIGURATION

<!--Device-uiAppearance-function getFontWeightScale(): number--><!--Device-uiAppearance-function getFontWeightScale(): number-End-->

**System capability:** SystemCapability.ArkUI.UiAppearance

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [500001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-uiappearance.md#500001-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { uiAppearance } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let fontWeightScale = uiAppearance.getFontWeightScale();
  console.info('Get fontWeightScale ' + fontWeightScale);
} catch (error) {
  let err = error as BusinessError;
  console.error(`Get fontWeightScale failed. Code: ${err.code}, message: ${err.message}`);
}
```
