# shiftAppWindowTouchEvent

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## shiftAppWindowTouchEvent

```TypeScript
function shiftAppWindowTouchEvent(sourceWindowId: number, targetWindowId: number, fingerId: number): Promise<void>
```

Transfers a touchscreen input event from one window to another within the same application. This API takes effect only for the main window and its child windows. This API uses a promise to return the result.To transfer touchscreen input events, the source window must call this API within the callback of the onTouch event (the event type must be **TouchType.Down**). After a successful call, the system sends a **TouchType.Up** event to the source window and a **TouchType.Down** event to the target window.

**Since:** 20

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceWindowId | number | Yes |
| targetWindowId | number | Yes |
| fingerId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |
