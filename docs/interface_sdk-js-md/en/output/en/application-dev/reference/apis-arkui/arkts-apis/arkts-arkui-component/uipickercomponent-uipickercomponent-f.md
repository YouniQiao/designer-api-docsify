# UIPickerComponent

## UIPickerComponent

```TypeScript
export declare function UIPickerComponent(
    options?: UIPickerComponentOptions,
    content_?: CustomBuilder
): UIPickerComponentAttribute
```

Defines the Picker container.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function UIPickerComponent(    options?: UIPickerComponentOptions,    content_?: CustomBuilder): UIPickerComponentAttribute--><!--Device-unnamed-export declare function UIPickerComponent(    options?: UIPickerComponentOptions,    content_?: CustomBuilder): UIPickerComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | picker options. |
| content\_ | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | - The attribute of the Picker. |


## UIPickerComponent

```TypeScript
export declare function UIPickerComponent(
  style: CustomBuilderT<UIPickerComponentAttribute>,
  content_?: CustomBuilder
): UIPickerComponentAttribute
```

Defines the UIPickerComponent component. It requires call setUIPickerComponentOptions at start of the component attribute set-up. and it requires call applyAttributeFinish at the end of the component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function UIPickerComponent(  style: CustomBuilderT<UIPickerComponentAttribute>,  content_?: CustomBuilder): UIPickerComponentAttribute--><!--Device-unnamed-export declare function UIPickerComponent(  style: CustomBuilderT<UIPickerComponentAttribute>,  content_?: CustomBuilder): UIPickerComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; | Yes | the callback to set up component's attribute. |
| content\_ | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | The attribute of the UIPickerComponent. |

