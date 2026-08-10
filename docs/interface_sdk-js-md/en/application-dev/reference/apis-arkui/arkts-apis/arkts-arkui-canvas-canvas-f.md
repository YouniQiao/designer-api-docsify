# Canvas

## Canvas

```TypeScript
export declare function Canvas(
  context?: CanvasRenderingContext2D | DrawingRenderingContext, imageAIOptions?: ImageAIOptions
): CanvasAttribute
```

创建Canvas组件时，最大面积不超过10000px*10000px，超过最大面积则无法正常创建。CanvasRenderingContext2D: 不支持多个Canvas共用一个CanvasRenderingContext2D对象。DrawingRenderingContext: 不支持多个Canvas共用一个DrawingRenderingContext对象。异常值null和undefined按未设置context处理。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Canvas(  context?: CanvasRenderingContext2D | DrawingRenderingContext, imageAIOptions?: ImageAIOptions): CanvasAttribute--><!--Device-unnamed-export declare function Canvas(  context?: CanvasRenderingContext2D | DrawingRenderingContext, imageAIOptions?: ImageAIOptions): CanvasAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [CanvasRenderingContext2D](arkts-arkui-canvasrenderingcontext2d-c.md) \| DrawingRenderingContext | No | Canvas组件的绘图上下文。 |
| imageAIOptions | [ImageAIOptions](arkts-arkui-imageaioptions-i.md) | No | 给组件设置一个AI分析选项， 通过此项可配置分析类型或绑定一个分析控制器。 异常值null和undefined按ImageAIOptions的默认值处理， 默认取值为{ type: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT], aiController: new ImageAnalyzerController() }， 即开启主体识别和文字识别功能。 |

**Return value:**

| Type | Description |
| --- | --- |
| [CanvasAttribute](arkts-arkui-canvas-canvasattribute-i.md) | The attribute of the Canvas. |


## Canvas

```TypeScript
export declare function Canvas(
  params: CanvasParams
): CanvasAttribute
```

使用CanvasParams创建不缓存指令的Canvas组件。创建Canvas组件时，最大面积不超过10000px*10000px，超过最大面积则无法正常创建。Canvas组件未设置固定尺寸时，默认扩展至其最大可用尺寸。

> **说明：**
> 
> - 使用本接口创建的Canvas组件将在onReady回调的入参中返回一个
> DrawingRenderingContext对象，可用于在该Canvas组件上进行绘制。
> 
> - 使用这个接口创建的Canvas组件在组件不可见时将不响应绘制指令。
> 
> - 不可见场景主要包括组件所在的页面进入后台、组件滑到窗口外、
> 设置visibility属性为隐藏等，不包括组件被其他组件或是其他窗口遮挡导致不可见的场景。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Canvas(  params: CanvasParams): CanvasAttribute--><!--Device-unnamed-export declare function Canvas(  params: CanvasParams): CanvasAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [CanvasParams](arkts-arkui-canvas-canvasparams-i.md) | Yes | Canvas组件的构造参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [CanvasAttribute](arkts-arkui-canvas-canvasattribute-i.md) | The attribute of the Canvas. |


## Canvas

```TypeScript
export declare function Canvas(
    style_: CustomBuilderT<CanvasAttribute>
): CanvasAttribute
```

Defines Canvas Component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Canvas(    style_: CustomBuilderT<CanvasAttribute>): CanvasAttribute--><!--Device-unnamed-export declare function Canvas(    style_: CustomBuilderT<CanvasAttribute>): CanvasAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;CanvasAttribute&gt; | Yes | Canvas attribute instance. |

**Return value:**

| Type | Description |
| --- | --- |
| [CanvasAttribute](arkts-arkui-canvas-canvasattribute-i.md) |  |

