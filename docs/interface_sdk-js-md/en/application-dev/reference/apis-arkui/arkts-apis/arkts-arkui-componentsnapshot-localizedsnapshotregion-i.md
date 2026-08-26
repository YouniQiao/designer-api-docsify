# LocalizedSnapshotRegion

Defines the rectangular region for capturing the component snapshot, with coordinates adjusted based on the layout direction (LTR or RTL).

> **NOTE：**
> 
> Directly using **componentSnapshot** can lead to the issue of
> [ambiguous UI context](../../../ui/arkts-global-interface.md#ambiguous-ui-context). To avoid this, obtain a
> **UIContext** instance using **getUIContext()**, and then obtain the associated **componentSnapshot** object
> using
> [getComponentSnapshot](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getcomponentsnapshot).

**Since:** 15

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import componentSnapshot from '@kit.ArkUI';
```

## bottom

```TypeScript
bottom: number
```

Y-coordinate of the lower right corner of the rectangular region.Unit: px.Value range: [0, Component height].

**Type:** number

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## end

```TypeScript
end: number
```

For LTR layouts: X-coordinate of the lower right corner of the rectangular region.For RTL layouts: X-coordinate of the lower left corner of the rectangular region.Unit: px.Value range: [0, Component width].

**Type:** number

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## start

```TypeScript
start: number
```

For LTR layouts: X-coordinate of the upper left corner of the rectangular region.For RTL layouts: X-coordinate of the upper right corner of the rectangular region.Unit: px.Value range: [0, Component width].

**Type:** number

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## top

```TypeScript
top: number
```

For LTR layouts: Y-coordinate of the upper left corner of the rectangular region.For RTL layouts: Y-coordinate of the upper right corner of the rectangular region.Unit: px.Value range: [0, Component height].

**Type:** number

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

```TypeScript
import { image } from '@kit.ImageKit';

@Entry
@Component
struct SnapshotExample {
  @State pixmap: image.PixelMap | undefined = undefined

  build() {
    Column() {
      Row() {
        Column() {
          TextClock()
          Button('Button ABCDE').type(ButtonType.Normal)
          Row() {
            Checkbox()
            Text('√')
            Text(' | ')
            Checkbox()
            Text('×')
          }.align(Alignment.Start)

          TextInput()
        }
        .align(Alignment.Start)
        .id('component1')
        .width('600px')
        .height('600px')
        .borderRadius(6)
        .borderWidth(2)
        .borderColor(Color.Green)

      }

      Button('get capture')
        .onClick(() => {
          try {
            let pixelmap = this.getUIContext().getComponentSnapshot().getSync('component1',
              {
                scale: 2,
                waitUntilRenderFinished: true,
                region: {
                  start: 20,
                  top: 20,
                  end: 200,
                  bottom: 240
                }
              })
            this.pixmap = pixelmap;
          } catch (error) {
            console.error(`getSync error message:${error.message}`);
          }
        }).margin(10)
      Image(this.pixmap).border({ color: Color.Black, width: 2 }).width('600px')
    }.width('100%').align(Alignment.Center)
  }
}
```
