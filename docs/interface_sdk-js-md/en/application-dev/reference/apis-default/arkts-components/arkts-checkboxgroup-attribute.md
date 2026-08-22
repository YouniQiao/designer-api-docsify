# CheckboxGroupAttribute

Defines the CheckboxGroup component attributes.

@extends CommonMethod @interface CheckboxGroupAttribute

**Inheritance/Implementation:** CheckboxGroupAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface CheckboxGroupAttribute--><!--Device-unnamed-export declare interface CheckboxGroupAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(
        modifier: AttributeModifier<CheckboxGroupAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-CheckboxGroupAttribute-attributeModifier(        modifier: AttributeModifier<CheckboxGroupAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-CheckboxGroupAttribute-attributeModifier(        modifier: AttributeModifier<CheckboxGroupAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CheckboxGroupAttribute](arkts-checkboxgroup-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## checkboxShape

```TypeScript
checkboxShape(value: CheckBoxShape | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-CheckboxGroupAttribute-checkboxShape(value: CheckBoxShape | undefined): this--><!--Device-CheckboxGroupAttribute-checkboxShape(value: CheckBoxShape | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [CheckBoxShape](../../apis-arkui/arkts-apis/arkts-arkui-checkboxshape-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## contentModifier

```TypeScript
contentModifier(modifier: ContentModifier<CheckBoxGroupConfiguration> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-CheckboxGroupAttribute-contentModifier(modifier: ContentModifier<CheckBoxGroupConfiguration> | undefined): this--><!--Device-CheckboxGroupAttribute-contentModifier(modifier: ContentModifier<CheckBoxGroupConfiguration> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../../apis-arkui/arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[CheckBoxGroupConfiguration](arkts-checkboxgroup-checkboxgroupconfiguration-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## mark

```TypeScript
mark(value: MarkStyle | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-CheckboxGroupAttribute-mark(value: MarkStyle | undefined): this--><!--Device-CheckboxGroupAttribute-mark(value: MarkStyle | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [MarkStyle](../../apis-arkui/arkts-apis/arkts-arkui-markstyle-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onChange

```TypeScript
onChange(callback: OnCheckboxGroupChangeCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-CheckboxGroupAttribute-onChange(callback: OnCheckboxGroupChangeCallback | undefined): this--><!--Device-CheckboxGroupAttribute-onChange(callback: OnCheckboxGroupChangeCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnCheckboxGroupChangeCallback](arkts-oncheckboxgroupchangecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## selectAll

```TypeScript
selectAll(isAllSelected: boolean | undefined | Bindable<boolean>): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-CheckboxGroupAttribute-selectAll(isAllSelected: boolean | undefined | Bindable<boolean>): this--><!--Device-CheckboxGroupAttribute-selectAll(isAllSelected: boolean | undefined | Bindable<boolean>): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isAllSelected | boolean \| undefined \| [Bindable](../arkts-apis/arkts-common-bindable-i.md)&lt;boolean&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## selectedColor

```TypeScript
selectedColor(value: ResourceColor | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-CheckboxGroupAttribute-selectedColor(value: ResourceColor | undefined): this--><!--Device-CheckboxGroupAttribute-selectedColor(value: ResourceColor | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## setCheckboxGroupOptions

```TypeScript
setCheckboxGroupOptions(options?: CheckboxGroupOptions): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-CheckboxGroupAttribute-setCheckboxGroupOptions(options?: CheckboxGroupOptions): this--><!--Device-CheckboxGroupAttribute-setCheckboxGroupOptions(options?: CheckboxGroupOptions): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [CheckboxGroupOptions](arkts-checkboxgroup-checkboxgroupoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## unselectedColor

```TypeScript
unselectedColor(value: ResourceColor | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-CheckboxGroupAttribute-unselectedColor(value: ResourceColor | undefined): this--><!--Device-CheckboxGroupAttribute-unselectedColor(value: ResourceColor | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## default

```TypeScript
default
```

Set checkboxgroup options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxGroupAttribute-default--><!--Device-CheckboxGroupAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

