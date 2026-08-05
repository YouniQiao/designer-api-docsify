# CheckboxGroupAttribute

Defines the CheckboxGroup component attributes.

**Inheritance/Implementation:** CheckboxGroupAttribute extends [CommonMethod](common-commonmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface CheckboxGroupAttribute extends CommonMethod--><!--Device-unnamed-export declare interface CheckboxGroupAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(
        modifier: AttributeModifier<CheckboxGroupAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier of checkbox group.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxGroupAttribute-default attributeModifier(        modifier: AttributeModifier<CheckboxGroupAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-CheckboxGroupAttribute-default attributeModifier(        modifier: AttributeModifier<CheckboxGroupAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes | The attribute modifier of checkbox group. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## checkboxShape

```TypeScript
default checkboxShape(value: CheckBoxShape | undefined): this
```

Setting the shape of checkbox group.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxGroupAttribute-default checkboxShape(value: CheckBoxShape | undefined): this--><!--Device-CheckboxGroupAttribute-default checkboxShape(value: CheckBoxShape | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | The configuration of checkbox group shape. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<CheckBoxGroupConfiguration> | undefined): this
```

Set the content modifier of checkboxgroup.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxGroupAttribute-default contentModifier(modifier: ContentModifier<CheckBoxGroupConfiguration> | undefined): this--><!--Device-CheckboxGroupAttribute-default contentModifier(modifier: ContentModifier<CheckBoxGroupConfiguration> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; \| undefined | Yes | The content modifier of checkboxgroup. |

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

<!--Device-CheckboxGroupAttribute-default mark(value: MarkStyle | undefined): this--><!--Device-CheckboxGroupAttribute-default mark(value: MarkStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | The style configuration of checkboxgroup mark. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onChange

```TypeScript
default onChange(callback: OnCheckboxGroupChangeCallback | undefined): this
```

Called when the selection status changes. Anonymous Object Rectification.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxGroupAttribute-default onChange(callback: OnCheckboxGroupChangeCallback | undefined): this--><!--Device-CheckboxGroupAttribute-default onChange(callback: OnCheckboxGroupChangeCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## selectAll

```TypeScript
default selectAll(isAllSelected: boolean | undefined | Bindable<boolean>): this
```

setting whether all checkbox is selected.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxGroupAttribute-default selectAll(isAllSelected: boolean | undefined | Bindable<boolean>): this--><!--Device-CheckboxGroupAttribute-default selectAll(isAllSelected: boolean | undefined | Bindable<boolean>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isAllSelected | boolean \| undefined \| Bindable&lt;boolean&gt; | Yes |  |

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

<!--Device-CheckboxGroupAttribute-default selectedColor(value: ResourceColor | undefined): this--><!--Device-CheckboxGroupAttribute-default selectedColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setCheckboxGroupOptions

```TypeScript
default setCheckboxGroupOptions(options?: CheckboxGroupOptions): this
```

Set checkboxgroup options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxGroupAttribute-default setCheckboxGroupOptions(options?: CheckboxGroupOptions): this--><!--Device-CheckboxGroupAttribute-default setCheckboxGroupOptions(options?: CheckboxGroupOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | checkboxgroup constructor options |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the CheckboxGroupAttribute. |

## unselectedColor

```TypeScript
default unselectedColor(value: ResourceColor | undefined): this
```

Set the display border color of unselected checkbox.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxGroupAttribute-default unselectedColor(value: ResourceColor | undefined): this--><!--Device-CheckboxGroupAttribute-default unselectedColor(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes | The color of border when checkboxgroup unselected. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

