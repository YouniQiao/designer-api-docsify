# SymbolGlyph

SymbolGlyph组件用于显示系统预置的图标小符号，支持设置颜色、大小、粗细、渲染策略、动效策略等样式属性，适用于需要在应用中展示系统图标的场景，如导航栏图标、按钮图标、状态指示图标等。相比使用图片资源，SymbolGlyph具有
体积小、可动态着色、支持动效等优势。<!--RP1--><!--RP1End-->

## 子组件

不支持子组件。

## SymbolGlyph

```TypeScript
SymbolGlyph(value?: Resource)
```

定义SymbolGlyph组件构造函数。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-SymbolGlyphInterface-(value?: Resource): SymbolGlyphAttribute--><!--Device-SymbolGlyphInterface-(value?: Resource): SymbolGlyphAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | No | SymbolGlyph组件的资源名，如 \$r('sys.symbol.ohos_wifi')。不传入时不显示图标。 |

## Summary

- [EffectDirection](arkts-arkui-symbolglyph-effectdirection-e.md)
- [EffectFillStyle](arkts-arkui-symbolglyph-effectfillstyle-e.md)
- [EffectScope](arkts-arkui-symbolglyph-effectscope-e.md)
- [ReplaceEffectType](arkts-arkui-symbolglyph-replaceeffecttype-e.md)
- [SymbolEffectStrategy](arkts-arkui-symbolglyph-symboleffectstrategy-e.md)
- [SymbolRenderingStrategy](arkts-arkui-symbolglyph-symbolrenderingstrategy-e.md)
