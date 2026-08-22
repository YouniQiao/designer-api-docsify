# ChipSuffixSymbolGlyphOptions

symbol类型后缀图标的无障碍朗读功能属性及点击事件回调。

**起始版本：** 14

<!--Device-unnamed-export interface ChipSuffixSymbolGlyphOptions--><!--Device-unnamed-export interface ChipSuffixSymbolGlyphOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

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

后缀图标点击事件回调。

值为undefined时，不设定后缀图标事件。

默认值：undefined

**类型：** VoidCallback

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-ChipSuffixSymbolGlyphOptions-action?: VoidCallback--><!--Device-ChipSuffixSymbolGlyphOptions-action?: VoidCallback-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## activatedAccessibility

```TypeScript
activatedAccessibility?: AccessibilityOptions
```

激活态无障碍朗读功能属性。

默认值：undefined

**类型：** [AccessibilityOptions](arkts-arkui-arkui-advanced-chip-accessibilityoptions-i.md)

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-ChipSuffixSymbolGlyphOptions-activatedAccessibility?: AccessibilityOptions--><!--Device-ChipSuffixSymbolGlyphOptions-activatedAccessibility?: AccessibilityOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## normalAccessibility

```TypeScript
normalAccessibility?: AccessibilityOptions
```

非激活态无障碍朗读功能属性。

默认值：undefined

**类型：** [AccessibilityOptions](arkts-arkui-arkui-advanced-chip-accessibilityoptions-i.md)

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

<!--Device-ChipSuffixSymbolGlyphOptions-normalAccessibility?: AccessibilityOptions--><!--Device-ChipSuffixSymbolGlyphOptions-normalAccessibility?: AccessibilityOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

