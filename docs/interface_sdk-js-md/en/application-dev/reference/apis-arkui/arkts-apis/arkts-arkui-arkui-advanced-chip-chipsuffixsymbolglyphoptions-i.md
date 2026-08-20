# ChipSuffixSymbolGlyphOptions

Defines the accessibility options of the symbol-type suffix icon.

**Since:** 14

<!--Device-unnamed-export interface ChipSuffixSymbolGlyphOptions--><!--Device-unnamed-export interface ChipSuffixSymbolGlyphOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { Chip, ChipOptions, ChipSize, IconCommonOptions, LabelMarginOptions, LabelOptions, PrefixIconOptions, SuffixIconOptions, ChipSymbolGlyphOptions, AccessibilitySelectedType, AccessibilityOptions, CloseOptions, ChipSuffixSymbolGlyphOptions } from '@kit.ArkUI';
import { ChipV2Size, ChipV2AccessibilitySelectedType, ChipV2ImageIconConfig, ChipV2ImageIcon, ChipV2SuffixImageIconConfig, ChipV2SuffixImageIcon, ChipV2Icon, ChipV2PrefixImageIconConfig, ChipV2PrefixImageIcon, ChipV2AccessibilityConfig, ChipV2Accessibility, ChipV2CloseConfig, ChipV2CloseIcon, ChipV2SymbolIconConfig, ChipV2SymbolIcon, ChipV2PrefixSymbolIconConfig, ChipV2PrefixSymbolIcon, ChipV2SuffixSymbolIconConfig, ChipV2SuffixSymbolIcon, ChipV2LabelMarginConfig, ChipV2LocalizedLabelMarginConfig, ChipV2LabelConfig, ChipV2Label, IChipV2OptionsConfig, ChipV2Options, ChipV2 } from '@kit.ArkUI';
import { IconOptions, LabelOptions as ChipItemLabelOptions, ChipGroupItemOptions, ChipItemStyle, ChipGroupSpaceOptions, IconItemOptions, IconGroupSuffix, ChipGroup, SuffixImageIconOptions, SymbolItemOptions } from '@kit.ArkUI';
import { ChipGroupV2ItemConfig, ChipGroupV2Item, ChipGroupV2Items, ChipGroupV2ItemStyleConfig, ChipGroupV2ItemStyle, ChipGroupV2SpaceConfig, ChipGroupV2Space, ChipGroupV2IconItemConfig, ChipGroupV2SymbolItemConfig, ChipGroupV2PaddingConfig, ChipGroupV2Padding, ChipGroupV2IconGroupSuffix, ChipGroupV2 } from '@kit.ArkUI';
```

## action

```TypeScript
action?: VoidCallback
```

Action of the suffix icon.

Default value: **undefined**

**Type:** VoidCallback

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-ChipSuffixSymbolGlyphOptions-action?: VoidCallback--><!--Device-ChipSuffixSymbolGlyphOptions-action?: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## activatedAccessibility

```TypeScript
activatedAccessibility?: AccessibilityOptions
```

Accessibility settings for the activated state.

Default value: **undefined**

**Type:** [AccessibilityOptions](../../apis-default/arkts-apis/arkts-arkui-advanced-chip-accessibilityoptions-i.md)

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-ChipSuffixSymbolGlyphOptions-activatedAccessibility?: AccessibilityOptions--><!--Device-ChipSuffixSymbolGlyphOptions-activatedAccessibility?: AccessibilityOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## normalAccessibility

```TypeScript
normalAccessibility?: AccessibilityOptions
```

Accessibility settings for the normal state.

Default value: **undefined**

**Type:** [AccessibilityOptions](../../apis-default/arkts-apis/arkts-arkui-advanced-chip-accessibilityoptions-i.md)

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-ChipSuffixSymbolGlyphOptions-normalAccessibility?: AccessibilityOptions--><!--Device-ChipSuffixSymbolGlyphOptions-normalAccessibility?: AccessibilityOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

