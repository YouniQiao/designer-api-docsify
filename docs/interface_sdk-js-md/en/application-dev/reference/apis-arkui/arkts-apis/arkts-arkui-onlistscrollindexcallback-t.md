# OnListScrollIndexCallback

```TypeScript
export type OnListScrollIndexCallback = (start: int, end: int, center: int) => void
```

List组件可见区域item变化事件的回调类型。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnListScrollIndexCallback = (start: int, end: int, center: int) => void--><!--Device-unnamed-export type OnListScrollIndexCallback = (start: int, end: int, center: int) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | List显示区域内第一个子组件的索引值。 |
| end | int | Yes | List显示区域内最后一个子组件的索引值。 |
| center | int | Yes | List显示区域内中间位置子组件的索引值。 |

