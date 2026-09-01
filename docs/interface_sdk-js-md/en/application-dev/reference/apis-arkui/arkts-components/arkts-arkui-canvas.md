# Canvas

The **Canvas** component can be used to customize drawings.

## Canvas

```TypeScript
Canvas(context?: CanvasRenderingContext2D | DrawingRenderingContext)
```

Creates a **Canvas** component. The maximum allowed size cannot exceed 10000 px × 10000 px. If the size exceeds this limit, the **Canvas** component will fail to be created.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [CanvasRenderingContext2D](arkts-arkui-canvasrenderingcontext2d-c.md) \| [DrawingRenderingContext](arkts-arkui-drawingrenderingcontext-c.md) | No | 2D rendering context for a canvas.    **CanvasRenderingContext2D**: Canvases cannot share one **CanvasRenderingContext2D** object. **DrawingRenderingContext**: Canvases cannot share one **DrawingRenderingContext** object. If the value is **null** or **undefined**, **context** is considered unset. |

## Canvas

```TypeScript
Canvas(context: CanvasRenderingContext2D | DrawingRenderingContext, imageAIOptions: ImageAIOptions)
```

Creates a **Canvas** component. You can specify a **CanvasRenderingContext2D** or **DrawingRenderingContext** object, along with AI image analysis options.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [CanvasRenderingContext2D](arkts-arkui-canvasrenderingcontext2d-c.md) \| [DrawingRenderingContext](arkts-arkui-drawingrenderingcontext-c.md) | Yes | 2D rendering context for a canvas.    **CanvasRenderingContext2D**: Canvases cannot share one **CanvasRenderingContext2D** object. **DrawingRenderingContext**: Canvases cannot share one **DrawingRenderingContext** object. If the value is **null** or **undefined**, **context** is considered unset. |
| imageAIOptions | [ImageAIOptions](../arkts-apis/arkts-arkui-imageaioptions-i.md) | Yes | AI image analysis options. You can configure the analysis type or bind an analyzer controller through this parameter. If the value is **null** or **undefined**, the default value of **ImageAIOptions** is used. |

## Canvas

```TypeScript
Canvas(params: CanvasParams)
```

Creates a **Canvas** component that does not cache commands using **CanvasParams**. The maximum allowed size cannot exceed 10000 px × 10000 px. If the size exceeds this limit, the **Canvas** component will fail to be created.

> **NOTE：**
> 
> * The **Canvas** component created using this API will return a DrawingRenderingContext
> object in the input parameter of the onReady callback, which can be used for drawing on the
> **Canvas** component.
> 
> * The **Canvas** component created using this API will not respond to drawing commands
> when it is not visible.
> 
> * Scenarios where the component is not visible mainly include: the page containing the
> component moves to the background, the component slides outside the window, or the
> visibility
> attribute is set to hidden. This does not include scenarios where the component is obscured
> by other components or windows.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [CanvasParams](arkts-arkui-canvasparams-i.md) | Yes | Construction parameters of the **Canvas** component. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [CanvasParams](arkts-arkui-canvasparams-i.md) | Defines the parameters of the **Canvas** component. |
| [CanvasPattern](arkts-arkui-canvaspattern-i.md) | **CanvasPattern** represents an object, created by the createPattern API, describing an image filling pattern based on the image and repetition mode. |
| [RenderingContextOptions](arkts-arkui-renderingcontextoptions-i.md) | Defines the specific configuration parameters for the rendering context. |
| [Size](arkts-arkui-size-i.md) | Provides size information of the **DrawingRenderingContext** object. |
| [TextMetrics](arkts-arkui-textmetrics-i.md) | Size information of the text. |

### Types

| Name | Description |
| --- | --- |
| [CanvasDirection](arkts-arkui-canvasdirection-t.md) | Defines the current text direction. The value type is a union of the types listed in the table below. |
| [CanvasFillRule](arkts-arkui-canvasfillrule-t.md) | Defines the fill pattern algorithm used to determine whether a point is inside or outside a path. The value type is a union of the types listed in the table below. |
| [CanvasLineCap](arkts-arkui-canvaslinecap-t.md) | Specifies the attribute of drawing the end of each line segment. |
| [CanvasLineJoin](arkts-arkui-canvaslinejoin-t.md) | Defines the type of join between two non-zero-length segments (lines, arcs, and curves). The value type is a union of the types listed in the table below. |
| [CanvasTextAlign](arkts-arkui-canvastextalign-t.md) | Defines the type of text alignment. The value type is a union of the types listed in the table below. |
| [CanvasTextBaseline](arkts-arkui-canvastextbaseline-t.md) | Defines the text baseline type. The value type is a union of the types listed in the table below. |
| [DrawingCanvas](arkts-arkui-drawingcanvas-t.md) | Defines a canvas object for drawing content on the **XComponent** component. |
| [FrameNode](arkts-arkui-framenode-t.md) | Import the frame node type object for Canvas. |
| [ImageSmoothingQuality](arkts-arkui-imagesmoothingquality-t.md) | Sets the image smoothness attribute. |

## Examples

This example describes how to use the APIs in [CanvasRenderingContext2D](./ts-canvasrenderingcontext2d.md) for drawing on a canvas.

```TypeScript
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillRect(0, 30, 100, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

This example demonstrates how to use the APIs in [DrawingRenderingContext](./ts-drawingrenderingcontext.md) for drawing on a canvas.

```TypeScript
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private context: DrawingRenderingContext = new DrawingRenderingContext();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.canvas.drawCircle(200, 200, 100)
          this.context.invalidate()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

This example demonstrates how to use [attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier) to dynamically set the [enableAnalyzer](#enableanalyzer12) attribute and [onReady](#onready) method of the Canvas component.

```TypeScript
// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';

class MyCanvasModifier implements AttributeModifier<CanvasAttribute> {
  context: CanvasRenderingContext2D = new CanvasRenderingContext2D()

  applyNormalAttribute(instance: CanvasAttribute): void {
    // Draw an image with the width and height of 200 vp from (0, 0).
    instance.onReady(() => {
      // Replace "common/img.png" with the image resource file you use.
      let image = new ImageBitmap("common/img.png")
      this.context.drawImage(image, 0, 0, 200, 200)
    })
    // Enable the component AI analysis function, and click the start button to call the startImageAnalyzer method to start AI analysis.
    instance.enableAnalyzer(true)
  }
}

@Entry
@Component
struct attributeDemo {
  @State modifier: MyCanvasModifier = new MyCanvasModifier()
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  private config: ImageAnalyzerConfig = {
    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT]
  }
  private aiController: ImageAnalyzerController = new ImageAnalyzerController()
  private options: ImageAIOptions = {
    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT],
    aiController: this.aiController
  }

  build() {
    Row() {
      Column() {
        Button('start')
          .width(100)
          .height(50)
          .margin(5)
          .onClick(() => {
            this.context.startImageAnalyzer(this.config)
              .then(() => {
                console.info("analysis complete")
              })
              .catch((error: BusinessError) => {
                console.error(`Error code: ${error.code}, message: ${error.message}`)
              })
          })
        Button('stop')
          .width(100)
          .height(50)
          .margin(5)
          .onClick(() => {
            this.context.stopImageAnalyzer()
          })
        Button('getTypes')
          .width(100)
          .height(50)
          .margin(5)
          .onClick(() => {
            this.aiController.getImageAnalyzerSupportTypes()
          })
        Canvas(this.context, this.options)
          .borderWidth(1)
          .height(200)
          .width(200)
          .attributeModifier(this.modifier)
          .onAppear(() => {
            this.modifier.context = this.context
          })
      }
    }
  }
}
```

This example demonstrates how to use [CanvasParams](arkts-arkui-canvasparams-i.md) to create a Canvas component that does not cache commands for drawing.

```TypeScript
// xxx.ets
import { LengthMetricsUnit } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

@Entry
@Component
struct CanvasExample {
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas({ unit: LengthMetricsUnit.DEFAULT })
        .onReady((drawingContext?: DrawingRenderingContext) => {
          if (!drawingContext) {
            return
          }
          // Use DrawingRenderingContext for drawing.
          let brush = new drawing.Brush()
          brush.setColor({
            alpha: 255,
            red: 39,
            green: 135,
            blue: 217
          })
          drawingContext.canvas.attachBrush(brush)
          drawingContext.canvas.drawCircle(200, 200, 100)
          drawingContext.invalidate()

          // Use CanvasRenderingContext2D for drawing.
          let context2D: CanvasRenderingContext2D =
            CanvasRenderingContext2D.getContext2DFromDrawingContext(drawingContext, { antialias: true })
          context2D.fillStyle = 'rgb(39,135,217)'
          context2D.fillRect(110, 30, 100, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
