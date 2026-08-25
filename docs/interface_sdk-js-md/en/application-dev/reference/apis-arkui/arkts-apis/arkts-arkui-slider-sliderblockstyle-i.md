# SliderBlockStyle

Describes the style of the slider in the block direction.@interface SliderBlockStyle

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## image

```TypeScript
image?: ResourceStr
```

Image resource of the slider. The area size for displaying the image is subject to the blockSize attribute. Be mindful of the image size when selecting an image.

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shape

```TypeScript
shape?: CircleShape | EllipseShape | PathShape | RectShape
```

Custom shape of the slider.

**Type:** [CircleShape](arkts-arkui-arkui-shape-circleshape-c.md) \| [EllipseShape](arkts-arkui-arkui-shape-ellipseshape-c.md) \| [PathShape](arkts-arkui-arkui-shape-pathshape-c.md) \| [RectShape](arkts-arkui-arkui-shape-rectshape-c.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: SliderBlockType
```

Type of the slider in the block direction.

**Type:** [SliderBlockType](arkts-arkui-slider-sliderblocktype-e.md)

**Default:** SliderBlockType.DEFAULT - indicating the round slider.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
