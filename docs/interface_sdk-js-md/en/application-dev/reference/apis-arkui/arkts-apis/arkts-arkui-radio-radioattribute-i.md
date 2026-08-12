# RadioAttribute

Defines the Radio component attributes.

**Inheritance/Implementation:** RadioAttribute extends [CommonMethod](CommonMethod)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface RadioAttribute extends CommonMethod--><!--Device-unnamed-export declare interface RadioAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<RadioAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier of radio.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RadioAttribute-default attributeModifier(modifier: AttributeModifier<RadioAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-RadioAttribute-default attributeModifier(modifier: AttributeModifier<RadioAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[RadioAttribute](arkts-arkui-radio-radioattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes | The attribute modifier of radio. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## checked

```TypeScript
default checked(isChecked: boolean | undefined | Bindable<boolean>): this
```

Called when the radio box is selected.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RadioAttribute-default checked(isChecked: boolean | undefined | Bindable<boolean>): this--><!--Device-RadioAttribute-default checked(isChecked: boolean | undefined | Bindable<boolean>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isChecked | boolean \| undefined \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;boolean&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<RadioConfiguration> | undefined): this
```

Set the Configuration of radio.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RadioAttribute-default contentModifier(modifier: ContentModifier<RadioConfiguration> | undefined): this--><!--Device-RadioAttribute-default contentModifier(modifier: ContentModifier<RadioConfiguration> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[RadioConfiguration](arkts-arkui-radio-radioconfiguration-i.md)&gt; \| undefined | Yes | The contentModifier of radio. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onChange

```TypeScript
default onChange(callback: OnRadioChangeCallback | undefined): this
```

Called when the radio box selection status changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RadioAttribute-default onChange(callback: OnRadioChangeCallback | undefined): this--><!--Device-RadioAttribute-default onChange(callback: OnRadioChangeCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnRadioChangeCallback](arkts-arkui-onradiochangecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## radioStyle

```TypeScript
default radioStyle(value?: RadioStyle | undefined): this
```

Set the radio style.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RadioAttribute-default radioStyle(value?: RadioStyle | undefined): this--><!--Device-RadioAttribute-default radioStyle(value?: RadioStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [RadioStyle](arkts-arkui-radio-radiostyle-i.md) \| undefined | No | the radio style. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setRadioOptions

```TypeScript
default setRadioOptions(options: RadioOptions): this
```

Set radio options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RadioAttribute-default setRadioOptions(options: RadioOptions): this--><!--Device-RadioAttribute-default setRadioOptions(options: RadioOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RadioOptions](arkts-arkui-radio-radiooptions-i.md) | Yes | radio constructor options |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the RadioAttribute. |

