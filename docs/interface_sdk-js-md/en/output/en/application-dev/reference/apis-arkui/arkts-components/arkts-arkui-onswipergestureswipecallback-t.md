# OnSwiperGestureSwipeCallback

```TypeScript
declare type OnSwiperGestureSwipeCallback = (index: number, extraInfo: SwiperAnimationEvent) => void
```

Defines the callback triggered on a frame-by-frame basis when the page is turned by a swipe.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-declare type OnSwiperGestureSwipeCallback = (index: number, extraInfo: SwiperAnimationEvent) => void--><!--Device-unnamed-declare type OnSwiperGestureSwipeCallback = (index: number, extraInfo: SwiperAnimationEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | Index of the currently displayed element. If there are multiple columns, **index** indicates the index of the leftmost component.  |
| extraInfo | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Extra information of the animation, which is the offset of the currently displayed element relative to the start position of the **Swiper** along the main axis.  |

