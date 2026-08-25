# TextTimerAttribute

除支持通用属性外，还支持以下属性。除支持通用事件外，还支持以下事件。

**继承/实现关系：** TextTimerAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<TextTimerAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置组件的动态属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[TextTimerAttribute](arkts-arkui-texttimer-texttimerattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextTimerAttribute](arkts-arkui-texttimer-texttimerattribute-i.md) |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<TextTimerConfiguration> | undefined): this
```

定制TextTimer内容区的方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[TextTimerConfiguration](arkts-arkui-texttimer-texttimerconfiguration-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextTimerAttribute](arkts-arkui-texttimer-texttimerattribute-i.md) |

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
| [TextTimerAttribute](arkts-arkui-texttimer-texttimerattribute-i.md) |

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
| [TextTimerAttribute](arkts-arkui-texttimer-texttimerattribute-i.md) |

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
| [TextTimerAttribute](arkts-arkui-texttimer-texttimerattribute-i.md) |

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
| [TextTimerAttribute](arkts-arkui-texttimer-texttimerattribute-i.md) |

## fontWeight

```TypeScript
default fontWeight(value: int | FontWeight | ResourceStr | undefined): this
```

设置文本的字体粗细，设置过大可能会导致不同字体下的文字出现截断。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int \| [FontWeight](arkts-arkui-fontweight-e.md) \| [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextTimerAttribute](arkts-arkui-texttimer-texttimerattribute-i.md) |

## format

```TypeScript
default format(value: string | undefined): this
```

设置自定义格式，需至少包含一个HH、mm、ss、SS中的关键字。使用yy、MM、dd等日期格式时，使用默认值。计时器更新频率按format最小单位处理，例如：format设置为'HH:mm'时，更新频率为一分钟。

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
| [TextTimerAttribute](arkts-arkui-texttimer-texttimerattribute-i.md) |

## onTimer

```TypeScript
default onTimer(event: TimerCallback | undefined): this
```

时间文本发生变化时触发该事件。锁屏状态和应用后台状态下不会触发该事件。设置高精度的[format](#format)（SS）时，回调间隔可能会出现波动。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [TimerCallback](arkts-arkui-timercallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [TextTimerAttribute](arkts-arkui-texttimer-texttimerattribute-i.md) |

## setTextTimerOptions

```TypeScript
default setTextTimerOptions(options?: TextTimerOptions): this
```

设置TextTimer组件的选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [TextTimerOptions](arkts-arkui-texttimer-texttimeroptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [TextTimerAttribute](arkts-arkui-texttimer-texttimerattribute-i.md) |

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
| [TextTimerAttribute](arkts-arkui-texttimer-texttimerattribute-i.md) |
