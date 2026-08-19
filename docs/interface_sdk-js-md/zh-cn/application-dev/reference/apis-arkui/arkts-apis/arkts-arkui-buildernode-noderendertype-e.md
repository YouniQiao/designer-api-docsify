# NodeRenderType

节点渲染类型枚举。 &gt; **说明：** &gt; &gt; - RENDER_TYPE_TEXTURE类型目前仅在[BuilderNode](../../apis-na/arkts-apis/arkts-na-buildernode-c.md)持有组件树的根节点为自定义组件时以及 &gt; [XComponentNode](arkts-arkui-xcomponentnode-c.md)中设置生效。 &gt; &gt; - 在[BuilderNode](../../apis-na/arkts-apis/arkts-na-buildernode-c.md)的情况下，目前在作为根节点的自定义组件中支持纹理导出的有以下组件：Badge &gt; 、Blank、Button、 &gt; CanvasGradient、CanvasPattern、 &gt; CanvasRenderingContext2D、 &gt; Canvas、CheckboxGroup、 &gt; Checkbox、Circle、 &gt; ColumnSplit、Column、 &gt; ContainerSpan、 &gt; Counter、DataPanel、 &gt; Divider、Ellipse、 &gt; Flex、Gauge、 &gt; Hyperlink、ImageBitmap、 &gt; ImageData、Image、 &gt; Line、LoadingProgress、 &gt; Marquee、Matrix2D、 &gt; OffscreenCanvasRenderingContext2D、 &gt; OffscreenCanvas、Path2D、 &gt; Path、PatternLock、 &gt; Polygon、Polyline、 &gt; Progress、QRCode、 &gt; Radio、Rating、 &gt; Rect、 &gt; RelativeContainer、 &gt; RowSplit、Row、 &gt; Shape、Slider、 &gt; Span、Stack、 &gt; TextArea、TextClock、 &gt; TextInput、TextTimer、 &gt; Text、Toggle、 &gt; Video（不含全屏播放能力）、Web、 &gt; XComponent。 &gt; &gt; - 从API version 12开始，新增以下组件支持纹理导出：DatePicker、 &gt; ForEach、Grid、 &gt; [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md)、 &gt; LazyForEach、List、 &gt; Scroll、Swiper、 &gt; TimePicker、 &gt; [@Component](../../../ui/state-management/arkts-create-custom-components.md#component)修饰的自定义组件、 &gt; NodeContainer以及 &gt; NodeContainer下挂载的FrameNode和 &gt; [RenderNode](arkts-arkui-rendernode-c.md)。 &gt; &gt; - 使用方式可参考[同层渲染绘制](../../../web/web-same-layer.md)。

**起始版本：** 11

<!--Device-unnamed-export declare enum NodeRenderType--><!--Device-unnamed-export declare enum NodeRenderType-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## RENDER_TYPE_DISPLAY

```TypeScript
RENDER_TYPE_DISPLAY = 0
```

表示该节点将被显示到屏幕上。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NodeRenderType-RENDER_TYPE_DISPLAY = 0--><!--Device-NodeRenderType-RENDER_TYPE_DISPLAY = 0-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## RENDER_TYPE_TEXTURE

```TypeScript
RENDER_TYPE_TEXTURE = 1
```

表示该节点将被导出为纹理。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-NodeRenderType-RENDER_TYPE_TEXTURE = 1--><!--Device-NodeRenderType-RENDER_TYPE_TEXTURE = 1-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

