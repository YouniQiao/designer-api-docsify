# getFontScale (System API)

## Modules to Import

```TypeScript
import { uiAppearance } from 'uiAppearance';
```

## getFontScale

```TypeScript
function getFontScale(): number
```

Obtains the current font size scale factor. &lt;!--Del--&gt; > **NOTE：**> This API is a system API in API version 19 and earlier. Using this API requires the > [ohos.permission.UPDATE_CONFIGURATION](../../../security/AccessToken/permissions-for-system-apps.md#ohospermissionupdate_configuration) > permission. &lt;!--DelEnd--&gt;

**Since:** 12

**Required permissions:** 
- API version 12 - 19: ohos.permission.UPDATE_CONFIGURATION

<!--Device-uiAppearance-function getFontScale(): number--><!--Device-uiAppearance-function getFontScale(): number-End-->

**System capability:** SystemCapability.ArkUI.UiAppearance

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| number | current font-scale. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [500001](../errorcode-uiappearance.md#500001-internal-error) | Internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied.<br>**Applicable version:** 12 - 19 |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API.<br>**Applicable version:** 12 - 19 |

**Examples**

```TypeScript
import { uiAppearance } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let fontScale = uiAppearance.getFontScale();
  console.info('Get fontScale ' + fontScale);
} catch (error) {
  let message = (error as BusinessError).message;
  console.error('Get fontScale failed, ' + message);
}
```

