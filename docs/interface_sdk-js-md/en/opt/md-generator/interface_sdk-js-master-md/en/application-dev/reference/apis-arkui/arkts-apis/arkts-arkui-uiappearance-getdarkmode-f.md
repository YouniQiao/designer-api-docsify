# getDarkMode

## Modules to Import

```TypeScript
import { uiAppearance } from 'kits/@kit.ArkUI';
```

## getDarkMode

```TypeScript
function getDarkMode(): DarkMode
```

Obtains the current system dark mode configuration.

&lt;!--Del--&gt;

> **NOTE：**

> This API is a system API in API version 19 and earlier. Using this API requires the
> [ohos.permission.UPDATE_CONFIGURATION](../../../security/AccessToken/permissions-for-system-apps.md#ohospermissionupdate_configuration)
> permission.

&lt;!--DelEnd--&gt;

**Since:** 20

**Required permissions:** 
- API version 10 - 19: ohos.permission.UPDATE_CONFIGURATION

<!--Device-uiAppearance-function getDarkMode(): DarkMode--><!--Device-uiAppearance-function getDarkMode(): DarkMode-End-->

**System capability:** SystemCapability.ArkUI.UiAppearance

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DarkMode](arkts-arkui-uiappearance-darkmode-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [500001](../errorcode-uiappearance.md#500001-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { uiAppearance } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let darkMode = uiAppearance.getDarkMode();
  console.info('Get dark-mode ' + darkMode);
} catch (error) {
  let err = error as BusinessError;
  console.error(`Get dark-mode failed. Code: ${err.code}, message: ${err.message}`);
}
```
