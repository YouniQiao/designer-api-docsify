# TextPicker

## TextPicker

```TypeScript
@ComponentBuilder
export declare function TextPicker(
    options?: TextPickerOptions
): TextPickerAttribute
```

Defines the TextPicker component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function TextPicker(    options?: TextPickerOptions): TextPickerAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function TextPicker(    options?: TextPickerOptions): TextPickerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TextPickerOptions](arkts-na-textpicker-textpickeroptions-i.md) | No | text picker options. |

**Return value:**

| Type | Description |
| --- | --- |
| TextPickerAttribute | The attribute of the TextPicker. |


## TextPicker

```TypeScript
@Builder
export declare function TextPicker(style: CustomBuilderT<TextPickerAttribute>): TextPickerAttribute
```

Defines the TextPicker component. It requires call setTextPickerOptions at start of the component attribute set-up. ant it requires call applyAttributeFinish at the end of the component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function TextPicker(style: CustomBuilderT<TextPickerAttribute>): TextPickerAttribute--><!--Device-unnamed-@Builderexport declare function TextPicker(style: CustomBuilderT<TextPickerAttribute>): TextPickerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | CustomBuilderT&lt;TextPickerAttribute&gt; | Yes | the callback to set up component's attribute. |

**Return value:**

| Type | Description |
| --- | --- |
| TextPickerAttribute | The attribute of the TextPicker. |

