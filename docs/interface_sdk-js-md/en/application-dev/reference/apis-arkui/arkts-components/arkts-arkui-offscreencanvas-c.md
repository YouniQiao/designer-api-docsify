# OffscreenCanvas

The **OffscreenCanvas** component is used to draw custom graphics.

When the Canvas component or **CanvasRenderingContext2D** object is used, rendering, animation, and user interaction usually occur on the main thread of the application. Calculations related to canvas animation and rendering may affect application performance. **OffscreenCanvas** allows for rendering off the screen. This means that some tasks can be run in a separate thread to reduce the load on the main thread.

> **NOTE：**
> 
> **OffscreenCanvas** cannot be used in ServiceExtensionAbility. It is recommended
> that you use the
> [drawing module](../../../reference/apis-arkgraphics2d/arkts-apis-graphics-drawing.md)
> for offscreen drawing in ServiceExtensionAbility.

@extends CanvasRenderer [since 8 - 10]

**Since:** 8

<!--Device-unnamed-declare class OffscreenCanvas--><!--Device-unnamed-declare class OffscreenCanvas-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(width: number, height: number)
```

Constructs an OffscreenCanvas for creating an offscreen canvas object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-OffscreenCanvas-constructor(width: number, height: number)--><!--Device-OffscreenCanvas-constructor(width: number, height: number)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | number | Yes | Width of the offscreen canvas.<br> **NaN** and **Infinity** are treated as invalid values.<br>Default unit: vp |
| height | number | Yes | Height of the offscreen canvas.<br> **NaN** and **Infinity** are treated as invalid values.<br>Default unit: vp |

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

## constructor

```TypeScript
constructor(width: number, height: number, unit: LengthMetricsUnit)
```

Constructs an **OffscreenCanvas** object for creating an offscreen canvas object. The unit mode is configurable for the **OffscreenCanvas** object.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-OffscreenCanvas-constructor(width: number, height: number, unit: LengthMetricsUnit)--><!--Device-OffscreenCanvas-constructor(width: number, height: number, unit: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | number | Yes | Width of the offscreen canvas.<br> **NaN** and **Infinity** are treated as invalid values.<br>Default unit: vp |
| height | number | Yes | Height of the offscreen canvas.<br> **NaN** and **Infinity** are treated as invalid values.<br>Default unit: vp |
| unit | LengthMetricsUnit | Yes | Unit mode of the OffscreenCanvas object. The value cannot be dynamically changed once set. The configuration method is the same as that of [CanvasRenderingContext2D](arkts-arkui-canvasrenderingcontext2d-c.md).<br> Invalid values **NaN** and **Infinity** are treated as the default value.<br> Default value: **DEFAULT**. |

**Examples**

See [constructor](#constructor)

## getContext

```TypeScript
getContext(contextType: "2d", options?: RenderingContextSettings): OffscreenCanvasRenderingContext2D
```

Obtains the drawing context of the offscreen canvas.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-OffscreenCanvas-getContext(contextType: "2d", options?: RenderingContextSettings): OffscreenCanvasRenderingContext2D--><!--Device-OffscreenCanvas-getContext(contextType: "2d", options?: RenderingContextSettings): OffscreenCanvasRenderingContext2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| contextType | "2d" | Yes | Type of the drawing context of the offscreen canvas. The value can only be **"2d"**.<br> **"2d"**: creates an **OffscreenCanvasRenderingContext2D** object that represents a two-dimensional rendering context.<br> The values **undefined** and **null** are considered as invalid values, and **undefined** is returned. |
| options | [RenderingContextSettings](arkts-arkui-renderingcontextsettings-c.md) | No | Parameters of the **OffscreenCanvasRenderingContext2D** object. For details, see [RenderingContextSettings](#renderingcontextsettings).<br> **undefined** and **null** values are processed based on the default value of [RenderingContextSettings](#renderingcontextsettings).<br> Default value: **null**. |

**Return value:**

| Type | Description |
| --- | --- |
| [OffscreenCanvasRenderingContext2D](arkts-arkui-offscreencanvasrenderingcontext2d-c.md) | Drawing context of the offscreen canvas. If the input parameter contextType of the **getContext** method is not **"2d"** (including null or undefined), **undefined** will be returned. Before using the method, check whether the return value is **undefined**. |

**Examples**

```TypeScript
@Entry
@Component
struct OffscreenCanvasExamplePage {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offscreenCanvas: OffscreenCanvas = new OffscreenCanvas(600, 800);

  build() {
    Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Start, justifyContent: FlexAlign.Start }) {
      Column() {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .backgroundColor('#FFFFFF')
          .onReady(() => {
            let offContext = this.offscreenCanvas.getContext("2d", this.settings)
            offContext.font = '70px sans-serif'
            offContext.fillText("Offscreen : Hello World!", 20, 60)
            offContext.fillStyle = "#0000ff"
            offContext.fillRect(230, 350, 50, 50)
            offContext.fillStyle = "#EE0077"
            offContext.translate(70, 70)
            offContext.fillRect(230, 350, 50, 50)
            offContext.fillStyle = "#77EE0077"
            offContext.translate(-70, -70)
            offContext.fillStyle = "#00ffff"
            offContext.rotate(45 * Math.PI / 180);
            offContext.fillRect(180, 120, 50, 50);
            offContext.rotate(-45 * Math.PI / 180);
            offContext.beginPath()
            offContext.moveTo(10, 150)
            offContext.bezierCurveTo(20, 100, 200, 100, 200, 20)
            offContext.stroke()
            offContext.fillStyle = '#FF00FF'
            offContext.fillRect(100, 100, 60, 60)
            let imageData = this.offscreenCanvas.transferToImageBitmap()
            this.context.transferFromImageBitmap(imageData)
          })
      }.width('100%').height('100%')
    }
    .width('100%')
    .height('100%')
  }
}
```

## transferToImageBitmap

```TypeScript
transferToImageBitmap(): ImageBitmap
```

Creates an **ImageBitmap** object from the most recently rendered image of the offscreen canvas.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-OffscreenCanvas-transferToImageBitmap(): ImageBitmap--><!--Device-OffscreenCanvas-transferToImageBitmap(): ImageBitmap-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [ImageBitmap](arkts-arkui-imagebitmap-c.md) | ImageBitmap** object created. |

**Examples**

```TypeScript
// xxx.ets
@Entry
@Component
struct OffscreenCanvasPage {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(400, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .borderWidth(5)
        .borderColor('rgb(39,135,217)')
        .backgroundColor('#FFFFFF')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.fillStyle = '#CDCDCD'
          offContext.fillRect(0, 0, 400, 600)
          offContext.fillStyle = '#000000'
          offContext.font = '40px serif bold'
          offContext.fillText("Offscreen : Hello World!", 20, 60)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

```TypeScript
// xxx.ets
@Entry
@Component
struct PutImageData {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          let imageData = offContext.createImageData(100, 100)
          for (let i = 0; i < imageData.data.length; i += 4) {
            imageData.data[i + 0] = 112
            imageData.data[i + 1] = 112
            imageData.data[i + 2] = 112
            imageData.data[i + 3] = 255
          }
          offContext.putImageData(imageData, 10, 10)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

## height

```TypeScript
height: number
```

Height of the offscreen canvas.

Default unit: vp

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-OffscreenCanvas-height: number--><!--Device-OffscreenCanvas-height: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width: number
```

Width of the offscreen canvas.

Default unit: vp

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-OffscreenCanvas-width: number--><!--Device-OffscreenCanvas-width: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

