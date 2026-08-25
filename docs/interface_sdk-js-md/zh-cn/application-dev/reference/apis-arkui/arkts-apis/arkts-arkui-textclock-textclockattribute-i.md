# TextClockAttribute

除支持通用属性外，还支持以下属性。除支持通用事件外，还支持以下事件。

**继承/实现关系：** TextClockAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<TextClockAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置组件的动态属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<TextClockConfiguration> | undefined): this
```

定制TextClock内容区的方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[TextClockConfiguration](arkts-arkui-textclock-textclockconfiguration-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |

## dateTimeOptions

```TypeScript
default dateTimeOptions(dateTimeOptions: DateTimeOptions | undefined): this
```

设置小时是否显示前导0。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [dateTimeOptions](#datetimeoptions) | DateTimeOptions \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |

## fontColor

```TypeScript
default fontColor(value: ResourceColor | undefined): this
```

设置字体颜色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |

## fontFamily

```TypeScript
default fontFamily(value: ResourceStr | undefined): this
```

设置字体列表。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |

## fontFeature

```TypeScript
default fontFeature(value: string | undefined): this
```

设置文字特性效果，比如数字等宽的特性。格式为：normal \| \&lt;feature-tag-value\&gt;\&lt;feature-tag-value\&gt;的格式为：\&lt;string\&gt; \[ \&lt;integer\&gt; \| on \| off ]\&lt;feature-tag-value\&gt;的个数可以有多个，中间用','隔开。例如，使用等宽时钟数字的输入格式为："ss01" on。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |

## fontSize

```TypeScript
default fontSize(value: Length | undefined): this
```

设置字体大小。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |

## fontStyle

```TypeScript
default fontStyle(value: FontStyle | undefined): this
```

设置字体样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [FontStyle](arkts-arkui-fontstyle-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |

## fontWeight

```TypeScript
default fontWeight(value: int | FontWeight | string | undefined): this
```

设置文本的字体粗细，设置过大可能会导致不同字体下的文字出现截断。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int \| [FontWeight](arkts-arkui-fontweight-e.md) \| string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |

## format

```TypeScript
default format(value: ResourceStr | undefined): this
```

设置显示时间格式，如“yyyy/MM/dd”、“yyyy-MM-dd”。y：年（yyyy表示完整年份，yy表示年份后两位）M：月（若想使用01月则使用MM）d：日（若想使用01日则使用dd）E：星期（若想使用星期六则使用EEEE，若想使用周六则使用E、EE、EEE）H：小时（24小时制） h：小时（12小时制）m：分钟s：秒SS：厘秒（format中S个数&lt;3，全部按厘秒处理）SSS：毫秒（format中S个数&gt;=3，全部按毫秒处理）a：上午/下午（当设置小时制式为H时，该参数不生效）日期间隔符："年月日"、“/”、"-"、"."（可以自定义间隔符样式，字母不可以作为间隔符，汉字可以作为间隔符处理）允许自行拼接组合显示格式，即：年、月、日、星期、时、分、秒、毫秒可拆分为子元素，可自行排布组合。时间更新频率最高为一秒一次，不建议单独设置厘秒和毫秒格式。当设置无效字母时（非上述字母被认为是无效字母），该字母会被忽略。如果format全是无效字母时，显示格式跟随系统语言和系统小时制。例如系统语言为中文时，12小时制显示格式为yyyy/MM/dd aa hh:mm:ss.SSS， 24小时制显示格式为yyyy/MM/dd HH:mm:ss.SSS。若format为空字符串（""）或者undefined，则使用默认值。非卡片中默认值：12小时制：aa hh:mm:ss，24小时制：HH:mm:ss。卡片中默认值：12小时制：hh:mm，24小时制：HH:mm 。卡片中使用时，最小时间单位为分钟。如果设置格式中有秒或厘秒按默认值处理。以下是format输入的格式样式及对应的显示效果：  
| 输入格式 | 显示效果 | | ---------------------- | ------------------- | | yyyy年M月d日 EEEE | 2023年2月4日 星期六 | | yyyy年M月d日 | 2023年2月4日 | | M月d日 EEEE | 2月4日 星期六 | | M月d日 | 2月4日 | | MM/dd/yyyy | 02/04/2023 | | EEEE MM月dd日 | 星期六 02月04日 | | yyyy（完整年份） | 2023年 | | yy（年份后两位） | 23年 | | MM（完整月份） | 02月 | | M（月份） | 2月 | | dd（完整日期） | 04日 | | d（日期） | 4日 | | EEEE（完整星期） | 星期六 | | E、EE、EEE（简写星期） | 周六 | | yyyy年M月d日 | 2023年2月4日 | | yyyy/M/d | 2023/2/4 | | yyyy-M-d | 2023-2-4 | | yyyy.M.d | 2023.2.4 | | HH:mm:ss（时:分:秒） | 17:00:04 | | aa hh:mm:ss（时:分:秒） | 上午 5:00:04 | | hh:mm:ss（时:分:秒） | 5:00:04 | | HH:mm（时:分） | 17:00 | | aa hh:mm（时:分） | 上午 5:00 | | hh:mm（时:分） | 5:00 | | mm:ss（分:秒） | 00:04 | | mm:ss.SS（分:秒.厘秒） | 00:04.91 | | mm:ss.SSS（分:秒.毫秒） | 00:04.536 | | hh:mm:ss aa | 5:00:04 上午 | | HH |

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |

## onDateChange

```TypeScript
default onDateChange(event: Callback<long> | undefined): this
```

组件不可见时不回调。非卡片中使用时，该事件回调间隔为秒。卡片中使用时，该事件回调间隔为分钟。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;long&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |

## setTextClockOptions

```TypeScript
default setTextClockOptions(options?: TextClockOptions): this
```

设置TextClock组件的选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [TextClockOptions](arkts-arkui-textclock-textclockoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |

## textShadow

```TypeScript
default textShadow(value: ShadowOptions | Array<ShadowOptions> | undefined): this
```

设置文字阴影效果。该接口支持以数组形式入参，实现多重文字阴影。不支持fill字段, 不支持智能取色模式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ShadowOptions](../arkts-components/arkts-arkui-shadowoptions-i.md) \| Array&lt;[ShadowOptions](../arkts-components/arkts-arkui-shadowoptions-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextClockAttribute](arkts-arkui-textclock-textclockattribute-i.md) |
