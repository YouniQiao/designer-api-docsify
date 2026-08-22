# ToolBarV2SymbolGlyph

Defines the icon symbol options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class ToolBarV2SymbolGlyph--><!--Device-unnamed-export declare class ToolBarV2SymbolGlyph-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor(options: ToolBarV2SymbolGlyphOptions)
```

A constructor used to create a **ToolBarV2SymbolGlyph** object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarV2SymbolGlyph-constructor(options: ToolBarV2SymbolGlyphOptions)--><!--Device-ToolBarV2SymbolGlyph-constructor(options: ToolBarV2SymbolGlyphOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ToolBarV2SymbolGlyphOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-toolbarv2-toolbarv2symbolglyphoptions-i.md) | Yes | symbol info. |

## activated

```TypeScript
@Trace
  public activated?: SymbolGlyphModifier
```

Icon symbol of the toolbar item in activated state.

Default value:

**fontColor**: **\$r('sys.color.icon_emphasize')**, **fontSize**: **24vp**

Decorator: @Trace

**Type:** [SymbolGlyphModifier](../../apis-arkui/arkts-apis/arkts-arkui-symbolglyphmodifier-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarV2SymbolGlyph-@Trace  public activated?: SymbolGlyphModifier--><!--Device-ToolBarV2SymbolGlyph-@Trace  public activated?: SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## normal

```TypeScript
@Trace
  public normal: SymbolGlyphModifier
```

Icon symbol of the toolbar item in normal state.

Decorator: @Trace

**Type:** [SymbolGlyphModifier](../../apis-arkui/arkts-apis/arkts-arkui-symbolglyphmodifier-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarV2SymbolGlyph-@Trace  public normal: SymbolGlyphModifier--><!--Device-ToolBarV2SymbolGlyph-@Trace  public normal: SymbolGlyphModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

