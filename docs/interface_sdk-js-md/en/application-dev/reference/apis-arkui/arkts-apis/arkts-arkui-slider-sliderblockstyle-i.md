# SliderBlockStyle

Slider组件滑块形状参数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface SliderBlockStyle--><!--Device-unnamed-export declare interface SliderBlockStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## image

```TypeScript
image?: ResourceStr
```

设置滑块图片资源。

图片显示区域大小由blockSize属性控制，请勿输入尺寸过大的图片。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderBlockStyle-image?: ResourceStr--><!--Device-SliderBlockStyle-image?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shape

```TypeScript
shape?: CircleShape | EllipseShape | PathShape | RectShape
```

设置滑块使用的自定义形状。

**Type:** [CircleShape](arkts-arkui-arkui-shape-circleshape-c.md) \| EllipseShape \| PathShape \| RectShape

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderBlockStyle-shape?: CircleShape | EllipseShape | PathShape | RectShape--><!--Device-SliderBlockStyle-shape?: CircleShape | EllipseShape | PathShape | RectShape-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: SliderBlockType
```

设置滑块形状。

默认值：SliderBlockType.DEFAULT，使用圆形滑块。

**Type:** [SliderBlockType](arkts-arkui-slider-sliderblocktype-e.md)

**Default:** SliderBlockType.DEFAULT - indicating the round slider.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderBlockStyle-type: SliderBlockType--><!--Device-SliderBlockStyle-type: SliderBlockType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

