# shiftAppWindowFocus

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## shiftAppWindowFocus

```TypeScript
function shiftAppWindowFocus(sourceWindowId: number, targetWindowId: number): Promise<void>
```

Shifts the window focus from the source window to the target window in the same application. The window focus can be shifted within the main window and child windows. This API uses a promise to return the result.Ensure that the target window can gain focus (configurable by calling [setWindowFocusable()](arkts-arkui-window-window-i.md#setwindowfocusable)) and that [showWindow()](arkts-arkui-window-window-i.md#showwindow) has been successfully executed.

> **NOTE：**&gt;
> Before calling **shiftAppWindowFocus()**, ensure that the target window has called
> [loadContent()](arkts-arkui-window-window-i.md#loadcontent)
> or [setUIContent()](arkts-arkui-window-window-i.md#setuicontent)
> and these operations have been effective. Otherwise, an invisible window may gain focus, causing function
> exceptions or affecting user experience.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceWindowId | number | Yes |
| targetWindowId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
