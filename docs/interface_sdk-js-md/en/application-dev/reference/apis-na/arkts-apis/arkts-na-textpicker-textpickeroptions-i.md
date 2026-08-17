# TextPickerOptions

Defines the options of TextPicker.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface TextPickerOptions--><!--Device-unnamed-export declare interface TextPickerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## columnWidths

```TypeScript
columnWidths?: LengthMetrics[]
```

Width of each column in the picker. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If the text length exceeds the column width, the text will be truncated. &lt;/p&gt;

**Type:** [LengthMetrics](arkts-na-graphics-lengthmetrics-c.md)[]

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerOptions-columnWidths?: LengthMetrics[]--><!--Device-TextPickerOptions-columnWidths?: LengthMetrics[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## range

```TypeScript
range: string[] | string[][] | Resource | TextPickerRangeContent[] | TextCascadePickerRangeContent[]
```

Data selection range of the picker. Support the display of pictures, text and pictures plus text, or multi column plain text.

**Type:** string[] \| string[][] \| [Resource](../../apis-arkui/arkts-apis/arkts-arkui-resource-t.md) \| [TextPickerRangeContent](arkts-na-textpicker-textpickerrangecontent-i.md)[] \| [TextCascadePickerRangeContent](arkts-na-textpicker-textcascadepickerrangecontent-i.md)[]

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerOptions-range: string[] | string[][] | Resource | TextPickerRangeContent[] | TextCascadePickerRangeContent[]--><!--Device-TextPickerOptions-range: string[] | string[][] | Resource | TextPickerRangeContent[] | TextCascadePickerRangeContent[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selected

```TypeScript
selected?: int | int[] | Bindable<int> | Bindable<int[]>
```

Current selected subscript.

**Type:** int \| int[] \| [Bindable](arkts-na-common-bindable-i.md)&lt;int&gt; \| [Bindable](arkts-na-common-bindable-i.md)&lt;int[]&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerOptions-selected?: int | int[] | Bindable<int> | Bindable<int[]>--><!--Device-TextPickerOptions-selected?: int | int[] | Bindable<int> | Bindable<int[]>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value?: BindableResourceStr | BindableResourceStrArray
```

Value of the current selection. Only valid when only text is displayed.

**Type:** [BindableResourceStr](arkts-na-bindableresourcestr-t.md) \| [BindableResourceStrArray](arkts-na-bindableresourcestrarray-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerOptions-value?: BindableResourceStr | BindableResourceStrArray--><!--Device-TextPickerOptions-value?: BindableResourceStr | BindableResourceStrArray-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

