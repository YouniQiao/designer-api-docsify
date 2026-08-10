# TextPickerOptions

文本选择器的参数说明。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare interface TextPickerOptions--><!--Device-unnamed-declare interface TextPickerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## columnWidths

```TypeScript
columnWidths?: LengthMetrics[]
```

设置每一列的列宽。

> 默认值：每一列的列宽相等，为组件宽度除以列数。

> **说明：**
> 
> 1. 当文本长度大于列宽时，文本被截断。
> 2. 当设置为异常值时，使用默认值。
> 3. 支持设置为Undefined和Null，不支持Undefined[]和Null[]。
> 4. 当columnWidths数组长度与实际列数不匹配时，超出列数的列宽值将被忽略；未指定列宽的列将均分组件剩余可用宽度
> （组件宽度减去已指定列宽之和）。

**Type:** [LengthMetrics](../arkts-apis/arkts-arkui-lengthmetrics-t.md)[]

**Default:** Each column has equal width, calculated by dividing the total component width by the number of columns.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-TextPickerOptions-columnWidths?: LengthMetrics[]--><!--Device-TextPickerOptions-columnWidths?: LengthMetrics[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## range

```TypeScript
range: string[] | string[][] | Resource | TextPickerRangeContent[] | TextCascadePickerRangeContent[]
```

选择器的数据选择列表。不可设置为空数组，若设置为空数组，则不显示；若动态变化为空数组，则保持当前正常值显示。

> **说明：**
> 
> 1. 单列数据选择器使用string[]，[Resource](../arkts-apis/arkts-arkui-resource-t.md/arkts-arkui-resource-t.md)，[TextPickerRangeContent](arkts-arkui-textpickerrangecontent-i.md)[]类型。
> 2. 多列非联动数据选择器使用string[][]类型。
> 3. 多列联动数据选择器使用[TextCascadePickerRangeContent](arkts-arkui-textcascadepickerrangecontent-i.md)[]类型。
> 4. Resource类型只支持[strarray.json](../../../quick-start/resource-categories-and-access.md#资源组目录)。
> 5. range的类型及列数不可以动态修改。

**Type:** string[] \| string[][] \| Resource \| TextPickerRangeContent[] \| TextCascadePickerRangeContent[]

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextPickerOptions-range: string[] | string[][] | Resource | TextPickerRangeContent[] | TextCascadePickerRangeContent[]--><!--Device-TextPickerOptions-range: string[] | string[][] | Resource | TextPickerRangeContent[] | TextCascadePickerRangeContent[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selected

```TypeScript
selected?: number | number[]
```

设置选中项在数据选择列表中的索引值，索引从0开始。

> 默认值：0

> **说明：**
> 
> 1. 单列数据选择器使用number类型。
> 2. 多列非联动数据选择器使用number[]类型，数组长度与列数一致。
> 3. 多列联动数据选择器使用number[]类型，数组长度与层级数一致。
> 4. 从API version 10开始，该参数支持[\$\$](../../../ui/state-management/arkts-two-way-sync.md)双向绑定变量。
> 5. 未设置该属性或设置的值无效时，使用默认值。

**Type:** number \| number[]

**Default:** 0

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextPickerOptions-selected?: number | number[]--><!--Device-TextPickerOptions-selected?: number | number[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value?: ResourceStr | ResourceStr[]
```

设置选中项的值，优先级低于selected。

默认值：数据选择列表中第一个元素的值。

> **说明：**
> 
> 1. 从API version 10开始，该参数支持[\$\$](../../../ui/state-management/arkts-two-way-sync.md)双向绑定变量。
> 2. 从API version 20开始，支持[Resource](../arkts-apis/arkts-arkui-resource-t.md/arkts-arkui-resource-t.md)类型。
> 3. 只有显示文本列表时该值有效。显示图片或图文混排的列表时，该值无效。
> 4. 单列数据选择器使用[ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md/arkts-arkui-resourcestr-t.md)类型。
> 5. 多列非联动数据选择器使用[ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md/arkts-arkui-resourcestr-t.md)[]类型，数组长度与列数一致。
> 6. 多列联动数据选择器使用[ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md/arkts-arkui-resourcestr-t.md)[]类型，数组长度与层级数一致。
> 7. 当selected和value均未设置，或selected值无效时，使用默认值。

**Type:** [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) \| ResourceStr[]

**Default:** value of the first item [since 8 - 9]

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextPickerOptions-value?: ResourceStr | ResourceStr[]--><!--Device-TextPickerOptions-value?: ResourceStr | ResourceStr[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

