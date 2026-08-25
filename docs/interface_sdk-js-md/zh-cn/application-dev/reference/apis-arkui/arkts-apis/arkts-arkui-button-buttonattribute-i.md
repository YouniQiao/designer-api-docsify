# ButtonAttribute

除支持通用属性外，还支持以下属性：

**继承/实现关系：** ButtonAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<ButtonAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置Button组件的属性修改器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ButtonAttribute](arkts-arkui-button-buttonattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ButtonAttribute](arkts-arkui-button-buttonattribute-i.md) |

## buttonStyle

```TypeScript
default buttonStyle(value: ButtonStyleMode | undefined): this
```

设置Button组件的样式和重要程度。根据设置枚举值的不同，系统自动会调整按钮的背景色和文字颜色。背景色和文字颜色也支持开发者通过 backgroundColor、[fontColor](#fontcolor)和 role接口设置，实际显示效果以最后一次设置为准。

> **说明：**&gt;
> 从API version 12开始，该接口支持在attributeModifier中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ButtonStyleMode](arkts-arkui-button-buttonstylemode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ButtonAttribute](arkts-arkui-button-buttonattribute-i.md) |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<ButtonConfiguration> | undefined): this
```

定制Button内容区的方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[ButtonConfiguration](arkts-arkui-button-buttonconfiguration-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ButtonAttribute](arkts-arkui-button-buttonattribute-i.md) |

## controlSize

```TypeScript
default controlSize(value: ControlSize | undefined): this
```

设置Button组件的尺寸。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ControlSize](arkts-arkui-button-controlsize-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ButtonAttribute](arkts-arkui-button-buttonattribute-i.md) |

## fontColor

```TypeScript
default fontColor(value: ResourceColor | undefined): this
```

设置文本显示颜色。

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
| [ButtonAttribute](arkts-arkui-button-buttonattribute-i.md) |

## fontFamily

```TypeScript
default fontFamily(value: string | Resource | undefined): this
```

设置字体列表。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ButtonAttribute](arkts-arkui-button-buttonattribute-i.md) |

## fontSize

```TypeScript
default fontSize(value: Length | undefined): this
```

设置文本显示字号。

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
| [ButtonAttribute](arkts-arkui-button-buttonattribute-i.md) |

## fontStyle

```TypeScript
default fontStyle(value: FontStyle | undefined): this
```

设置文本的字体样式。

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
| [ButtonAttribute](arkts-arkui-button-buttonattribute-i.md) |

## fontWeight

```TypeScript
default fontWeight(value: int | FontWeight | string | undefined): this
```

设置文本的字体粗细。

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
| [ButtonAttribute](arkts-arkui-button-buttonattribute-i.md) |

## labelStyle

```TypeScript
default labelStyle(value: ButtonLabelStyle | undefined): this
```

设置Button组件label文本和字体的样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ButtonLabelStyle](arkts-arkui-button-buttonlabelstyle-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ButtonAttribute](arkts-arkui-button-buttonattribute-i.md) |

## maxFontScale

```TypeScript
default maxFontScale(scale: double | Resource | undefined): this
```

设置文本最大的字体缩放倍数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scale | double \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ButtonAttribute](arkts-arkui-button-buttonattribute-i.md) |

## minFontScale

```TypeScript
default minFontScale(scale: double | Resource | undefined): this
```

设置文本最小的字体缩放倍数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scale | double \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ButtonAttribute](arkts-arkui-button-buttonattribute-i.md) |

## role

```TypeScript
default role(value: ButtonRole | undefined): this
```

设置Button组件的角色。根据设置枚举值的不同，系统自动会调整按钮的背景色和文字颜色。背景色和文字颜色也支持开发者通过 backgroundColor、[fontColor](#fontcolor)和 buttonStyle接口设置，实际显示效果以最后一次设置为准。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ButtonRole](arkts-arkui-button-buttonrole-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ButtonAttribute](arkts-arkui-button-buttonattribute-i.md) |

## stateEffect

```TypeScript
default stateEffect(value: boolean | undefined): this
```

设置是否开启按压态显示效果。

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
| [ButtonAttribute](arkts-arkui-button-buttonattribute-i.md) |

## type

```TypeScript
default type(value: ButtonType | undefined): this
```

设置Button样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ButtonType](arkts-arkui-button-buttontype-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ButtonAttribute](arkts-arkui-button-buttonattribute-i.md) |
