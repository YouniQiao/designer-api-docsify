# CanvasGradient

*CanvasGradient** provides a canvas gradient object.

**Since:** 8

<!--Device-unnamed-declare class CanvasGradient--><!--Device-unnamed-declare class CanvasGradient-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## addColorStop

```TypeScript
addColorStop(offset: number, color: string): void
```

Adds a color stop for the **CanvasGradient** object based on the specified offset and gradient color.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-CanvasGradient-addColorStop(offset: number, color: string): void--><!--Device-CanvasGradient-addColorStop(offset: number, color: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | number | Yes | Relative position of the gradient stop along the gradient vector, represented by the ratio of the distance between the gradient stop and the start point to the total length. The value ranges from 0 to 1.<br> If the value of **offset** is less than 0 or greater than 1, there is no gradient effect.<br> **undefined** and **null** are treated as invalid values, and the current stop is ignored. **NaN** causes a **CanvasGradient** exception, and **Infinity** causes **CanvasGradient** to be invalid. |
| color | string | Yes | Gradient color to set. For details about the color notation, see the description of the string type in ResourceColor.<br> Invalid values result in no gradient effect being displayed. |

**Examples**

This example shows how to add a color stop using addColorStop. Colors in RGB or ARGB format can be set.

```TypeScript
// xxx.ets
@Entry
@Component
struct AddColorStop {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let grad = this.context.createLinearGradient(50, 0, 300, 100)
          grad.addColorStop(0.0, 'rgb(39,135,217)')
          grad.addColorStop(0.5, 'rgb(255,238,240)')
          grad.addColorStop(1.0, 'rgb(23,169,141)')
          this.context.fillStyle = grad
          this.context.fillRect(0, 0, 400, 400)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

## addColorStop

```TypeScript
addColorStop(offset: number, color: string | ColorMetrics): void
```

Adds a color stop for the **CanvasGradient** object based on the specified offset and gradient color. Colors in RGB or ARGB format can be set. You can set P3 color gamut values by passing in the ColorMetrics type, which can achieve richer color reproduction on devices that support high color gamut.

> **NOTE：**
> 
> Only the &gt; fillStyle &gt; and &gt; strokeStyle &gt; attributes of the &gt; [CanvasRenderingContext2D](arkts-arkui-canvasrenderingcontext2d-c.md) &gt; object support the **CanvasGradient** object with the P3 wide color gamut. In addition, &gt; the color gamut mode of the window where the **Canvas** component is located must be set &gt; to wide color gamut mode **WIDE_GAMUT** via the &gt; [setWindowColorSpace](../arkts-apis/arkts-arkui-window-window-i.md#setwindowcolorspace) &gt; method.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 20.

<!--Device-CanvasGradient-addColorStop(offset: number, color: string | ColorMetrics): void--><!--Device-CanvasGradient-addColorStop(offset: number, color: string | ColorMetrics): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | number | Yes | Relative position of the gradient stop along the gradient vector, represented by the ratio of the distance between the gradient stop and the start point to the total length. The value ranges from 0 to 1.<br> If the value of **offset** is less than 0 or greater than 1, there is no gradient effect.<br> **undefined** and **null** are treated as invalid values and are not applied. **NaN** causes a **CanvasGradient** exception, and **Infinity** causes **CanvasGradient** to be invalid. |
| color | string \| ColorMetrics | Yes | Color of the gradient fill.<br> You can use the [colorWithSpace](../../apis-default/arkts-apis/arkts-graphics-colormetrics-c.md#colorwithspace) method to construct a color with the color gamut attribute ColorSpace set to **SRGB** or **DISPLAY_P3**. The color gamut attributes of each gradient ColorMetrics must be the same. If different color gamut attributes are set, an exception is thrown, and the error code is 103701.<br> **undefined** and **null** are treated as invalid values, and the current stop is ignored. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [103701](../errorcode-canvas.md#103701-parameter-error) | The color's ColorSpace is not the same as the last color's. |

**Examples**

Sets the gradient breakpoint value of a specified color gamut, including the offset and color. Set the color gamut mode of the window to wide color gamut. For details, see [setWindowColorSpace](../arkts-apis-window-Window.md#setwindowcolorspace).

```TypeScript
// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { ColorMetrics } from '@kit.ArkUI'

@Entry
@Component
struct AddColorStop {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .onReady(() => {
          // Set fillStyle to gradient with the SRGB color gamut.
          let gradSRGB = this.context.createLinearGradient(85, 10, 160, 110)
          // Use try catch to capture possible exceptions.
          try {
            gradSRGB.addColorStop(0.0, ColorMetrics.colorWithSpace(ColorSpace.SRGB, 1.0, 0.0, 0.0, 1.0))
            gradSRGB.addColorStop(0.5, ColorMetrics.colorWithSpace(ColorSpace.SRGB, 1.0, 1.0, 1.0, 1.0))
            gradSRGB.addColorStop(1.0, ColorMetrics.colorWithSpace(ColorSpace.SRGB, 0.0, 1.0, 0.0, 1.0))
          } catch (error) {
            let e: BusinessError = error as BusinessError;
            console.error(`Failed to addColorStop. Code: ${e.code}, message: ${e.message}`);
          }
          this.context.fillStyle = gradSRGB
          this.context.fillRect(10, 10, 150, 150)

          // Set fillStyle to the gradient effect of the DISPLAY_P3 color gamut.
          let gradP3 = this.context.createLinearGradient(245, 10, 320, 110)
          // Use try catch to capture possible exceptions.
          try {
            gradP3.addColorStop(0.0, ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 1.0, 0.0, 0.0, 1.0))
            gradP3.addColorStop(0.5, ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 1.0, 1.0, 1.0, 1.0))
            gradP3.addColorStop(1.0, ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 0.0, 1.0, 0.0, 1.0))
          } catch (error) {
            let e: BusinessError = error as BusinessError;
            console.error(`Failed to addColorStop. Code: ${e.code}, message: ${e.message}`);
          }
          this.context.fillStyle = gradP3
          this.context.fillRect(170, 10, 150, 150)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

