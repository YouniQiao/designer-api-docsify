# ContentDidScrollCallback

```TypeScript
export type ContentDidScrollCallback = (selectedIndex: int, index: int, position: double,
  mainAxisLength: double) => void
```

The callback of onContentDidScroll.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type ContentDidScrollCallback = (selectedIndex: int, index: int, position: double,  mainAxisLength: double) => void--><!--Device-unnamed-export type ContentDidScrollCallback = (selectedIndex: int, index: int, position: double,  mainAxisLength: double) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectedIndex | int | Yes | the index value of the swiper content selected before animation start. The value range is all integers The value should be an integer. |
| index | int | Yes | the index value of the swiper content. The value range is all integers The value should be an integer. |
| position | double | Yes | the moving ratio of the swiper content from the start position of the swiper main axis. |
| mainAxisLength | double | Yes | the swiper main axis length for calculating position. |

