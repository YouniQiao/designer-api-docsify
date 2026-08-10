# OnGridScrollIndexCallback

```TypeScript
declare type OnGridScrollIndexCallback = (first: number, last: number) => void
```

Grid组件可见区域item变化事件的回调类型。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-unnamed-declare type OnGridScrollIndexCallback = (first: number, last: number) => void--><!--Device-unnamed-declare type OnGridScrollIndexCallback = (first: number, last: number) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| first | number | Yes | 当前显示的Grid起始位置的索引值。 |
| last | number | Yes | 当前显示的Grid终止位置的索引值。 |

