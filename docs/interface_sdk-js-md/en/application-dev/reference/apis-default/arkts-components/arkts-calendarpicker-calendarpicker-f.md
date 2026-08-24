# CalendarPicker

## CalendarPicker

```TypeScript
@ComponentBuilder
export declare function CalendarPicker(
    options?: CalendarOptions
): CalendarPickerAttribute
```

Defines CalendarPicker Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @ComponentBuilder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function CalendarPicker(    options?: CalendarOptions): CalendarPickerAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function CalendarPicker(    options?: CalendarOptions): CalendarPickerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [CalendarOptions](arkts-calendarpicker-calendaroptions-i.md) | No | calendar options. |

**Return value:**

| Type | Description |
| --- | --- |
| [CalendarPickerAttribute](arkts-calendarpicker-attribute.md) |  |


## CalendarPicker

```TypeScript
@Builder
export declare function CalendarPicker(style: CustomBuilderT<CalendarPickerAttribute>): CalendarPickerAttribute
```

Defines the CalendarPicker component. It requires call setCalendarPickerOptions at start of the component attribute set-up. ant it requires call applyAttributeFinish at the end of the component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function CalendarPicker(style: CustomBuilderT<CalendarPickerAttribute>): CalendarPickerAttribute--><!--Device-unnamed-@Builderexport declare function CalendarPicker(style: CustomBuilderT<CalendarPickerAttribute>): CalendarPickerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[CalendarPickerAttribute](arkts-calendarpicker-attribute.md)&gt; | Yes | the callback to set up component's attribute. |

**Return value:**

| Type | Description |
| --- | --- |
| [CalendarPickerAttribute](arkts-calendarpicker-attribute.md) | The attribute of the CalendarPicker. |

