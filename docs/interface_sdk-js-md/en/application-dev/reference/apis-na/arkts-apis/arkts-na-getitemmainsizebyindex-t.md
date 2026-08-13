# GetItemMainSizeByIndex

```TypeScript
export type GetItemMainSizeByIndex = (index: int) => double
```

function that returns item main size by index.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type GetItemMainSizeByIndex = (index: int) => double--><!--Device-unnamed-export type GetItemMainSizeByIndex = (index: int) => double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | Index of the target water flow item. <br>Value range: [0, total number of child nodes - 1]. |

**Return value:**

| Type | Description |
| --- | --- |
| double | main size of the FlowItem at index |

