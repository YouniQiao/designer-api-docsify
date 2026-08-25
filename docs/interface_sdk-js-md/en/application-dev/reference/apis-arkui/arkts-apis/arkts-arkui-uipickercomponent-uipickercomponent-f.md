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

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [UIPickerComponentOptions](arkts-arkui-uipickercomponent-uipickercomponentoptions-i.md) | No |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [UIPickerComponentAttribute](arkts-arkui-uipickercomponent-uipickercomponentattribute-i.md) |


## UIPickerComponent

```TypeScript
export declare function UIPickerComponent(
  style: CustomBuilderT<UIPickerComponentAttribute>,
  content_?: CustomBuilder
): UIPickerComponentAttribute
```

Defines the UIPickerComponent component. It requires call setUIPickerComponentOptions at start of the component attribute set-up. and it requires call applyAttributeFinish at the end of the component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[UIPickerComponentAttribute](arkts-arkui-uipickercomponent-uipickercomponentattribute-i.md)&gt; | Yes |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [UIPickerComponentAttribute](arkts-arkui-uipickercomponent-uipickercomponentattribute-i.md) |
