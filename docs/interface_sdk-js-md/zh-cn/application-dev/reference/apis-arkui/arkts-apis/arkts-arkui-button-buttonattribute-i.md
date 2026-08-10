# ButtonAttribute

除支持[通用属性](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)外，还支持以下属性：

**继承/实现关系：** ButtonAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface ButtonAttribute extends CommonMethod--><!--Device-unnamed-export declare interface ButtonAttribute extends CommonMethod-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<ButtonAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置Button组件的属性修改器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ButtonAttribute-default attributeModifier(modifier: AttributeModifier<ButtonAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-ButtonAttribute-default attributeModifier(modifier: AttributeModifier<ButtonAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;ButtonAttribute&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | 是 | Button组件的属 性修改器。 取值为undefined时，则不使用attributeModifier。&lt;br/&gt;ButtonAttribute：当前组件的[属性](../arkts-components/arkts-arkui-button-attribute.md/arkts-arkui-button-attribute.md)&lt;br/&gt; CommonMethod：[通用属性](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## buttonStyle

```TypeScript
default buttonStyle(value: ButtonStyleMode | undefined): this
```

设置Button组件的样式和重要程度。根据设置枚举值的不同，系统自动会调整按钮的背景色和文字颜色。背景色和文字颜色也支持开发者通过  
[backgroundColor](arkts-arkui-common-commonmethod-i.md#backgroundcolor)、[fontColor](arkts-arkui-button-buttonattribute-i.md#fontcolor)和  
[role](arkts-arkui-button-buttonattribute-i.md#role)接口设置，实际显示效果以最后一次设置为准。

> **说明：**
> 
> 从API version 12开始，该接口支持在[attributeModifier](../arkts-components/arkts-arkui-commonmethod-c.md/arkts-arkui-commonmethod-c.md#attributemodifier)中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ButtonAttribute-default buttonStyle(value: ButtonStyleMode | undefined): this--><!--Device-ButtonAttribute-default buttonStyle(value: ButtonStyleMode | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ButtonStyleMode](arkts-arkui-button-buttonstylemode-e.md) \| undefined | 是 | Button组件的样式和重要程度。&lt;br/&gt;默认值：ButtonStyleMode.EMPHASIZED &lt;br/&gt;设置undefined时与默认值保持一 致。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<ButtonConfiguration> | undefined): this
```

定制Button内容区的方法。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ButtonAttribute-default contentModifier(modifier: ContentModifier<ButtonConfiguration> | undefined): this--><!--Device-ButtonAttribute-default contentModifier(modifier: ContentModifier<ButtonConfiguration> | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;ButtonConfiguration&gt; \| undefined | 是 | 在Button组件上，定制内容区的方法。&lt;br/&gt;modifier：内容修改器，开发者需要自定义class实 现ContentModifier接口。取值为undefined时，则不使用contentModifier。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## controlSize

```TypeScript
default controlSize(value: ControlSize | undefined): this
```

设置Button组件的尺寸。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ButtonAttribute-default controlSize(value: ControlSize | undefined): this--><!--Device-ButtonAttribute-default controlSize(value: ControlSize | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ControlSize](arkts-arkui-button-controlsize-e.md) \| undefined | 是 | Button组件的尺寸。&lt;br/&gt;默认值：ControlSize.NORMAL &lt;br/&gt;设置undefined时与默认值保持一致。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## fontColor

```TypeScript
default fontColor(value: ResourceColor | undefined): this
```

设置文本显示颜色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ButtonAttribute-default fontColor(value: ResourceColor | undefined): this--><!--Device-ButtonAttribute-default fontColor(value: ResourceColor | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 | 文本显示颜色。&lt;br/&gt;默认值：\\$r('sys.color.font_on_primary')，显示为白色字体。&lt;br/&gt;设置undefined时与默认值保持一 致。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## fontFamily

```TypeScript
default fontFamily(value: string | Resource | undefined): this
```

设置字体列表。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ButtonAttribute-default fontFamily(value: string | Resource | undefined): this--><!--Device-ButtonAttribute-default fontFamily(value: string | Resource | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string \| Resource \| undefined | 是 | 字体列表。默认字体'HarmonyOS Sans'，当前支持'HarmonyOS Sans'字体和 [注册自定义字体](arkts-font.md)。&lt;br/&gt;设置undefined时与默认值保持一致。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## fontSize

```TypeScript
default fontSize(value: Length | undefined): this
```

设置文本显示字号。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ButtonAttribute-default fontSize(value: Length | undefined): this--><!--Device-ButtonAttribute-default fontSize(value: Length | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 | 文本显示字号。&lt;br/&gt;默认值：当controlSize为ControlSize.NORMAL时，默认值为`\\$r('sys.float.Body_L')`。&lt;br/&gt;当 controlSize为ControlSize.SMALL时，默认值为`\\$r('sys.float.Body_S')`。&lt;br/&gt;**说明：**设置string类型时，不支持百分比。&lt;br/&gt;设置undefined时与 默认值保持一致。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## fontStyle

```TypeScript
default fontStyle(value: FontStyle | undefined): this
```

设置文本的字体样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ButtonAttribute-default fontStyle(value: FontStyle | undefined): this--><!--Device-ButtonAttribute-default fontStyle(value: FontStyle | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [FontStyle](arkts-arkui-fontstyle-e.md) \| undefined | 是 | 文本的字体样式。&lt;br/&gt;默认值：FontStyle.Normal &lt;br/&gt;设置undefined时与默认值保持一致。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## fontWeight

```TypeScript
default fontWeight(value: int | FontWeight | string | undefined): this
```

设置文本的字体粗细。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ButtonAttribute-default fontWeight(value: int | FontWeight | string | undefined): this--><!--Device-ButtonAttribute-default fontWeight(value: int | FontWeight | string | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int \| FontWeight \| string \| undefined | 是 | 文本的字体粗细，number类型取值[100, 900]，取值间隔为100，取值越大，字体越粗。&lt;br&gt;默认值：500&lt;br/&gt; string类型仅支持number类型取值的字符串形式，例如'400'，以及'bold'、'bolder'、'lighter'、'regular'、'medium'，分别对应FontWeight中相应的枚举值。&lt;br/ &gt;当值为异常值或非法值时，字体粗细取值为400。&lt;br/&gt;设置undefined时与异常值保持一致。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## labelStyle

```TypeScript
default labelStyle(value: ButtonLabelStyle | undefined): this
```

设置Button组件label文本和字体的样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ButtonAttribute-default labelStyle(value: ButtonLabelStyle | undefined): this--><!--Device-ButtonAttribute-default labelStyle(value: ButtonLabelStyle | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ButtonLabelStyle](arkts-arkui-button-buttonlabelstyle-i.md) \| undefined | 是 | Button组件label文本和字体的样式。取值为undefined时，按各属性的默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## maxFontScale

```TypeScript
default maxFontScale(scale: double | Resource | undefined): this
```

设置文本最大的字体缩放倍数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ButtonAttribute-default maxFontScale(scale: double | Resource | undefined): this--><!--Device-ButtonAttribute-default maxFontScale(scale: double | Resource | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | double \| Resource \| undefined | 是 | 文本最大的字体缩放倍数。&lt;br/&gt;取值范围： [1, +∞)&lt;br/&gt;**说明：** &lt;br/&gt;设置的值小于1时，按值为1处理，异常值默认不生效。&lt;br/&gt;未设置最大缩放倍数时，圆形按钮最大缩放倍数为1倍，胶囊型按钮、普通按钮、圆角矩形按钮最大缩放倍数跟随系统设置。&lt;br/&gt;设置undefined时不生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## minFontScale

```TypeScript
default minFontScale(scale: double | Resource | undefined): this
```

设置文本最小的字体缩放倍数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ButtonAttribute-default minFontScale(scale: double | Resource | undefined): this--><!--Device-ButtonAttribute-default minFontScale(scale: double | Resource | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | double \| Resource \| undefined | 是 | 文本最小的字体缩放倍数。&lt;br/&gt;取值范围：[0, 1]&lt;br/&gt;**说明：** &lt;br/&gt;设置的值小于0时，按值为0处理，设置的值大于1，按值为1处 理，异常值默认不生效。&lt;br/&gt;设置undefined时不生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## role

```TypeScript
default role(value: ButtonRole | undefined): this
```

设置Button组件的角色。根据设置枚举值的不同，系统自动会调整按钮的背景色和文字颜色。背景色和文字颜色也支持开发者通过  
[backgroundColor](arkts-arkui-common-commonmethod-i.md#backgroundcolor)、[fontColor](arkts-arkui-button-buttonattribute-i.md#fontcolor)和  
[buttonStyle](arkts-arkui-button-buttonattribute-i.md#buttonstyle)接口设置，实际显示效果以最后一次设置为准。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ButtonAttribute-default role(value: ButtonRole | undefined): this--><!--Device-ButtonAttribute-default role(value: ButtonRole | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ButtonRole](../arkts-components/arkts-arkui-buttonrole-e.md) \| undefined | 是 | 设置Button组件的角色。&lt;br/&gt;默认值：ButtonRole.NORMAL &lt;br/&gt;设置undefined时与默认值保持一致。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## stateEffect

```TypeScript
default stateEffect(value: boolean | undefined): this
```

设置是否开启按压态显示效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ButtonAttribute-default stateEffect(value: boolean | undefined): this--><!--Device-ButtonAttribute-default stateEffect(value: boolean | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 | 按钮按下时是否开启按压态显示效果。&lt;br/&gt;true：开启按压效果；false：关闭按压效果。&lt;br/&gt;默认值：true &lt;br/&gt;设置undefined时与默认值保持一 致。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## type

```TypeScript
default type(value: ButtonType | undefined): this
```

设置Button样式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ButtonAttribute-default type(value: ButtonType | undefined): this--><!--Device-ButtonAttribute-default type(value: ButtonType | undefined): this-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ButtonType](arkts-arkui-button-buttontype-e.md) \| undefined | 是 | Button样式。&lt;br/&gt;API version 18及之后，ButtonType的默认值从ButtonType.Capsule变更为 ButtonType.ROUNDED_RECTANGLE。API version 18之前的版本，ButtonType的默认值为ButtonType.Capsule。&lt;br/&gt;设置undefined时与默认值保持一致。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

