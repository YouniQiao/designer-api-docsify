# ChipGroupPaddingOptions

Defines the top and bottom padding of a **ChipGroup** component, which is used to control the overall height of the ChipGroup.

**Since:** 12

<!--Device-unnamed-export interface ChipGroupPaddingOptions--><!--Device-unnamed-export interface ChipGroupPaddingOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { IconOptions, LabelOptions as ChipItemLabelOptions, ChipGroupItemOptions, ChipItemStyle, ChipGroupSpaceOptions, IconItemOptions, IconGroupSuffix, ChipGroup, SuffixImageIconOptions, SymbolItemOptions } from '@kit.ArkUI';
import { ChipGroupV2ItemConfig, ChipGroupV2Item, ChipGroupV2Items, ChipGroupV2ItemStyleConfig, ChipGroupV2ItemStyle, ChipGroupV2SpaceConfig, ChipGroupV2Space, ChipGroupV2IconItemConfig, ChipGroupV2SymbolItemConfig, ChipGroupV2PaddingConfig, ChipGroupV2Padding, ChipGroupV2IconGroupSuffix, ChipGroupV2 } from '@kit.ArkUI';
```

## bottom

```TypeScript
bottom: Length
```

Bottom padding. Percentage values are not supported.

Default value: **14**

Unit: vp

If this parameter is set to **undefined**, the default value is used.

**Type:** Length

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ChipGroupPaddingOptions-bottom: Length--><!--Device-ChipGroupPaddingOptions-bottom: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## top

```TypeScript
top: Length
```

Top padding. Percentage values are not supported.

Default value: **14**

Unit: vp

If the value is **undefined**, the default value is used.

**Type:** Length

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ChipGroupPaddingOptions-top: Length--><!--Device-ChipGroupPaddingOptions-top: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

