# OnTabsContentDidScrollCallback

```TypeScript
export type OnTabsContentDidScrollCallback = (selectedIndex: int, index: int, position: double, mainAxisLength: double) => void
```

Defines a tabs callback when onContentDidScroll.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnTabsContentDidScrollCallback = (selectedIndex: int, index: int, position: double, mainAxisLength: double) => void--><!--Device-unnamed-export type OnTabsContentDidScrollCallback = (selectedIndex: int, index: int, position: double, mainAxisLength: double) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectedIndex | int | Yes | the index value of the Tabs content selected before animation start. The value range is all integers The value should be an integer. |
| index | int | Yes | the index value of the Tabs content. The value range is all integers The value should be an integer. |
| position | double | Yes | the moving ratio of the Tabs content from the start position of the Tabs main axis. |
| mainAxisLength | double | Yes | the Tabs main axis length for calculating position. |

