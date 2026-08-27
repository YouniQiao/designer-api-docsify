# ImageData

An **ImageData** object stores pixel data rendered on a canvas.

> **NOTE：**
> 
> A constructor used to create an **ImageData** object. To ensure successful drawing,
> make sure the object's area does not exceed 16000 x 16000, with its width and height
> not greater than 16384 px. If the created area exceeds 536870911 px, the returned
> width and height are both 0 px, and **data** is **undefined**.

**Since:** 8

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(width: number, height: number, data?: Uint8ClampedArray)
```

Creates an **ImageData** object with the specified width, height, and color. If data is not defined, it is populated with a one-dimensional array of 0s.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | number | Yes | Width of the rectangle.Default unit: vp Invalid values **NaN** and **Infinity** are treated as **0**. |
| height | number | Yes | Height of the rectangle.Default unit: vp Invalid values **NaN** and **Infinity** are treated as **0**. |
| data | Uint8ClampedArray | No | A one-dimensional array of color values. The values range from 0 to 255.If the value specified is **undefined**, **data** is **undefined**.Default value: a one-dimensional array of all 0s |

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
          // Draw graphics in px unit mode.
          this.contextPX.fillRect(10, 10, 100, 100)
          this.contextPX.clearRect(10, 10, 50, 50)
        })

      Canvas(this.contextVP)
        .width('100%')
        .height(150)
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.contextVP.fillRect(10, 10, 100, 100)
          this.contextVP.clearRect(10, 10, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

## constructor

```TypeScript
constructor(width: number, height: number, data?: Uint8ClampedArray, unit?: LengthMetricsUnit)
```

Creates an **ImageData** object with the specified width, height, and color. If data is not defined, it is populated with a one-dimensional array of 0s. The unit of the **ImageData** object can be configured using **unit**.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | number | Yes | Width of the rectangle.Default unit: vp Invalid values **NaN** and **Infinity** are treated as **0**. |
| height | number | Yes | Height of the rectangle.Default unit: vp Invalid values **NaN** and **Infinity** are treated as **0**. |
| data | Uint8ClampedArray | No | A one-dimensional array of color values. The values range from 0 to 255.If the value specified is **undefined**, **data** is **undefined**.Default value: a one-dimensional array of all 0s |
| unit | LengthMetricsUnit | No | Unit mode of the **ImageData** object. The value cannot be dynamically changed once set. The configuration method is the same as that of [CanvasRenderingContext2D](arkts-arkui-canvasrenderingcontext2d-c.md).Invalid values **undefined**, **NaN** and **Infinity** are treated as the default value.Default value: **DEFAULT**. |

**Examples**

See [constructor](#constructor)

## data

```TypeScript
readonly data: Uint8ClampedArray
```

A one-dimensional array of color values. The values range from 0 to 255.

**Type:** Uint8ClampedArray

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
readonly height: number
```

Actual height of the rectangle on the canvas.

The unit is px.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

```TypeScript
// xxx.ets
@Entry
@Component
struct OffscreenCanvasPage {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(200, 300);

  build() {
    Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Start, justifyContent: FlexAlign.Start }) {
      Column() {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .borderWidth(5)
          .borderColor('#057D02')
          .backgroundColor('#FFFFFF')
          .onReady(() => {
            let offContext = this.offCanvas.getContext("2d", this.settings)
            offContext.fillStyle = '#CDCDCD'
            offContext.fillRect(0, 0, 100, this.offCanvas.height)
            let image = this.offCanvas.transferToImageBitmap()
            this.context.setTransform(1, 0, 0, 1, 50, 200)
            this.context.transferFromImageBitmap(image)
          })
      }
    }.width('100%').height('100%')
  }
}
```

## width

```TypeScript
readonly width: number
```

Actual width of the rectangle on the canvas.

The unit is px.

> **NOTE：**
> 
> The px2vp
> API can be used for unit conversion.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

```TypeScript
// xxx.ets
@Entry
@Component
struct OffscreenCanvasPage {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(200, 300);

  build() {
    Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Start, justifyContent: FlexAlign.Start }) {
      Column() {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .borderWidth(5)
          .borderColor('#057D02')
          .backgroundColor('#FFFFFF')
          .onReady(() => {
            let offContext = this.offCanvas.getContext("2d", this.settings)
            offContext.fillStyle = '#CDCDCD'
            offContext.fillRect(0, 0, this.offCanvas.width, 150)
            let image = this.offCanvas.transferToImageBitmap()
            this.context.setTransform(1, 0, 0, 1, 50, 200)
            this.context.transferFromImageBitmap(image)
          })
      }
    }.width('100%').height('100%')
  }
}
```
