# on_didLayout

## Modules to Import

```TypeScript
import { uiObserver } from '@kit.ArkUI';
```

## on_didLayout

```TypeScript
export function on(type: 'didLayout', context: UIContext, callback: Callback<void>): void
```

Listens for layout completion status in each frame.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-uiObserver-export function on(type: 'didLayout', context: UIContext, callback: Callback<void>): void--><!--Device-uiObserver-export function on(type: 'didLayout', context: UIContext, callback: Callback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'didLayout' | Yes |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
import { uiObserver } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  didLayoutCallback = () => {
    console.info("Layout completed.");
  }
  build() {
    Column() {
      Button('Listen for Layout Completion')
        .onClick(() => {
          uiObserver.on('didLayout', this.getUIContext(), this.didLayoutCallback);
        })
    }
  }
}
```
