# SliderBlockStyle

Describes the style of the slider in the block direction.

**Since:** 10

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## image

```TypeScript
image?: ResourceStr
```

Image resource of the slider.The area size for displaying the image is subject to the **blockSize** attribute. Be mindful of the image size when selecting an image.

**Type:** [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shape

```TypeScript
shape?: CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute
```

Custom shape of the slider.

**Type:** [CircleAttribute](arkts-arkui-circle-attribute.md) \| [EllipseAttribute](arkts-arkui-ellipse-attribute.md) \| [PathAttribute](arkts-arkui-path-attribute.md) \| [RectAttribute](arkts-arkui-rect-attribute.md)

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: SliderBlockType
```

Type of the slider in the block direction.Default value: **SliderBlockType.DEFAULT**, indicating the round slider.

**Type:** [SliderBlockType](arkts-arkui-sliderblocktype-e.md)

**Default:** SliderBlockType.DEFAULT - indicating the round slider. [since 11]

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
