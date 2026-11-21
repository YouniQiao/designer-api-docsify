# AdvancedToolBarV2Item

```TypeScript
export declare class AdvancedToolBarV2Item extends ToolBarV2Item
```

Defines the advanced toolbar item.

Extends [ToolBarV2Item](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2item-c.md) with advanced layout capabilities such as custom builder, title configuration, placement, display priority, activated background color, item size, separator, text visibility, overflow menu, and item grouping.

Items with the same non-empty `groupID` form a group. Group-level configuration (placement, spacing, container style) is read from the first item in the array that carries that `groupID`.

**Inheritance/Implementation:** AdvancedToolBarV2Item extends [ToolBarV2Item](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2item-c.md)

**Since:** 26.1.0

**Decorator:** @ObservedV2

<!--Device-unnamed-export declare class AdvancedToolBarV2Item extends ToolBarV2Item--><!--Device-unnamed-export declare class AdvancedToolBarV2Item extends ToolBarV2Item-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ToolBarV2ItemState, ToolBarV2SymbolGlyph, ToolBarV2SymbolGlyphOptions, ToolBarV2ItemText, ToolBarV2ItemTextOptions, ToolBarV2ItemIconType, ToolBarV2ItemImage, ToolBarV2ItemImageOptions, ToolBarV2, ToolBarV2Item, ToolBarV2ItemOptions, ToolBarV2Modifier, ToolBarV2ItemAction, AdvancedToolBarV2Item, AdvancedToolBarV2ItemOptions, AdvancedToolBarV2Modifier, BarBackgroundVisibility, ToolBarV2ItemGroupStyle, ToolBarV2ItemGroupStyleOptions, ToolBarV2ItemPlacement, ToolBarV2OverflowMenuStyle, ToolBarV2PaddingOptions, ToolBarV2StyleConfigs, ToolBarV2StyleOptions, ToolBarV2TitleConfigs, ToolBarV2TitleOptions, ToolBarV2TitleStyle, ToolBarV2TitleStyleOptions, ToolBarV2MaterialStyle } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(params: AdvancedToolBarV2ItemParams)
```

The constructor used to create a AdvancedToolBarV2Item object.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-AdvancedToolBarV2Item-constructor(params: AdvancedToolBarV2ItemParams)--><!--Device-AdvancedToolBarV2Item-constructor(params: AdvancedToolBarV2ItemParams)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [AdvancedToolBarV2ItemParams](arkts-arkui-arkui-advanced-toolbarv2-advancedtoolbarv2itemparams-i.md) | Yes | item info. |

## activatedBackgroundColor

```TypeScript
activatedBackgroundColor?: ColorMetrics
```

Item background color in `ACTIVATE` status (activated background color). Only applies to icon-only items; icon+text items cannot set a background color. Defaults to transparent when not specified. Recommend using `$r('sys.color.comp_background_emphasize')` (HarmonyOS blue). Default value: Color.Transparent.

**Type:** [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-AdvancedToolBarV2Item-activatedBackgroundColor?: ColorMetrics--><!--Device-AdvancedToolBarV2Item-activatedBackgroundColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## builder

```TypeScript
builder?: CustomBuilder
```

Custom content builder for the toolbar item. When set, content and icon are ignored. Default value: undefined.

**Type:** [CustomBuilder](../arkts-components/arkts-arkui-common-comp-custombuilder-t.md)

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-AdvancedToolBarV2Item-builder?: CustomBuilder--><!--Device-AdvancedToolBarV2Item-builder?: CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## displayPriority

```TypeScript
displayPriority?: number
```

Display priority of the toolbar item in the layout container. Higher values indicate higher display priority. Value range: [0,10]. Default value: 1.

**Type:** number

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-AdvancedToolBarV2Item-displayPriority?: number--><!--Device-AdvancedToolBarV2Item-displayPriority?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## groupID

```TypeScript
groupID?: string
```

Group identifier. Items sharing the same non-empty `groupID` are rendered as a visual group. Group-level configuration is read from the first item in the array that carries this `groupID`. Default value: undefined.

**Type:** string

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-AdvancedToolBarV2Item-groupID?: string--><!--Device-AdvancedToolBarV2Item-groupID?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## groupStyle

```TypeScript
groupStyle?: ToolBarV2ItemGroupStyle
```

Style configuration for the group that this item belongs to. Only the value on the first item (in array order) carrying a given `groupID` takes effect; values on subsequent items with the same `groupID` are ignored. Default value: undefined.

**Type:** [ToolBarV2ItemGroupStyle](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2itemgroupstyle-c.md)

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-AdvancedToolBarV2Item-groupStyle?: ToolBarV2ItemGroupStyle--><!--Device-AdvancedToolBarV2Item-groupStyle?: ToolBarV2ItemGroupStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## id

```TypeScript
id?: string
```

Unique identifier for the toolbar item.

**Type:** string

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-AdvancedToolBarV2Item-id?: string--><!--Device-AdvancedToolBarV2Item-id?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isShowOverflowMenu

```TypeScript
isShowOverflowMenu?: boolean
```

Whether to display the overflowMenu of the toolbar in this item. Default value: false.

**Type:** boolean

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-AdvancedToolBarV2Item-isShowOverflowMenu?: boolean--><!--Device-AdvancedToolBarV2Item-isShowOverflowMenu?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isShowSeparator

```TypeScript
isShowSeparator?: boolean
```

Whether to show a separator after this item. When true, a separator is rendered after this item (not after the last item in the toolbar). Default value: false.

**Type:** boolean

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-AdvancedToolBarV2Item-isShowSeparator?: boolean--><!--Device-AdvancedToolBarV2Item-isShowSeparator?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isShowText

```TypeScript
isShowText?: boolean
```

Whether to display the text content of the toolbar item. When set to false, the text specified by `content` is not rendered in the toolbar, but `content` is still used for overflow menu identification. This is useful when an icon-only item still needs text identification in the overflow menu. Default value: true.

**Type:** boolean

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-AdvancedToolBarV2Item-isShowText?: boolean--><!--Device-AdvancedToolBarV2Item-isShowText?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## itemSize

```TypeScript
itemSize?: Size
```

Item size (width × height) for the toolbar item. Default value: mainAxis 56vp x crossAxis 48vp. When horizontal: 56vp(width) x 48vp(height). When vertical: 48vp(width) x 56vp(height).

**Type:** Size

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-AdvancedToolBarV2Item-itemSize?: Size--><!--Device-AdvancedToolBarV2Item-itemSize?: Size-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## placement

```TypeScript
placement?: ToolBarV2ItemPlacement
```

Placement position of the toolbar item. Default value: ToolBarV2ItemPlacement.MAIN.

**Type:** [ToolBarV2ItemPlacement](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2itemplacement-e.md)

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-AdvancedToolBarV2Item-placement?: ToolBarV2ItemPlacement--><!--Device-AdvancedToolBarV2Item-placement?: ToolBarV2ItemPlacement-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## titleConfigs

```TypeScript
titleConfigs?: ToolBarV2TitleConfigs
```

Define advanced ToolBarV2 title settings. When not provided, no title is rendered.

**Type:** [ToolBarV2TitleConfigs](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2titleconfigs-c.md)

**Since:** 26.1.0

**Decorator:** @Trace

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-AdvancedToolBarV2Item-titleConfigs?: ToolBarV2TitleConfigs--><!--Device-AdvancedToolBarV2Item-titleConfigs?: ToolBarV2TitleConfigs-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
