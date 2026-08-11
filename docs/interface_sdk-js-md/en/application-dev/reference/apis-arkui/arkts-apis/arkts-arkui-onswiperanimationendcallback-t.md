# OnSwiperAnimationEndCallback

```TypeScript
export type OnSwiperAnimationEndCallback = (index: int, extraInfo: SwiperAnimationEvent) => void
```

Defines a swiper callback when onAnimationEnd.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnSwiperAnimationEndCallback = (index: int, extraInfo: SwiperAnimationEvent) => void--><!--Device-unnamed-export type OnSwiperAnimationEndCallback = (index: int, extraInfo: SwiperAnimationEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index value of the swiper page that when animation end. The value range is all integers The value should be an integer. |
| extraInfo | [SwiperAnimationEvent](../arkts-components/arkts-arkui-swiperanimationevent-i.md) | Yes | The extra callback info. |

