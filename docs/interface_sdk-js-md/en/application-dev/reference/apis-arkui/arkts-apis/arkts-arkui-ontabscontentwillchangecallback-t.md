# OnTabsContentWillChangeCallback

```TypeScript
export type OnTabsContentWillChangeCallback = (currentIndex: int, comingIndex: int) => boolean
```

Defines a tabs callback when onContentWillChange.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnTabsContentWillChangeCallback = (currentIndex: int, comingIndex: int) => boolean--><!--Device-unnamed-export type OnTabsContentWillChangeCallback = (currentIndex: int, comingIndex: int) => boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| currentIndex | int | Yes | The index value of the current tab. The value range is all integers The value should be an integer.  |
| comingIndex | int | Yes | The index value of the tab that will change. The value range is all integers The value should be an integer.  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Tabs can change from currentIndex to comingIndex if function return true. Tabs can not change from currentIndex to comingIndex if function return false.  |

