# NodeRenderType

Enumerates the node rendering types.
> **NOTE**  
>  
> - Currently, the **RENDER_TYPE_TEXTURE** type takes effect only for the  
> [XComponentNode](arkts-arkui-xcomponentnode-c.md) and the [BuilderNode](arkts-arkui-buildernode-c.md) holding a  
> component tree whose root node is a custom component.  
>  
> - The following custom components currently support texture export as root nodes in  
> [BuilderNode](arkts-arkui-buildernode-c.md) scenarios: [Badge](../../apis-arkui/arkts-components/arkts-arkui-badge-i),  
> [Blank](../../apis-arkui/arkts-components/arkts-arkui-blank-i), [Button](../../apis-arkui/arkts-components/arkts-arkui-button-i),  
> [CanvasGradient](../../apis-arkui/arkts-components/arkts-arkui-canvas-i),  
> [CanvasPattern](../../apis-arkui/arkts-components/arkts-arkui-canvas-i),  
> [CanvasRenderingContext2D](../../apis-arkui/arkts-components/arkts-arkui-canvas-i),  
> [Canvas](../../apis-arkui/arkts-components/arkts-arkui-canvas-i), [CheckboxGroup](../../apis-arkui/arkts-components/arkts-arkui-checkboxgroup-i),  
> [Checkbox](../../apis-arkui/arkts-components/arkts-arkui-checkbox-i), [Circle](../../apis-arkui/arkts-components/arkts-arkui-circle-i),  
> [ColumnSplit](../../apis-arkui/arkts-components/arkts-arkui-column_split-i), [Column](../../apis-arkui/arkts-components/arkts-arkui-column-i),  
> [ContainerSpan](../../apis-arkui/arkts-components/arkts-arkui-container_span-i),  
> [Counter](../../apis-arkui/arkts-components/arkts-arkui-counter-i), [DataPanel](../../apis-arkui/arkts-components/arkts-arkui-data_panel-i),  
> [Divider](../../apis-arkui/arkts-components/arkts-arkui-divider-i), [Ellipse](../../apis-arkui/arkts-components/arkts-arkui-ellipse-i),  
> [Flex](../../apis-arkui/arkts-components/arkts-arkui-flex-i), [Gauge](../../apis-arkui/arkts-components/arkts-arkui-gauge-i),  
> [Hyperlink](../../apis-arkui/arkts-components/arkts-arkui-hyperlink-i), [ImageBitmap](../../apis-arkui/arkts-components/arkts-arkui-canvas-i),  
> [ImageData](../../apis-arkui/arkts-components/arkts-arkui-canvas-i), [Image](../../apis-arkui/arkts-components/arkts-arkui-image-i),  
> [Line](../../apis-arkui/arkts-components/arkts-arkui-line-i),  
> [LoadingProgress](../../apis-arkui/arkts-components/arkts-arkui-loading_progress-i),  
> [Marquee](../../apis-arkui/arkts-components/arkts-arkui-marquee-i), [Matrix2D](../../apis-arkui/arkts-components/arkts-arkui-canvas-i),  
> [OffscreenCanvasRenderingContext2D](../../apis-arkui/arkts-components/arkts-arkui-canvas-i),  
> [OffscreenCanvas](../../apis-arkui/arkts-components/arkts-arkui-canvas-i), [Path2D](../../apis-arkui/arkts-components/arkts-arkui-canvas-i),  
> [Path](../../apis-arkui/arkts-components/arkts-arkui-path-i), [PatternLock](../../apis-arkui/arkts-components/arkts-arkui-pattern_lock-i),  
> [Polygon](../../apis-arkui/arkts-components/arkts-arkui-polygon-i), [Polyline](../../apis-arkui/arkts-components/arkts-arkui-polyline-i),  
> [Progress](../../apis-arkui/arkts-components/arkts-arkui-progress-i), [QRCode](../../apis-arkui/arkts-components/arkts-arkui-qrcode-i),  
> [Radio](../../apis-arkui/arkts-components/arkts-arkui-radio-i), [Rating](../../apis-arkui/arkts-components/arkts-arkui-rating-i),  
> [Rect](../../apis-arkui/arkts-components/arkts-arkui-rect-i),  
> [RelativeContainer](../../apis-arkui/arkts-components/arkts-arkui-relative_container-i),  
> [RowSplit](../../apis-arkui/arkts-components/arkts-arkui-row_split-i), [Row](../../apis-arkui/arkts-components/arkts-arkui-row-i),  
> [Shape](../../apis-arkui/arkts-components/arkts-arkui-shape-i), [Slider](../../apis-arkui/arkts-components/arkts-arkui-slider-i),  
> [Span](../../apis-arkui/arkts-components/arkts-arkui-span-i), [Stack](../../apis-arkui/arkts-components/arkts-arkui-stack-i),  
> [TextArea](../../apis-arkui/arkts-components/arkts-arkui-text_area-i), [TextClock](../../apis-arkui/arkts-components/arkts-arkui-text_clock-i),  
> [TextInput](../../apis-arkui/arkts-components/arkts-arkui-text_input-i), [TextTimer](../../apis-arkui/arkts-components/arkts-arkui-text_timer-i),  
> [Text](../../apis-arkui/arkts-components/arkts-arkui-text-i), [Toggle](../../apis-arkui/arkts-components/arkts-arkui-toggle-i),  
> [Video](../../apis-arkui/arkts-components/arkts-arkui-video-i) (excluding full-screen playback),  
> [Web](../../apis-arkui/arkts-components/arkts-arkui-web-i), [XComponent](../../apis-arkui/arkts-components/arkts-arkui-xcomponent-i).  
>  
> - Since API version 12, the following components also support texture export:  
> [DatePicker](../../apis-arkui/arkts-components/arkts-arkui-date_picker-i), [ForEach](../../apis-arkui/arkts-components/arkts-arkui-for_each-i),  
> [Grid](../../apis-arkui/arkts-components/arkts-arkui-grid-i),  
> [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md),  
> [LazyForEach](../../apis-arkui/arkts-components/arkts-arkui-lazy_for_each-i), [List](../../apis-arkui/arkts-components/arkts-arkui-list-i),  
> [Scroll](../../apis-arkui/arkts-components/arkts-arkui-scroll-i), [Swiper](../../apis-arkui/arkts-components/arkts-arkui-swiper-i),  
> [TimePicker](../../apis-arkui/arkts-components/arkts-arkui-time_picker-i), custom components decorated with  
> [@Component](../../../ui/state-management/arkts-create-custom-components.md#component),  
> [NodeContainer](../../apis-arkui/arkts-components/arkts-arkui-node_container-i), and [FrameNode](arkts-arkui-framenode-c.md) and  
> [RenderNode](arkts-arkui-rendernode-c.md) mounted to  
> [NodeContainer](../../apis-arkui/arkts-components/arkts-arkui-node_container-i).  
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

