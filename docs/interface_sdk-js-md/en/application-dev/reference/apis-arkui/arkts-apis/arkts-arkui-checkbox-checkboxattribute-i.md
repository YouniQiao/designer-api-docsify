# CheckboxAttribute

Defines the Checkbox component attributes.

**Inheritance/Implementation:** CheckboxAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface CheckboxAttribute extends CommonMethod--><!--Device-unnamed-export declare interface CheckboxAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(
        modifier: AttributeModifier<CheckboxAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier of checkbox.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxAttribute-default attributeModifier(        modifier: AttributeModifier<CheckboxAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-CheckboxAttribute-default attributeModifier(        modifier: AttributeModifier<CheckboxAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CheckboxAttribute](arkts-arkui-checkbox-checkboxattribute-i.md)&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes | The attribute modifier of checkbox. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<CheckBoxConfiguration> | undefined): this
```

Set the content modifier of checkbox.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxAttribute-default contentModifier(modifier: ContentModifier<CheckBoxConfiguration> | undefined): this--><!--Device-CheckboxAttribute-default contentModifier(modifier: ContentModifier<CheckBoxConfiguration> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;CheckBoxConfiguration&gt; \| undefined | Yes | The content modifier of checkbox. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## mark

```TypeScript
default mark(value: MarkStyle | undefined): this
```

Set the mark style of checkbox.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxAttribute-default mark(value: MarkStyle | undefined): this--><!--Device-CheckboxAttribute-default mark(value: MarkStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [MarkStyle](arkts-arkui-markstyle-i.md) \| undefined | Yes | The style configuration of checkbox mark. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onChange

```TypeScript
default onChange(callback: OnCheckboxChangeCallback | undefined): this
```

Called when the selection status changes.Anonymous Object Rectification.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxAttribute-default onChange(callback: OnCheckboxChangeCallback | undefined): this--><!--Device-CheckboxAttribute-default onChange(callback: OnCheckboxChangeCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnCheckboxChangeCallback](../arkts-components/arkts-arkui-oncheckboxchangecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## select

```TypeScript
default select(isSelected: boolean | undefined | Bindable<boolean>): this
```

setting whether checkbox is selected.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxAttribute-default select(isSelected: boolean | undefined | Bindable<boolean>): this--><!--Device-CheckboxAttribute-default select(isSelected: boolean | undefined | Bindable<boolean>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isSelected | boolean \| undefined \| Bindable&lt;boolean&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## selectedColor

```TypeScript
default selectedColor(value: ResourceColor | undefined): this
```

setting the display color of checkbox.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxAttribute-default selectedColor(value: ResourceColor | undefined): this--><!--Device-CheckboxAttribute-default selectedColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setCheckboxOptions

```TypeScript
default setCheckboxOptions(options?: CheckboxOptions): this
```

Set checkbox options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxAttribute-default setCheckboxOptions(options?: CheckboxOptions): this--><!--Device-CheckboxAttribute-default setCheckboxOptions(options?: CheckboxOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [CheckboxOptions](../arkts-components/arkts-arkui-checkboxoptions-i.md) | No | checkbox constructor options |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the CheckboxAttribute. |

## shape

```TypeScript
default shape(value: CheckBoxShape | undefined): this
```

setting the shape of checkbox.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxAttribute-default shape(value: CheckBoxShape | undefined): this--><!--Device-CheckboxAttribute-default shape(value: CheckBoxShape | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [CheckBoxShape](arkts-arkui-checkboxshape-e.md) \| undefined | Yes | The configuration of checkbox shape. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## unselectedColor

```TypeScript
default unselectedColor(value: ResourceColor | undefined): this
```

Set the display border color of unselected checkbox.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxAttribute-default unselectedColor(value: ResourceColor | undefined): this--><!--Device-CheckboxAttribute-default unselectedColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes | The color of border when checkbox unselected. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

