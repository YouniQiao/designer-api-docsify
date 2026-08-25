# @ohos.graphics.text

The Text module provides a set of APIs for text layout and font management. It aims to deliver high-quality typesetting through features like character-to-glyph conversion, kerning, line breaking, alignment, and text measurement. Additionally, it provides font management capabilities, including font registration, font descriptors, and font collection management.This module provides the following classes for creating complex text paragraphs:  
- [TextStyle](arkts-arkgraphics2d-text-textstyle-i.md): defines the font type, size, spacing, and other text properties.  
- [FontCollection](arkts-arkgraphics2d-text-fontcollection-c.md): manages a collection of different fonts.  
- [FontDescriptor](arkts-arkgraphics2d-text-fontdescriptor-i.md): provides information about font descriptors.  
- [ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md): controls line break and word break strategies for the entire  
paragraph.  
- [ParagraphBuilder](arkts-arkgraphics2d-text-paragraphbuilder-c.md): used to create different paragraph objects.  
- [Paragraph](arkts-arkgraphics2d-text-paragraph-c.md): created by calling [build()](arkts-arkgraphics2d-text-paragraphbuilder-c.md#build) of the  
**ParagraphBuilder** class.  
- [LineTypeset](arkts-arkgraphics2d-text-linetypeset-c.md): created by calling  
[buildLineTypeset()](arkts-arkgraphics2d-text-paragraphbuilder-c.md#buildlinetypeset) of the **ParagraphBuilder** class.  
- [TextLine](arkts-arkgraphics2d-text-textline-c.md): paragraph text on a line-by-line basis, obtained by calling  
[getTextLines()](arkts-arkgraphics2d-text-paragraph-c.md#gettextlines) of the **Paragraph** class.  
- [Run](arkts-arkgraphics2d-text-run-c.md): text typesetting unit, obtained by calling  
[getGlyphRuns()](arkts-arkgraphics2d-text-textline-c.md#getglyphruns) of the **TextLine** class.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getFontCount](arkts-arkgraphics2d-text-getfontcount-f.md) |
| [getFontDescriptorByFullName](arkts-arkgraphics2d-text-getfontdescriptorbyfullname-f.md) |
| [getFontDescriptorsFromPath](arkts-arkgraphics2d-text-getfontdescriptorsfrompath-f.md) |
| [getFontPathsByType](arkts-arkgraphics2d-text-getfontpathsbytype-f.md) |
| [getFontUnicodeSet](arkts-arkgraphics2d-text-getfontunicodeset-f.md) |
| [getSystemFontFullNamesByType](arkts-arkgraphics2d-text-getsystemfontfullnamesbytype-f.md) |
| [isFontSupported](arkts-arkgraphics2d-text-isfontsupported-f.md) |
| [matchFontDescriptors](arkts-arkgraphics2d-text-matchfontdescriptors-f.md) |
| [setTextHighContrast](arkts-arkgraphics2d-text-settexthighcontrast-f.md) |
| [setTextUndefinedGlyphDisplay](arkts-arkgraphics2d-text-settextundefinedglyphdisplay-f.md) |

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FontCollection](arkts-arkgraphics2d-text-fontcollection-c.md) |
| [LineTypeset](arkts-arkgraphics2d-text-linetypeset-c.md) |
| [Paragraph](arkts-arkgraphics2d-text-paragraph-c.md) |
| [ParagraphBuilder](arkts-arkgraphics2d-text-paragraphbuilder-c.md) |
| [Run](arkts-arkgraphics2d-text-run-c.md) |
| [TextLine](arkts-arkgraphics2d-text-textline-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Decoration](arkts-arkgraphics2d-text-decoration-i.md) |
| [FontDescriptor](arkts-arkgraphics2d-text-fontdescriptor-i.md) |
| [FontFeature](arkts-arkgraphics2d-text-fontfeature-i.md) |
| [FontVariation](arkts-arkgraphics2d-text-fontvariation-i.md) |
| [FontVariationAxis](arkts-arkgraphics2d-text-fontvariationaxis-i.md) |
| [FontVariationInstance](arkts-arkgraphics2d-text-fontvariationinstance-i.md) |
| [LineMetrics](arkts-arkgraphics2d-text-linemetrics-i.md) |
| [ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md) |
| [PlaceholderSpan](arkts-arkgraphics2d-text-placeholderspan-i.md) |
| [PositionWithAffinity](arkts-arkgraphics2d-text-positionwithaffinity-i.md) |
| [Range](arkts-arkgraphics2d-text-range-i.md) |
| [RectStyle](arkts-arkgraphics2d-text-rectstyle-i.md) |
| [RunMetrics](arkts-arkgraphics2d-text-runmetrics-i.md) |
| [StrutStyle](arkts-arkgraphics2d-text-strutstyle-i.md) |
| [TextBox](arkts-arkgraphics2d-text-textbox-i.md) |
| [TextLayoutResult](arkts-arkgraphics2d-text-textlayoutresult-i.md) |
| [TextRectSize](arkts-arkgraphics2d-text-textrectsize-i.md) |
| [TextShadow](arkts-arkgraphics2d-text-textshadow-i.md) |
| [TextStyle](arkts-arkgraphics2d-text-textstyle-i.md) |
| [TextTab](arkts-arkgraphics2d-text-texttab-i.md) |
| [TypographicBounds](arkts-arkgraphics2d-text-typographicbounds-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Affinity](arkts-arkgraphics2d-text-affinity-e.md) |
| [BreakStrategy](arkts-arkgraphics2d-text-breakstrategy-e.md) |
| [EllipsisMode](arkts-arkgraphics2d-text-ellipsismode-e.md) |
| [FontStyle](arkts-arkgraphics2d-text-fontstyle-e.md) |
| [FontWeight](arkts-arkgraphics2d-text-fontweight-e.md) |
| [FontWidth](arkts-arkgraphics2d-text-fontwidth-e.md) |
| [LineHeightStyle](arkts-arkgraphics2d-text-lineheightstyle-e.md) |
| [PlaceholderAlignment](arkts-arkgraphics2d-text-placeholderalignment-e.md) |
| [RectHeightStyle](arkts-arkgraphics2d-text-rectheightstyle-e.md) |
| [RectWidthStyle](arkts-arkgraphics2d-text-rectwidthstyle-e.md) |
| [SystemFontType](arkts-arkgraphics2d-text-systemfonttype-e.md) |
| [TextAlign](arkts-arkgraphics2d-text-textalign-e.md) |
| [TextBadgeType](arkts-arkgraphics2d-text-textbadgetype-e.md) |
| [TextBaseline](arkts-arkgraphics2d-text-textbaseline-e.md) |
| [TextDecorationStyle](arkts-arkgraphics2d-text-textdecorationstyle-e.md) |
| [TextDecorationType](arkts-arkgraphics2d-text-textdecorationtype-e.md) |
| [TextDirection](arkts-arkgraphics2d-text-textdirection-e.md) |
| [TextDisplayState](arkts-arkgraphics2d-text-textdisplaystate-e.md) |
| [TextHeightBehavior](arkts-arkgraphics2d-text-textheightbehavior-e.md) |
| [TextHighContrast](arkts-arkgraphics2d-text-texthighcontrast-e.md) |
| [TextProcessState](arkts-arkgraphics2d-text-textprocessstate-e.md) |
| [TextUndefinedGlyphDisplay](arkts-arkgraphics2d-text-textundefinedglyphdisplay-e.md) |
| [TextVerticalAlign](arkts-arkgraphics2d-text-textverticalalign-e.md) |
| [WordBreak](arkts-arkgraphics2d-text-wordbreak-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CaretOffsetsCallback](arkts-arkgraphics2d-text-caretoffsetscallback-t.md) |
