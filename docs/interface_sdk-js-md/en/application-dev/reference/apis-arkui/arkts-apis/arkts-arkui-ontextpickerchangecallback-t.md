# OnTextPickerChangeCallback

```TypeScript
export type OnTextPickerChangeCallback = (selectItem: string | string[], index: int | int[]) => void
```

滑动选中TextPicker文本内容后，触发该回调。当显示文本或图片加文本列表时，选中项的文本值为选中项中的文本值，当显示图片列表时，选中项的文本值为空。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnTextPickerChangeCallback = (selectItem: string | string[], index: int | int[]) => void--><!--Device-unnamed-export type OnTextPickerChangeCallback = (selectItem: string | string[], index: int | int[]) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectItem | string \| string[] | Yes | 当前选中项的文本。多列数据选择器的selectItem为数组类型。<br/>**说明：**<br/> 当选择器内容为文本或图文混排时，selectItem值为选中项中的文本值；当选择器内容为图片时，selectItem值为空。 |
| index | int \| int[] | Yes | 当前选中项的索引值，索引从0开始。多列数据选择器的index为数组类型。 |

