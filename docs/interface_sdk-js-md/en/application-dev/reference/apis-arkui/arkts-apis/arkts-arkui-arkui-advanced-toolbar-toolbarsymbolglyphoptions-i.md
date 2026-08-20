# ToolBarSymbolGlyphOptions

Defines the icon symbol options.

**Since:** 13

<!--Device-unnamed-export interface ToolBarSymbolGlyphOptions--><!--Device-unnamed-export interface ToolBarSymbolGlyphOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ItemState, ToolBar, ToolBarOption, ToolBarOptions, ToolBarModifier } from '@kit.ArkUI';
import { ToolBarV2ItemState, ToolBarV2SymbolGlyph, ToolBarV2SymbolGlyphOptions, ToolBarV2ItemText, ToolBarV2ItemTextOptions, ToolBarV2ItemIconType, ToolBarV2ItemImage, ToolBarV2ItemImageOptions, ToolBarV2, ToolBarV2Item, ToolBarV2ItemOptions, ToolBarV2Modifier, ToolBarV2ItemAction } from '@kit.ArkUI';
```

## activated

```TypeScript
activated?: SymbolGlyphModifier
```

Icon symbol of the toolbar item in activated state.

Default value: **fontColor: \$r('sys.color.icon_emphasize'), fontSize: 24vp**

**Type:** SymbolGlyphModifier

**Since:** 13

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-ToolBarSymbolGlyphOptions-activated?: SymbolGlyphModifier--><!--Device-ToolBarSymbolGlyphOptions-activated?: SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## normal

```TypeScript
normal?: SymbolGlyphModifier
```

Icon symbol of the toolbar item in normal state.

Default value: **fontColor: \$r('sys.color.icon_primary'), fontSize: 24vp**

**Type:** SymbolGlyphModifier

**Since:** 13

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

<!--Device-ToolBarSymbolGlyphOptions-normal?: SymbolGlyphModifier--><!--Device-ToolBarSymbolGlyphOptions-normal?: SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

