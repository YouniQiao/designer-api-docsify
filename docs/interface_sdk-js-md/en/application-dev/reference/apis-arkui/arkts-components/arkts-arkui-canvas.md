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

<!--Device-CanvasInterface-(context?: CanvasRenderingContext2D | DrawingRenderingContext): CanvasAttribute--><!--Device-CanvasInterface-(context?: CanvasRenderingContext2D | DrawingRenderingContext): CanvasAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [CanvasRenderingContext2D](arkts-arkui-canvasrenderingcontext2d-c.md) \| [DrawingRenderingContext](arkts-arkui-drawingrenderingcontext-c.md) | No | 2D rendering context for a canvas. <br>**CanvasRenderingContext2D**: Canvases cannot share one **CanvasRenderingContext2D** object. **DrawingRenderingContext**: Canvases cannot share one **DrawingRenderingContext** object. <br>If the value is **null** or **undefined**, **context** is considered unset. |

## Canvas

```TypeScript
Canvas(context: CanvasRenderingContext2D | DrawingRenderingContext, imageAIOptions: ImageAIOptions)
```

Creates a **Canvas** component. You can specify a **CanvasRenderingContext2D** or **DrawingRenderingContext** object, along with AI image analysis options.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CanvasInterface-(context: CanvasRenderingContext2D | DrawingRenderingContext, imageAIOptions: ImageAIOptions): CanvasAttribute--><!--Device-CanvasInterface-(context: CanvasRenderingContext2D | DrawingRenderingContext, imageAIOptions: ImageAIOptions): CanvasAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [CanvasRenderingContext2D](arkts-arkui-canvasrenderingcontext2d-c.md) \| [DrawingRenderingContext](arkts-arkui-drawingrenderingcontext-c.md) | Yes | 2D rendering context for a canvas. <br>**CanvasRenderingContext2D**: Canvases cannot share one **CanvasRenderingContext2D** object. **DrawingRenderingContext**: Canvases cannot share one **DrawingRenderingContext** object. <br>If the value is **null** or **undefined**, **context** is considered unset. |
| imageAIOptions | ImageAIOptions | Yes | AI image analysis options. You can configure the analysis type or bind an analyzer controller through this parameter. <br>If the value is **null** or **undefined**, the default value of **ImageAIOptions** is used. |

## Canvas

```TypeScript
Canvas(params: CanvasParams)
```

Creates a **Canvas** component that does not cache commands using **CanvasParams**. The maximum allowed size cannot exceed 10000 px × 10000 px. If the size exceeds this limit, the **Canvas** component will fail to be created. &gt; **NOTE：**&gt; &gt; * The **Canvas** component created using this API will return a DrawingRenderingContext &gt; object in the input parameter of the onReady callback, which can be used for drawing on the &gt; **Canvas** component. &gt; &gt; * The **Canvas** component created using this API will not respond to drawing commands &gt; when it is not visible. &gt; &gt; * Scenarios where the component is not visible mainly include: the page containing the &gt; component moves to the background, the component slides outside the window, or the &gt; visibility &gt; attribute is set to hidden. This does not include scenarios where the component is obscured &gt; by other components or windows.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CanvasInterface-(params: CanvasParams): CanvasAttribute--><!--Device-CanvasInterface-(params: CanvasParams): CanvasAttribute-End-->

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

