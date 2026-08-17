# moveMainWindowToTargetDisplay (System API)

## Modules to Import

```TypeScript
import { window } from 'window';
```

## moveMainWindowToTargetDisplay

```TypeScript
function moveMainWindowToTargetDisplay(displayId: long, windowId: int, userId?: int): Promise<void>
```

Move a window to the target display. The window must be a main window.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-window-function moveMainWindowToTargetDisplay(displayId: long, windowId: int, userId?: int): Promise<void>--><!--Device-window-function moveMainWindowToTargetDisplay(displayId: long, windowId: int, userId?: int): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| displayId | long | Yes | Indicate the id of display. |
| windowId | int | Yes | A main window id which will be moved. |
| userId | int | No | Indicate the user ID of the target application space. If not provided, the current user is used by default. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value indicates complete. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) | This window manager service works abnormally. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) | This window state is abnormal. Possible cause: The window is not found or has been destroyed. |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) | Parameter error. Possible cause: 1. The userId is not exist. |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) | Unauthorized operation. Possible cause: The window is not a main window. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [1300008](../errorcode-window.md#1300008-display-device-exception) | Invalid display. Possible cause: 1. DisplayId is a negative number or not exists. |

