# ToolBarV2TitleOptions

```TypeScript
export interface ToolBarV2TitleOptions
```

Defines the constructor options for ToolBarV2TitleConfigs.

**Since:** 26.1.0

<!--Device-unnamed-export interface ToolBarV2TitleOptions--><!--Device-unnamed-export interface ToolBarV2TitleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ToolBarV2ItemState, ToolBarV2SymbolGlyph, ToolBarV2SymbolGlyphOptions, ToolBarV2ItemText, ToolBarV2ItemTextOptions, ToolBarV2ItemIconType, ToolBarV2ItemImage, ToolBarV2ItemImageOptions, ToolBarV2, ToolBarV2Item, ToolBarV2ItemOptions, ToolBarV2Modifier, ToolBarV2ItemAction, AdvancedToolBarV2Item, AdvancedToolBarV2ItemOptions, AdvancedToolBarV2Modifier, BarBackgroundVisibility, ToolBarV2ItemGroupStyle, ToolBarV2ItemGroupStyleOptions, ToolBarV2ItemPlacement, ToolBarV2OverflowMenuStyle, ToolBarV2PaddingOptions, ToolBarV2StyleConfigs, ToolBarV2StyleOptions, ToolBarV2TitleConfigs, ToolBarV2TitleOptions, ToolBarV2TitleStyle, ToolBarV2TitleStyleOptions, ToolBarV2MaterialStyle } from '@kit.ArkUI';
```

## content

```TypeScript
content?: ResourceStr
```

Title text content. Required when constructing ToolBarV2TitleConfigs. Default value: undefined.

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarV2TitleOptions-content?: ResourceStr--><!--Device-ToolBarV2TitleOptions-content?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## placement

```TypeScript
placement?: ToolBarV2ItemPlacement
```

Placement position of the title within the toolbar. Reuses `ToolBarV2ItemPlacement` — the title is arranged in the same area as items with the same placement. Default value: ToolBarV2ItemPlacement.LEADING.

**Type:** [ToolBarV2ItemPlacement](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2itemplacement-e.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarV2TitleOptions-placement?: ToolBarV2ItemPlacement--><!--Device-ToolBarV2TitleOptions-placement?: ToolBarV2ItemPlacement-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## style

```TypeScript
style?: ToolBarV2TitleStyle
```

Title text style.

**Type:** [ToolBarV2TitleStyle](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2titlestyle-c.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarV2TitleOptions-style?: ToolBarV2TitleStyle--><!--Device-ToolBarV2TitleOptions-style?: ToolBarV2TitleStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## subTitleContent

```TypeScript
subTitleContent?: ResourceStr
```

Subtitle text content.

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarV2TitleOptions-subTitleContent?: ResourceStr--><!--Device-ToolBarV2TitleOptions-subTitleContent?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## subTitleStyle

```TypeScript
subTitleStyle?: ToolBarV2TitleStyle
```

Subtitle text style.

**Type:** [ToolBarV2TitleStyle](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2titlestyle-c.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarV2TitleOptions-subTitleStyle?: ToolBarV2TitleStyle--><!--Device-ToolBarV2TitleOptions-subTitleStyle?: ToolBarV2TitleStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## visible

```TypeScript
visible?: boolean
```

Whether the title is visible. Default value: true.

**Type:** boolean

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarV2TitleOptions-visible?: boolean--><!--Device-ToolBarV2TitleOptions-visible?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
