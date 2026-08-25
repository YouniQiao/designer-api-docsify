# CalendarPickerAttribute

除支持通用属性外，还支持以下属性：除支持通用事件，还支持以下事件：@extends CommonMethod @interface CalendarPickerAttribute

**继承/实现关系：** CalendarPickerAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<CalendarPickerAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置属性修改器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CalendarPickerAttribute](arkts-arkui-calendarpicker-calendarpickerattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [CalendarPickerAttribute](arkts-arkui-calendarpicker-calendarpickerattribute-i.md) |

## edgeAlign

```TypeScript
default edgeAlign(alignType: CalendarAlign | undefined, offset?: Offset): this
```

设置选择器与入口组件的对齐方式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [alignType](arkts-arkui-atomicservice-atomicservicesearch-menualignparams-i.md) | [CalendarAlign](arkts-arkui-calendarpicker-calendaralign-e.md) \| undefined | 是 |
| offset | [Offset](arkts-arkui-componentutils-offset-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [CalendarPickerAttribute](arkts-arkui-calendarpicker-calendarpickerattribute-i.md) |

## markToday

```TypeScript
default markToday(enabled: boolean | undefined): this
```

设置日历选择器中系统当前日期是否保持高亮显示。

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
| [CalendarPickerAttribute](arkts-arkui-calendarpicker-calendarpickerattribute-i.md) |

## onChange

```TypeScript
default onChange(callback: Callback<Date> | undefined): this
```

选择日期时触发该事件。不能通过双向绑定的状态变量触发。

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
| [CalendarPickerAttribute](arkts-arkui-calendarpicker-calendarpickerattribute-i.md) |

## textStyle

```TypeScript
default textStyle(value: PickerTextStyle | undefined): this
```

入口区的文本颜色、字号、字体粗细。

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
| [CalendarPickerAttribute](arkts-arkui-calendarpicker-calendarpickerattribute-i.md) |
