# OnListScrollIndexCallback

```TypeScript
declare type OnListScrollIndexCallback = (start: number, end: number, center: number) => void
```

List组件可见区域item变化事件的回调类型。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**Widget capability:** This API can be used in ArkTS widgets since API version 19.

<!--Device-unnamed-declare type OnListScrollIndexCallback = (start: number, end: number, center: number) => void--><!--Device-unnamed-declare type OnListScrollIndexCallback = (start: number, end: number, center: number) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | number | Yes | List显示区域内第一个子组件的索引值。 |
| end | number | Yes | List显示区域内最后一个子组件的索引值。 |
| center | number | Yes | List显示区域内中间位置子组件的索引值。 |

