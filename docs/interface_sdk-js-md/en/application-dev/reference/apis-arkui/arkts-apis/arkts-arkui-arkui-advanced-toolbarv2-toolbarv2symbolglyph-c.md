# ToolBarV2SymbolGlyph

Defines toolBarV2 symbolGlyph.

**Since:** 18

<!--Device-unnamed-export class ToolBarV2SymbolGlyph--><!--Device-unnamed-export class ToolBarV2SymbolGlyph-End-->

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
constructor(options: ToolBarV2SymbolGlyphOptions)
```

The constructor used to create a ToolBarV2SymbolGlyph object.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ToolBarV2SymbolGlyph-constructor(options: ToolBarV2SymbolGlyphOptions)--><!--Device-ToolBarV2SymbolGlyph-constructor(options: ToolBarV2SymbolGlyphOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ToolBarV2SymbolGlyphOptions](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2symbolglyphoptions-i.md) | Yes | symbol info. |

## activated

```TypeScript
@Trace
  activated?: SymbolGlyphModifier
```

Modifier of toolbarV2's activated symbol.

**Type:** SymbolGlyphModifier

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ToolBarV2SymbolGlyph-@Trace  activated?: SymbolGlyphModifier--><!--Device-ToolBarV2SymbolGlyph-@Trace  activated?: SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## normal

```TypeScript
@Trace
  normal: SymbolGlyphModifier
```

Modifier of toolbarV2's normal symbol.

**Type:** SymbolGlyphModifier

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ToolBarV2SymbolGlyph-@Trace  normal: SymbolGlyphModifier--><!--Device-ToolBarV2SymbolGlyph-@Trace  normal: SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

