# MenuCallback

```TypeScript
declare type MenuCallback = (start: number, end: number) => void
```

自定义选择菜单显示或隐藏时触发的回调事件。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-unnamed-declare type MenuCallback = (start: number, end: number) => void--><!--Device-unnamed-declare type MenuCallback = (start: number, end: number) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | number | Yes | 选中内容的起始位置。 |
| end | number | Yes | 选中内容的终止位置。 |

