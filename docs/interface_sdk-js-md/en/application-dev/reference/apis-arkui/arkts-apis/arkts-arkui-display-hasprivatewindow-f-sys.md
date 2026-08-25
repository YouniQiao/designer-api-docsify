# hasPrivateWindow (System API)

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## hasPrivateWindow

```TypeScript
function hasPrivateWindow(displayId: long): boolean
```

Checks whether there is a visible privacy window on a display. The window privacy mode can be set by calling setWindowPrivacyMode(). The content in the privacy window cannot be captured or recorded.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayId | ArkTS-Dyn: number<br>ArkTS-Sta：long | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |

**Examples**

```TypeScript
import { display } from '@kit.ArkUI';

let displayClass: display.Display | null = null;
try {
  displayClass = display.getDefaultDisplaySync();

  let ret: boolean = true;
  try {
    ret = display.hasPrivateWindow(displayClass.id);
  } catch (exception) {
    console.error(`Failed to check has privateWindow or not. Code: ${exception.code} , message : ${exception.message}`);
  }
  if (ret == undefined) {
    console.error("Failed to check has privateWindow or not.");
  }
  if (ret) {
    console.info("There has privateWindow.");
  } else if (!ret) {
    console.info("There has no privateWindow.");
  }
} catch (exception) {
  console.error(`Failed to obtain the default display object. Code: ${exception.code} , message : ${exception.message}`);
}
```
