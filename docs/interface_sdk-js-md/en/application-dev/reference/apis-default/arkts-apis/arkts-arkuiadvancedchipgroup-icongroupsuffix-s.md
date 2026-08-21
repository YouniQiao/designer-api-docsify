# IconGroupSuffix

Defines IconGroupSuffix.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare struct IconGroupSuffix--><!--Device-unnamed-export declare struct IconGroupSuffix-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## build

```TypeScript
@Builder
  build(): void
```

The method to build component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IconGroupSuffix-@Builder  build(): void--><!--Device-IconGroupSuffix-@Builder  build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## iconBackgroundSystemMaterial

```TypeScript
@PropRef
  iconBackgroundSystemMaterial?: uiMaterial.Material
```

Set system-styled materials for the component. Different materials have different effects, which can influence the backgroundColor, border, shadow, and other visual attributes of the component.

**Type:** uiMaterial.Material

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IconGroupSuffix-@PropRef  iconBackgroundSystemMaterial?: uiMaterial.Material--><!--Device-IconGroupSuffix-@PropRef  iconBackgroundSystemMaterial?: uiMaterial.Material-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## items

```TypeScript
@Require
  @PropRef
  items: Array<IconItemOptions | SymbolGlyphModifier | SymbolItemOptions>
```

Suffix item.

**Type:** Array&lt;[IconItemOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedchipgroup-iconitemoptions-i.md) \| SymbolGlyphModifier \| [SymbolItemOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedchipgroup-symbolitemoptions-i.md)&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IconGroupSuffix-@Require  @PropRef  items: Array<IconItemOptions | SymbolGlyphModifier | SymbolItemOptions>--><!--Device-IconGroupSuffix-@Require  @PropRef  items: Array<IconItemOptions | SymbolGlyphModifier | SymbolItemOptions>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

