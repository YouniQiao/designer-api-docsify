# OnGridScrollIndexCallback

```TypeScript
export type OnGridScrollIndexCallback = (first: int, last: int) => void
```

Grid组件可见区域item变化事件的回调类型。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnGridScrollIndexCallback = (first: int, last: int) => void--><!--Device-unnamed-export type OnGridScrollIndexCallback = (first: int, last: int) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| first | int | Yes | 当前显示的Grid起始位置的索引值。 |
| last | int | Yes | 当前显示的Grid终止位置的索引值。 |

