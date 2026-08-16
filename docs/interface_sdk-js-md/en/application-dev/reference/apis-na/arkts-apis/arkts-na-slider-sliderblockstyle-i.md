# SliderBlockStyle

Describes the style of the slider in the block direction.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface SliderBlockStyle--><!--Device-unnamed-export declare interface SliderBlockStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## image

```TypeScript
image?: ResourceStr
```

Image resource of the slider. The area size for displaying the image is subject to the blockSize attribute. Be mindful of the image size when selecting an image.

**Type:** [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderBlockStyle-image?: ResourceStr--><!--Device-SliderBlockStyle-image?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shape

```TypeScript
shape?: CircleShape | EllipseShape | PathShape | RectShape
```

Custom shape of the slider.

**Type:** [CircleShape](../../apis-arkui/arkts-apis/arkts-arkui-arkui-shape-circleshape-c.md) \| [EllipseShape](../../apis-arkui/arkts-apis/arkts-arkui-arkui-shape-ellipseshape-c.md) \| [PathShape](../../apis-arkui/arkts-apis/arkts-arkui-arkui-shape-pathshape-c.md) \| [RectShape](../../apis-arkui/arkts-apis/arkts-arkui-arkui-shape-rectshape-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderBlockStyle-shape?: CircleShape | EllipseShape | PathShape | RectShape--><!--Device-SliderBlockStyle-shape?: CircleShape | EllipseShape | PathShape | RectShape-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: SliderBlockType
```

Type of the slider in the block direction.

**Type:** [SliderBlockType](arkts-na-slider-sliderblocktype-e.md)

**Default:** SliderBlockType.DEFAULT - indicating the round slider.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderBlockStyle-type: SliderBlockType--><!--Device-SliderBlockStyle-type: SliderBlockType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

