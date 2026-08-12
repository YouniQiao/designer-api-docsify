# TextPicker

## TextPicker

```TypeScript
export declare function TextPicker(
    options?: TextPickerOptions
): TextPickerAttribute
```

Defines the TextPicker component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function TextPicker(    options?: TextPickerOptions): TextPickerAttribute--><!--Device-unnamed-export declare function TextPicker(    options?: TextPickerOptions): TextPickerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TextPickerOptions](arkts-arkui-textpicker-textpickeroptions-i.md) | No | text picker options. |

**Return value:**

| Type | Description |
| --- | --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) | The attribute of the TextPicker. |


## TextPicker

```TypeScript
export declare function TextPicker(style: CustomBuilderT<TextPickerAttribute>): TextPickerAttribute
```

Defines the TextPicker component. It requires call setTextPickerOptions at start of the component attribute set-up.ant it requires call applyAttributeFinish at the end of the component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function TextPicker(style: CustomBuilderT<TextPickerAttribute>): TextPickerAttribute--><!--Device-unnamed-export declare function TextPicker(style: CustomBuilderT<TextPickerAttribute>): TextPickerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md)&gt; | Yes | the callback to set up component's attribute. |

**Return value:**

| Type | Description |
| --- | --- |
| [TextPickerAttribute](arkts-arkui-textpicker-textpickerattribute-i.md) | The attribute of the TextPicker. |

