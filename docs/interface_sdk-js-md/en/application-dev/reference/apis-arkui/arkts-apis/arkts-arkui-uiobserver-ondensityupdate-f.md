# on_densityUpdate

## Modules to Import

```TypeScript
import { uiObserver } from '@kit.ArkUI';
```

## on('densityUpdate')

```TypeScript
export function on(type: 'densityUpdate', context: UIContext, callback: Callback<DensityInfo>): void
```

Listens for screen pixel density changes.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-uiObserver-export function on(type: 'densityUpdate', context: UIContext, callback: Callback<DensityInfo>): void--><!--Device-uiObserver-export function on(type: 'densityUpdate', context: UIContext, callback: Callback<DensityInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'densityUpdate' | Yes | Event type. Set to **'densityUpdate'** for screen pixel density change events. |
| context | [UIContext](../../apis-default/arkts-apis/arkts-arkui-uicontext-uicontext-c.md) | Yes | Context information, which is used to specify the target page scope. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[DensityInfo](arkts-arkui-uiobserver-densityinfo-c.md)&gt; | Yes | Callback used to return the result. It provides information about the changed screen pixel density. |

**Examples**

```TypeScript
import { uiObserver } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State density: number = 0;
  @State message: string = 'Listener not registered';

  densityUpdateCallback = (info: uiObserver.DensityInfo) => {
    this.density = info.density;
    this.message = 'DPI after change:' + this.density.toString();
  }

  build() {
    Column() {
      Text(this.message)
        .fontSize(24)
        .fontWeight(FontWeight.Bold)
      Button('Subscribe to Screen Pixel Density Changes')
        .onClick(() => {
          this.message = 'Listener registered'
          uiObserver.on('densityUpdate', this.getUIContext(), this.densityUpdateCallback);
        })
    }
  }
}
```

