# @ohos.arkui.advanced.ChipGroup

## Modules to Import

```TypeScript
import { IconOptions, LabelOptions as ChipItemLabelOptions, ChipGroupItemOptions, ChipItemStyle, ChipGroupSpaceOptions, IconItemOptions, IconGroupSuffix, ChipGroup, SuffixImageIconOptions, SymbolItemOptions } from '@kit.ArkUI';
import { ChipGroupV2ItemConfig, ChipGroupV2Item, ChipGroupV2Items, ChipGroupV2ItemStyleConfig, ChipGroupV2ItemStyle, ChipGroupV2SpaceConfig, ChipGroupV2Space, ChipGroupV2IconItemConfig, ChipGroupV2SymbolItemConfig, ChipGroupV2PaddingConfig, ChipGroupV2Padding, ChipGroupV2IconGroupSuffix, ChipGroupV2 } from '@kit.ArkUI';
```

## Summary

### Structs

| Name | Description |
| --- | --- |
| [ChipGroup](arkts-arkui-arkuiadvancedchipgroup-chipgroup-s.md) | > **NOTE：** >  > 1. When **multiple** is set to **false**, if **selectedIndexes** is not passed in, the first chip is automatically > selected by default. However, if the provided **selectedIndexes** includes multiple elements, the chip at the first > index is selected by default. >  > 2. To use the suffix functionality, the **IconGroupSuffix** API must be imported. If this API is not provided, the > suffix area will remain empty. >  > 3. The icon fill colors (**fillColor** and **activedFillColor**) must match the font color (**fontColor**). If > different colors need to be set, use **prefixSymbol** when passing in > [ChipGroupSpaceOptions](arkts-arkui-arkuiadvancedchipgroup-chipgroupspaceoptions-i.md). |
| [IconGroupSuffix](arkts-arkui-arkuiadvancedchipgroup-icongroupsuffix-s.md) | The **ChipGroup** component provides a set of chips for organizing and categorizing files or resource content. |

### Interfaces

| Name | Description |
| --- | --- |
| [ChipGroupItemOptions](arkts-arkui-arkuiadvancedchipgroup-chipgroupitemoptions-i.md) | Defines the specific attributes of individual chips. |
| [ChipGroupPaddingOptions](arkts-arkui-arkuiadvancedchipgroup-chipgrouppaddingoptions-i.md) | Defines the top and bottom padding of a **ChipGroup** component, which is used to control the overall height of the ChipGroup. |
| [ChipGroupSpaceOptions](arkts-arkui-arkuiadvancedchipgroup-chipgroupspaceoptions-i.md) | Defines the left and right padding of the chip group, and the spacing between chips. |
| [ChipItemStyle](arkts-arkui-arkuiadvancedchipgroup-chipitemstyle-i.md) | Defines the common attributes shared by all chips. |
| [IconItemOptions](arkts-arkui-arkuiadvancedchipgroup-iconitemoptions-i.md) | Defines the configuration for the trailing builder, with constraints applied to background size and color settings. |
| [IconOptions](arkts-arkui-arkuiadvancedchipgroup-iconoptions-i.md) | Defines the common attributes of icons. |
| [LabelOptions](arkts-arkui-arkuiadvancedchipgroup-labeloptions-i.md) | Defines the label configuration options. |
| [SuffixImageIconOptions](arkts-arkui-arkuiadvancedchipgroup-suffiximageiconoptions-i.md) | Defines the configuration options for suffix icons. |
| [SymbolItemOptions](arkts-arkui-arkuiadvancedchipgroup-symbolitemoptions-i.md) | Suffix icon option type of ChipGroup. |

