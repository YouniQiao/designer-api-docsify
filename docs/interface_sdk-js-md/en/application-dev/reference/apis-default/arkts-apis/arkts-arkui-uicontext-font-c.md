# Font

class Font

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class Font--><!--Device-unnamed-export declare class Font-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## getFontByName

```TypeScript
getFontByName(fontName: string): font.FontInfo
```

Get font details according to the font name.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Font-getFontByName(fontName: string): font.FontInfo--><!--Device-Font-getFontByName(fontName: string): font.FontInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fontName | string | Yes | font name |

**Return value:**

| Type | Description |
| --- | --- |
| font.FontInfo | Returns the font info |

## getSystemFontList

```TypeScript
getSystemFontList(): Array<string>
```

Gets a list of fonts supported by system.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Font-getSystemFontList(): Array<string>--><!--Device-Font-getSystemFontList(): Array<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | A list of font names |

## registerFont

```TypeScript
registerFont(options: font.FontOptions): void
```

Register a customized font in the FontManager.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Font-registerFont(options: font.FontOptions): void--><!--Device-Font-registerFont(options: font.FontOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | font.FontOptions | Yes | FontOptions |

