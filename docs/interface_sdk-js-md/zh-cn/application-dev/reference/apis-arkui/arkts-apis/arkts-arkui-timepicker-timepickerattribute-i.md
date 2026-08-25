# TimePickerAttribute

除支持通用属性外，还支持以下属性：除支持通用事件外，还支持以下事件：@extends CommonMethod @interface TimePickerAttribute

**继承/实现关系：** TimePickerAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<TimePickerAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置属性修改器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[TimePickerAttribute](arkts-arkui-timepicker-timepickerattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TimePickerAttribute](arkts-arkui-timepicker-timepickerattribute-i.md) |

## dateTimeOptions

```TypeScript
default dateTimeOptions(value: DateTimeOptions | undefined): this
```

设置时分秒是否显示前导0。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | DateTimeOptions \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TimePickerAttribute](arkts-arkui-timepicker-timepickerattribute-i.md) |

## digitalCrownSensitivity

```TypeScript
default digitalCrownSensitivity(sensitivity: CrownSensitivity | undefined): this
```

设置表冠灵敏度。

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
| [TimePickerAttribute](arkts-arkui-timepicker-timepickerattribute-i.md) |

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
| [TimePickerAttribute](arkts-arkui-timepicker-timepickerattribute-i.md) |

## enableCascade

```TypeScript
default enableCascade(enabled: boolean | undefined): this
```

设置上午和下午的标识是否根据小时数自动切换，仅在useMilitaryTime设置为false时生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TimePickerAttribute](arkts-arkui-timepicker-timepickerattribute-i.md) |

## enableHapticFeedback

```TypeScript
default enableHapticFeedback(enable: boolean | undefined): this
```

设置是否支持触控反馈。开启触控反馈时，需要在工程的src/main/module.json5文件的"module"内配置requestPermissions字段开启振动权限，配置如下：

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
| [TimePickerAttribute](arkts-arkui-timepicker-timepickerattribute-i.md) |

## loop

```TypeScript
default loop(value: boolean | undefined): this
```

设置是否启用循环模式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** 
- SystemCapability.ArkUI.ArkUI.Full
- SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TimePickerAttribute](arkts-arkui-timepicker-timepickerattribute-i.md) |

## onChange

```TypeScript
default onChange(callback: OnTimePickerChangeCallback | undefined): this
```

滑动TimePicker后，时间选项归位至选中项位置时，触发该回调。不能通过双向绑定的状态变量触发。与onChange相比， callback参数类型为[OnTimePickerChangeCallback](arkts-arkui-ontimepickerchangecallback-t.md) \| undefined。回调会在滑动动画结束后触发，如果需要快速获取索引值变化，建议使用onEnterSelectedArea接口。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnTimePickerChangeCallback](arkts-arkui-ontimepickerchangecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TimePickerAttribute](arkts-arkui-timepicker-timepickerattribute-i.md) |

## onEnterSelectedArea

```TypeScript
default onEnterSelectedArea(callback: Callback<TimePickerResult> | undefined): this
```

滑动TimePicker过程中，选项进入分割线区域内，触发该回调。与onChange事件的差别在于，该事件的触发时机早于onChange事件，当当前滑动列滑动距离超过选中项 高度的一半时，选项此时已经进入分割线区域内，会触发该事件。当enableCascade设置为true时，由于上午/下午列与小 时列存在联动关系，不建议使用该回调。该回调标识的是滑动过程中选项进入分割线区域内的节点，而联动变化的选项并不涉及滑动，因此，回调的返回值 中，仅当前滑动列的值会正常变化，其余未滑动列的值保持不变。  
**说明：**
- 该接口不支持在attributeModifier中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[TimePickerResult](arkts-arkui-timepicker-timepickerresult-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TimePickerAttribute](arkts-arkui-timepicker-timepickerattribute-i.md) |

## selectedTextStyle

```TypeScript
default selectedTextStyle(value: PickerTextStyle | undefined): this
```

设置选中项的文本颜色、字号和字体粗细。

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
| [TimePickerAttribute](arkts-arkui-timepicker-timepickerattribute-i.md) |

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
| [TimePickerAttribute](arkts-arkui-timepicker-timepickerattribute-i.md) |

## useMilitaryTime

```TypeScript
default useMilitaryTime(value: boolean | undefined): this
```

设置展示时间是否为24小时制。如果展示时间为12小时制，上下午与小时无联动。

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
| [TimePickerAttribute](arkts-arkui-timepicker-timepickerattribute-i.md) |
