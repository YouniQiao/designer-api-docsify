# ArcScrollIndexHandler

```TypeScript
export type ArcScrollIndexHandler = (start: int, end: int, center: int) => void
```

有子组件划入或划出ArcList显示区域时触发的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export type ArcScrollIndexHandler = (start: int, end: int, center: int) => void--><!--Device-unnamed-export type ArcScrollIndexHandler = (start: int, end: int, center: int) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | ArcList显示区域内第一个子组件的索引值。 <br>取值限定为整数。 |
| end | int | Yes | ArcList显示区域内最后一个子组件的索引值。 <br>取值限定为整数。 |
| center | int | Yes | ArcList显示区域内中间位置子组件的索引值。 <br>取值限定为整数。 |

