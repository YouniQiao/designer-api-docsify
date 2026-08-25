# getDefaultDisplaySync

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## getDefaultDisplaySync

```TypeScript
function getDefaultDisplaySync(): Display
```

Obtains the **Display** object of the screen where the application is located. If multiple abilities of an application are on different screens, the **Display** object of the main screen is returned. If multiple abilities of an application are on the same screen, the **Display** object of the screen is returned.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Display](arkts-arkui-display-display-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [1400001](../errorcode-display.md#1400001-invalid-display-or-screen) |
