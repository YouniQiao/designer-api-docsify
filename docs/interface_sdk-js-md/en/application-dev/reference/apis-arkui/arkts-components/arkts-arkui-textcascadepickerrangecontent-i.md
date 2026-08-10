# TextCascadePickerRangeContent

多列联动数据选择器的数据选项内容。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface TextCascadePickerRangeContent--><!--Device-unnamed-declare interface TextCascadePickerRangeContent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## children

```TypeScript
children?: TextCascadePickerRangeContent[]
```

联动数据。表示当前数据项的子选项数组，用于构建多列联动数据选择器的层级结构。数组的每个元素为[TextCascadePickerRangeContent](arkts-arkui-textcascadepickerrangecontent-i.md)类型，包含text和children属性，支持多级嵌套。当选择器支持多级联动时传入此参数；不传入时表示该选项没有子级数据。

**Type:** [TextCascadePickerRangeContent](arkts-arkui-textcascadepickerrangecontent-i.md)[]

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextCascadePickerRangeContent-children?: TextCascadePickerRangeContent[]--><!--Device-TextCascadePickerRangeContent-children?: TextCascadePickerRangeContent[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## text

```TypeScript
text: string | Resource
```

文本信息。

> **说明：**当文本长度大于列宽时，文本被截断。

**Type:** string \| Resource

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextCascadePickerRangeContent-text: string | Resource--><!--Device-TextCascadePickerRangeContent-text: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

