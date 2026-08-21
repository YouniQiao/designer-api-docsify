# ChipGroupV2IconGroupSuffix

Defines IconGroupSuffix.

**Since:** 26.0.0

<!--Device-unnamed-export declare struct ChipGroupV2IconGroupSuffix--><!--Device-unnamed-export declare struct ChipGroupV2IconGroupSuffix-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ChipGroupV2ItemConfig, ChipGroupV2Item, ChipGroupV2Items, ChipGroupV2ItemStyleConfig, ChipGroupV2ItemStyle, ChipGroupV2SpaceConfig, ChipGroupV2Space, ChipGroupV2IconItemConfig, ChipGroupV2SymbolItemConfig, ChipGroupV2PaddingConfig, ChipGroupV2Padding, ChipGroupV2IconGroupSuffix, ChipGroupV2 } from '@kit.ArkUI';
```

## build

```TypeScript
build(): void
```

Build function for ChipGroupV2IconGroupSuffix

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipGroupV2IconGroupSuffix-build(): void--><!--Device-ChipGroupV2IconGroupSuffix-build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## iconBackgroundSystemMaterial

```TypeScript
@Param
  iconBackgroundSystemMaterial?: uiMaterial.Material
```

IconGroupSuffix background system material.

**Type:** uiMaterial.Material

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipGroupV2IconGroupSuffix-@Param  iconBackgroundSystemMaterial?: uiMaterial.Material--><!--Device-ChipGroupV2IconGroupSuffix-@Param  iconBackgroundSystemMaterial?: uiMaterial.Material-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## items

```TypeScript
@Require
  @Param
  items: Array<ChipGroupV2IconItemConfig | SymbolGlyphModifier | ChipGroupV2SymbolItemConfig>
```

Suffix item.

**Type:** Array&lt;[ChipGroupV2IconItemConfig](../../apis-default/arkts-apis/arkts-arkuiadvancedchipgroupv2-chipgroupv2iconitemconfig-i.md) \| SymbolGlyphModifier \| [ChipGroupV2SymbolItemConfig](../../apis-default/arkts-apis/arkts-arkuiadvancedchipgroupv2-chipgroupv2symbolitemconfig-i.md)&gt;

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ChipGroupV2IconGroupSuffix-@Require  @Param  items: Array<ChipGroupV2IconItemConfig | SymbolGlyphModifier | ChipGroupV2SymbolItemConfig>--><!--Device-ChipGroupV2IconGroupSuffix-@Require  @Param  items: Array<ChipGroupV2IconItemConfig | SymbolGlyphModifier | ChipGroupV2SymbolItemConfig>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

