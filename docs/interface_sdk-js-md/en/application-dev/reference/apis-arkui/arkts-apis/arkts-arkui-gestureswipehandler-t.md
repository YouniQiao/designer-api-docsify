# GestureSwipeHandler

```TypeScript
export type GestureSwipeHandler = (index: int, event: SwiperAnimationEvent) => void
```

Handler of swiper, used in OnGestureSwipe.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type GestureSwipeHandler = (index: int, event: SwiperAnimationEvent) => void--><!--Device-unnamed-export type GestureSwipeHandler = (index: int, event: SwiperAnimationEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index of the current swiper. |
| event | SwiperAnimationEvent | Yes | The extra information of the animation. |

