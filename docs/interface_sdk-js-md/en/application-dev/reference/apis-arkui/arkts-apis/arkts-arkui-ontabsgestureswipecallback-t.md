# OnTabsGestureSwipeCallback

```TypeScript
export type OnTabsGestureSwipeCallback = (index: int, extraInfo: TabsAnimationEvent) => void
```

Defines a tabs callback when onGestureSwipe.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnTabsGestureSwipeCallback = (index: int, extraInfo: TabsAnimationEvent) => void--><!--Device-unnamed-export type OnTabsGestureSwipeCallback = (index: int, extraInfo: TabsAnimationEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index value of the tab before gesture swipe. The value range is all integers The value should be an integer. |
| extraInfo | [TabsAnimationEvent](arkts-arkui-tabs-tabsanimationevent-i.md) | Yes | The extra callback info. |

