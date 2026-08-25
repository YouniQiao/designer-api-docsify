# SymbolGlyphAttribute

支持通用属性，不支持文本通用属性，仅支持以下特有属性：

**继承/实现关系：** SymbolGlyphAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<SymbolGlyphAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置组件的动态属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## effectStrategy

```TypeScript
default effectStrategy(value: SymbolEffectStrategy | undefined): this
```

设置SymbolGlyph组件动效策略。

> **说明：**&gt;
> 从API version 12开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SymbolEffectStrategy](arkts-arkui-symbolglyph-symboleffectstrategy-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## fontColor

```TypeScript
default fontColor(value: Array<ResourceColor> | undefined): this
```

设置SymbolGlyph组件字体颜色。

> **说明：**&gt;
> 从API version 12开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array&lt;[ResourceColor](arkts-arkui-resourcecolor-t.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## fontSize

```TypeScript
default fontSize(value: double | string | Resource | undefined): this
```

设置SymbolGlyph组件字体大小。设置string类型时，支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。组件的图标显示大小由fontSize控制，设置width或height后，其他通用属性仅对组件的占位大小生效。

> **说明：**&gt;
> 从API version 12开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## fontWeight

```TypeScript
default fontWeight(value: int | FontWeight | string | undefined): this
```

设置SymbolGlyph组件字体粗细。number类型取值[100,900]，取值间隔为100，默认为400，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如"400"，以及"bold"、"bolder"、"lighter"、"regular" 、"medium"分别对应FontWeight中相应的枚举值。sys.symbol.ohos_lungs图标不支持设置fontWeight。

> **说明：**&gt;
> 从API version 12开始，该接口支持在
> attributeModifier
> 中调用。

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
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## fontWeight

```TypeScript
default fontWeight(value: int | FontWeight | ResourceStr | undefined, fontWeightConfigs?: FontWeightConfigs): this
```

设置SymbolGlyph组件字体粗细及配置。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int \| [FontWeight](arkts-arkui-fontweight-e.md) \| [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | 是 |
| fontWeightConfigs | [FontWeightConfigs](arkts-arkui-textcommon-fontweightconfigs-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## maxFontScale

```TypeScript
default maxFontScale(scale: double | Resource | undefined): this
```

设置SymbolGlyph组件最大的字体缩放倍数。

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
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## minFontScale

```TypeScript
default minFontScale(scale: double | Resource | undefined): this
```

设置SymbolGlyph组件最小的字体缩放倍数。

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
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## renderingStrategy

```TypeScript
default renderingStrategy(value: SymbolRenderingStrategy | undefined): this
```

设置SymbolGlyph组件渲染策略。

> **说明：**&gt;
> 从API version 12开始，该接口支持在
> attributeModifier
> 中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [SymbolRenderingStrategy](arkts-arkui-symbolglyph-symbolrenderingstrategy-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## setSymbolGlyphOptions

```TypeScript
default setSymbolGlyphOptions(value?: Resource): this
```

设置SymbolGlyph组件选项。

**起始版本：** 26.1.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## shaderStyle

```TypeScript
default shaderStyle(shader: Array<ShaderStyle | undefined> | ShaderStyle | undefined): this
```

设置SymbolGlyph组件的渐变色效果。可以显示为径向渐变RadialGradientStyle或线 性渐变LinearGradientStyle或纯色 ColorShaderStyle的效果，shaderStyle的优 先级高于[fontColor](#fontcolor)和AI识别，纯色建议使用 [fontColor](#fontcolor)。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| shader | Array&lt;[ShaderStyle](arkts-arkui-textcommon-shaderstyle-c.md) \| undefined & gt; \ | [ShaderStyle](arkts-arkui-textcommon-shaderstyle-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## symbolColor

```TypeScript
default symbolColor(value: Array<ResourceColor> | Array<ColorMetrics> | Array<ResourceColor | ColorMetrics> | undefined): this
```

设置SymbolGlyph组件的字体颜色，相比[fontColor](#fontcolor)接口，本接口支持传入 [ColorMetrics](../../../reference/apis-arkui/js-apis-arkui-graphics.md#colormetrics12)类型参数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array&lt;[ResourceColor](arkts-arkui-resourcecolor-t.md)&gt; \| Array&lt;[ColorMetrics](arkts-arkui-colormetrics-t.md)&gt; \| Array&lt;[ResourceColor](arkts-arkui-resourcecolor-t.md) \| [ColorMetrics](arkts-arkui-colormetrics-t.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## symbolEffect

```TypeScript
default symbolEffect(symbolEffect: SymbolEffect | undefined): this
```

设置SymbolGlyph组件动效策略。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [symbolEffect](#symboleffect) | [SymbolEffect](arkts-arkui-symbolglyph-symboleffect-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## symbolEffect

```TypeScript
default symbolEffect(symbolEffect: SymbolEffect | undefined, isActive: boolean | undefined): this
```

设置SymbolGlyph组件动效策略及播放状态。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [symbolEffect](#symboleffect) | [SymbolEffect](arkts-arkui-symbolglyph-symboleffect-c.md) \| undefined | 是 |
| isActive | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## symbolEffect

```TypeScript
default symbolEffect(symbolEffect: SymbolEffect | undefined, triggerValue: int | undefined): this
```

设置SymbolGlyph组件动效策略及播放触发器。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [symbolEffect](#symboleffect) | [SymbolEffect](arkts-arkui-symbolglyph-symboleffect-c.md) \| undefined | 是 |
| triggerValue | int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## symbolShadow

```TypeScript
default symbolShadow(shadow: ShadowOptions | undefined): this
```

设置SymbolGlyph组件的阴影效果。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| shadow | [ShadowOptions](../arkts-components/arkts-arkui-shadowoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |
