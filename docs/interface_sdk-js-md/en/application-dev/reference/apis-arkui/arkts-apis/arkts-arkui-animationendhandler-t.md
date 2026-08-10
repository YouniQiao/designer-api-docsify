# AnimationEndHandler

```TypeScript
export type AnimationEndHandler = (index: int, event: SwiperAnimationEvent) => void
```

切换动画结束时的回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type AnimationEndHandler = (index: int, event: SwiperAnimationEvent) => void--><!--Device-unnamed-export type AnimationEndHandler = (index: int, event: SwiperAnimationEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | 当前显示元素的索引。 |
| event | [SwiperAnimationEvent](../arkts-components/arkts-arkui-swiperanimationevent-i.md) | Yes | 动画相关信息，只返回主轴方向上当前显示元素相对于ArcSwiper起始位置的位移。 |

