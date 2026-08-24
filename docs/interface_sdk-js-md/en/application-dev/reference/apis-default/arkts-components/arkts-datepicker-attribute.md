# DatePickerAttribute

Defines the DatePicker component attributes.@extends CommonMethod @interface DatePickerAttribute

**Inheritance/Implementation:** DatePickerAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface DatePickerAttribute--><!--Device-unnamed-export declare interface DatePickerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<DatePickerAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-DatePickerAttribute-attributeModifier(modifier: AttributeModifier<DatePickerAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-DatePickerAttribute-attributeModifier(modifier: AttributeModifier<DatePickerAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[DatePickerAttribute](arkts-datepicker-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## canLoop

```TypeScript
canLoop(isLoop: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-DatePickerAttribute-canLoop(isLoop: boolean | undefined): this--><!--Device-DatePickerAttribute-canLoop(isLoop: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isLoop | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## digitalCrownSensitivity

```TypeScript
digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-DatePickerAttribute-digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this--><!--Device-DatePickerAttribute-digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sensitivity | [CrownSensitivity](../../apis-arkui/arkts-apis/arkts-arkui-crownsensitivity-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## disappearTextStyle

```TypeScript
disappearTextStyle(value: PickerTextStyle | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-DatePickerAttribute-disappearTextStyle(value: PickerTextStyle | undefined): this--><!--Device-DatePickerAttribute-disappearTextStyle(value: PickerTextStyle | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PickerTextStyle](../../apis-arkui/arkts-components/arkts-arkui-pickertextstyle-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableHapticFeedback

```TypeScript
enableHapticFeedback(enable: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-DatePickerAttribute-enableHapticFeedback(enable: boolean | undefined): this--><!--Device-DatePickerAttribute-enableHapticFeedback(enable: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## lunar

```TypeScript
lunar(value: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-DatePickerAttribute-lunar(value: boolean | undefined): this--><!--Device-DatePickerAttribute-lunar(value: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onDateChange

```TypeScript
onDateChange(callback: Callback<Date> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-DatePickerAttribute-onDateChange(callback: Callback<Date> | undefined): this--><!--Device-DatePickerAttribute-onDateChange(callback: Callback<Date> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;Date&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## selectedTextStyle

```TypeScript
selectedTextStyle(value: PickerTextStyle | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-DatePickerAttribute-selectedTextStyle(value: PickerTextStyle | undefined): this--><!--Device-DatePickerAttribute-selectedTextStyle(value: PickerTextStyle | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PickerTextStyle](../../apis-arkui/arkts-components/arkts-arkui-pickertextstyle-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## setDatePickerOptions

```TypeScript
setDatePickerOptions(options?: DatePickerOptions): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-DatePickerAttribute-setDatePickerOptions(options?: DatePickerOptions): this--><!--Device-DatePickerAttribute-setDatePickerOptions(options?: DatePickerOptions): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DatePickerOptions](arkts-datepicker-datepickeroptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## textStyle

```TypeScript
textStyle(value: PickerTextStyle | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-DatePickerAttribute-textStyle(value: PickerTextStyle | undefined): this--><!--Device-DatePickerAttribute-textStyle(value: PickerTextStyle | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PickerTextStyle](../../apis-arkui/arkts-components/arkts-arkui-pickertextstyle-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## default

```TypeScript
default
```

Set the attribute modifier

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DatePickerAttribute-default--><!--Device-DatePickerAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

