# shiftAppWindowPointerEvent

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## shiftAppWindowPointerEvent

```TypeScript
function shiftAppWindowPointerEvent(sourceWindowId: number, targetWindowId: number): Promise<void>
```

Transfers a mouse input event from one window to another within the same application. This API takes effect only for the main window and its child windows. This API uses a promise to return the result.

To transfer mouse input events, the source window must call this API within the callback of the  
[onTouch](onTouch) event (the event type must be **TouchType.Down**). After a successful call, the system sends a **TouchType.Up** event to the source window and a **TouchType.Down** event to the target window.

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-window-function shiftAppWindowPointerEvent(sourceWindowId: int, targetWindowId: int): Promise<void>--><!--Device-window-function shiftAppWindowPointerEvent(sourceWindowId: int, targetWindowId: int): Promise<void>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sourceWindowId | number | Yes |
| targetWindowId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300003](../errorcode-window.md#1300003-abnormal-window-manager-service) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300004](../errorcode-window.md#1300004-unauthorized-operation) |

## Examples

```TypeScript
// ets/pages/Index.ets
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
struct Index {
  build() {
    Row() {
      Column() {
        Blank('160')
          .color(Color.Blue)
          .onTouch((event: TouchEvent) => {
            if (event.type === TouchType.Down) {
              try {
                let sourceWindowId = 1;
                let targetWindowId = 2;
                let promise = window.shiftAppWindowPointerEvent(sourceWindowId, targetWindowId);
                promise.then(() => {
                  console.info('Succeeded in shifting app window pointer event');
                }).catch((err: BusinessError) => {
                  console.error(`Failed to shift app window pointer event. Cause code: ${err.code}, message: ${err.message}`);
                });
              } catch (exception) {
                console.error(`Failed to shift app pointer event. Cause code: ${exception.code}, message: ${exception.message}`);
              }
            }
          })
      }.width('100%')
    }.height('100%').width('100%')
  }
}
```
