# UIPickerComponent

## UIPickerComponent

```TypeScript
@ComponentBuilder
export declare function UIPickerComponent(
    options?: UIPickerComponentOptions,
    content_?: CustomBuilder
): UIPickerComponentAttribute
```

Defines the Picker container.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function UIPickerComponent(    options?: UIPickerComponentOptions,    content_?: CustomBuilder): UIPickerComponentAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function UIPickerComponent(    options?: UIPickerComponentOptions,    content_?: CustomBuilder): UIPickerComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [UIPickerComponentOptions](arkts-uipickercomponent-uipickercomponentoptions-i.md) | No | picker options. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [UIPickerComponentAttribute](arkts-uipickercomponent-attribute.md) | The attribute of the Picker. |


## UIPickerComponent

```TypeScript
@Builder
export declare function UIPickerComponent(
  style: CustomBuilderT<UIPickerComponentAttribute>,
  content_?: CustomBuilder
): UIPickerComponentAttribute
```

Defines the UIPickerComponent component. It requires call setUIPickerComponentOptions at start of the component attribute set-up. and it requires call applyAttributeFinish at the end of the component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function UIPickerComponent(  style: CustomBuilderT<UIPickerComponentAttribute>,  content_?: CustomBuilder): UIPickerComponentAttribute--><!--Device-unnamed-@Builderexport declare function UIPickerComponent(  style: CustomBuilderT<UIPickerComponentAttribute>,  content_?: CustomBuilder): UIPickerComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[UIPickerComponentAttribute](arkts-uipickercomponent-attribute.md)&gt; | Yes | the callback to set up component's attribute. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [UIPickerComponentAttribute](arkts-uipickercomponent-attribute.md) | The attribute of the UIPickerComponent. |

