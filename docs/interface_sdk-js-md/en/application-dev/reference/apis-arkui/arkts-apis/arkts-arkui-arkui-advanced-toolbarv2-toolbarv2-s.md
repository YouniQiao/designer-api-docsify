# ToolBarV2

Declare Component ToolBarV2

**Since:** 18

<!--Device-unnamed-export declare struct ToolBarV2--><!--Device-unnamed-export declare struct ToolBarV2-End-->

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

## activatedIndex

```TypeScript
@Param
  activatedIndex?: number
```

Define toolbarV2 activate item index, default is -1.

**Type:** number

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ToolBarV2-@Param  activatedIndex?: number--><!--Device-ToolBarV2-@Param  activatedIndex?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dividerModifier

```TypeScript
@Param
  dividerModifier?: DividerModifier
```

Define divider Modifier.

**Type:** [DividerModifier](arkts-arkui-dividermodifier-c.md)

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ToolBarV2-@Param  dividerModifier?: DividerModifier--><!--Device-ToolBarV2-@Param  dividerModifier?: DividerModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## toolBarList

```TypeScript
@Require
  @Param
  toolBarList: ToolBarV2Item[]
```

Define toolbarV2 item list.

**Type:** [ToolBarV2Item](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2item-c.md)[]

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ToolBarV2-@Require  @Param  toolBarList: ToolBarV2Item[]--><!--Device-ToolBarV2-@Require  @Param  toolBarList: ToolBarV2Item[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## toolBarModifier

```TypeScript
@Param
  toolBarModifier?: ToolBarV2Modifier
```

Define toolbarV2 modifier.

**Type:** [ToolBarV2Modifier](arkts-arkui-arkui-advanced-toolbarv2-toolbarv2modifier-c.md)

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ToolBarV2-@Param  toolBarModifier?: ToolBarV2Modifier--><!--Device-ToolBarV2-@Param  toolBarModifier?: ToolBarV2Modifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

