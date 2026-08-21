# ChipSymbolGlyphOptions

ChipSymbolGlyphOptions定义前缀图标和后缀图标的属性。

> **说明：**
> 
> 不支持使用SymbolEffect修改动效类型及
> effectStrategy设置动效。

**起始版本：** 12

<!--Device-unnamed-export interface ChipSymbolGlyphOptions--><!--Device-unnamed-export interface ChipSymbolGlyphOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { Chip, ChipOptions, ChipSize, IconCommonOptions, LabelMarginOptions, LabelOptions, PrefixIconOptions, SuffixIconOptions, ChipSymbolGlyphOptions, AccessibilitySelectedType, AccessibilityOptions, CloseOptions, ChipSuffixSymbolGlyphOptions } from '@kit.ArkUI';
import { ChipV2Size, ChipV2AccessibilitySelectedType, ChipV2ImageIconConfig, ChipV2ImageIcon, ChipV2SuffixImageIconConfig, ChipV2SuffixImageIcon, ChipV2Icon, ChipV2PrefixImageIconConfig, ChipV2PrefixImageIcon, ChipV2AccessibilityConfig, ChipV2Accessibility, ChipV2CloseConfig, ChipV2CloseIcon, ChipV2SymbolIconConfig, ChipV2SymbolIcon, ChipV2PrefixSymbolIconConfig, ChipV2PrefixSymbolIcon, ChipV2SuffixSymbolIconConfig, ChipV2SuffixSymbolIcon, ChipV2LabelMarginConfig, ChipV2LocalizedLabelMarginConfig, ChipV2LabelConfig, ChipV2Label, IChipV2OptionsConfig, ChipV2Options, ChipV2 } from '@kit.ArkUI';
import { IconOptions, LabelOptions as ChipItemLabelOptions, ChipGroupItemOptions, ChipItemStyle, ChipGroupSpaceOptions, IconItemOptions, IconGroupSuffix, ChipGroup, SuffixImageIconOptions, SymbolItemOptions } from '@kit.ArkUI';
import { ChipGroupV2ItemConfig, ChipGroupV2Item, ChipGroupV2Items, ChipGroupV2ItemStyleConfig, ChipGroupV2ItemStyle, ChipGroupV2SpaceConfig, ChipGroupV2Space, ChipGroupV2IconItemConfig, ChipGroupV2SymbolItemConfig, ChipGroupV2PaddingConfig, ChipGroupV2Padding, ChipGroupV2IconGroupSuffix, ChipGroupV2 } from '@kit.ArkUI';
```

## activated

```TypeScript
activated?: SymbolGlyphModifier
```

设置Chip在激活状态下显示的symbol类型图标。

默认值：不显示前缀图标或后缀图标

值为undefined时，按默认值处理。

**类型：** SymbolGlyphModifier

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ChipSymbolGlyphOptions-activated?: SymbolGlyphModifier--><!--Device-ChipSymbolGlyphOptions-activated?: SymbolGlyphModifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## normal

```TypeScript
normal?: SymbolGlyphModifier
```

设置Chip在非激活状态下显示的symbol类型图标。

默认值：不显示前缀图标或后缀图标

值为undefined时，按默认值处理。

**类型：** SymbolGlyphModifier

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-ChipSymbolGlyphOptions-normal?: SymbolGlyphModifier--><!--Device-ChipSymbolGlyphOptions-normal?: SymbolGlyphModifier-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

