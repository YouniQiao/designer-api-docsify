# TextPickerScrollStopCallback

```TypeScript
export type TextPickerScrollStopCallback = (value: string | string[], index: int | int[]) => void
```

Callback of the listened scroll stop event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type TextPickerScrollStopCallback = (value: string | string[], index: int | int[]) => void--><!--Device-unnamed-export type TextPickerScrollStopCallback = (value: string | string[], index: int | int[]) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| string[] | Yes | Value of the selected item. |
| index | int \| int[] | Yes | Index of the selected item. |

