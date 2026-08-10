# OnRadioChangeCallback

```TypeScript
export type OnRadioChangeCallback = (isChecked: boolean) => void
```

单选框选中状态改变时触发的回调函数类型定义。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnRadioChangeCallback = (isChecked: boolean) => void--><!--Device-unnamed-export type OnRadioChangeCallback = (isChecked: boolean) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isChecked | boolean | Yes | 单选框的状态。<br/>值为true时，表示从未选中变为选中。值为false时，表示从选中变为未选中。 |

