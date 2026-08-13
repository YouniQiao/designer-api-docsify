# on_willDraw

## Modules to Import

```TypeScript
import { uiObserver } from '@kit.ArkUI';
```

## on_willDraw

```TypeScript
export function on(type: 'willDraw', context: UIContext, callback: Callback<void>): void
```

Listens for drawing instruction dispatch in each frame.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-uiObserver-export function on(type: 'willDraw', context: UIContext, callback: Callback<void>): void--><!--Device-uiObserver-export function on(type: 'willDraw', context: UIContext, callback: Callback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'willDraw' | Yes |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
import { uiObserver } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  willDrawCallback = () => {
    console.info("willDraw instruction dispatched.");
  }
  build() {
    Column() {
      Button('Listen for Drawing Instruction Dispatch')
        .onClick(() => {
          uiObserver.on('willDraw', this.getUIContext(), this.willDrawCallback);
        })
    }
  }
}
```
