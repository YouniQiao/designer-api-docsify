# SymbolGlyphAttribute

Provides attribute for SymbolGlyph.

**Inheritance/Implementation:** SymbolGlyphAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<SymbolGlyphAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Sets the attribute modifier.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## effectStrategy

```TypeScript
default effectStrategy(value: SymbolEffectStrategy | undefined): this
```

Called when the symbolGlyph effect is set.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [SymbolEffectStrategy](arkts-arkui-symbolglyph-symboleffectstrategy-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## fontColor

```TypeScript
default fontColor(value: Array<ResourceColor> | undefined): this
```

Called when the SymbolGlyph color is set.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | Array&lt;[ResourceColor](arkts-arkui-resourcecolor-t.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## fontSize

```TypeScript
default fontSize(value: double | string | Resource | undefined): this
```

Called when the SymbolGlyph size is set.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## fontWeight

```TypeScript
default fontWeight(value: int | FontWeight | string | undefined): this
```

Called when the font symbolGlyph weight is set.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int \| [FontWeight](arkts-arkui-fontweight-e.md) \| string \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## fontWeight

```TypeScript
default fontWeight(value: int | FontWeight | ResourceStr | undefined, fontWeightConfigs?: FontWeightConfigs): this
```

Used to set the font weight of SymbolGlyph.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int \| [FontWeight](arkts-arkui-fontweight-e.md) \| [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | Yes |
| fontWeightConfigs | [FontWeightConfigs](arkts-arkui-textcommon-fontweightconfigs-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## maxFontScale

```TypeScript
default maxFontScale(scale: double | Resource | undefined): this
```

Called when the maximum font scale of the font is set.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scale | double \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## minFontScale

```TypeScript
default minFontScale(scale: double | Resource | undefined): this
```

Called when the minimum font scale of the font is set.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scale | double \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## renderingStrategy

```TypeScript
default renderingStrategy(value: SymbolRenderingStrategy | undefined): this
```

Called when the symbolGlyph rendering strategy is set.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [SymbolRenderingStrategy](arkts-arkui-symbolglyph-symbolrenderingstrategy-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## setSymbolGlyphOptions

```TypeScript
default setSymbolGlyphOptions(value?: Resource): this
```

Set SymbolGlyph options.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## shaderStyle

```TypeScript
default shaderStyle(shader: Array<ShaderStyle | undefined> | ShaderStyle | undefined): this
```

Set the shader style of the symbol, such as lineargradient or radialgradient.If a single `ShaderStyle` is provided, all layers of the symbol will use this shader style. If an array is provided, each item corresponds to the shader style of the matching symbol layer.  
- If an array item is `undefined`, that layer will use its default color. - Any layers beyond the length of the array will also use their default color.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| shader | Array&lt;[ShaderStyle](arkts-arkui-textcommon-shaderstyle-c.md) \| undefined & gt; \ | [ShaderStyle](arkts-arkui-textcommon-shaderstyle-c.md) \| undefined | Yes | The shader style(s) to apply. - `ShaderStyle`: Apply the same shader style to all symbol layers. - `Array&lt;ShaderStyle \|

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## symbolColor

```TypeScript
default symbolColor(value: Array<ResourceColor> | Array<ColorMetrics> | Array<ResourceColor | ColorMetrics> | undefined): this
```

Called when the SymbolGlyph color is set.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | Array&lt;[ResourceColor](arkts-arkui-resourcecolor-t.md)&gt; \| Array&lt;[ColorMetrics](arkts-arkui-colormetrics-t.md)&gt; \| Array&lt;[ResourceColor](arkts-arkui-resourcecolor-t.md) \| [ColorMetrics](arkts-arkui-colormetrics-t.md)&gt; \| undefined | Yes | The custom color list applied to the symbol. - `Array&lt;ResourceColor&gt;` means each item is a resource-based color value, for example a color resource, numeric color value, or color string. - `Array&lt;ColorMetrics&gt;` means each item is a ColorMetrics color object. - `Array&lt;ResourceColor \|

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## symbolEffect

```TypeScript
default symbolEffect(symbolEffect: SymbolEffect | undefined): this
```

Define effect options for SymbolGlyph.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [symbolEffect](#symboleffect) | [SymbolEffect](arkts-arkui-symbolglyph-symboleffect-c.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## symbolEffect

```TypeScript
default symbolEffect(symbolEffect: SymbolEffect | undefined, isActive: boolean | undefined): this
```

Define effect options for SymbolGlyph.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [symbolEffect](#symboleffect) | [SymbolEffect](arkts-arkui-symbolglyph-symboleffect-c.md) \| undefined | Yes |
| isActive | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## symbolEffect

```TypeScript
default symbolEffect(symbolEffect: SymbolEffect | undefined, triggerValue: int | undefined): this
```

Define effect options for SymbolGlyph.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [symbolEffect](#symboleffect) | [SymbolEffect](arkts-arkui-symbolglyph-symboleffect-c.md) \| undefined | Yes |
| triggerValue | int \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |

## symbolShadow

```TypeScript
default symbolShadow(shadow: ShadowOptions | undefined): this
```

Set the shadow of symbol.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This API does not work with the fill attribute, showType attribute or coloring strategy. </p>

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| shadow | [ShadowOptions](../arkts-components/arkts-arkui-shadowoptions-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SymbolGlyphAttribute](arkts-arkui-symbolglyph-symbolglyphattribute-i.md) |
