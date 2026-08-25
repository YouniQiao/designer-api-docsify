# DatePicker

## DatePicker

```TypeScript
export declare function DatePicker(
    options?: DatePickerOptions
): DatePickerAttribute
```

Defines the DatePicker component.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [DatePickerOptions](arkts-arkui-datepicker-datepickeroptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DatePickerAttribute](arkts-arkui-datepicker-datepickerattribute-i.md) |


## DatePicker

```TypeScript
export declare function DatePicker(style: CustomBuilderT<DatePickerAttribute>): DatePickerAttribute
```

Defines the DatePicker component. It requires call setDatePickerOptions at start of the component attribute set-up. ant it requires call applyAttributeFinish at the end of the component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[DatePickerAttribute](arkts-arkui-datepicker-datepickerattribute-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DatePickerAttribute](arkts-arkui-datepicker-datepickerattribute-i.md) |
