# NodeRenderType

Enumerates the node rendering types.

> **NOTE：**
> 
> - Currently, the **RENDER_TYPE_TEXTURE** type takes effect only for the
> [XComponentNode](arkts-arkui-xcomponentnode-c.md#XComponentNode) and the [BuilderNode](arkts-arkui-buildernode-c.md#BuilderNode) holding a
> component tree whose root node is a custom component.
> 
> - The following custom components currently support texture export as root nodes in
> [BuilderNode](arkts-arkui-buildernode-c.md#BuilderNode) scenarios: [Badge](../@internal/component/ets/badge),
> [Blank](../@internal/component/ets/blank), [Button](../@internal/component/ets/button),
> [CanvasGradient](../@internal/component/ets/canvas),
> [CanvasPattern](../@internal/component/ets/canvas),
> [CanvasRenderingContext2D](../@internal/component/ets/canvas),
> [Canvas](../@internal/component/ets/canvas), [CheckboxGroup](../@internal/component/ets/checkboxgroup),
> [Checkbox](../@internal/component/ets/checkbox), [Circle](../@internal/component/ets/circle),
> [ColumnSplit](../@internal/component/ets/column_split), [Column](../@internal/component/ets/column),
> [ContainerSpan](../@internal/component/ets/container_span),
> [Counter](../@internal/component/ets/counter), [DataPanel](../@internal/component/ets/data_panel),
> [Divider](../@internal/component/ets/divider), [Ellipse](../@internal/component/ets/ellipse),
> [Flex](../@internal/component/ets/flex), [Gauge](../@internal/component/ets/gauge),
> [Hyperlink](../@internal/component/ets/hyperlink), [ImageBitmap](../@internal/component/ets/canvas),
> [ImageData](../@internal/component/ets/canvas), [Image](../@internal/component/ets/image),
> [Line](../@internal/component/ets/line),
> [LoadingProgress](../@internal/component/ets/loading_progress),
> [Marquee](../@internal/component/ets/marquee), [Matrix2D](../@internal/component/ets/canvas),
> [OffscreenCanvasRenderingContext2D](../@internal/component/ets/canvas),
> [OffscreenCanvas](../@internal/component/ets/canvas), [Path2D](../@internal/component/ets/canvas),
> [Path](../@internal/component/ets/path), [PatternLock](../@internal/component/ets/pattern_lock),
> [Polygon](../@internal/component/ets/polygon), [Polyline](../@internal/component/ets/polyline),
> [Progress](../@internal/component/ets/progress), [QRCode](../@internal/component/ets/qrcode),
> [Radio](../@internal/component/ets/radio), [Rating](../@internal/component/ets/rating),
> [Rect](../@internal/component/ets/rect),
> [RelativeContainer](../@internal/component/ets/relative_container),
> [RowSplit](../@internal/component/ets/row_split), [Row](../@internal/component/ets/row),
> [Shape](../@internal/component/ets/shape), [Slider](../@internal/component/ets/slider),
> [Span](../@internal/component/ets/span), [Stack](../@internal/component/ets/stack),
> [TextArea](../@internal/component/ets/text_area), [TextClock](../@internal/component/ets/text_clock),
> [TextInput](../@internal/component/ets/text_input), [TextTimer](../@internal/component/ets/text_timer),
> [Text](../@internal/component/ets/text), [Toggle](../@internal/component/ets/toggle),
> [Video](../@internal/component/ets/video) (excluding full-screen playback),
> [Web](../@internal/component/ets/web), [XComponent](../@internal/component/ets/xcomponent).
> 
> - Since API version 12, the following components also support texture export:
> [DatePicker](../@internal/component/ets/date_picker), [ForEach](../@internal/component/ets/for_each),
> [Grid](../@internal/component/ets/grid),
> [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md),
> [LazyForEach](../@internal/component/ets/lazy_for_each), [List](../@internal/component/ets/list),
> [Scroll](../@internal/component/ets/scroll), [Swiper](../@internal/component/ets/swiper),
> [TimePicker](../@internal/component/ets/time_picker), custom components decorated with
> [@Component](../../../ui/state-management/arkts-create-custom-components.md#component),
> [NodeContainer](../@internal/component/ets/node_container), and [FrameNode](./FrameNode) and
> [RenderNode](arkts-arkui-rendernode-c.md#RenderNode) mounted to
> [NodeContainer](../@internal/component/ets/node_container).
> 
> - For details, see
> [Rendering and Drawing Video and Button Components at the Same Layer](../../../web/web-same-layer.md).

**Since:** 11

<!--Device-unnamed-export declare enum NodeRenderType--><!--Device-unnamed-export declare enum NodeRenderType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RENDER_TYPE_DISPLAY

```TypeScript
RENDER_TYPE_DISPLAY = 0
```

The node is displayed on the screen.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NodeRenderType-RENDER_TYPE_DISPLAY = 0--><!--Device-NodeRenderType-RENDER_TYPE_DISPLAY = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RENDER_TYPE_TEXTURE

```TypeScript
RENDER_TYPE_TEXTURE = 1
```

The node is exported as a texture.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-NodeRenderType-RENDER_TYPE_TEXTURE = 1--><!--Device-NodeRenderType-RENDER_TYPE_TEXTURE = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
