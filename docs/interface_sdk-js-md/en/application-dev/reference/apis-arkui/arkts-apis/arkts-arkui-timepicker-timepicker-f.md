# TimePicker

## TimePicker

```TypeScript
export declare function TimePicker(
    options?: TimePickerOptions
): TimePickerAttribute
```

Defines the TimePicker component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function TimePicker(    options?: TimePickerOptions): TimePickerAttribute--><!--Device-unnamed-export declare function TimePicker(    options?: TimePickerOptions): TimePickerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TimePickerOptions](arkts-arkui-timepicker-timepickeroptions-i.md) | No | timer picker options. |

**Return value:**

| Type | Description |
| --- | --- |
| [TimePickerAttribute](../arkts-components/arkts-arkui-timepicker-attribute.md) | The attribute of the TimePicker. |


## TimePicker

```TypeScript
export declare function TimePicker(style: CustomBuilderT<TimePickerAttribute>): TimePickerAttribute
```

Defines the TimePicker component. It requires call setTimePickerOptions at start of the component attribute set-up.ant it requires call applyAttributeFinish at the end of the component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function TimePicker(style: CustomBuilderT<TimePickerAttribute>): TimePickerAttribute--><!--Device-unnamed-export declare function TimePicker(style: CustomBuilderT<TimePickerAttribute>): TimePickerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;TimePickerAttribute&gt; | Yes | the callback to set up component's attribute. |

**Return value:**

| Type | Description |
| --- | --- |
| [TimePickerAttribute](../arkts-components/arkts-arkui-timepicker-attribute.md) | The attribute of the TimePicker. |

