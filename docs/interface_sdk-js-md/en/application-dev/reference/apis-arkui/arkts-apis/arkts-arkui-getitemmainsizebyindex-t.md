# GetItemMainSizeByIndex

```TypeScript
export type GetItemMainSizeByIndex = (index: int) => double
```

根据index获取指定Item的主轴大小。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type GetItemMainSizeByIndex = (index: int) => double--><!--Device-unnamed-export type GetItemMainSizeByIndex = (index: int) => double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | FlowItem在WaterFlow中的索引。<br/>。 <br>取值范围：[0, 子节点总数-1]。 |

**Return value:**

| Type | Description |
| --- | --- |
| double | 指定index的FlowItem的主轴大小，纵向瀑布流时为高度，横向瀑布流时为宽度，单位vp。 |

