# CheckboxAttribute

Defines the Checkbox component attributes.

**Inheritance/Implementation:** CheckboxAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface CheckboxAttribute--><!--Device-unnamed-export declare interface CheckboxAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(
        modifier: AttributeModifier<CheckboxAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-CheckboxAttribute-attributeModifier(        modifier: AttributeModifier<CheckboxAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-CheckboxAttribute-attributeModifier(        modifier: AttributeModifier<CheckboxAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CheckboxAttribute](arkts-na-checkbox-checkboxattribute-i.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## contentModifier

```TypeScript
contentModifier(modifier: ContentModifier<CheckBoxConfiguration> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-CheckboxAttribute-contentModifier(modifier: ContentModifier<CheckBoxConfiguration> | undefined): this--><!--Device-CheckboxAttribute-contentModifier(modifier: ContentModifier<CheckBoxConfiguration> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../../apis-arkui/arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[CheckBoxConfiguration](arkts-na-checkbox-checkboxconfiguration-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## mark

```TypeScript
mark(value: MarkStyle | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-CheckboxAttribute-mark(value: MarkStyle | undefined): this--><!--Device-CheckboxAttribute-mark(value: MarkStyle | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [MarkStyle](../../apis-arkui/arkts-apis/arkts-arkui-markstyle-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onChange

```TypeScript
onChange(callback: OnCheckboxChangeCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-CheckboxAttribute-onChange(callback: OnCheckboxChangeCallback | undefined): this--><!--Device-CheckboxAttribute-onChange(callback: OnCheckboxChangeCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnCheckboxChangeCallback](arkts-na-oncheckboxchangecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## select

```TypeScript
select(isSelected: boolean | undefined | Bindable<boolean>): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-CheckboxAttribute-select(isSelected: boolean | undefined | Bindable<boolean>): this--><!--Device-CheckboxAttribute-select(isSelected: boolean | undefined | Bindable<boolean>): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isSelected | boolean \| undefined \| [Bindable](arkts-na-common-bindable-i.md)&lt;boolean&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## selectedColor

```TypeScript
selectedColor(value: ResourceColor | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-CheckboxAttribute-selectedColor(value: ResourceColor | undefined): this--><!--Device-CheckboxAttribute-selectedColor(value: ResourceColor | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## setCheckboxOptions

```TypeScript
setCheckboxOptions(options?: CheckboxOptions): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-CheckboxAttribute-setCheckboxOptions(options?: CheckboxOptions): this--><!--Device-CheckboxAttribute-setCheckboxOptions(options?: CheckboxOptions): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [CheckboxOptions](arkts-na-checkbox-checkboxoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## shape

```TypeScript
shape(value: CheckBoxShape | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-CheckboxAttribute-shape(value: CheckBoxShape | undefined): this--><!--Device-CheckboxAttribute-shape(value: CheckBoxShape | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [CheckBoxShape](../../apis-arkui/arkts-apis/arkts-arkui-checkboxshape-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## unselectedColor

```TypeScript
unselectedColor(value: ResourceColor | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-CheckboxAttribute-unselectedColor(value: ResourceColor | undefined): this--><!--Device-CheckboxAttribute-unselectedColor(value: ResourceColor | undefined): this-End-->

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

Set checkbox options.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CheckboxAttribute-default--><!--Device-CheckboxAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

