# moveMainWindowToTargetDisplay (System API)

## Modules to Import

```TypeScript
import { window } from '@kit.ArkUI';
```

## moveMainWindowToTargetDisplay

```TypeScript
function moveMainWindowToTargetDisplay(displayId: long, windowId: int, userId?: int): Promise<void>
```

Move a window to the target display. The window must be a main window.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayId | ArkTS-Dyn: number<br>ArkTS-Sta：long | Yes |
| windowId | ArkTS-Dyn: number<br>ArkTS-Sta：int | Yes |
| userId | ArkTS-Dyn: number<br>ArkTS-Sta：int | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
| [1300008](../errorcode-window.md#1300008-display-device-exception) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |
