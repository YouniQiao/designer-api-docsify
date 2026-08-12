# NodeRenderType

节点渲染类型枚举。

> **说明：**
> 
> - RENDER_TYPE_TEXTURE类型目前仅在[BuilderNode](arkts-arkui-buildernode-c.md#BuilderNode)持有组件树的根节点为自定义组件时以及
> [XComponentNode](arkts-arkui-xcomponentnode-c.md#XComponentNode)中设置生效。
> 
> - 在[BuilderNode](arkts-arkui-buildernode-c.md#BuilderNode)的情况下，目前在作为根节点的自定义组件中支持纹理导出的有以下组件：[Badge](arkts-arkui-tabcontent-tabbaroptions-i.md#badge)、[Blank](blank)、
> [Button](button)、[CanvasGradient](canvas)、[CanvasPattern](canvas)、
> [CanvasRenderingContext2D](canvas)、[Canvas](canvas)、[CheckboxGroup](checkboxgroup)、
> [Checkbox](checkbox)、[Circle](circle)、[ColumnSplit](column_split)、[Column](column)、
> [ContainerSpan](container_span)、[Counter](counter)、[DataPanel](data_panel)、
> [Divider](divider)、[Ellipse](ellipse)、[Flex](flex)、[Gauge](gauge)、
> [Hyperlink](hyperlink)、[ImageBitmap](canvas)、[ImageData](canvas)、[Image](image)、
> [Line](line)、[LoadingProgress](loading_progress)、[Marquee](marquee)、[Matrix2D](canvas)、
> [OffscreenCanvasRenderingContext2D](canvas)、[OffscreenCanvas](canvas)、[Path2D](canvas)、
> [Path](path)、[PatternLock](pattern_lock)、[Polygon](polygon)、[Polyline](polyline)、
> [Progress](progress)、[QRCode](qrcode)、[Radio](radio)、[Rating](rating)、[Rect](rect)、
> [RelativeContainer](relative_container)、[RowSplit](row_split)、[Row](row)、[Shape](shape)、
> [Slider](slider)、[Span](span)、[Stack](stack)、[TextArea](text_area)、
> [TextClock](text_clock)、[TextInput](text_input)、[TextTimer](text_timer)、[Text](text)、
> [Toggle](toggle)、[Video](../../apis-core-file-kit/arkts-apis/arkts-corefile-storagestatistics-storagestats-i-sys.md#video)（不含全屏播放能力）、[Web](web)、[XComponent](xcomponent)。
> 
> - 从API version 12开始，新增以下组件支持纹理导出：[DatePicker](date_picker)、[ForEach](for_each)、[Grid](grid)、
> [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md)、[LazyForEach](lazy_for_each)、
> [List](list)、[Scroll](scroll)、[Swiper](swiper)、[TimePicker](time_picker)、
> [@Component](../../../ui/state-management/arkts-create-custom-components.md#component)修饰的自定义组件、
> [NodeContainer](node_container)以及[NodeContainer](node_container)下挂载的[FrameNode](FrameNode)和
> [RenderNode](arkts-arkui-rendernode-c.md#RenderNode)。
> 
> - 使用方式可参考[同层渲染绘制](../../../web/web-same-layer.md)。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare enum NodeRenderType--><!--Device-unnamed-export declare enum NodeRenderType-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## RENDER_TYPE_DISPLAY

```TypeScript
RENDER_TYPE_DISPLAY = 0
```

表示该节点将被显示到屏幕上。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NodeRenderType-RENDER_TYPE_DISPLAY = 0--><!--Device-NodeRenderType-RENDER_TYPE_DISPLAY = 0-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## RENDER_TYPE_TEXTURE

```TypeScript
RENDER_TYPE_TEXTURE = 1
```

表示该节点将被导出为纹理。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-NodeRenderType-RENDER_TYPE_TEXTURE = 1--><!--Device-NodeRenderType-RENDER_TYPE_TEXTURE = 1-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

