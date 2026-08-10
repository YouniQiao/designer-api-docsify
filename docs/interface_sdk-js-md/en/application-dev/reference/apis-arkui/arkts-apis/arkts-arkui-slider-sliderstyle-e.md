# SliderStyle

滑动条滑块在滑轨上显示的样式，具体样式请参考[Slider组件滑块与滑轨是如何对齐的](../../../ui/arkts-select-component-faq.md#slider组件滑块与滑轨是如何对齐的)。

> **说明：**
> 
> - Slider无默认padding。
> 
> - 当Slider为水平滑动条时，默认高度为40vp，宽度为父容器的宽度，滑动条居中显示，当滑动条的style为SliderStyle.OutSet时，左右间距分别为9vp，即为
> [blockSize](blockSize)宽度的一半，当滑动条的style为SliderStyle.InSet时，左右间距分别为6vp，若设置padding，padding不会覆盖左右间距。
> 
> - 当Slider为竖直滑动条时，默认宽度为40vp，高度为父容器的高度，滑动条居中显示，当滑动条的style为SliderStyle.OutSet时，上下间距分别为10vp，当滑动条的style为
> SliderStyle.InSet时，上下间距分别为6vp，若设置padding，padding不会覆盖上下间距。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum SliderStyle--><!--Device-unnamed-export declare enum SliderStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## OutSet

```TypeScript
OutSet
```

滑块在滑轨上。

**卡片能力（仅ArkTS-Dyn）：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**原子化服务API（仅ArkTS-Dyn）：** 从API version 11开始，该接口支持在原子化服务中使用。

**ArkTS-Dyn起始版本：** 7

**ArkTS-Sta起始版本：** 23

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderStyle-OutSet--><!--Device-SliderStyle-OutSet-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## InSet

```TypeScript
InSet
```

滑块在滑轨内。

**卡片能力（仅ArkTS-Dyn）：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**原子化服务API（仅ArkTS-Dyn）：** 从API version 11开始，该接口支持在原子化服务中使用。

**ArkTS-Dyn起始版本：** 7

**ArkTS-Sta起始版本：** 23

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderStyle-InSet--><!--Device-SliderStyle-InSet-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NONE

```TypeScript
NONE
```

无滑块 

**卡片能力（仅ArkTS-Dyn）：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**原子化服务API（仅ArkTS-Dyn）：** 从API version 12开始，该接口支持在原子化服务中使用。

**ArkTS-Dyn起始版本：** 12

**ArkTS-Sta起始版本：** 23

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderStyle-NONE--><!--Device-SliderStyle-NONE-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

