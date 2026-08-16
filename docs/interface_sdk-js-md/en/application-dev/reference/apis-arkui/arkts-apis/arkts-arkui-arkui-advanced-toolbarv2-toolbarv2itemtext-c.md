# ToolBarV2ItemText

Declare type ToolBarV2ItemText

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

<!--Device-unnamed-export declare class ToolBarV2ItemText--><!--Device-unnamed-export declare class ToolBarV2ItemText-End-->

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
constructor(options: ToolBarV2ItemTextOptions)
```

The constructor used to create a ToolBarV2ItemText object.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ToolBarV2ItemText-constructor(options: ToolBarV2ItemTextOptions)--><!--Device-ToolBarV2ItemText-constructor(options: ToolBarV2ItemTextOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ToolBarV2ItemTextOptions](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2itemtextoptions-i.md) | Yes | text info. |

## activatedColor

```TypeScript
@Trace
  activatedColor?: ColorMetrics
```

Text fontColor when the item is activated.

**Type:** [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

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

**Type:** [ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

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

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ToolBarV2ItemText-@Trace  text: ResourceStr--><!--Device-ToolBarV2ItemText-@Trace  text: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

