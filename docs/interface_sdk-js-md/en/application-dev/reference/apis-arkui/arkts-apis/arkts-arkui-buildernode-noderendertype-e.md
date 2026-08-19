# NodeRenderType

Enumerates the node rendering types. &gt; **NOTE：**&gt; &gt; - Currently, the **RENDER_TYPE_TEXTURE** type takes effect only for the &gt; [XComponentNode](arkts-arkui-xcomponentnode-c.md) and the [BuilderNode](../../apis-na/arkts-apis/arkts-na-buildernode-c.md) holding a &gt; component tree whose root node is a custom component. &gt; &gt; - The following custom components currently support texture export as root nodes in &gt; [BuilderNode](../../apis-na/arkts-apis/arkts-na-buildernode-c.md) scenarios: Badge, &gt; Blank, Button, &gt; CanvasGradient, &gt; CanvasPattern, &gt; CanvasRenderingContext2D, &gt; Canvas, CheckboxGroup, &gt; Checkbox, Circle, &gt; ColumnSplit, Column, &gt; ContainerSpan, &gt; Counter, DataPanel, &gt; Divider, Ellipse, &gt; Flex, Gauge, &gt; Hyperlink, ImageBitmap, &gt; ImageData, Image, &gt; Line, &gt; LoadingProgress, &gt; Marquee, Matrix2D, &gt; OffscreenCanvasRenderingContext2D, &gt; OffscreenCanvas, Path2D, &gt; Path, PatternLock, &gt; Polygon, Polyline, &gt; Progress, QRCode, &gt; Radio, Rating, &gt; Rect, &gt; RelativeContainer, &gt; RowSplit, Row, &gt; Shape, Slider, &gt; Span, Stack, &gt; TextArea, TextClock, &gt; TextInput, TextTimer, &gt; Text, Toggle, &gt; Video (excluding full-screen playback), &gt; Web, XComponent. &gt; &gt; - Since API version 12, the following components also support texture export: &gt; DatePicker, ForEach, &gt; Grid, &gt; [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md), &gt; LazyForEach, List, &gt; Scroll, Swiper, &gt; TimePicker, custom components decorated with &gt; [@Component](../../../ui/state-management/arkts-create-custom-components.md#component), &gt; NodeContainer, and FrameNode and &gt; [RenderNode](../../apis-na/arkts-apis/arkts-na-rendernode-c.md) mounted to &gt; NodeContainer. &gt; &gt; - For details, see &gt; [Rendering and Drawing Video and Button Components at the Same Layer](../../../web/web-same-layer.md).

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

