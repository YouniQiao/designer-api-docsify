# Button属性/事件

除支持通用属性外，还支持以下属性： 支持通用事件。

**继承/实现关系：** ButtonAttribute extends CommonMethod<ButtonAttribute>

**起始版本：** 7

**废弃版本：** -1

<!--Device-unnamed-declare class ButtonAttribute--><!--Device-unnamed-declare class ButtonAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## buttonStyle

```TypeScript
buttonStyle(value: ButtonStyleMode)
```

设置Button组件的样式和重要程度。根据设置枚举值的不同，系统自动调整按钮的背景色和文字颜色。背景色和文字颜色也支持开发者通过 backgroundColor、 [fontColor](#fontColor)和[role](#role)接口设置，实际显示效果以最后一次设置为准。 > **说明：** > > 从API version 12开始，该接口支持在attributeModifier中调用。

**起始版本：** 11

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

<!--Device-ButtonAttribute-buttonStyle(value: ButtonStyleMode): ButtonAttribute--><!--Device-ButtonAttribute-buttonStyle(value: ButtonStyleMode): ButtonAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ButtonStyleMode](arkts-arkui-buttonstylemode-e.md) | 是 |

## contentModifier

```TypeScript
contentModifier(modifier: ContentModifier<ButtonConfiguration>)
```

定制Button内容区的方法。

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ButtonAttribute-contentModifier(modifier: ContentModifier<ButtonConfiguration>): ButtonAttribute--><!--Device-ButtonAttribute-contentModifier(modifier: ContentModifier<ButtonConfiguration>): ButtonAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [ContentModifier](arkts-arkui-contentmodifier-i.md)&lt;[ButtonConfiguration](arkts-arkui-buttonconfiguration-i.md)&gt; | 是 |

## controlSize

```TypeScript
controlSize(value: ControlSize)
```

设置Button组件的尺寸。 > **说明：** > > 从API version 12开始，该接口支持在attributeModifier中调用。

**起始版本：** 11

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

<!--Device-ButtonAttribute-controlSize(value: ControlSize): ButtonAttribute--><!--Device-ButtonAttribute-controlSize(value: ControlSize): ButtonAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ControlSize](arkts-arkui-controlsize-e.md) | 是 |

## fontColor

```TypeScript
fontColor(value: ResourceColor)
```

设置文本显示颜色。

**起始版本：** 7

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-ButtonAttribute-fontColor(value: ResourceColor): ButtonAttribute--><!--Device-ButtonAttribute-fontColor(value: ResourceColor): ButtonAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## fontFamily

```TypeScript
fontFamily(value: string | Resource)
```

设置字体列表。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-ButtonAttribute-fontFamily(value: string | Resource): ButtonAttribute--><!--Device-ButtonAttribute-fontFamily(value: string | Resource): ButtonAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

## fontSize

```TypeScript
fontSize(value: Length)
```

设置文本显示字号。

**起始版本：** 7

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-ButtonAttribute-fontSize(value: Length): ButtonAttribute--><!--Device-ButtonAttribute-fontSize(value: Length): ButtonAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | 是 |

## fontStyle

```TypeScript
fontStyle(value: FontStyle)
```

设置文本的字体样式。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-ButtonAttribute-fontStyle(value: FontStyle): ButtonAttribute--><!--Device-ButtonAttribute-fontStyle(value: FontStyle): ButtonAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [FontStyle](#fontStyle) | 是 |

## fontWeight

```TypeScript
fontWeight(value: number | FontWeight | string)
```

设置文本的字体粗细。

**起始版本：** 7

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-ButtonAttribute-fontWeight(value: number | FontWeight | string): ButtonAttribute--><!--Device-ButtonAttribute-fontWeight(value: number | FontWeight | string): ButtonAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number \| FontWeight \| string | 是 |

## labelStyle

```TypeScript
labelStyle(value: LabelStyle)
```

设置Button组件label文本和字体的样式。

**起始版本：** 10

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-ButtonAttribute-labelStyle(value: LabelStyle): ButtonAttribute--><!--Device-ButtonAttribute-labelStyle(value: LabelStyle): ButtonAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [LabelStyle](arkts-arkui-labelstyle-i.md) | 是 |

## maxFontScale

```TypeScript
maxFontScale(scale: number | Resource)
```

设置文本最大的字体缩放倍数。

**起始版本：** 18

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ButtonAttribute-maxFontScale(scale: number | Resource): ButtonAttribute--><!--Device-ButtonAttribute-maxFontScale(scale: number | Resource): ButtonAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scale | number \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

## minFontScale

```TypeScript
minFontScale(scale: number | Resource)
```

设置文本最小的字体缩放倍数。

**起始版本：** 18

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-ButtonAttribute-minFontScale(scale: number | Resource): ButtonAttribute--><!--Device-ButtonAttribute-minFontScale(scale: number | Resource): ButtonAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scale | number \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

## role

```TypeScript
role(value: ButtonRole)
```

设置Button组件的角色。根据设置枚举值的不同，系统自动调整按钮的背景色和文字颜色。背景色和文字颜色也支持开发者通过 backgroundColor、 [fontColor](#fontColor)和[buttonStyle](#buttonStyle)接口设置，实际显示效果以最后一次设置为准。ERROR角色通常用于删除、清空等危险或警示性操作。

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-ButtonAttribute-role(value: ButtonRole): ButtonAttribute--><!--Device-ButtonAttribute-role(value: ButtonRole): ButtonAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ButtonRole](arkts-arkui-buttonrole-e.md) | 是 |

## stateEffect

```TypeScript
stateEffect(value: boolean)
```

设置是否开启按压态显示效果。

**起始版本：** 7

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-ButtonAttribute-stateEffect(value: boolean): ButtonAttribute--><!--Device-ButtonAttribute-stateEffect(value: boolean): ButtonAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## type

```TypeScript
type(value: ButtonType)
```

设置Button样式。

**起始版本：** 7

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-ButtonAttribute-type(value: ButtonType): ButtonAttribute--><!--Device-ButtonAttribute-type(value: ButtonType): ButtonAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ButtonType](arkts-arkui-buttontype-e.md) | 是 |
