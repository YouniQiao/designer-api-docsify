# MenuCallback

```TypeScript
export type MenuCallback = (start: int, end: int) => void
```

自定义选择菜单显示或隐藏时触发的回调事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type MenuCallback = (start: int, end: int) => void--><!--Device-unnamed-export type MenuCallback = (start: int, end: int) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | int | Yes | 选中内容的起始位置。 |
| end | int | Yes | 选中内容的终止位置。 |

