# setTextUndefinedGlyphDisplay

## Modules to Import

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## setTextUndefinedGlyphDisplay

```TypeScript
function setTextUndefinedGlyphDisplay(noGlyphShow: TextUndefinedGlyphDisplay): void
```

Sets the glyph type to be used when characters are mapped to the .notdef (undefined) glyph.After this API is called, any subsequently rendered text containing undefined glyphs will be displayed according to this setting.This setting affects how to display undefined characters in the font:  
- The default behavior follows the .notdef glyph design of the font.  
- After this feature is enabled, characters without glyphs are displayed as a tofu block.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| noGlyphShow | [TextUndefinedGlyphDisplay](arkts-arkgraphics2d-text-textundefinedglyphdisplay-e.md) | Yes |
