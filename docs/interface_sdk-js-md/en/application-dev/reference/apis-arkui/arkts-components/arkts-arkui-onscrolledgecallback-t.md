# OnScrollEdgeCallback

```TypeScript
declare type OnScrollEdgeCallback = (side: Edge) => void
```

滚动到边缘时触发的回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-declare type OnScrollEdgeCallback = (side: Edge) => void--><!--Device-unnamed-declare type OnScrollEdgeCallback = (side: Edge) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| side | [Edge](../arkts-apis/arkts-arkui-edge-e.md) | Yes | 滚动到的边缘位置。竖直方向滚动时，Edge.Top和Edge.Start表示起始边缘，Edge.Bottom和Edge.End表示末尾边缘。水平方向滚动时，Edge.Center表示水平方 向起始位置，Edge.Baseline表示水平方向末尾位置。 |

