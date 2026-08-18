# on_didLayout

## Modules to Import

```TypeScript
import { uiObserver } from '@kit.ArkUI';
```

## on_didLayout('didLayout')

```TypeScript
export function on(type: 'didLayout', context: UIContext, callback: Callback<void>): void
```

Listens for layout completion status in each frame.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-uiObserver-export function on(type: 'didLayout', context: UIContext, callback: Callback<void>): void--><!--Device-uiObserver-export function on(type: 'didLayout', context: UIContext, callback: Callback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'didLayout' | Yes | Event type. The value **'didLayout'** indicates whether the layout has been completed. |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | Context information, which is used to specify the target page scope. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Examples**

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

