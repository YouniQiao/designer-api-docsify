# AnimationStartHandler

```TypeScript
export type AnimationStartHandler = (index: int, targetIndex: int, event: SwiperAnimationEvent) => void
```

切换动画开始时的回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type AnimationStartHandler = (index: int, targetIndex: int, event: SwiperAnimationEvent) => void--><!--Device-unnamed-export type AnimationStartHandler = (index: int, targetIndex: int, event: SwiperAnimationEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | 当前显示元素的索引，动画开始前的index值（不是最终结束动画的index值）。 |
| targetIndex | int | Yes | 当前显示元素的索引，动画开始前的index值（不是最终结束动画的index值）。 |
| event | [SwiperAnimationEvent](../arkts-components/arkts-arkui-swiperanimationevent-i.md) | Yes | 动画相关信息，包括主轴方向上当前显示元素和目标元素相对ArcSwiper起始位置的位移，以及离手速度。 |

