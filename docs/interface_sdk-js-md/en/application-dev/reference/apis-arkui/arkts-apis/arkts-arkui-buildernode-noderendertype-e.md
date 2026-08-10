# NodeRenderType

节点渲染类型枚举。

> **说明：**
> 
> - RENDER_TYPE_TEXTURE类型目前仅在[BuilderNode](arkts-arkui-buildernode-c.md)持有组件树的根节点为自定义组件时以及
> [XComponentNode](arkts-arkui-xcomponentnode-c.md)中设置生效。
> 
> - 在[BuilderNode](arkts-arkui-buildernode-c.md)的情况下，目前在作为根节点的自定义组件中支持纹理导出的有以下组件：[Badge](arkts-arkui-badge-badge-f.md#badge)、[Blank](arkts-arkui-blank-blank-f.md#blank)、
> [Button](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-mouseevent-button-e.md/arkts-input-multimodalinput-mouseevent-button-e.md)、[CanvasGradient](arkts-arkui-canvas-canvas-f.md#canvas)、[CanvasPattern](arkts-arkui-canvas-canvas-f.md#canvas)、
> [CanvasRenderingContext2D](arkts-arkui-canvas-canvas-f.md#canvas)、[Canvas](arkts-arkui-canvas-canvas-f.md#canvas)、[CheckboxGroup](arkts-arkui-checkboxgroup-checkboxgroup-f.md#checkboxgroup)、
> [Checkbox](arkts-arkui-checkbox-checkbox-f.md#checkbox)、[Circle](arkts-arkui-graphics-circle-i.md)、[ColumnSplit](column_split)、[Column](arkts-arkui-column-column-f.md#column)、
> [ContainerSpan](container_span)、[Counter](arkts-arkui-counter-counter-f.md#counter)、[DataPanel](data_panel)、
> [Divider](arkts-arkui-divider-divider-f.md#divider)、[Ellipse](arkts-arkui-ellipse-ellipse-f.md#ellipse)、[Flex](arkts-arkui-flex-flex-f.md#flex)、[Gauge](arkts-arkui-gauge-gauge-f.md#gauge)、
> [Hyperlink](arkts-arkui-hyperlink-hyperlink-f.md#hyperlink)、[ImageBitmap](arkts-arkui-canvas-canvas-f.md#canvas)、[ImageData](arkts-arkui-canvas-canvas-f.md#canvas)、[Image](../../apis-image-kit/arkts-apis/arkts-multimedia-image.md/arkts-multimedia-image.md)、
> [Line](arkts-arkui-line-line-f.md#line)、[LoadingProgress](loading_progress)、[Marquee](arkts-arkui-marquee-marquee-f.md#marquee)、[Matrix2D](arkts-arkui-canvas-canvas-f.md#canvas)、
> [OffscreenCanvasRenderingContext2D](arkts-arkui-canvas-canvas-f.md#canvas)、[OffscreenCanvas](arkts-arkui-canvas-canvas-f.md#canvas)、[Path2D](arkts-arkui-canvas-canvas-f.md#canvas)、
> [Path](arkts-arkui-path-path-f.md#path)、[PatternLock](pattern_lock)、[Polygon](arkts-arkui-polygon-polygon-f.md#polygon)、[Polyline](arkts-arkui-polyline-polyline-f.md#polyline)、
> [Progress](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-progress-i.md/arkts-corefile-file-fs-progress-i.md)、[QRCode](arkts-arkui-qrcode-qrcode-f.md#qrcode)、[Radio](../../apis-telephony-kit/arkts-apis/arkts-telephony-radio.md/arkts-telephony-radio.md)、[Rating](arkts-arkui-rating-rating-f.md#rating)、[Rect](../../apis-test-kit/arkts-apis/arkts-test-uitest-rect-i.md/arkts-test-uitest-rect-i.md)、
> [RelativeContainer](relative_container)、[RowSplit](row_split)、[Row](arkts-arkui-row-row-f.md#row)、[Shape](arkts-arkui-shape-shape-f.md#shape)、
> [Slider](arkts-arkui-slider-slider-f.md#slider)、[Span](arkts-arkui-span-span-f.md#span)、[Stack](../../apis-arkts/arkts-apis/arkts-arkts-util-stack-stack-c.md/arkts-arkts-util-stack-stack-c.md)、[TextArea](text_area)、
> [TextClock](text_clock)、[TextInput](text_input)、[TextTimer](text_timer)、[Text](../../apis-arkgraphics2d/arkts-apis/arkts-graphics-text.md/arkts-graphics-text.md)、
> [Toggle](arkts-arkui-toggle-toggle-f.md#toggle)、[Video](arkts-arkui-video-video-f.md#video)（不含全屏播放能力）、[Web](../../apis-arkweb/arkts-apis/arkts-arkweb-web-web-f.md/arkts-arkweb-web-web-f.md#web)、[XComponent](arkts-arkui-xcomponent-xcomponent-f.md#xcomponent)。
> 
> - 从API version 12开始，新增以下组件支持纹理导出：[DatePicker](date_picker)、[ForEach](for_each)、[Grid](arkts-arkui-grid-grid-f.md#grid)、
> [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md)、[LazyForEach](lazy_for_each)、
> [List](../../apis-arkts/arkts-apis/arkts-arkts-util-list-list-c.md/arkts-arkts-util-list-list-c.md)、[Scroll](arkts-arkui-scroll-scroll-f.md#scroll)、[Swiper](arkts-arkui-swiper-swiper-f.md#swiper)、[TimePicker](time_picker)、
> [@Component](../../../ui/state-management/arkts-create-custom-components.md#component)修饰的自定义组件、
> [NodeContainer](node_container)以及[NodeContainer](node_container)下挂载的[FrameNode](arkts-arkui-framenode-c.md)和
> [RenderNode](arkts-arkui-rendernode-c.md)。
> 
> - 使用方式可参考[同层渲染绘制](../../../web/web-same-layer.md)。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum NodeRenderType--><!--Device-unnamed-export declare enum NodeRenderType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RENDER_TYPE_DISPLAY

```TypeScript
RENDER_TYPE_DISPLAY = 0
```

表示该节点将被显示到屏幕上。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeRenderType-RENDER_TYPE_DISPLAY = 0--><!--Device-NodeRenderType-RENDER_TYPE_DISPLAY = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RENDER_TYPE_TEXTURE

```TypeScript
RENDER_TYPE_TEXTURE = 1
```

表示该节点将被导出为纹理。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NodeRenderType-RENDER_TYPE_TEXTURE = 1--><!--Device-NodeRenderType-RENDER_TYPE_TEXTURE = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

