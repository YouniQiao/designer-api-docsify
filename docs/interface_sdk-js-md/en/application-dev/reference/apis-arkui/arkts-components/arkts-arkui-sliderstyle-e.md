# SliderStyle

滑动条滑块在滑轨上显示的样式，样式说明请参考[Slider组件滑块与滑轨是如何对齐的](../../../ui/arkts-select-component-faq.md#slider组件滑块与滑轨是如何对齐的)。

> **说明：**
> 
> - Slider无默认padding。
> 
> - 当Slider为水平滑动条时，默认高度为40vp，宽度为父容器的宽度，滑动条居中显示，当滑动条的style为SliderStyle.OutSet时，左右间距分别为9vp，即为
> [blockSize](SliderAttribute#blockSize)宽度的一半，当滑动条的style为SliderStyle.InSet时，左右间距分别为6vp，若设置padding，padding不会覆盖左右
> 间距。
> 
> - 当Slider为竖直滑动条时，默认宽度为40vp，高度为父容器的高度，滑动条居中显示，当滑动条的style为SliderStyle.OutSet时，上下间距分别为10vp，当滑动条的style为
> SliderStyle.InSet时，上下间距分别为6vp，若设置padding，padding不会覆盖上下间距。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-declare enum SliderStyle--><!--Device-unnamed-declare enum SliderStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## OutSet

```TypeScript
OutSet
```

滑块在滑轨上。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-SliderStyle-OutSet--><!--Device-SliderStyle-OutSet-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## InSet

```TypeScript
InSet
```

滑块在滑轨内。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-SliderStyle-InSet--><!--Device-SliderStyle-InSet-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NONE

```TypeScript
NONE
```

无滑块

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-SliderStyle-NONE--><!--Device-SliderStyle-NONE-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

