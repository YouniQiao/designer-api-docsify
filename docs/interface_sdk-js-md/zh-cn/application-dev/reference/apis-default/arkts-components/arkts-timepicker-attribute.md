# TimePickerAttribute

除支持通用属性外，还支持以下属性：除支持通用事件外，还支持以下事件：@extends CommonMethod @interface TimePickerAttribute

**继承/实现关系：** TimePickerAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare interface TimePickerAttribute--><!--Device-unnamed-export declare interface TimePickerAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<TimePickerAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-TimePickerAttribute-attributeModifier(modifier: AttributeModifier<TimePickerAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-TimePickerAttribute-attributeModifier(modifier: AttributeModifier<TimePickerAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[TimePickerAttribute](arkts-timepicker-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## dateTimeOptions

```TypeScript
dateTimeOptions(value: DateTimeOptions | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-TimePickerAttribute-dateTimeOptions(value: DateTimeOptions | undefined): this--><!--Device-TimePickerAttribute-dateTimeOptions(value: DateTimeOptions | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | DateTimeOptions \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## digitalCrownSensitivity

```TypeScript
digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-TimePickerAttribute-digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this--><!--Device-TimePickerAttribute-digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sensitivity | [CrownSensitivity](../../apis-arkui/arkts-apis/arkts-arkui-crownsensitivity-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## disappearTextStyle

```TypeScript
disappearTextStyle(value: PickerTextStyle | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-TimePickerAttribute-disappearTextStyle(value: PickerTextStyle | undefined): this--><!--Device-TimePickerAttribute-disappearTextStyle(value: PickerTextStyle | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PickerTextStyle](../../apis-arkui/arkts-components/arkts-arkui-pickertextstyle-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enableCascade

```TypeScript
enableCascade(enabled: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-TimePickerAttribute-enableCascade(enabled: boolean | undefined): this--><!--Device-TimePickerAttribute-enableCascade(enabled: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enableHapticFeedback

```TypeScript
enableHapticFeedback(enable: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-TimePickerAttribute-enableHapticFeedback(enable: boolean | undefined): this--><!--Device-TimePickerAttribute-enableHapticFeedback(enable: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## loop

```TypeScript
loop(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-TimePickerAttribute-loop(value: boolean | undefined): this--><!--Device-TimePickerAttribute-loop(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onChange

```TypeScript
onChange(callback: OnTimePickerChangeCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-TimePickerAttribute-onChange(callback: OnTimePickerChangeCallback | undefined): this--><!--Device-TimePickerAttribute-onChange(callback: OnTimePickerChangeCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnTimePickerChangeCallback](arkts-ontimepickerchangecallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onEnterSelectedArea

```TypeScript
onEnterSelectedArea(callback: Callback<TimePickerResult> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-TimePickerAttribute-onEnterSelectedArea(callback: Callback<TimePickerResult> | undefined): this--><!--Device-TimePickerAttribute-onEnterSelectedArea(callback: Callback<TimePickerResult> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[TimePickerResult](arkts-timepicker-timepickerresult-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## selectedTextStyle

```TypeScript
selectedTextStyle(value: PickerTextStyle | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-TimePickerAttribute-selectedTextStyle(value: PickerTextStyle | undefined): this--><!--Device-TimePickerAttribute-selectedTextStyle(value: PickerTextStyle | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PickerTextStyle](../../apis-arkui/arkts-components/arkts-arkui-pickertextstyle-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## textStyle

```TypeScript
textStyle(value: PickerTextStyle | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-TimePickerAttribute-textStyle(value: PickerTextStyle | undefined): this--><!--Device-TimePickerAttribute-textStyle(value: PickerTextStyle | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PickerTextStyle](../../apis-arkui/arkts-components/arkts-arkui-pickertextstyle-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## useMilitaryTime

```TypeScript
useMilitaryTime(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-TimePickerAttribute-useMilitaryTime(value: boolean | undefined): this--><!--Device-TimePickerAttribute-useMilitaryTime(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

设置属性修改器。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-TimePickerAttribute-default--><!--Device-TimePickerAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

