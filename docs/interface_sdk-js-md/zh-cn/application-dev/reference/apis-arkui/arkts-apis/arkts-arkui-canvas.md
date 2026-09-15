# canvas

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

```TypeScript
使用drawImage绘制图像，通过getImageData接口获取ImageData对象，再使用putImageData接口将图像数据绘制到Canvas上。
```

```TypeScript
### 示例1（width属性用法）


```

```TypeScript
### 示例2（height属性用法）


```

```TypeScript
### 示例3（canvas属性用法）
```

```TypeScript
通过createPattern创建CanvasPattern对象，在onReady回调和按钮点击时分别设置matrix参数，并调用setTransform方法进行矩阵变换。

> 说明：
> 
> 此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-profile#section754823013348)相关介绍。
```

```TypeScript
### 示例1（使用CanvasRenderingContext2D中的方法）

该示例实现了如何在Canvas组件使用[CanvasRenderingContext2D](./ts-canvasrenderingcontext2d.md)中的方法进行绘制。


```

```TypeScript
### 示例2（使用DrawingRenderingContext中的方法）

该示例实现了如何在Canvas组件使用[DrawingRenderingContext](./ts-drawingrenderingcontext.md)中的方法进行绘制。


```

```TypeScript
### 示例3（使用attributeModifier动态设置Canvas组件的属性及方法）

该示例展示了如何使用[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置Canvas组件的enableAnalyzer属性和onReady方法。

> 说明：
> 
> 此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需启用相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-profile#section754823013348)相关介绍。


```

```TypeScript
### 示例4（创建不缓存指令Canvas并进行绘制）

该示例介绍了如何使用[CanvasParams](arkts-arkui-canvasparams-i.md)创建不缓存指令的Canvas组件并进行绘制。

从API version 23开始，新增CanvasParams接口。
```

```TypeScript
### 示例1（绘制图形）

该示例实现了如何使用DrawingRenderingContext中的方法绘制图形。

图1 绘制圆心为(200, 200)，半径为100的圆，填充色为RGBA(39, 135, 217, 255)



图2 点击Clear按钮清空画布


```

```TypeScript
### 示例2（绘制文本）

该示例实现了通过[makeFromRawFile](../../apis-arkgraphics2d/arkts-apis-graphics-drawing-Typeface.md#makefromrawfile)（从API version 18开始）加载自定义字体。并使用[drawTextBlob](../../apis-arkgraphics2d/arkts-apis-graphics-drawing-Canvas.md#drawtextblob)绘制文本，drawing接口绘制自定义文字时，不需要调用this.uiContext.getFont().[registerFont](../arkts-apis-uicontext-font.md#registerfont)或者fontCollection.[loadFontSync](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-text-fontcollection-c.md#loadfontsync)提前注册字体，而是通过drawing.Typeface.[makeFromRawFile](../../apis-arkgraphics2d/arkts-apis-graphics-drawing-Typeface.md#makefromrawfile)（从API version 18开始）传入rawfile目录下的自定义字体文件。
```

```TypeScript
### 示例1（加载图片）

通过ImageBitmap加载本地图片。

> 说明：
> 
> 此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需启用相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-profile#section754823013348)相关介绍。


```

```TypeScript
### 示例2（创建ImageBitmap）

通过PixelMap创建ImageBitmap对象。

> 说明：
> 
> DevEco Studio的预览器不支持getPixelMap接口，不支持显示PixelMap绘制的内容。


```

```TypeScript
### 示例3（支持并发线程绘制）

通过创建Worker线程，实现并发线程绘制。

> 说明：
> 
> DevEco Studio的预览器不支持显示在Worker线程中绘制的内容。
```

```TypeScript
Worker线程在onmessage中接收到主线程postMessage发送的ImageBitmap，并进行绘制。


```

```TypeScript
### 示例4（加载Resource图片）

通过constructor接口创建Resource类型的ImageBitmap对象，用于Canvas绘制。

从API版本26.0.0开始，新增[constructor](#constructor-2)接口。
```
