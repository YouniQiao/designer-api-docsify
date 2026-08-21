# CloseOptions

Defines the default close icon behavior attributes for the chip, including accessibility attributes. The default value of **accessibilityText** is **"Delete"**.

Inherits from [AccessibilityOptions](../../apis-default/arkts-apis/arkts-arkuiadvancedchip-accessibilityoptions-i.md).

**Inheritance/Implementation:** CloseOptions extends [AccessibilityOptions](../../apis-default/arkts-apis/arkts-arkuiadvancedchip-accessibilityoptions-i.md)

**Since:** 14

<!--Device-unnamed-export interface CloseOptions--><!--Device-unnamed-export interface CloseOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { Chip, ChipOptions, ChipSize, IconCommonOptions, LabelMarginOptions, LabelOptions, PrefixIconOptions, SuffixIconOptions, ChipSymbolGlyphOptions, AccessibilitySelectedType, AccessibilityOptions, CloseOptions, ChipSuffixSymbolGlyphOptions } from '@kit.ArkUI';
import { ChipV2Size, ChipV2AccessibilitySelectedType, ChipV2ImageIconConfig, ChipV2ImageIcon, ChipV2SuffixImageIconConfig, ChipV2SuffixImageIcon, ChipV2Icon, ChipV2PrefixImageIconConfig, ChipV2PrefixImageIcon, ChipV2AccessibilityConfig, ChipV2Accessibility, ChipV2CloseConfig, ChipV2CloseIcon, ChipV2SymbolIconConfig, ChipV2SymbolIcon, ChipV2PrefixSymbolIconConfig, ChipV2PrefixSymbolIcon, ChipV2SuffixSymbolIconConfig, ChipV2SuffixSymbolIcon, ChipV2LabelMarginConfig, ChipV2LocalizedLabelMarginConfig, ChipV2LabelConfig, ChipV2Label, IChipV2OptionsConfig, ChipV2Options, ChipV2 } from '@kit.ArkUI';
import { IconOptions, LabelOptions as ChipItemLabelOptions, ChipGroupItemOptions, ChipItemStyle, ChipGroupSpaceOptions, IconItemOptions, IconGroupSuffix, ChipGroup, SuffixImageIconOptions, SymbolItemOptions } from '@kit.ArkUI';
import { ChipGroupV2ItemConfig, ChipGroupV2Item, ChipGroupV2Items, ChipGroupV2ItemStyleConfig, ChipGroupV2ItemStyle, ChipGroupV2SpaceConfig, ChipGroupV2Space, ChipGroupV2IconItemConfig, ChipGroupV2SymbolItemConfig, ChipGroupV2PaddingConfig, ChipGroupV2Padding, ChipGroupV2IconGroupSuffix, ChipGroupV2 } from '@kit.ArkUI';
```

## fontSize

```TypeScript
fontSize?: Dimension
```

Default close icon size of the chip. Percentage is not supported.

Default value:

When **size** is **ChipSize.SMALL**:**\$r('sys.float.chip_small_font_size')**.

Other cases: **\$r('sys.float.chip_normal_font_size')**.

If the value is **undefined**, the default value is used.

**Type:** Dimension

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CloseOptions-fontSize?: Dimension--><!--Device-CloseOptions-fontSize?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

