# DrawingRenderingContext

*DrawingRenderingContext** provides a rendering context for drawing rectangles, text, images, and other objects on a canvas.

**Since:** 12

<!--Device-unnamed-declare class DrawingRenderingContext--><!--Device-unnamed-declare class DrawingRenderingContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(unit?: LengthMetricsUnit)
```

Creates a **Canvas** object for drawing operations using the drawing API. Configuration of the unit mode for the **DrawingRenderingContext** object is supported.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DrawingRenderingContext-constructor(unit?: LengthMetricsUnit)--><!--Device-DrawingRenderingContext-constructor(unit?: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| unit | LengthMetricsUnit | No | Unit mode of the **DrawingRenderingContext** object. The value cannot be changed once set. The configuration method is the same as that of [CanvasRenderingContext2D](arkts-arkui-canvasrenderingcontext2d-c.md). <br>Invalid values **undefined**, **NaN** and **Infinity** are treated as the default value. <br>Default value: **DEFAULT**. |

**Examples**

The following example shows how to specify the unit mode during the creation of a CanvasRenderingContext2D object. The default unit mode is LengthMetricsUnit.DEFAULT, which corresponds to the default unit vp. Once set, this unit mode cannot be changed dynamically. For details, see LengthMetricsUnit.

```TypeScript
// xxx.ets
import { LengthMetricsUnit } from '@kit.ArkUI'

@Entry
@Component
struct LengthMetricsUnitDemo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private contextPX: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings, LengthMetricsUnit.PX);
  private contextVP: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.contextPX)
        .width('100%')
        .height(150)
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.contextPX.fillRect(10,10,100,100)
          this.contextPX.clearRect(10,10,50,50)
        })

      Canvas(this.contextVP)
        .width('100%')
        .height(150)
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.contextVP.fillRect(10,10,100,100)
          this.contextVP.clearRect(10,10,50,50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

## invalidate

```TypeScript
invalidate(): void
```

Invalidates the component and triggers re-rendering of the component.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DrawingRenderingContext-invalidate(): void--><!--Device-DrawingRenderingContext-invalidate(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

