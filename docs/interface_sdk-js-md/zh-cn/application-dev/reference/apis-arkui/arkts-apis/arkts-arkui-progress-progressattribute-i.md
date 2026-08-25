# ProgressAttribute

除支持通用属性外，还支持以下属性。支持通用事件。

> **说明：**&gt;
> 该组件重写了通用属性backgroundColor，直接添加在Progress组件上，设置进度条的底色。如需设
> 置整个Progress组件的背景色，需要在外层容器上添加backgroundColor，并用该容器包裹Progress组件。

**继承/实现关系：** ProgressAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<ProgressAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ProgressAttribute](arkts-arkui-progress-progressattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ProgressAttribute](arkts-arkui-progress-progressattribute-i.md) |

## color

```TypeScript
default color(value: ResourceColor | LinearGradient | undefined): this
```

设置进度条前景色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [value](#value) | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| [LinearGradient](arkts-arkui-datapanel-lineargradient-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ProgressAttribute](arkts-arkui-progress-progressattribute-i.md) |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<ProgressConfiguration> | undefined): this
```

定制progress内容区的方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[ProgressConfiguration](arkts-arkui-progress-progressconfiguration-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ProgressAttribute](arkts-arkui-progress-progressattribute-i.md) |

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
| [ProgressAttribute](arkts-arkui-progress-progressattribute-i.md) |

## setProgressOptions

```TypeScript
default setProgressOptions(options: ProgressOptions): this
```

设置Progress组件选项。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ProgressOptions](arkts-arkui-progress-progressoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ProgressAttribute](arkts-arkui-progress-progressattribute-i.md) |

## style

```TypeScript
default style(value: LinearStyleOptions | RingStyleOptions | CapsuleStyleOptions | ProgressStyleOptions | undefined): this
```

设置组件的样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [value](#value) | [LinearStyleOptions](arkts-arkui-progress-linearstyleoptions-i.md) \| [RingStyleOptions](arkts-arkui-progress-ringstyleoptions-i.md) \| [CapsuleStyleOptions](arkts-arkui-progress-capsulestyleoptions-i.md) \| [ProgressStyleOptions](arkts-arkui-progress-progressstyleoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ProgressAttribute](arkts-arkui-progress-progressattribute-i.md) |

## value

```TypeScript
default value(value: double | undefined): this
```

设置当前进度值。设置小于0的数值时置为0，设置大于total的数值时置为total。非法数值不生效。

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
| [ProgressAttribute](arkts-arkui-progress-progressattribute-i.md) |
