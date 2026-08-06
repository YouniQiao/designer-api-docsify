# OnTabsAnimationEndCallback

```TypeScript
export type OnTabsAnimationEndCallback = (index: int, extraInfo: TabsAnimationEvent) => void
```

Defines a tabs callback when onAnimationEnd.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnTabsAnimationEndCallback = (index: int, extraInfo: TabsAnimationEvent) => void--><!--Device-unnamed-export type OnTabsAnimationEndCallback = (index: int, extraInfo: TabsAnimationEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index value of the tab that when animation end. The value range is all integers The value should be an integer.  |
| extraInfo | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The extra callback info.  |

