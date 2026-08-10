# GetItemMainSizeByIndex

```TypeScript
declare type GetItemMainSizeByIndex = (index: number) => number
```

根据index获取指定Item的主轴大小。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-declare type GetItemMainSizeByIndex = (index: number) => number--><!--Device-unnamed-declare type GetItemMainSizeByIndex = (index: number) => number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | FlowItem在WaterFlow中的索引。<br/>取值范围：[0, 子组件总数-1] |

**Return value:**

| Type | Description |
| --- | --- |
| number | 指定index的FlowItem的主轴大小，纵向瀑布流时为高度，横向瀑布流时为宽度，单位vp。 |

