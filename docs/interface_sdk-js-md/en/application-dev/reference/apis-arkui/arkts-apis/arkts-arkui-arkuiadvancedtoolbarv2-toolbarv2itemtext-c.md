# ToolBarV2ItemText

Declare type ToolBarV2ItemText

**Since:** 18

<!--Device-unnamed-export declare class ToolBarV2ItemText--><!--Device-unnamed-export declare class ToolBarV2ItemText-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ToolBarV2ItemState, ToolBarV2SymbolGlyph, ToolBarV2SymbolGlyphOptions, ToolBarV2ItemText, ToolBarV2ItemTextOptions, ToolBarV2ItemIconType, ToolBarV2ItemImage, ToolBarV2ItemImageOptions, ToolBarV2, ToolBarV2Item, ToolBarV2ItemOptions, ToolBarV2Modifier, ToolBarV2ItemAction } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options: ToolBarV2ItemTextOptions)
```

The constructor used to create a ToolBarV2ItemText object.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ToolBarV2ItemText-constructor(options: ToolBarV2ItemTextOptions)--><!--Device-ToolBarV2ItemText-constructor(options: ToolBarV2ItemTextOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ToolBarV2ItemTextOptions](arkts-arkui-arkuiadvancedtoolbarv2-toolbarv2itemtextoptions-i.md) | Yes | text info. |

## activatedColor

```TypeScript
@Trace
  activatedColor?: ColorMetrics
```

Text fontColor when the item is activated.

**Type:** [ColorMetrics](../../apis-default/arkts-apis/arkts-graphics-colormetrics-c.md)

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ToolBarV2ItemText-@Trace  activatedColor?: ColorMetrics--><!--Device-ToolBarV2ItemText-@Trace  activatedColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
@Trace
  color?: ColorMetrics
```

Define text fontColor.

**Type:** [ColorMetrics](../../apis-default/arkts-apis/arkts-graphics-colormetrics-c.md)

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ToolBarV2ItemText-@Trace  color?: ColorMetrics--><!--Device-ToolBarV2ItemText-@Trace  color?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## text

```TypeScript
@Trace
  text: ResourceStr
```

Define text content.

**Type:** ResourceStr

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ToolBarV2ItemText-@Trace  text: ResourceStr--><!--Device-ToolBarV2ItemText-@Trace  text: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

