# NodeRenderType

节点渲染类型枚举。 &gt; **说明：** &gt; &gt; - RENDER_TYPE_TEXTURE类型目前仅在[BuilderNode](arkts-na-buildernode-c.md)持有组件树的根节点为自定义组件时以及 &gt; [XComponentNode](../../apis-arkui/arkts-apis/arkts-arkui-xcomponentnode-c.md)中设置生效。 &gt; &gt; - 在[BuilderNode](arkts-na-buildernode-c.md)的情况下，目前在作为根节点的自定义组件中支持纹理导出的有以下组件：[Badge](arkts-na-tabcontent-tabbaroptions-i.md#badge)、Blank、 &gt; Button、[CanvasGradient](../../apis-arkui/arkts-apis/arkts-arkui-canvasrenderingcontext2d-c.md#canvas)、[CanvasPattern](../../apis-arkui/arkts-apis/arkts-arkui-canvasrenderingcontext2d-c.md#canvas)、 &gt; [CanvasRenderingContext2D](../../apis-arkui/arkts-apis/arkts-arkui-canvasrenderingcontext2d-c.md#canvas)、[Canvas](../../apis-arkui/arkts-apis/arkts-arkui-canvasrenderingcontext2d-c.md#canvas)、CheckboxGroup、 &gt; Checkbox、Circle、ColumnSplit、Column、 &gt; ContainerSpan、Counter、DataPanel、 &gt; Divider、Ellipse、Flex、Gauge、 &gt; Hyperlink、[ImageBitmap](../../apis-arkui/arkts-apis/arkts-arkui-canvasrenderingcontext2d-c.md#canvas)、[ImageData](../../apis-arkui/arkts-apis/arkts-arkui-canvasrenderingcontext2d-c.md#canvas)、Image、 &gt; Line、LoadingProgress、Marquee、[Matrix2D](../../apis-arkui/arkts-apis/arkts-arkui-canvasrenderingcontext2d-c.md#canvas)、 &gt; [OffscreenCanvasRenderingContext2D](../../apis-arkui/arkts-apis/arkts-arkui-canvasrenderingcontext2d-c.md#canvas)、[OffscreenCanvas](../../apis-arkui/arkts-apis/arkts-arkui-canvasrenderingcontext2d-c.md#canvas)、[Path2D](../../apis-arkui/arkts-apis/arkts-arkui-canvasrenderingcontext2d-c.md#canvas)、 &gt; Path、PatternLock、Polygon、Polyline、 &gt; Progress、QRCode、Radio、Rating、Rect、 &gt; RelativeContainer、RowSplit、Row、Shape、 &gt; Slider、Span、Stack、TextArea、 &gt; TextClock、TextInput、TextTimer、Text、 &gt; Toggle、[Video](../../apis-core-file-kit/arkts-apis/arkts-corefile-storagestatistics-storagestats-i-sys.md#video)（不含全屏播放能力）、Web、XComponent。 &gt; &gt; - 从API version 12开始，新增以下组件支持纹理导出：DatePicker、ForEach、Grid、 &gt; [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md)、LazyForEach、 &gt; List、Scroll、Swiper、TimePicker、 &gt; [@Component](../../../ui/state-management/arkts-create-custom-components.md#component)修饰的自定义组件、 &gt; NodeContainer以及NodeContainer下挂载的FrameNode和 &gt; [RenderNode](../../apis-arkui/arkts-apis/arkts-arkui-rendernode-c.md)。 &gt; &gt; - 使用方式可参考[同层渲染绘制](../../../web/web-same-layer.md)。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare enum NodeRenderType--><!--Device-unnamed-export declare enum NodeRenderType-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## RENDER_TYPE_DISPLAY

```TypeScript
RENDER_TYPE_DISPLAY = 0
```

表示该节点将被显示到屏幕上。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NodeRenderType-RENDER_TYPE_DISPLAY = 0--><!--Device-NodeRenderType-RENDER_TYPE_DISPLAY = 0-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## RENDER_TYPE_TEXTURE

```TypeScript
RENDER_TYPE_TEXTURE = 1
```

表示该节点将被导出为纹理。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NodeRenderType-RENDER_TYPE_TEXTURE = 1--><!--Device-NodeRenderType-RENDER_TYPE_TEXTURE = 1-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

