# SliderBlockStyle

Describes the style of the slider in the block direction.

**Since:** 10

<!--Device-unnamed-declare interface SliderBlockStyle--><!--Device-unnamed-declare interface SliderBlockStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## image

```TypeScript
image?: ResourceStr
```

Image resource of the slider.

The area size for displaying the image is subject to the **blockSize** attribute. Be mindful of the image size when selecting an image.

**Type:** ResourceStr

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SliderBlockStyle-image?: ResourceStr--><!--Device-SliderBlockStyle-image?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shape

```TypeScript
shape?: CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute
```

Custom shape of the slider.

**Type:** CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SliderBlockStyle-shape?: CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute--><!--Device-SliderBlockStyle-shape?: CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: SliderBlockType
```

Type of the slider in the block direction.

Default value: **SliderBlockType.DEFAULT**, indicating the round slider.

**Type:** SliderBlockType

**Default:** SliderBlockType.DEFAULT - indicating the round slider. [since 11]

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SliderBlockStyle-type: SliderBlockType--><!--Device-SliderBlockStyle-type: SliderBlockType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

