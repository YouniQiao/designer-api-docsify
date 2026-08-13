# OnSwiperGestureSwipeCallback

```TypeScript
declare type OnSwiperGestureSwipeCallback = (index: number, extraInfo: SwiperAnimationEvent) => void
```

Defines the callback triggered on a frame-by-frame basis when the page is turned by a swipe.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-declare type OnSwiperGestureSwipeCallback = (index: number, extraInfo: SwiperAnimationEvent) => void--><!--Device-unnamed-declare type OnSwiperGestureSwipeCallback = (index: number, extraInfo: SwiperAnimationEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| extraInfo | [SwiperAnimationEvent](arkts-arkui-swiperanimationevent-i.md) | Yes |
