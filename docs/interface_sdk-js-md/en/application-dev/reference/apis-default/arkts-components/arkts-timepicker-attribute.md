# TimePickerAttribute

Defines the TimePicker component attributes.

@extends CommonMethod @interface TimePickerAttribute

**Inheritance/Implementation:** TimePickerAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface TimePickerAttribute--><!--Device-unnamed-export declare interface TimePickerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<TimePickerAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-TimePickerAttribute-attributeModifier(modifier: AttributeModifier<TimePickerAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-TimePickerAttribute-attributeModifier(modifier: AttributeModifier<TimePickerAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[TimePickerAttribute](arkts-timepicker-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## dateTimeOptions

```TypeScript
dateTimeOptions(value: DateTimeOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-TimePickerAttribute-dateTimeOptions(value: DateTimeOptions | undefined): this--><!--Device-TimePickerAttribute-dateTimeOptions(value: DateTimeOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | DateTimeOptions \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## digitalCrownSensitivity

```TypeScript
digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-TimePickerAttribute-digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this--><!--Device-TimePickerAttribute-digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this-End-->

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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-TimePickerAttribute-disappearTextStyle(value: PickerTextStyle | undefined): this--><!--Device-TimePickerAttribute-disappearTextStyle(value: PickerTextStyle | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PickerTextStyle](../../apis-arkui/arkts-components/arkts-arkui-pickertextstyle-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableCascade

```TypeScript
enableCascade(enabled: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-TimePickerAttribute-enableCascade(enabled: boolean | undefined): this--><!--Device-TimePickerAttribute-enableCascade(enabled: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableHapticFeedback

```TypeScript
enableHapticFeedback(enable: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-TimePickerAttribute-enableHapticFeedback(enable: boolean | undefined): this--><!--Device-TimePickerAttribute-enableHapticFeedback(enable: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## loop

```TypeScript
loop(value: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-TimePickerAttribute-loop(value: boolean | undefined): this--><!--Device-TimePickerAttribute-loop(value: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onChange

```TypeScript
onChange(callback: OnTimePickerChangeCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-TimePickerAttribute-onChange(callback: OnTimePickerChangeCallback | undefined): this--><!--Device-TimePickerAttribute-onChange(callback: OnTimePickerChangeCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnTimePickerChangeCallback](arkts-ontimepickerchangecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onEnterSelectedArea

```TypeScript
onEnterSelectedArea(callback: Callback<TimePickerResult> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-TimePickerAttribute-onEnterSelectedArea(callback: Callback<TimePickerResult> | undefined): this--><!--Device-TimePickerAttribute-onEnterSelectedArea(callback: Callback<TimePickerResult> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[TimePickerResult](arkts-timepicker-timepickerresult-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## selectedTextStyle

```TypeScript
selectedTextStyle(value: PickerTextStyle | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-TimePickerAttribute-selectedTextStyle(value: PickerTextStyle | undefined): this--><!--Device-TimePickerAttribute-selectedTextStyle(value: PickerTextStyle | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PickerTextStyle](../../apis-arkui/arkts-components/arkts-arkui-pickertextstyle-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## setTimePickerOptions

```TypeScript
setTimePickerOptions(options?: TimePickerOptions): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-TimePickerAttribute-setTimePickerOptions(options?: TimePickerOptions): this--><!--Device-TimePickerAttribute-setTimePickerOptions(options?: TimePickerOptions): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TimePickerOptions](arkts-timepicker-timepickeroptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## textStyle

```TypeScript
textStyle(value: PickerTextStyle | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-TimePickerAttribute-textStyle(value: PickerTextStyle | undefined): this--><!--Device-TimePickerAttribute-textStyle(value: PickerTextStyle | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PickerTextStyle](../../apis-arkui/arkts-components/arkts-arkui-pickertextstyle-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## useMilitaryTime

```TypeScript
useMilitaryTime(value: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-TimePickerAttribute-useMilitaryTime(value: boolean | undefined): this--><!--Device-TimePickerAttribute-useMilitaryTime(value: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## default

```TypeScript
default
```

Set the attribute modifier

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TimePickerAttribute-default--><!--Device-TimePickerAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

