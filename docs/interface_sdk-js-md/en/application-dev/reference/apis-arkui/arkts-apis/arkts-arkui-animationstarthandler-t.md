# AnimationStartHandler

```TypeScript
export type AnimationStartHandler = (index: int, targetIndex: int, event: SwiperAnimationEvent) => void
```

Handler of swiper, used in OnAnimationStart.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type AnimationStartHandler = (index: int, targetIndex: int, event: SwiperAnimationEvent) => void--><!--Device-unnamed-export type AnimationStartHandler = (index: int, targetIndex: int, event: SwiperAnimationEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index of the current swiper. |
| targetIndex | int | Yes | The index of the target swiper. |
| event | [SwiperAnimationEvent](../arkts-components/arkts-arkui-swiperanimationevent-i.md) | Yes | The extra information of the animation. |

