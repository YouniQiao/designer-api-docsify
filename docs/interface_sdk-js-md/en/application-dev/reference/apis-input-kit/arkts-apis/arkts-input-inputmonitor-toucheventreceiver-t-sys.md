# TouchEventReceiver (System API)

```TypeScript
type TouchEventReceiver = (touchEvent: TouchEvent) => boolean
```

Callback used to return the touch event.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| touchEvent | [TouchEvent](arkts-input-multimodalinput-touchevent-touchevent-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
import { inputMonitor } from '@kit.InputKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            inputMonitor.on('touch', touchEvent => {
              if (touchEvent.touches.length === 3) { // Three fingers are pressed.
                return true;
              }
              return false;
            });
          } catch (error) {
            console.error(`Monitor on failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
          }
        })
    }
  }
}
```
