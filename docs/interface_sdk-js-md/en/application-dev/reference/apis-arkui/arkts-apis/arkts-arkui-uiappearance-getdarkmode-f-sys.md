# getDarkMode (System API)

## Modules to Import

```TypeScript
import { uiAppearance } from '@kit.ArkUI';
```

## getDarkMode

```TypeScript
function getDarkMode(): DarkMode
```

Obtains the current system dark mode configuration.

<!--Del-->

> **NOTE：**

> This API is a system API in API version 19 and earlier. Using this API requires the &gt; [ohos.permission.UPDATE_CONFIGURATION](../../../security/AccessToken/permissions-for-system-apps.md#ohospermissionupdate_configuration) &gt; permission.

<!--DelEnd-->

**Since:** 10

**Required permissions:** 
- API version 10 - 19: ohos.permission.UPDATE_CONFIGURATION

<!--Device-uiAppearance-function getDarkMode(): DarkMode--><!--Device-uiAppearance-function getDarkMode(): DarkMode-End-->

**System capability:** SystemCapability.ArkUI.UiAppearance

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [DarkMode](../../apis-default/arkts-apis/arkts-uiappearance-darkmode-e.md) | current dark-mode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied.<br>**Applicable version:** 10 - 19 |
| [500001](../errorcode-uiappearance.md#500001-internal-error) | Internal error. |

**Examples**

```TypeScript
import { uiAppearance } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let darkMode = uiAppearance.getDarkMode();
  console.info('Get dark-mode ' + darkMode);
} catch (error) {
  let message = (error as BusinessError).message;
  console.error('Get dark-mode failed, ' + message);
}
```

