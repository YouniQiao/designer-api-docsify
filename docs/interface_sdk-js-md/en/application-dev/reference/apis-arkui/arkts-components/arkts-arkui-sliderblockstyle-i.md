# SliderBlockStyle

Slider组件滑块形状参数。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface SliderBlockStyle--><!--Device-unnamed-declare interface SliderBlockStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## image

```TypeScript
image?: ResourceStr
```

设置滑块图片资源。

图片显示区域大小由blockSize属性控制，请勿输入尺寸过大的图片。

**Type:** [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SliderBlockStyle-image?: ResourceStr--><!--Device-SliderBlockStyle-image?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shape

```TypeScript
shape?: CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute
```

设置滑块使用的自定义形状。

**Type:** [CircleAttribute](arkts-arkui-circle-attribute.md) \| EllipseAttribute \| PathAttribute \| RectAttribute

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SliderBlockStyle-shape?: CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute--><!--Device-SliderBlockStyle-shape?: CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: SliderBlockType
```

滑块形状。

默认值：SliderBlockType.DEFAULT，使用圆形滑块。

**Type:** [SliderBlockType](../arkts-apis/arkts-arkui-slider-sliderblocktype-e.md)

**Default:** SliderBlockType.DEFAULT - indicating the round slider. [since 11]

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SliderBlockStyle-type: SliderBlockType--><!--Device-SliderBlockStyle-type: SliderBlockType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

