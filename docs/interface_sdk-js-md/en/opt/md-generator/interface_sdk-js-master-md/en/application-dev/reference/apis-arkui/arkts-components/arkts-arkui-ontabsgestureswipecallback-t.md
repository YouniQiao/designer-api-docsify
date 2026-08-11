# OnTabsGestureSwipeCallback

```TypeScript
declare type OnTabsGestureSwipeCallback = (index: number, extraInfo: TabsAnimationEvent) => void
```

Defines the callback triggered on a frame-by-frame basis during a swipe-based page turn.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-declare type OnTabsGestureSwipeCallback = (index: number, extraInfo: TabsAnimationEvent) => void--><!--Device-unnamed-declare type OnTabsGestureSwipeCallback = (index: number, extraInfo: TabsAnimationEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| extraInfo | [TabsAnimationEvent](arkts-arkui-tabsanimationevent-i.md) | Yes |
