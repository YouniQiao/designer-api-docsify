# RadioAttribute

Defines the Radio component attributes.

**Inheritance/Implementation:** RadioAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface RadioAttribute--><!--Device-unnamed-export declare interface RadioAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<RadioAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta only, since version -1.

**Deprecated since:** -1

<!--Device-RadioAttribute-attributeModifier(modifier: AttributeModifier<RadioAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-RadioAttribute-attributeModifier(modifier: AttributeModifier<RadioAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[RadioAttribute](arkts-na-radio-radioattribute-i.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## checked

```TypeScript
checked(isChecked: boolean | undefined | Bindable<boolean>): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta only, since version -1.

**Deprecated since:** -1

<!--Device-RadioAttribute-checked(isChecked: boolean | undefined | Bindable<boolean>): this--><!--Device-RadioAttribute-checked(isChecked: boolean | undefined | Bindable<boolean>): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isChecked | boolean \| undefined \| [Bindable](arkts-na-common-bindable-i.md)&lt;boolean&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## contentModifier

```TypeScript
contentModifier(modifier: ContentModifier<RadioConfiguration> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta only, since version -1.

**Deprecated since:** -1

<!--Device-RadioAttribute-contentModifier(modifier: ContentModifier<RadioConfiguration> | undefined): this--><!--Device-RadioAttribute-contentModifier(modifier: ContentModifier<RadioConfiguration> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../../apis-arkui/arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[RadioConfiguration](arkts-na-radio-radioconfiguration-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onChange

```TypeScript
onChange(callback: OnRadioChangeCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta only, since version -1.

**Deprecated since:** -1

<!--Device-RadioAttribute-onChange(callback: OnRadioChangeCallback | undefined): this--><!--Device-RadioAttribute-onChange(callback: OnRadioChangeCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnRadioChangeCallback](arkts-na-onradiochangecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## radioStyle

```TypeScript
radioStyle(value?: RadioStyle | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta only, since version -1.

**Deprecated since:** -1

<!--Device-RadioAttribute-radioStyle(value?: RadioStyle | undefined): this--><!--Device-RadioAttribute-radioStyle(value?: RadioStyle | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [RadioStyle](arkts-na-radio-radiostyle-i.md) \| undefined | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setRadioOptions

```TypeScript
setRadioOptions(options: RadioOptions): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta only, since version -1.

**Deprecated since:** -1

<!--Device-RadioAttribute-setRadioOptions(options: RadioOptions): this--><!--Device-RadioAttribute-setRadioOptions(options: RadioOptions): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RadioOptions](arkts-na-radio-radiooptions-i.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## default

```TypeScript
default
```

Set radio options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-RadioAttribute-default--><!--Device-RadioAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

