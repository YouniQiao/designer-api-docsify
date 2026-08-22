# IconGroupSuffix

The **ChipGroup** component provides a set of chips for organizing and categorizing files or resource content.

> **NOTE：**
> 
> With **SymbolGlyphModifier**, neither modifying the animation type with **symbolEffect** nor setting the effect
> strategy with effectStrategy is supported.

**Since:** 12

<!--Device-unnamed-export declare struct IconGroupSuffix--><!--Device-unnamed-export declare struct IconGroupSuffix-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { IconOptions, LabelOptions as ChipItemLabelOptions, ChipGroupItemOptions, ChipItemStyle, ChipGroupSpaceOptions, IconItemOptions, IconGroupSuffix, ChipGroup, SuffixImageIconOptions, SymbolItemOptions } from '@kit.ArkUI';
import { ChipGroupV2ItemConfig, ChipGroupV2Item, ChipGroupV2Items, ChipGroupV2ItemStyleConfig, ChipGroupV2ItemStyle, ChipGroupV2SpaceConfig, ChipGroupV2Space, ChipGroupV2IconItemConfig, ChipGroupV2SymbolItemConfig, ChipGroupV2PaddingConfig, ChipGroupV2Padding, ChipGroupV2IconGroupSuffix, ChipGroupV2 } from '@kit.ArkUI';
```

## iconBackgroundSystemMaterial

```TypeScript
@Prop
  iconBackgroundSystemMaterial?: uiMaterial.Material
```

Set system-styled materials for the component. Different materials have different effects, which can influence the backgroundColor, border, shadow, and other visual attributes of the component.

**Type:** uiMaterial.Material

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-IconGroupSuffix-@Prop  iconBackgroundSystemMaterial?: uiMaterial.Material--><!--Device-IconGroupSuffix-@Prop  iconBackgroundSystemMaterial?: uiMaterial.Material-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## items

```TypeScript
@Require
  @Prop
  items: Array<IconItemOptions | SymbolGlyphModifier | SymbolItemOptions>
```

Custom builder items.

**Type:** Array&lt;[IconItemOptions](arkts-arkui-arkui-advanced-chipgroup-iconitemoptions-i.md) \| SymbolGlyphModifier \| [SymbolItemOptions](arkts-arkui-arkui-advanced-chipgroup-symbolitemoptions-i.md)&gt;

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-IconGroupSuffix-@Require  @Prop  items: Array<IconItemOptions | SymbolGlyphModifier | SymbolItemOptions>--><!--Device-IconGroupSuffix-@Require  @Prop  items: Array<IconItemOptions | SymbolGlyphModifier | SymbolItemOptions>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

