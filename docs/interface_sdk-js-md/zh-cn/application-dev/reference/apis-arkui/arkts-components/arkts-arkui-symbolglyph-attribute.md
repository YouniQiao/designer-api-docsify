# SymbolGlyph属性/事件

支持通用属性，不支持文本通用属性，仅支持以下特有属性。支持通用事件。

**继承/实现关系：** SymbolGlyphAttribute extends CommonMethod<SymbolGlyphAttribute>

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为11。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## effectStrategy

```TypeScript
effectStrategy(value: SymbolEffectStrategy)
```

设置SymbolGlyph组件动效策略。未通过该接口设置时，默认动效策略为SymbolEffectStrategy.NONE。

> **说明：**&gt;
> - 从API version 12开始，该接口支持在attributeModifier中调用。&gt;
> - 动效属性，仅支持使用effectStrategy属性或单个symbolEffect属性，不支持多种动效属性混合使用。&gt;
> - 本接口仅支持NONE、SCALE、HIERARCHICAL三种预置动效类型，设置后动效自动播放。如需使用更丰富的动效类型（如出现、消失、弹跳、替换、脉冲动效等）或控制动效的播放状态和触发时机，请使用
> [symbolEffect](#symboleffect)接口。两者不可同时使
> 用，详见[symbolEffect](#symboleffect)接口说明。

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为11。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SymbolEffectStrategy](arkts-arkui-symboleffectstrategy-e.md) | 是 |

## fontColor

```TypeScript
fontColor(value: Array<ResourceColor>)
```

设置SymbolGlyph组件字体颜色。

> **说明：**&gt;
> 从API version 12开始，该接口支持在attributeModifier中调用。

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为11。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array & lt;ResourceColor & gt; | 是 |

## fontColor

```TypeScript
fontColor(value: Array<ResourceColor | ColorMetrics> | undefined)
```

设置SymbolGlyph组件的字体颜色，相比[fontColor](#fontcolor)接口，本接口支持传入 [ColorMetrics](../arkts-apis/arkts-arkui-graphics-colormetrics-c.md)类型参数。

> **说明：**&gt;
> 该接口支持在attributeModifier中调用。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array & lt;ResourceColor \ | ColorMetrics & gt; \ | undefined | 是 |

## fontSize

```TypeScript
fontSize(value: number | string | Resource)
```

设置SymbolGlyph组件字体大小。设置string类型时，支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。组件的图标显示大小由fontSize控制，设置width或height后，其他通用属性仅对组件的占位大小生效。未通过该接口设置时，默认字体大小为16fp。

> **说明：**&gt;
> 从API version 12开始，该接口支持在attributeModifier中调用。

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为11。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

## fontWeight

```TypeScript
fontWeight(value: number | FontWeight | string)
```

设置SymbolGlyph组件字体粗细。未通过该接口设置时，默认字体粗细为FontWeight.Normal（正常粗细，对应数值400）。sys.symbol.ohos_lungs图标不支持设置fontWeight。

> **说明：**&gt;
> 从API version 12开始，该接口支持在attributeModifier中调用。

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为11。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number \| FontWeight \| string | 是 |

## fontWeight

```TypeScript
fontWeight(value: number | FontWeight | ResourceStr, fontWeightConfigs?: FontWeightConfigs)
```

设置SymbolGlyph组件图标小符号的粗细，支持通过FontWeightConfigs配置是否开启可变字重调节（启用后可设置非100整数倍的精细字重值，如220、660）、是否开启随设备的字体粗细级别自动更新字重（启用后组件字 重随系统字体粗细设置自动调整）。未通过该接口设置时，默认字体粗细为FontWeight.Normal（正常粗细，对应数值400）。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number \| FontWeight \| [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | 是 |
| fontWeightConfigs | [FontWeightConfigs](../arkts-apis/arkts-arkui-fontweightconfigs-i.md) | 否 |

## maxFontScale

```TypeScript
maxFontScale(scale: Optional<number|Resource>)
```

设置SymbolGlyph组件最大的字体缩放倍数。适用于需要防止图标在用户字体缩放设置过大时超出布局容器或破坏界面一致性的场景，例如限制图标在小尺寸容器中的最大显示尺寸。

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为18。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scale | Optional & lt;number \ | Resource & gt; | 是 |

## minFontScale

```TypeScript
minFontScale(scale: Optional<number|Resource>)
```

设置SymbolGlyph组件最小的字体缩放倍数。适用于需要防止图标在用户字体缩放设置过小时变得不可识别的场景，例如确保图标在任意系统字体设置下仍保持最小可读尺寸。

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为18。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scale | Optional & lt;number \ | Resource & gt; | 是 |

## renderingStrategy

```TypeScript
renderingStrategy(value: SymbolRenderingStrategy)
```

设置SymbolGlyph组件渲染策略。未通过该接口设置时，默认渲染策略为SymbolRenderingStrategy.SINGLE。

> **说明：**&gt;
> 从API version 12开始，该接口支持在attributeModifier中调用。

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为11。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SymbolRenderingStrategy](arkts-arkui-symbolrenderingstrategy-e.md) | 是 |

## shaderStyle

```TypeScript
shaderStyle(shader: Array<ShaderStyle | undefined> | ShaderStyle)
```

设置SymbolGlyph组件的渐变色效果。可以显示为径向渐变RadialGradientStyle或线性渐变LinearGradientStyle或纯色 ColorShaderStyle，shaderStyle的优先级高于 [fontColor](#fontcolor)和AI识别，纯色建议使用 [fontColor](#fontcolor)。

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为20。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| shader | Array & lt;ShaderStyle \ | undefined & gt; \ | [ShaderStyle](#shaderstyle) | 是 |

## symbolEffect

```TypeScript
symbolEffect(symbolEffect: SymbolEffect, isActive?: boolean)
```

设置SymbolGlyph组件动效策略及播放状态。未通过该接口设置时，默认动效为SymbolEffect对象，默认播放状态为false。

> **说明：**&gt;
> 动效属性，仅支持使用effectStrategy属性或单个symbolEffect属性，不支持多种动效属性混合使用。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [symbolEffect](#symboleffect) | [SymbolEffect](arkts-arkui-symboleffect-c.md) | 是 |
| isActive | boolean | 否 |

## symbolEffect

```TypeScript
symbolEffect(symbolEffect: SymbolEffect, triggerValue?: number)
```

设置SymbolGlyph组件动效策略及播放触发器。未通过该接口设置时，默认动效为SymbolEffect对象，默认触发器值为-1。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [symbolEffect](#symboleffect) | [SymbolEffect](arkts-arkui-symboleffect-c.md) | 是 |
| triggerValue | number | 否 |

## symbolShadow

```TypeScript
symbolShadow(shadow: Optional<ShadowOptions>)
```

设置SymbolGlyph组件的阴影效果。未通过该接口设置时，默认阴影效果为{radius：0,color：Color.Black,offsetX：0,offsetY：0}。

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为20。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本20开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| shadow | Optional & lt;ShadowOptions & gt; | 是 |
