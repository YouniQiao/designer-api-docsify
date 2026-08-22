# IconOptions

Defines the common attributes of icons.

**Since:** 12

<!--Device-unnamed-export interface IconOptions--><!--Device-unnamed-export interface IconOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { IconOptions, LabelOptions as ChipItemLabelOptions, ChipGroupItemOptions, ChipItemStyle, ChipGroupSpaceOptions, IconItemOptions, IconGroupSuffix, ChipGroup, SuffixImageIconOptions, SymbolItemOptions } from '@kit.ArkUI';
import { ChipGroupV2ItemConfig, ChipGroupV2Item, ChipGroupV2Items, ChipGroupV2ItemStyleConfig, ChipGroupV2ItemStyle, ChipGroupV2SpaceConfig, ChipGroupV2Space, ChipGroupV2IconItemConfig, ChipGroupV2SymbolItemConfig, ChipGroupV2PaddingConfig, ChipGroupV2Padding, ChipGroupV2IconGroupSuffix, ChipGroupV2 } from '@kit.ArkUI';
```

## size

```TypeScript
size?: SizeOptions
```

Icon size. This parameter cannot be set in percentage.

Default value: **undefined**

**Type:** SizeOptions

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-IconOptions-size?: SizeOptions--><!--Device-IconOptions-size?: SizeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## src

```TypeScript
src: ResourceStr
```

Icon source, which can be a specific image resource or an image address reference. For details, see [Image](../../../reference/apis-arkui/arkui-ts/ts-basic-components-image.md#image-1).

**Type:** ResourceStr

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-IconOptions-src: ResourceStr--><!--Device-IconOptions-src: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

