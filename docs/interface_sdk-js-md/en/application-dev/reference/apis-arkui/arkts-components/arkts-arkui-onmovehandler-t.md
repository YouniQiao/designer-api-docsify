# OnMoveHandler

```TypeScript
declare type OnMoveHandler = (from: number, to: number) => void
```

定义数据源拖拽回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-declare type OnMoveHandler = (from: number, to: number) => void--><!--Device-unnamed-declare type OnMoveHandler = (from: number, to: number) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | number | Yes | 数据源拖拽起始索引号。取值范围是[0, 数据源长度-1]。 |
| to | number | Yes | 数据源拖拽目标索引号。取值范围是[0, 数据源长度-1]。 |

