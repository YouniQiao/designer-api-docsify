# TextPickerEnterSelectedAreaCallback

```TypeScript
declare type TextPickerEnterSelectedAreaCallback = (value: string | string[], index: number | number[]) => void
```

定义触发onEnterSelectedArea事件的回调类型。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-declare type TextPickerEnterSelectedAreaCallback = (value: string | string[], index: number | number[]) => void--><!--Device-unnamed-declare type TextPickerEnterSelectedAreaCallback = (value: string | string[], index: number | number[]) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| string[] | Yes | 当前选中项的文本。多列数据选择器的value为数组类型。 <br>**说明：** <br>当选择器内容为文本或图文混排时，value值为选中项中的文本值；当选择器内容为图片时，value值为空。 |
| index | number \| number[] | Yes | 当前选中项的索引值，索引从0开始。多列数据选择器的index为数组类型。 |

