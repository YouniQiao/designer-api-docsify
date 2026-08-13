# OnTextPickerChangeCallback

```TypeScript
export type OnTextPickerChangeCallback = (selectItem: string | string[], index: int | int[]) => void
```

Callback of TextPicker item is selected event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnTextPickerChangeCallback = (selectItem: string | string[], index: int | int[]) => void--><!--Device-unnamed-export type OnTextPickerChangeCallback = (selectItem: string | string[], index: int | int[]) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectItem | string \| string[] | Yes | Value of the selected item. |
| index | int \| int[] | Yes | Index of the selected item. |

