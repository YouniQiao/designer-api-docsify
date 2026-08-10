# TextPickerResult

文本选择器结果。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface TextPickerResult--><!--Device-unnamed-export declare interface TextPickerResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## index

```TypeScript
index: int | int[]
```

选中项在选择范围数组中的索引值，索引从0开始。（文本选择器显示多列时，index为数组类型。）

**Type:** int \| int[]

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerResult-index: int | int[]--><!--Device-TextPickerResult-index: int | int[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value: string | string[]
```

选中项的文本内容。

**说明：**当显示文本或图片加文本列表时，value值为选中项中的文本值。（文本选择器显示多列时，value为数组类型。）

当显示图片列表时，value值为空。

value值不支持包含转义字符'\'。

**Type:** string \| string[]

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerResult-value: string | string[]--><!--Device-TextPickerResult-value: string | string[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

