# DatePickerAttribute

除支持通用属性外，还支持以下属性：除支持通用事件外，还支持以下事件：@extends CommonMethod @interface DatePickerAttribute

**继承/实现关系：** DatePickerAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<DatePickerAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置属性修改器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[DatePickerAttribute](arkts-arkui-datepicker-datepickerattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [DatePickerAttribute](arkts-arkui-datepicker-datepickerattribute-i.md) |

## canLoop

```TypeScript
default canLoop(isLoop: boolean | undefined): this
```

设置是否可循环滚动。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isLoop | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [DatePickerAttribute](arkts-arkui-datepicker-datepickerattribute-i.md) |

## digitalCrownSensitivity

```TypeScript
default digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this
```

设置表冠灵敏度。  
**说明：**
- 用于穿戴设备圆形屏幕使用。组件响应表冠事件，需要先获取焦点。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sensitivity | [CrownSensitivity](arkts-arkui-crownsensitivity-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [DatePickerAttribute](arkts-arkui-datepicker-datepickerattribute-i.md) |

## disappearTextStyle

```TypeScript
default disappearTextStyle(value: PickerTextStyle | undefined): this
```

设置边缘项（以选中项为基准向上或向下的第二项）的文本样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [PickerTextStyle](../arkts-components/arkts-arkui-pickertextstyle-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [DatePickerAttribute](arkts-arkui-datepicker-datepickerattribute-i.md) |

## enableHapticFeedback

```TypeScript
default enableHapticFeedback(enable: boolean | undefined): this
```

设置是否开启触控反馈。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [DatePickerAttribute](arkts-arkui-datepicker-datepickerattribute-i.md) |

## lunar

```TypeScript
default lunar(value: boolean | undefined): this
```

设置日期是否显示为农历。  
**说明：**
- 仅在简体中文和繁体中文语言环境下生效，其他语言环境下设置该属性无效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [DatePickerAttribute](arkts-arkui-datepicker-datepickerattribute-i.md) |

## onDateChange

```TypeScript
default onDateChange(callback: Callback<Date> | undefined): this
```

滑动DatePicker文本内容后，选项完全归位至选中项位置时，触发该回调。不能通过双向绑定的状态变量触发。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;Date&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [DatePickerAttribute](arkts-arkui-datepicker-datepickerattribute-i.md) |

## selectedTextStyle

```TypeScript
default selectedTextStyle(value: PickerTextStyle | undefined): this
```

设置选中项的文本样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [PickerTextStyle](../arkts-components/arkts-arkui-pickertextstyle-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [DatePickerAttribute](arkts-arkui-datepicker-datepickerattribute-i.md) |

## textStyle

```TypeScript
default textStyle(value: PickerTextStyle | undefined): this
```

设置待选项（以选中项为基准向上或向下的第一项）的文本样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [PickerTextStyle](../arkts-components/arkts-arkui-pickertextstyle-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [DatePickerAttribute](arkts-arkui-datepicker-datepickerattribute-i.md) |
