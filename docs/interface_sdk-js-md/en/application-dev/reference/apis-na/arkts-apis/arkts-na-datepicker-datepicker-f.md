# DatePicker

## DatePicker

```TypeScript
@ComponentBuilder
export declare function DatePicker(
    options?: DatePickerOptions
): DatePickerAttribute
```

Defines the DatePicker component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function DatePicker(    options?: DatePickerOptions): DatePickerAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function DatePicker(    options?: DatePickerOptions): DatePickerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DatePickerOptions](arkts-na-datepicker-datepickeroptions-i.md) | No | date picker options. |

**Return value:**

| Type | Description |
| --- | --- |
| DatePickerAttribute | The attribute of the DatePicker. |


## DatePicker

```TypeScript
@Builder
export declare function DatePicker(style: CustomBuilderT<DatePickerAttribute>): DatePickerAttribute
```

Defines the DatePicker component. It requires call setDatePickerOptions at start of the component attribute set-up. ant it requires call applyAttributeFinish at the end of the component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function DatePicker(style: CustomBuilderT<DatePickerAttribute>): DatePickerAttribute--><!--Device-unnamed-@Builderexport declare function DatePicker(style: CustomBuilderT<DatePickerAttribute>): DatePickerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | CustomBuilderT&lt;DatePickerAttribute&gt; | Yes | the callback to set up component's attribute. |

**Return value:**

| Type | Description |
| --- | --- |
| DatePickerAttribute | The attribute of the DatePicker. |

