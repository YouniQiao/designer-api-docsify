# ButtonAttribute

除支持通用属性外，还支持以下属性：

**继承/实现关系：** ButtonAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface ButtonAttribute--><!--Device-unnamed-export declare interface ButtonAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<ButtonAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ButtonAttribute-attributeModifier(modifier: AttributeModifier<ButtonAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-ButtonAttribute-attributeModifier(modifier: AttributeModifier<ButtonAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ButtonAttribute](arkts-button-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## buttonStyle

```TypeScript
buttonStyle(value: ButtonStyleMode | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ButtonAttribute-buttonStyle(value: ButtonStyleMode | undefined): this--><!--Device-ButtonAttribute-buttonStyle(value: ButtonStyleMode | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ButtonStyleMode](arkts-button-buttonstylemode-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## contentModifier

```TypeScript
contentModifier(modifier: ContentModifier<ButtonConfiguration> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ButtonAttribute-contentModifier(modifier: ContentModifier<ButtonConfiguration> | undefined): this--><!--Device-ButtonAttribute-contentModifier(modifier: ContentModifier<ButtonConfiguration> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../../apis-arkui/arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[ButtonConfiguration](arkts-button-buttonconfiguration-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## controlSize

```TypeScript
controlSize(value: ControlSize | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ButtonAttribute-controlSize(value: ControlSize | undefined): this--><!--Device-ButtonAttribute-controlSize(value: ControlSize | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ControlSize](arkts-button-controlsize-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## fontColor

```TypeScript
fontColor(value: ResourceColor | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ButtonAttribute-fontColor(value: ResourceColor | undefined): this--><!--Device-ButtonAttribute-fontColor(value: ResourceColor | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## fontFamily

```TypeScript
fontFamily(value: string | Resource | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ButtonAttribute-fontFamily(value: string | Resource | undefined): this--><!--Device-ButtonAttribute-fontFamily(value: string | Resource | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## fontSize

```TypeScript
fontSize(value: Length | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ButtonAttribute-fontSize(value: Length | undefined): this--><!--Device-ButtonAttribute-fontSize(value: Length | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## fontStyle

```TypeScript
fontStyle(value: FontStyle | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ButtonAttribute-fontStyle(value: FontStyle | undefined): this--><!--Device-ButtonAttribute-fontStyle(value: FontStyle | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [FontStyle](../../apis-arkui/arkts-apis/arkts-arkui-fontstyle-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## fontWeight

```TypeScript
fontWeight(value: int | FontWeight | string | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ButtonAttribute-fontWeight(value: int | FontWeight | string | undefined): this--><!--Device-ButtonAttribute-fontWeight(value: int | FontWeight | string | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int \| [FontWeight](../../apis-arkui/arkts-apis/arkts-arkui-fontweight-e.md) \| string \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## labelStyle

```TypeScript
labelStyle(value: ButtonLabelStyle | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ButtonAttribute-labelStyle(value: ButtonLabelStyle | undefined): this--><!--Device-ButtonAttribute-labelStyle(value: ButtonLabelStyle | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ButtonLabelStyle](arkts-button-buttonlabelstyle-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## maxFontScale

```TypeScript
maxFontScale(scale: double | Resource | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ButtonAttribute-maxFontScale(scale: double | Resource | undefined): this--><!--Device-ButtonAttribute-maxFontScale(scale: double | Resource | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | double \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## minFontScale

```TypeScript
minFontScale(scale: double | Resource | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ButtonAttribute-minFontScale(scale: double | Resource | undefined): this--><!--Device-ButtonAttribute-minFontScale(scale: double | Resource | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | double \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## role

```TypeScript
role(value: ButtonRole | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ButtonAttribute-role(value: ButtonRole | undefined): this--><!--Device-ButtonAttribute-role(value: ButtonRole | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ButtonRole](arkts-button-buttonrole-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## stateEffect

```TypeScript
stateEffect(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ButtonAttribute-stateEffect(value: boolean | undefined): this--><!--Device-ButtonAttribute-stateEffect(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## type

```TypeScript
type(value: ButtonType | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ButtonAttribute-type(value: ButtonType | undefined): this--><!--Device-ButtonAttribute-type(value: ButtonType | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ButtonType](arkts-button-buttontype-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

设置Button组件的属性修改器。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ButtonAttribute-default--><!--Device-ButtonAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

