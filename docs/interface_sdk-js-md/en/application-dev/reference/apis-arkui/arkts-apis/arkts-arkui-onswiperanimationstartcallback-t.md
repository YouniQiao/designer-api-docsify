# OnSwiperAnimationStartCallback

```TypeScript
export type OnSwiperAnimationStartCallback = (index: int, targetIndex: int,
  extraInfo: SwiperAnimationEvent) => void
```

切换动画开始时触发的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnSwiperAnimationStartCallback = (index: int, targetIndex: int,  extraInfo: SwiperAnimationEvent) => void--><!--Device-unnamed-export type OnSwiperAnimationStartCallback = (index: int, targetIndex: int,  extraInfo: SwiperAnimationEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | 当前显示元素的索引。多列Swiper时，index为最左侧组件的索引。 取值范围为全体整数 取值限定为整数。 |
| targetIndex | int | Yes | 当前显示元素的索引。多列Swiper时，index为最左侧组件的索引。 取值范围为全体整数 取值限定为整数。 |
| extraInfo | [SwiperAnimationEvent](../arkts-components/arkts-arkui-swiperanimationevent-i.md) | Yes | 动画相关信息，包括主轴方向上当前显示元素和目标元素相对Swiper起始位置的位移，以及离手速度。 |

