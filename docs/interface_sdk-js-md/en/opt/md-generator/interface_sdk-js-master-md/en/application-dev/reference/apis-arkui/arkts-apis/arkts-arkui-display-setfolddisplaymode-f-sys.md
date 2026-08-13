# setFoldDisplayMode (System API)

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## setFoldDisplayMode

```TypeScript
function setFoldDisplayMode(mode: FoldDisplayMode): void
```

Sets the display mode of the foldable device.

**Since:** 23

**Deprecated since:** -1

<!--Device-display-function setFoldDisplayMode(mode: FoldDisplayMode): void--><!--Device-display-function setFoldDisplayMode(mode: FoldDisplayMode): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [FoldDisplayMode](arkts-arkui-display-folddisplaymode-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { display } from '@kit.ArkUI';

try {
  let mode: display.FoldDisplayMode = display.FoldDisplayMode.FOLD_DISPLAY_MODE_FULL;
  // Set the display mode to full-screen display.
  display.setFoldDisplayMode(mode);
} catch (exception) {
  console.error(`Failed to change the fold display mode. Code: ${exception.code}, message: ${exception.message}`);
}
```


## setFoldDisplayMode

```TypeScript
function setFoldDisplayMode(mode: FoldDisplayMode, reason: string): void
```

Sets the display mode of the foldable device, with the reason for the change specified.

**Since:** 23

**Deprecated since:** -1

<!--Device-display-function setFoldDisplayMode(mode: FoldDisplayMode, reason: string): void--><!--Device-display-function setFoldDisplayMode(mode: FoldDisplayMode, reason: string): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [FoldDisplayMode](arkts-arkui-display-folddisplaymode-e.md) | Yes |
| reason | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { display } from '@kit.ArkUI';

try {
  let mode: display.FoldDisplayMode = display.FoldDisplayMode.FOLD_DISPLAY_MODE_MAIN;
  // Set the display mode to main screen display and specify the reason as "backSelfie".
  display.setFoldDisplayMode(mode, 'backSelfie');
} catch (exception) {
  console.error(`Failed to change the fold display mode. Code: ${exception.code}, message: ${exception.message}`);
}
```
