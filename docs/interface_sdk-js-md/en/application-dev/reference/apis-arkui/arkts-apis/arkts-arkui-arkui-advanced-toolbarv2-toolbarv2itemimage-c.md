# ToolBarV2ItemImage

Declare type ToolBarV2ItemImage

**Since:** 18

<!--Device-unnamed-export declare class ToolBarV2ItemImage--><!--Device-unnamed-export declare class ToolBarV2ItemImage-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ToolBarV2ItemState, ToolBarV2SymbolGlyph, ToolBarV2SymbolGlyphOptions, ToolBarV2ItemText, ToolBarV2ItemTextOptions, ToolBarV2ItemIconType, ToolBarV2ItemImage, ToolBarV2ItemImageOptions, ToolBarV2, ToolBarV2Item, ToolBarV2ItemOptions, ToolBarV2Modifier, ToolBarV2ItemAction } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options: ToolBarV2ItemImageOptions)
```

The constructor used to create a ToolBarV2ItemImage object.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ToolBarV2ItemImage-constructor(options: ToolBarV2ItemImageOptions)--><!--Device-ToolBarV2ItemImage-constructor(options: ToolBarV2ItemImageOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ToolBarV2ItemImageOptions](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2itemimageoptions-i.md) | Yes | image info. |

## activatedColor

```TypeScript
@Trace
  activatedColor?: ColorMetrics
```

Icon fillColor when the item is activated.

**Type:** [ColorMetrics](../../apis-default/arkts-apis/arkts-graphics-colormetrics-c.md)

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ToolBarV2ItemImage-@Trace  activatedColor?: ColorMetrics--><!--Device-ToolBarV2ItemImage-@Trace  activatedColor?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
@Trace
  color?: ColorMetrics
```

Define icon fillColor.

**Type:** [ColorMetrics](../../apis-default/arkts-apis/arkts-graphics-colormetrics-c.md)

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ToolBarV2ItemImage-@Trace  color?: ColorMetrics--><!--Device-ToolBarV2ItemImage-@Trace  color?: ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## src

```TypeScript
@Trace
  src: ResourceStr
```

Define icon resource.

**Type:** ResourceStr

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ToolBarV2ItemImage-@Trace  src: ResourceStr--><!--Device-ToolBarV2ItemImage-@Trace  src: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

