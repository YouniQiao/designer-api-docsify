# ToolBarV2ItemImage

Declare type ToolBarV2ItemImage

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

<!--Device-unnamed-export declare class ToolBarV2ItemImage--><!--Device-unnamed-export declare class ToolBarV2ItemImage-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ToolBarV2ItemState } from 'ToolBarV2ItemState';
import { ToolBarV2SymbolGlyph } from 'ToolBarV2SymbolGlyph';
import { ToolBarV2SymbolGlyphOptions } from 'ToolBarV2SymbolGlyphOptions';
import { ToolBarV2ItemText } from 'ToolBarV2ItemText';
import { ToolBarV2ItemTextOptions } from 'ToolBarV2ItemTextOptions';
import { ToolBarV2ItemIconType } from 'ToolBarV2ItemIconType';
import { ToolBarV2ItemImage } from 'ToolBarV2ItemImage';
import { ToolBarV2ItemImageOptions } from 'ToolBarV2ItemImageOptions';
import { ToolBarV2 } from 'ToolBarV2';
import { ToolBarV2Item } from 'ToolBarV2Item';
import { ToolBarV2ItemOptions } from 'ToolBarV2ItemOptions';
import { ToolBarV2Modifier } from 'ToolBarV2Modifier';
import { ToolBarV2ItemAction } from 'ToolBarV2ItemAction';
```

## constructor

```TypeScript
constructor(options: ToolBarV2ItemImageOptions)
```

The constructor used to create a ToolBarV2ItemImage object.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

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

**Type:** [ColorMetrics](../../apis-na/arkts-apis/arkts-na-graphics-colormetrics-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

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

**Type:** [ColorMetrics](../../apis-na/arkts-apis/arkts-na-graphics-colormetrics-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

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

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ToolBarV2ItemImage-@Trace  src: ResourceStr--><!--Device-ToolBarV2ItemImage-@Trace  src: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

