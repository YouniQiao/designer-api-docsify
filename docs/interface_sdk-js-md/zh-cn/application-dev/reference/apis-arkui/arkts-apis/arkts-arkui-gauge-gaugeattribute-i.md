# GaugeAttribute

除支持通用属性外，还支持以下属性。支持通用事件。

**继承/实现关系：** GaugeAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<GaugeAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置组件的动态属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[GaugeAttribute](arkts-arkui-gauge-gaugeattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [GaugeAttribute](arkts-arkui-gauge-gaugeattribute-i.md) |

## colors

```TypeScript
default colors(colors: ResourceColor | LinearGradient | Array<[ResourceColor | LinearGradient, double]> | undefined): this
```

设置仪表的颜色。可以设置纯色和分段的渐变色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [colors](#colors) | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| [LinearGradient](arkts-arkui-datapanel-lineargradient-c.md) \| Array & lt;[ResourceColor \ | [LinearGradient](arkts-arkui-datapanel-lineargradient-c.md), double]&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [GaugeAttribute](arkts-arkui-gauge-gaugeattribute-i.md) |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<GaugeConfiguration> | undefined): this
```

定制Gauge内容区的方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[GaugeConfiguration](arkts-arkui-gauge-gaugeconfiguration-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [GaugeAttribute](arkts-arkui-gauge-gaugeattribute-i.md) |

## description

```TypeScript
default description(value: CustomBuilder | undefined | null): this
```

设置说明内容。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [value](#value) | [CustomBuilder](arkts-arkui-custombuilder-t.md) \| undefined \| null | 是 |

**返回值：**

| 类型 |
| --- |
| [GaugeAttribute](arkts-arkui-gauge-gaugeattribute-i.md) |

## endAngle

```TypeScript
default endAngle(angle: double | undefined): this
```

设置终止角度位置。起始角度和终止角度的差值过小时，会绘制出异常图像，请取合理的起始角度和终止角度。建议使用单色环改变Gauge的value参数实现数据值的调节，可通过定时器setTimeout进行数值的延迟加载。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| angle | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [GaugeAttribute](arkts-arkui-gauge-gaugeattribute-i.md) |

## indicator

```TypeScript
default indicator(value: GaugeIndicatorOptions | undefined | null): this
```

设置指针样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [value](#value) | [GaugeIndicatorOptions](arkts-arkui-gauge-gaugeindicatoroptions-i.md) \| undefined \| null | 是 |

**返回值：**

| 类型 |
| --- |
| [GaugeAttribute](arkts-arkui-gauge-gaugeattribute-i.md) |

## privacySensitive

```TypeScript
default privacySensitive(isPrivacySensitiveMode: boolean | undefined): this
```

设置隐私敏感。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isPrivacySensitiveMode | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [GaugeAttribute](arkts-arkui-gauge-gaugeattribute-i.md) |

## setGaugeOptions

```TypeScript
default setGaugeOptions(options: GaugeOptions): this
```

设置Gauge选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [GaugeOptions](arkts-arkui-gauge-gaugeoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [GaugeAttribute](arkts-arkui-gauge-gaugeattribute-i.md) |

## startAngle

```TypeScript
default startAngle(angle: double | undefined): this
```

设置起始角度位置。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| angle | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [GaugeAttribute](arkts-arkui-gauge-gaugeattribute-i.md) |

## strokeWidth

```TypeScript
default strokeWidth(length: Length | undefined): this
```

设置环形量规图的环形厚度。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| length | [Length](arkts-arkui-length-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [GaugeAttribute](arkts-arkui-gauge-gaugeattribute-i.md) |

## trackShadow

```TypeScript
default trackShadow(value: GaugeShadowOptions | undefined | null): this
```

设置阴影样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [value](#value) | [GaugeShadowOptions](arkts-arkui-gauge-gaugeshadowoptions-i.md) \| undefined \| null | 是 |

**返回值：**

| 类型 |
| --- |
| [GaugeAttribute](arkts-arkui-gauge-gaugeattribute-i.md) |

## value

```TypeScript
default value(value: double | undefined): this
```

设置量规图的数据值。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [value](#value) | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [GaugeAttribute](arkts-arkui-gauge-gaugeattribute-i.md) |
