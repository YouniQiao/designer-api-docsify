# canvas

## 导入模块

```TypeScript
```

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [CanvasAttribute](arkts-arkui-canvasattribute-c.md) | 除支持[通用属性](../arkts-components/arkts-arkui-commonmethod-c.md)外，还支持以下属性： |
| [CanvasGradient](arkts-arkui-canvasgradient-c.md) | OffscreenCanvas支持以下属性： |
| [CanvasPath](arkts-arkui-canvaspath-c.md) | 路径对象，提供基本的路径绘制方法。路径相关API的详细说明请参见CanvasRenderingContext2D中的描述。 |
| [CanvasRenderer](arkts-arkui-canvasrenderer-c.md) | CanvasRenderingContext2D对象与Canvas组件绑定后，可在Canvas组件上绘制，绘制对象可以是形状、文本、图片等。 |
| [CanvasRenderingContext2D](arkts-arkui-canvasrenderingcontext2d-c.md) | CanvasRenderingContext2D对象与Canvas组件绑定后，可在Canvas组件上绘制，绘制对象可以是形状、文本、图片等。 |
| [DrawingRenderingContext](arkts-arkui-drawingrenderingcontext-c.md) | DrawingRenderingContext对象与Canvas组件绑定后，可在Canvas组件上进行绘制，绘制对象可以是形状、文本、图片等。 |
| [ImageBitmap](arkts-arkui-imagebitmap-c.md) | ImageBitmap对象可以存储canvas渲染的像素数据。从API version 11开始，当应用创建[Worker线程](../../../arkts-utils/worker-introduction.md)，支持使用postMessage将ImageBitmap实例传到Worker中进行绘制，并使用onmessage接收Worker线程发送的绘制结果进行显示。 |
| [ImageData](arkts-arkui-imagedata-c.md) | ImageData对象用于存储Canvas渲染的像素数据，支持对像素进行读取、修改和操作，适用于图像处理、像素级编辑、特效滤镜等场景。通过ImageData可以精确控制图像的每个像素点，实现自定义图像处理算法，为Canvas绘图提供灵活的像素级数据访问能力。 |
| [OffscreenCanvas](arkts-arkui-offscreencanvas-c.md) | OffscreenCanvas组件用于绘制自定义图形。 |
| [OffscreenCanvasRenderingContext2D](arkts-arkui-offscreencanvasrenderingcontext2d-c.md) |  |
| [Path2D](arkts-arkui-path2d-c.md) | 路径对象，支持通过对象的接口进行路径的描述和组合，并通过Canvas的stroke接口或者fill接口进行绘制。Path2D支持复用路径、组合多个路径、基于SVG路径字符串创建路径等功能，适用于需要多次绘制相同路径、动态组合复杂图形或基于SVG路径数据绘制图形的场景。 |
| [RenderingContextSettings](arkts-arkui-renderingcontextsettings-c.md) | 用于配置CanvasRenderingContext2D对象的参数，包括是否开启抗锯齿。 |

### 接口

| 名称 | 说明 |
| --- | --- |
| [CanvasInterface](arkts-arkui-canvasinterface-i.md) | 提供画布组件，用于自定义绘制图形。 |
| [CanvasParams](arkts-arkui-canvasparams-i.md) | 定义Canvas的具体配置参数。 |
| [CanvasPattern](arkts-arkui-canvaspattern-i.md) | 一个Object对象，使用[createPattern](arkts-arkui-canvasrenderer-c.md#createpattern)方法创建，通过指定图像和重复方式创建图片填充的模板。 |
| [OffscreenCanvasRenderingContext2DInterface](arkts-arkui-offscreencanvasrenderingcontext2dinterface-i.md) | 使用OffscreenCanvasRenderingContext2D在Canvas上进行离屏绘制，绘制对象可以是形状、文本、图片等。离屏绘制是指将需要绘制的内容先绘制在缓存区，然后将其转换成图片，一次性绘制到Canvas上。离屏绘制使用CPU进行绘制，绘制速度较慢，对绘制速度有要求的场景应避免使用离屏绘制。 |
| [RenderingContextOptions](arkts-arkui-renderingcontextoptions-i.md) | 定义渲染上下文的具体配置参数。 |
| [Size](arkts-arkui-size-i.md) | DrawingRenderingContext的尺寸信息。 |
| [TextMetrics](arkts-arkui-textmetrics-i.md) | 文本的尺寸信息。 |

### 类型

| 名称 | 说明 |
| --- | --- |
| [CanvasDirection](arkts-arkui-canvasdirection-t.md) | 定义当前文本方向的类型。取值类型为下表类型中的并集。 |
| [CanvasFillRule](arkts-arkui-canvasfillrule-t.md) | 定义用于确定点是在路径内还是路径外的填充样式算法的类型。取值类型为下表类型中的并集。 |
| [CanvasLineCap](arkts-arkui-canvaslinecap-t.md) | 定义绘制每条线段端点的类型。取值类型为下表类型中的并集。 |
| [CanvasLineJoin](arkts-arkui-canvaslinejoin-t.md) | 定义长度不为0的两个连接部分（线段、圆弧和曲线）的类型。取值类型为下表类型中的并集。 |
| [CanvasTextAlign](arkts-arkui-canvastextalign-t.md) | 定义文本对齐方式的类型。取值类型为下表类型中的并集。 |
| [CanvasTextBaseline](arkts-arkui-canvastextbaseline-t.md) | 定义文本基线类型。取值类型为下表类型中的并集。 |
| [DrawingCanvas](arkts-arkui-drawingcanvas-t.md) | 可用于向DrawingRenderingContext上绘制内容的画布对象。 |
| [FrameNode](arkts-arkui-framenode-t.md) | Import the frame node type object for Canvas. |
| [ImageSmoothingQuality](arkts-arkui-imagesmoothingquality-t.md) | 定义图片平滑度类型。取值类型为下表类型中的并集。 |

### 常量

| 名称 | 说明 |
| --- | --- |
| [Canvas](arkts-arkui-canvas-con.md) | 提供画布组件，用于自定义绘制图形。 |
| [CanvasInstance](arkts-arkui-canvas-con.md#canvasinstance) | 提供画布组件，用于自定义绘制图形。 |

## 示例

使用drawImage绘制图像，通过getImageData接口获取ImageData对象，再使用putImageData接口将图像数据绘制到Canvas上。

```TypeScript
// xxx.ets
@Entry
@Component
struct Translate {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // "common/images/1234.png"需要替换为开发者所需的图像资源文件
  private img: ImageBitmap = new ImageBitmap("common/images/1234.png");

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.drawImage(this.img, 0, 0, 130, 130)
          let imageData = this.context.getImageData(50, 50, 130, 130)
          this.context.putImageData(imageData, 150, 150)
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
struct WidthExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width(300)
        .height(300)
        .backgroundColor('#ffff00')
        .onReady(() => {
          let w = this.context.width
          this.context.fillRect(0, 0, w / 2, 300)
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
struct HeightExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width(300)
        .height(300)
        .backgroundColor('#ffff00')
        .onReady(() => {
          let h = this.context.height
          this.context.fillRect(0, 0, 300, h / 2)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

```TypeScript
import { FrameNode } from '@kit.ArkUI'
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  private text: string = ''

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          let node: FrameNode = this.context.canvas
          node?.commonEvent.setOnVisibleAreaApproximateChange(
            { ratios: [0, 1], expectedUpdateInterval: 10},
            (isVisible: boolean, currentRatio: number) => {
              if (!isVisible && currentRatio <= 0.0) {
                this.text = 'Canvas is completely invisible.'
              }
              if (isVisible && currentRatio >= 1.0) {
                this.text = 'Canvas is fully visible.'
              }
              this.context.reset()
              this.context.font = '30vp sans-serif'
              this.context.fillText(this.text, 50, 50)
            }
          )
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

通过createPattern创建CanvasPattern对象，在onReady回调和按钮点击时分别设置matrix参数，并调用setTransform方法进行矩阵变换。

```TypeScript
// xxx.ets
@Entry
@Component
struct CanvasPatternPage {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private matrix: Matrix2D = new Matrix2D();
  // "common/pattern.jpg"需要替换为开发者所需的图像资源文件
  private img: ImageBitmap = new ImageBitmap('common/pattern.jpg');
  private pattern: CanvasPattern | null = null;

  build() {
      Column() {
        Button('Click to set transform')
          .onClick(() => {
            this.matrix.scaleY = 1
            this.matrix.scaleX = 1
            this.matrix.translateX = 50
            this.matrix.translateY = 200
            if (this.pattern) {
              this.pattern.setTransform(this.matrix)
            }
            this.context.fillRect(0, 0, 480, 720)
          })
          .width('45%')
          .margin('5px')
        Canvas(this.context)
          .width('100%')
          .height('80%')
          .backgroundColor('#FFFFFF')
          .onReady(() => {
            this.pattern = this.context.createPattern(this.img, 'no-repeat')
            this.matrix.scaleY = 0.5
            this.matrix.scaleX = 0.5
            this.matrix.translateX = 50
            this.matrix.translateY = 50
            if (this.pattern) {
              this.context.fillStyle = this.pattern
              this.pattern.setTransform(this.matrix)
            }
            this.context.fillRect(0, 0, 480, 720)
          })
      }
      .width('100%')
      .height('100%')
  }
}
```

该示例实现了如何在Canvas组件使用[CanvasRenderingContext2D](./ts-canvasrenderingcontext2d.md)中的方法进行绘制。

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

该示例实现了如何在Canvas组件使用[DrawingRenderingContext](./ts-drawingrenderingcontext.md)中的方法进行绘制。

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

该示例展示了如何使用[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置Canvas组件的enableAnalyzer属性和onReady方法。

```TypeScript
// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';

class MyCanvasModifier implements AttributeModifier<CanvasAttribute> {
  context: CanvasRenderingContext2D = new CanvasRenderingContext2D()

  applyNormalAttribute(instance: CanvasAttribute): void {
    // 从（0，0）绘制一张宽高为200vp的图片
    instance.onReady(() => {
      // "common/img.png"需要替换为开发者所需的图像资源文件
      let image = new ImageBitmap("common/img.png")
      this.context.drawImage(image, 0, 0, 200, 200)
    })
    // 设置开启组件AI分析功能，点击start按钮调用startImageAnalyzer方法启动AI分析
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

该示例介绍了如何使用[CanvasParams](arkts-arkui-canvasparams-i.md)创建不缓存指令的Canvas组件并进行绘制。

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
          // 使用DrawingRenderingContext进行绘制。
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

          // 使用CanvasRenderingContext2D进行绘制。
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

该示例实现了如何使用DrawingRenderingContext中的方法绘制图形。

```TypeScript
import { common2D, drawing } from '@kit.ArkGraphics2D';

// xxx.ets
@Entry
@Component
struct CanvasExample {
  private context: DrawingRenderingContext = new DrawingRenderingContext();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('50%')
        .backgroundColor('#D5D5D5')
        .onReady(() => {
          let brush = new drawing.Brush();
          // 使用RGBA(39, 135, 217, 255)填充圆心为(200, 200)，半径为100的圆
          brush.setColor({
            alpha: 255,
            red: 39,
            green: 135,
            blue: 217
          });
          this.context.canvas.attachBrush(brush);
          this.context.canvas.drawCircle(200, 200, 100);
          this.context.canvas.detachBrush();
          this.context.invalidate();
        })
      Button("Clear")
        .width('120')
        .height('50')
        .onClick(() => {
          let color: common2D.Color = {
            alpha: 0,
            red: 0,
            green: 0,
            blue: 0
          };
          // 使用RGBA(0, 0, 0, 0)清空画布
          this.context.canvas.clear(color);
          this.context.invalidate();
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

该示例实现了通过[makeFromRawFile](../../apis-arkgraphics2d/arkts-apis-graphics-drawing-Typeface.md#makefromrawfile)（从API version 18开始）加载自定义字体。并使用[drawTextBlob](../../apis-arkgraphics2d/arkts-apis-graphics-drawing-Canvas.md#drawtextblob)绘制文本，drawing接口绘制自定义文字时，不需要调用this.uiContext.getFont().[registerFont](../arkts-apis-uicontext-font.md#registerfont)或者fontCollection.[loadFontSync](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-fontcollection-c.md#loadfontsync)提前注册字体，而是通过drawing.Typeface.[makeFromRawFile](../../apis-arkgraphics2d/arkts-apis-graphics-drawing-Typeface.md#makefromrawfile)（从API version 18开始）传入rawfile目录下的自定义字体文件。

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';

// xxx.ets
@Entry
@Component
struct CanvasExample {
  private context: DrawingRenderingContext = new DrawingRenderingContext();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('50%')
        .backgroundColor('#D5D5D5')
        .onReady(() => {
          // 创建字体对象并设置字体大小为50
          let font = new drawing.Font();
          font.setSize(50);
          // 加载rawfile目录下的自定义字体文件HarmonyOS_Sans_Bold.ttf
          const myTypeFace = drawing.Typeface.makeFromRawFile($rawfile('HarmonyOS_Sans_Bold.ttf'));
          font.setTypeface(myTypeFace);
          // 创建文本Blob对象，参数依次为：文本内容、字体对象、文本编码格式
          const textBlob =
            drawing.TextBlob.makeFromString("Hello World", font, drawing.TextEncoding.TEXT_ENCODING_UTF8);
          // 在坐标(60, 100)处绘制文本Blob
          this.context.canvas.drawTextBlob(textBlob, 60, 100);
          this.context.invalidate();
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

通过ImageBitmap加载本地图片。

```TypeScript
// xxx.ets
@Entry
@Component
struct ImageExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
  private img: ImageBitmap = new ImageBitmap('common/images/example.jpg');

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.drawImage(this.img, 0, 0, 500, 500, 0, 0, 400, 200)
          this.img.close()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

通过PixelMap创建ImageBitmap对象。

```TypeScript
// xxx.ets
@Entry
@Component
struct Demo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('50%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillStyle = '#00ff00'
          this.context.fillRect(0, 0, 100, 100)
          let pixel = this.context.getPixelMap(0, 0, 100, 100)
          let image = new ImageBitmap(pixel)
          this.context.drawImage(image, 100, 100)
        })

    }
    .width('100%')
    .height('100%')
  }
}
```

通过创建Worker线程，实现并发线程绘制。

```TypeScript
import { worker } from '@kit.ArkTS';

@Entry
@Component
struct imageBitmapExamplePage {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private myWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');
  // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
  private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.myWorker.postMessage({ myImage: this.img });
          this.myWorker.onmessage = (e): void => {
            if (e.data.myImage) {
              let image: ImageBitmap = e.data.myImage
              this.context.transferFromImageBitmap(image)
            }
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

Worker线程在onmessage中接收到主线程postMessage发送的ImageBitmap，并进行绘制。

```TypeScript
import { MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
workerPort.onmessage = (e: MessageEvents) => {
  if (e.data.myImage) {
    let img: ImageBitmap = e.data.myImage
    let offCanvas = new OffscreenCanvas(600, 600)
    let offContext = offCanvas.getContext('2d')
    offContext.drawImage(img, 0, 0, 500, 500, 0, 0, 400, 200)
    let image = offCanvas.transferToImageBitmap()
    workerPort.postMessage({ myImage: image });
  }
}
```

通过constructor接口创建Resource类型的ImageBitmap对象，用于Canvas绘制。

```TypeScript
// xxx.ets
@Entry
@Component
struct ImageBitmapResourceExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // "app.media.example"需要替换为开发者所需的图像资源文件
  private img: ImageBitmap = new ImageBitmap($r("app.media.example"));

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => { 
          this.context.drawImage(this.img, 0, 0, 500, 500, 0, 0, 400, 200)
          this.img.close()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
