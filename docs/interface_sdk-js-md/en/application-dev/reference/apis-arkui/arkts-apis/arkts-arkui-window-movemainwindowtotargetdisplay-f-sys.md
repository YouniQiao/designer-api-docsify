# moveMainWindowToTargetDisplay (System API)

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## moveMainWindowToTargetDisplay

```TypeScript
function moveMainWindowToTargetDisplay(displayId: number, windowId: number, userId?: number): Promise<void>
```

Move a window to the target display. The window must be a main window.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| displayId | number | Yes |
| windowId | number | Yes |
| userId | number | No |

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
