# CanvasGradient

**CanvasGradient** provides a canvas gradient object.

**Since:** 8

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

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | number | Yes | Relative position of the gradient stop along the gradient vector, represented by the ratio of the distance between the gradient stop and the start point to the total length. The value ranges from 0 to 1.If the value of **offset** is less than 0 or greater than 1, there is no gradient effect.    **undefined** and **null** are treated as invalid values, and the current stop is ignored. **NaN** causes a **CanvasGradient** exception, and **Infinity** causes **CanvasGradient** to be invalid. |
| color | string | Yes | Gradient color to set. For details about the color notation, see the description of the string type in [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md).Invalid values result in no gradient effect being displayed. |

**Examples**

Set the gradient breakpoint value through addColorStop, including the offset and color.

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
> Only the
> fillStyle
> and
> strokeStyle
> attributes of the
> [CanvasRenderingContext2D](arkts-arkui-canvasrenderingcontext2d-c.md)
> object support the **CanvasGradient** object with the P3 wide color gamut. In addition,
> the color gamut mode of the window where the **Canvas** component is located must be set
> to wide color gamut mode **WIDE_GAMUT** via the
> [setWindowColorSpace](../arkts-apis/arkts-arkui-window-window-i.md#setwindowcolorspace)
> method.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | number | Yes | Relative position of the gradient stop along the gradient vector, represented by the ratio of the distance between the gradient stop and the start point to the total length. The value ranges from 0 to 1.If the value of **offset** is less than 0 or greater than 1, there is no gradient effect.    **undefined** and **null** are treated as invalid values and are not applied. **NaN** causes a **CanvasGradient** exception, and **Infinity** causes **CanvasGradient** to be invalid. |
| color | string \| ColorMetrics | Yes | Color of the gradient fill.You can use the [colorWithSpace](../arkts-apis/arkts-arkui-graphics-colormetrics-c.md#colorwithspace) method to construct a color with the color gamut attribute ColorSpace set to **SRGB** or **DISPLAY_P3**. The color gamut attributes of each gradient ColorMetrics must be the same. If different color gamut attributes are set, an exception is thrown, and the error code is 103701.    **undefined** and **null** are treated as invalid values, and the current stop is ignored. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [103701](../errorcode-canvas.md#103701-parameter-error) | The color's ColorSpace is not the same as the last color's. |

**Examples**

This example demonstrates how to set the gradient stop value of a specified color gamut using addColorStop, including the offset and color. For details about how to set the color gamut mode of the window to wide color gamut, see [setWindowColorSpace](../arkts-apis-window-Window.md#setwindowcolorspace).

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
          // Set fillStyle to a gradient with sRGB color gamut effect.
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

addColorStop
The following example demonstrates the brightness difference between SDR and HDR gradients. Through ColorMetrics, you can construct HDR colors in the BT2020 color gamut, where color component values can exceed 1.0. The portion exceeding 1.0 is used to represent highlight effects beyond the normal screen brightness range. The left side uses an sRGB red-to-white-to-green gradient, while the right side uses HDR colors in the BT2020 color gamut with a highlight white brightness multiplier of 1.5. On an HDR-capable screen, the highlight area on the right is noticeably brighter than that on the left.
> NOTE
> 
> When using HDR colors, you must set the color gamut mode of the window where the Canvas component is located to the wide gamut mode (WIDE_GAMUT) through the [setWindowColorSpace](../arkts-apis-window-Window.md#setwindowcolorspace) method. Otherwise, the HDR brightening effect will not take effect.

Since API version 26.0.0, the [addColorStop](#addcolorstop) API additionally supports HDR brightening through the ColorMetrics type input parameter.

```TypeScript
// xxx.ets
import { ColorMetrics } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct CanvasGradientDemo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Column({ space: 30 }) {
      Canvas(this.context)
        .width(340)
        .height(240)
        .onReady(() => {
          // HDR gradients support brightness values exceeding 1.0. On HDR-capable devices, the highlight area on the right will be brighter than that on the left.
          this.drawCanvas();
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  private drawCanvas() {
    // Left: SDR gradient, red -> white -> green
    let gradSDR = this.context.createLinearGradient(20, 20, 160, 160)
    try {
      gradSDR.addColorStop(0.0, ColorMetrics.colorWithSpace(ColorSpace.SRGB, 1.0, 0.0, 0.0, 1.0)) // Red
      gradSDR.addColorStop(0.5, ColorMetrics.colorWithSpace(ColorSpace.SRGB, 1.0, 1.0, 1.0, 1.0)) // White
      gradSDR.addColorStop(1.0, ColorMetrics.colorWithSpace(ColorSpace.SRGB, 0.0, 1.0, 0.0, 1.0)) // Green
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`SDR Failed to addColorStop. Code: ${e.code}, message: ${e.message}`);
    }
    this.context.fillStyle = gradSDR
    this.context.fillRect(10, 10, 150, 150)

    this.context.fillStyle = '#FFFFFF'
    this.context.font = '16px sans-serif'
    this.context.textAlign = 'center'
    this.context.fillText("SDR", 85, 190)

    // Right: HDR gradient, red -> bright white (brightness 1.5) -> green
    let gradHDR = this.context.createLinearGradient(190, 20, 330, 160)
    try {
      gradHDR.addColorStop(0.0, ColorMetrics.createHDRColor(ColorSpace.BT2020, 1.0, 0.0, 0.0, 1.0)) // Red
      gradHDR.addColorStop(0.5, ColorMetrics.createHDRColor(ColorSpace.BT2020, 1.5, 1.5, 1.5, 1.0)) // Bright white
      gradHDR.addColorStop(1.0, ColorMetrics.createHDRColor(ColorSpace.BT2020, 0.0, 1.0, 0.0, 1.0)) // Green
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`HDR Failed to addColorStop. Code: ${e.code}, message: ${e.message}`);
    }
    this.context.fillStyle = gradHDR
    this.context.fillRect(180, 10, 150, 150)

    this.context.fillStyle = '#FFFFFF'
    this.context.fillText("HDR", 255, 190)
  }
}
```
