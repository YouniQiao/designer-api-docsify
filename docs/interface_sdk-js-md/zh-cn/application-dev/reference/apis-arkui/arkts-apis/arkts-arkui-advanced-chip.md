# @ohos.arkui.advanced.Chip

## 导入模块

```TypeScript
import { Chip, ChipOptions, ChipSize, IconCommonOptions, LabelMarginOptions, LabelOptions, PrefixIconOptions, SuffixIconOptions, ChipSymbolGlyphOptions, AccessibilitySelectedType, AccessibilityOptions, CloseOptions, ChipSuffixSymbolGlyphOptions } from '@kit.ArkUI';
import { ChipV2Size, ChipV2AccessibilitySelectedType, ChipV2ImageIconConfig, ChipV2ImageIcon, ChipV2SuffixImageIconConfig, ChipV2SuffixImageIcon, ChipV2Icon, ChipV2PrefixImageIconConfig, ChipV2PrefixImageIcon, ChipV2AccessibilityConfig, ChipV2Accessibility, ChipV2CloseConfig, ChipV2CloseIcon, ChipV2SymbolIconConfig, ChipV2SymbolIcon, ChipV2PrefixSymbolIconConfig, ChipV2PrefixSymbolIcon, ChipV2SuffixSymbolIconConfig, ChipV2SuffixSymbolIcon, ChipV2LabelMarginConfig, ChipV2LocalizedLabelMarginConfig, ChipV2LabelConfig, ChipV2Label, IChipV2OptionsConfig, ChipV2Options, ChipV2 } from '@kit.ArkUIV2';
import { IconOptions, LabelOptions as ChipItemLabelOptions, ChipGroupItemOptions, ChipItemStyle, ChipGroupSpaceOptions, IconItemOptions, IconGroupSuffix, ChipGroup, SuffixImageIconOptions, SymbolItemOptions } from '@kit.ArkUIGroup';
import { ChipGroupV2ItemConfig, ChipGroupV2Item, ChipGroupV2Items, ChipGroupV2ItemStyleConfig, ChipGroupV2ItemStyle, ChipGroupV2SpaceConfig, ChipGroupV2Space, ChipGroupV2IconItemConfig, ChipGroupV2SymbolItemConfig, ChipGroupV2PaddingConfig, ChipGroupV2Padding, ChipGroupV2IconGroupSuffix, ChipGroupV2 } from '@kit.ArkUIGroupV2';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [Chip](arkts-arkui-arkui-advanced-chip-chip-f.md) | 创建Chip组件。 |

### 接口

| 名称 | 说明 |
| --- | --- |
| [AccessibilityOptions](arkts-arkui-arkui-advanced-chip-accessibilityoptions-i.md) | 后缀图标的无障碍朗读功能属性。 |
| [ChipOptions](arkts-arkui-arkui-advanced-chip-chipoptions-i.md) | ChipOptions定义Chip的样式及具体样式参数。 |
| [ChipSuffixSymbolGlyphOptions](arkts-arkui-arkui-advanced-chip-chipsuffixsymbolglyphoptions-i.md) | symbol类型后缀图标的无障碍朗读功能属性及点击事件回调。 |
| [ChipSymbolGlyphOptions](arkts-arkui-arkui-advanced-chip-chipsymbolglyphoptions-i.md) | ChipSymbolGlyphOptions定义前缀图标和后缀图标的属性。 |
| [CloseOptions](arkts-arkui-arkui-advanced-chip-closeoptions-i.md) | CloseOptions用于定义Chip组件默认的关闭图标功能属性，包括无障碍功能属性，其中accessibilityText默认为"删除"。继承于[AccessibilityOptions](arkts-arkui-arkui-advanced-chip-accessibilityoptions-i.md)。 |
| [IconCommonOptions](arkts-arkui-arkui-advanced-chip-iconcommonoptions-i.md) | IconCommonOptions定义图标的共通属性。 |
| [LabelMarginOptions](arkts-arkui-arkui-advanced-chip-labelmarginoptions-i.md) | LabelMarginOptions用于定义文本与左右侧图标之间间距。 |
| [LabelOptions](arkts-arkui-arkui-advanced-chip-labeloptions-i.md) | LabelOptions定义文本属性。 |
| [LocalizedLabelMarginOptions](arkts-arkui-arkui-advanced-chip-localizedlabelmarginoptions-i.md) | LocalizedLabelMarginOptions用于定义本地化文本与左右侧图标之间间距。 |
| [PrefixIconOptions](arkts-arkui-arkui-advanced-chip-prefixiconoptions-i.md) | PrefixIconOptions定义前缀图标的属性。继承于[IconCommonOptions](arkts-arkui-arkui-advanced-chip-iconcommonoptions-i.md)。 |
| [SuffixIconOptions](arkts-arkui-arkui-advanced-chip-suffixiconoptions-i.md) | SuffixIconOptions定义后缀图标的属性。继承于[IconCommonOptions](arkts-arkui-arkui-advanced-chip-iconcommonoptions-i.md)。 |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [AccessibilitySelectedType](arkts-arkui-arkui-advanced-chip-accessibilityselectedtype-e.md) | AccessibilitySelectedType定义Chip可指定的选中态类型，用于控制无障碍服务如何向用户传达组件的选中状态。不同的选中态类型提供了不同的语义和用户体验。 |
| [ChipSize](arkts-arkui-arkui-advanced-chip-chipsize-e.md) | Enum for ChipSize |
