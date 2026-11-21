# ToolBarV2TitleConfigs

```TypeScript
export declare class ToolBarV2TitleConfigs
```

Title configuration. When not provided, no title is rendered.

The title participates in layout at the same level as toolbar items. The title reuses `ToolBarV2ItemPlacement` (`LEADING` / `MAIN` / `TRAILING`) to determine the rendering area, and is arranged in the same area as items with the same placement.

**Since:** 26.1.0

**Decorator:** @ObservedV2

<!--Device-unnamed-export declare class ToolBarV2TitleConfigs--><!--Device-unnamed-export declare class ToolBarV2TitleConfigs-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ToolBarV2ItemState, ToolBarV2SymbolGlyph, ToolBarV2SymbolGlyphOptions, ToolBarV2ItemText, ToolBarV2ItemTextOptions, ToolBarV2ItemIconType, ToolBarV2ItemImage, ToolBarV2ItemImageOptions, ToolBarV2, ToolBarV2Item, ToolBarV2ItemOptions, ToolBarV2Modifier, ToolBarV2ItemAction, AdvancedToolBarV2Item, AdvancedToolBarV2ItemOptions, AdvancedToolBarV2Modifier, BarBackgroundVisibility, ToolBarV2ItemGroupStyle, ToolBarV2ItemGroupStyleOptions, ToolBarV2ItemPlacement, ToolBarV2OverflowMenuStyle, ToolBarV2PaddingOptions, ToolBarV2StyleConfigs, ToolBarV2StyleOptions, ToolBarV2TitleConfigs, ToolBarV2TitleOptions, ToolBarV2TitleStyle, ToolBarV2TitleStyleOptions, ToolBarV2MaterialStyle } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options?: ToolBarV2TitleOptions)
```

Constructs a ToolBarV2TitleConfigs instance.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarV2TitleConfigs-constructor(options?: ToolBarV2TitleOptions)--><!--Device-ToolBarV2TitleConfigs-constructor(options?: ToolBarV2TitleOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ToolBarV2TitleOptions](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2titleoptions-i.md) | No | Constructor options. |

## content

```TypeScript
content: ResourceStr
```

Title text content. Required when constructing ToolBarV2TitleConfigs.

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarV2TitleConfigs-content: ResourceStr--><!--Device-ToolBarV2TitleConfigs-content: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## placement

```TypeScript
placement?: ToolBarV2ItemPlacement
```

Placement position of the title within the toolbar. Reuses `ToolBarV2ItemPlacement` — the title is arranged in the same area as items with the same placement. Default value: ToolBarV2ItemPlacement.LEADING.

**Type:** [ToolBarV2ItemPlacement](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2itemplacement-e.md)

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarV2TitleConfigs-placement?: ToolBarV2ItemPlacement--><!--Device-ToolBarV2TitleConfigs-placement?: ToolBarV2ItemPlacement-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## style

```TypeScript
style?: ToolBarV2TitleStyle
```

Title text style.

**Type:** [ToolBarV2TitleStyle](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2titlestyle-c.md)

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarV2TitleConfigs-style?: ToolBarV2TitleStyle--><!--Device-ToolBarV2TitleConfigs-style?: ToolBarV2TitleStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## subTitleContent

```TypeScript
subTitleContent?: ResourceStr
```

Subtitle text content. Default value: undefined. No content is available when this parameter is not set.

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarV2TitleConfigs-subTitleContent?: ResourceStr--><!--Device-ToolBarV2TitleConfigs-subTitleContent?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## subTitleStyle

```TypeScript
subTitleStyle?: ToolBarV2TitleStyle
```

Subtitle text style.

**Type:** [ToolBarV2TitleStyle](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2titlestyle-c.md)

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarV2TitleConfigs-subTitleStyle?: ToolBarV2TitleStyle--><!--Device-ToolBarV2TitleConfigs-subTitleStyle?: ToolBarV2TitleStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## visible

```TypeScript
visible?: boolean
```

Whether the title is visible. Default value: true.

**Type:** boolean

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ToolBarV2TitleConfigs-visible?: boolean--><!--Device-ToolBarV2TitleConfigs-visible?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
