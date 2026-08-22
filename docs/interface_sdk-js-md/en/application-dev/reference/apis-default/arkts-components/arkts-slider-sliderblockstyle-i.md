# SliderBlockStyle

Describes the style of the slider in the block direction.

@interface SliderBlockStyle

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface SliderBlockStyle--><!--Device-unnamed-export declare interface SliderBlockStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## image

```TypeScript
image?: ResourceStr
```

Image resource of the slider. The area size for displaying the image is subject to the blockSize attribute. Be mindful of the image size when selecting an image.

**Type:** [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderBlockStyle-image?: ResourceStr--><!--Device-SliderBlockStyle-image?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shape

```TypeScript
shape?: CircleShape | EllipseShape | PathShape | RectShape
```

Custom shape of the slider.

**Type:** [CircleShape](../arkts-apis/arkts-arkuishape-circleshape-c.md) \| [EllipseShape](../arkts-apis/arkts-arkuishape-ellipseshape-c.md) \| [PathShape](../arkts-apis/arkts-arkuishape-pathshape-c.md) \| [RectShape](../arkts-apis/arkts-arkuishape-rectshape-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderBlockStyle-shape?: CircleShape | EllipseShape | PathShape | RectShape--><!--Device-SliderBlockStyle-shape?: CircleShape | EllipseShape | PathShape | RectShape-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: SliderBlockType
```

Type of the slider in the block direction.

**Type:** [SliderBlockType](arkts-slider-sliderblocktype-e.md)

**Default:** SliderBlockType.DEFAULT - indicating the round slider.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderBlockStyle-type: SliderBlockType--><!--Device-SliderBlockStyle-type: SliderBlockType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

