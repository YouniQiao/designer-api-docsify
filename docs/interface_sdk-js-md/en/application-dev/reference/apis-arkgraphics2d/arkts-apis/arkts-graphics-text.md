# @ohos.graphics.text

The Text module provides a set of APIs for text layout and font management. It aims to deliver high-quality typesetting through features like character-to-glyph conversion, kerning, line breaking, alignment, and text measurement. Additionally, it provides font management capabilities, including font registration, font descriptors, and font collection management. This module provides the following classes for creating complex text paragraphs: - [TextStyle](arkts-arkgraphics2d-text-textstyle-i.md): defines the font type, size, spacing, and other text properties. - [FontCollection](arkts-arkgraphics2d-text-fontcollection-c.md): manages a collection of different fonts. - [FontDescriptor](arkts-arkgraphics2d-text-fontdescriptor-i.md): provides information about font descriptors. - [ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md): controls line break and word break strategies for the entire paragraph. - [ParagraphBuilder](arkts-arkgraphics2d-text-paragraphbuilder-c.md): used to create different paragraph objects. - [Paragraph](arkts-arkgraphics2d-text-paragraph-c.md): created by calling [build()](arkts-arkgraphics2d-text-paragraphbuilder-c.md#build) of the **ParagraphBuilder** class. - [LineTypeset](arkts-arkgraphics2d-text-linetypeset-c.md): created by calling [buildLineTypeset()](arkts-arkgraphics2d-text-paragraphbuilder-c.md#buildlinetypeset) of the **ParagraphBuilder** class. - [TextLine](arkts-arkgraphics2d-text-textline-c.md): paragraph text on a line-by-line basis, obtained by calling [getTextLines()](arkts-arkgraphics2d-text-paragraph-c.md#gettextlines) of the **Paragraph** class. - [Run](arkts-arkgraphics2d-text-run-c.md): text typesetting unit, obtained by calling [getGlyphRuns()](arkts-arkgraphics2d-text-textline-c.md#getglyphruns) of the **TextLine** class.

**Since:** 23

<!--Device-unnamed-declare namespace text--><!--Device-unnamed-declare namespace text-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { text } from '@kit.ArkGraphics2D';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getFontCount](arkts-arkgraphics2d-text-getfontcount-f.md) | Obtains the number of font files contained in a font file based on the font file path. Returns **0** if the font file is not found, the font file path is invalid, the font file does not have the required permission, or the file is not in the font format. |
| [getFontDescriptorByFullName](arkts-arkgraphics2d-text-getfontdescriptorbyfullname-f.md) | Obtains the font descriptor based on the font name and type. This API uses a promise to return the result. A font descriptor is a data structure that describes font features. It contains details of the font appearance and properties. |
| [getFontDescriptorsFromPath](arkts-arkgraphics2d-text-getfontdescriptorsfrompath-f.md) | Obtains an array of font descriptors by font file path. This API uses a promise to return the result. &gt; **NOTE：**&gt; &gt; - An empty array is returned if the font file is not found, the font file path is invalid, the font file does not &gt; have the required permission, or the file is not in the font format. &gt; &gt; - The **weight** field in [FontDescriptor](arkts-arkgraphics2d-text-fontdescriptor-i.md) does not exactly correspond to the weight &gt; value in the font file. Instead, the actual weight value in the font file is rounded off and mapped to the &gt; [FontWeight](arkts-arkgraphics2d-text-fontweight-e.md) enum value. For example, the weight value 350 in the font file is mapped to 4 &gt; 00, and the corresponding enum value is W400. |
| [getFontPathsByType](arkts-arkgraphics2d-text-getfontpathsbytype-f.md) | Obtains the paths of all font files of a specified font type. |
| [getFontUnicodeSet](arkts-arkgraphics2d-text-getfontunicodeset-f.md) | Obtains an array of font Unicode by font file path. This API uses a promise to return the result. An empty array is returned if the font file is not found, the font file path is invalid, the font file does not have the required permission, or the file is not in the font format. |
| [getSystemFontFullNamesByType](arkts-arkgraphics2d-text-getsystemfontfullnamesbytype-f.md) | Obtains the full names of all fonts of the specified type. This API uses a promise to return the result. |
| [isFontSupported](arkts-arkgraphics2d-text-isfontsupported-f.md) | Checks whether the system supports the specified font file. You can use this API to verify the availability of a font file before loading a custom font, preventing text rendering exceptions caused by unsupported fonts. |
| [matchFontDescriptors](arkts-arkgraphics2d-text-matchfontdescriptors-f.md) | Obtains all system font descriptors that match the provided font descriptor. This API uses a promise to return the result. |
| [setTextHighContrast](arkts-arkgraphics2d-text-settexthighcontrast-f.md) | Sets the high contrast mode for text rendering. The setting of this API takes effect for the entire process, and all pages in the process share the same mode. You can call this API to set the high contrast mode, or enable or disable the high contrast mode by toggling the switch on the system settings screen. This API is used to set the high contrast mode for text rendering. The setting of this API takes precedence over the one based on system settings. This API does not take effect for text drawn by the app through APIs such as Canvas. It only takes effect for text rendered using system text components. |
| [setTextUndefinedGlyphDisplay](arkts-arkgraphics2d-text-settextundefinedglyphdisplay-f.md) | Sets the glyph type to be used when characters are mapped to the .notdef (undefined) glyph. After this API is called, any subsequently rendered text containing undefined glyphs will be displayed according to this setting. This setting affects how to display undefined characters in the font: - The default behavior follows the .notdef glyph design of the font. - After this feature is enabled, characters without glyphs are displayed as a tofu block. |

### Classes

| Name | Description |
| --- | --- |
| [FontCollection](arkts-arkgraphics2d-text-fontcollection-c.md) | Represents a font collection, which manages the font resources required for text typesetting. FontCollection provides font matching and glyph lookup capabilities for [ParagraphBuilder](arkts-arkgraphics2d-text-paragraphbuilder-c.md), and serves as a fundamental component of the text typesetting pipeline. It provides a global instance ( [getGlobalInstance](arkts-arkgraphics2d-text-fontcollection-c.md#getglobalinstance)) and local instances ( [getLocalInstance](arkts-arkgraphics2d-text-fontcollection-c.md#getlocalinstance)). Fonts loaded by the global instance are shared within the app, making it suitable for common app scenarios. Local instances are independent of each other, and fonts loaded by a local instance take effect only for that instance without affecting others, making them recommended for widget scenarios. Custom fonts can be loaded through [loadFontSync](arkts-arkgraphics2d-text-fontcollection-c.md#loadfontsync) or [loadFont](arkts-arkgraphics2d-text-fontcollection-c.md#loadfont). |
| [LineTypeset](arkts-arkgraphics2d-text-linetypeset-c.md) | Implements a carrier that stores the text content and style. It can be used to compute layout details for individual lines of text. Before calling any of the following APIs, you must use [buildLineTypeset()](arkts-arkgraphics2d-text-paragraphbuilder-c.md#buildlinetypeset) in the [ParagraphBuilder](arkts-arkgraphics2d-text-paragraphbuilder-c.md) class to create a **LineTypeset** object. |
| [Paragraph](arkts-arkgraphics2d-text-paragraph-c.md) | Implements a carrier that stores the text content and style. You can perform operations such as layout and drawing. Before calling any of the following APIs, you must use [build()](arkts-arkgraphics2d-text-paragraphbuilder-c.md#build) of the [ParagraphBuilder](arkts-arkgraphics2d-text-paragraphbuilder-c.md) class to create a **Paragraph** object. |
| [ParagraphBuilder](arkts-arkgraphics2d-text-paragraphbuilder-c.md) | Implements a paragraph builder that uses the builder pattern to construct paragraph objects. Developers initialize ParagraphBuilder by passing [ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md) and [FontCollection](arkts-arkgraphics2d-text-fontcollection-c.md) to the constructor, then set the text style through [pushStyle](arkts-arkgraphics2d-text-paragraphbuilder-c.md#pushstyle), add text content through [addText](arkts-arkgraphics2d-text-paragraphbuilder-c.md#addtext), and finally call [build()](arkts-arkgraphics2d-text-paragraphbuilder-c.md#build) to generate a [Paragraph](arkts-arkgraphics2d-text-paragraph-c.md) object for typesetting and drawing. |
| [Run](arkts-arkgraphics2d-text-run-c.md) | Represents a text typesetting unit, which is a continuous text segment with the same style attributes. Run is obtained through the [getGlyphRuns()](arkts-arkgraphics2d-text-textline-c.md#getglyphruns) API of the [TextLine](arkts-arkgraphics2d-text-textline-c.md) class. Before calling any of the following APIs, you must use [getGlyphRuns()](arkts-arkgraphics2d-text-textline-c.md#getglyphruns) of the [TextLine](arkts-arkgraphics2d-text-textline-c.md) class to create a **Run** object. |
| [TextLine](arkts-arkgraphics2d-text-textline-c.md) | Implements a carrier that describes the basic text line structure of a paragraph. Before calling any of the following APIs, you must use [getTextLines()](arkts-arkgraphics2d-text-paragraph-c.md#gettextlines) of the [Paragraph](arkts-arkgraphics2d-text-paragraph-c.md) class or [createLine()](arkts-arkgraphics2d-text-linetypeset-c.md#createline) of the [LineTypeset](arkts-arkgraphics2d-text-linetypeset-c.md) class to create a **TextLine** object. |

### Interfaces

| Name | Description |
| --- | --- |
| [Decoration](arkts-arkgraphics2d-text-decoration-i.md) | Describes a text decoration. |
| [FontDescriptor](arkts-arkgraphics2d-text-fontdescriptor-i.md) | Describes the font descriptor information. |
| [FontFeature](arkts-arkgraphics2d-text-fontfeature-i.md) | Describes a font feature. |
| [FontVariation](arkts-arkgraphics2d-text-fontvariation-i.md) | Describes a font variation. |
| [FontVariationAxis](arkts-arkgraphics2d-text-fontvariationaxis-i.md) | Represents the font variable axis information. |
| [FontVariationInstance](arkts-arkgraphics2d-text-fontvariationinstance-i.md) | Font variable instance information, which stores preset variable font style information. |
| [LineMetrics](arkts-arkgraphics2d-text-linemetrics-i.md) | Describes the measurement information of a single line of text in the text layout. |
| [ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md) | Represents a paragraph style, which controls the overall layout behavior of a paragraph, including attributes such as alignment, line break strategy, and maximum number of lines. ParagraphStyle serves as a required parameter of the [ParagraphBuilder](arkts-arkgraphics2d-text-paragraphbuilder-c.md) constructor, and works together with [TextStyle](arkts-arkgraphics2d-text-textstyle-i.md) (which controls text-level styles) to determine the final typesetting result of the paragraph. |
| [PlaceholderSpan](arkts-arkgraphics2d-text-placeholderspan-i.md) | Describes the placeholder style. |
| [PositionWithAffinity](arkts-arkgraphics2d-text-positionwithaffinity-i.md) | Describes the position and affinity of a glyph. |
| [Range](arkts-arkgraphics2d-text-range-i.md) | Describes a left-closed and right-open interval. |
| [RectStyle](arkts-arkgraphics2d-text-rectstyle-i.md) | Describes the style of a rectangle. |
| [RunMetrics](arkts-arkgraphics2d-text-runmetrics-i.md) | Describes the layout information and measurement information of a run of text in a text line. |
| [StrutStyle](arkts-arkgraphics2d-text-strutstyle-i.md) | Describes the strut style, which determines the line spacing, baseline alignment mode, and other properties related to the line height when drawing texts. The strut style is disabled by default. |
| [TextBox](arkts-arkgraphics2d-text-textbox-i.md) | Rectangular area of the text, indicating the rectangular space occupied by the text during layout. |
| [TextLayoutResult](arkts-arkgraphics2d-text-textlayoutresult-i.md) | Represents the text layout result. |
| [TextRectSize](arkts-arkgraphics2d-text-textrectsize-i.md) | Represents the text rectangle size, which is used to describe the width and height of the text rectangle. It is a floating-point value in physical pixels (px). |
| [TextShadow](arkts-arkgraphics2d-text-textshadow-i.md) | Represents a text shadow. |
| [TextStyle](arkts-arkgraphics2d-text-textstyle-i.md) | Represents a text style, which controls the visual appearance attributes of text, including font, color, font size, spacing, decoration lines, and shadows. TextStyle is applied to subsequently added text content through the [pushStyle](arkts-arkgraphics2d-text-paragraphbuilder-c.md#pushstyle) method of [ParagraphBuilder](arkts-arkgraphics2d-text-paragraphbuilder-c.md), and works together with [ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md) (which controls paragraph-level attributes). Within the same paragraph, you can call pushStyle multiple times to apply different styles to different text segments. |
| [TextTab](arkts-arkgraphics2d-text-texttab-i.md) | Implements a paragraph-style text tab, which stores the alignment mode and position. |
| [TypographicBounds](arkts-arkgraphics2d-text-typographicbounds-i.md) | Describes the typographic boundaries of a text line. These boundaries depend on the typographic font and font size, but not on the characters themselves. For example, for the string " a b " (which has a space before "a" and a space after "b"), the typographic boundaries include the spaces at the beginning and end of the line. Similarly, the strings "j" and "E" have identical typographic boundaries, independent of the characters themselves. &gt; **NOTE：**&gt; &gt; The figure shows the text line typesetting parameters: width (the width of the text line including left and right &gt; spaces), ascent (the highest point of the ascent), descent (the lowest point of the descent), leading (line &gt; spacing), top (the highest point of the current line), baseline (the character baseline), bottom (the lowest &gt; point of the current line), and next line top (the highest point of the next line). &gt; &gt;  &gt; &gt; The figure shows the typesetting boundaries for the string " a b ". &gt; &gt;  &gt; &gt; The figure shows the typesetting boundaries for the string "j" or "E". &gt; &gt; ! &gt; [TypographicBounds-Character.png](../../../reference/apis-arkgraphics2d/figures/TypographicBounds-Character.png) |

### Enums

| Name | Description |
| --- | --- |
| [Affinity](arkts-arkgraphics2d-text-affinity-e.md) | Enumerates the affinity modes. |
| [BreakStrategy](arkts-arkgraphics2d-text-breakstrategy-e.md) | Enumerates the text break strategies. |
| [EllipsisMode](arkts-arkgraphics2d-text-ellipsismode-e.md) | Enumerates the ellipsis styles. **EllipsisMode.START** and **EllipsisMode.MIDDLE** take effect only when text overflows in a single line. |
| [FontStyle](arkts-arkgraphics2d-text-fontstyle-e.md) | Enumerates the font styles. |
| [FontWeight](arkts-arkgraphics2d-text-fontweight-e.md) | Enumerates the font weights. |
| [FontWidth](arkts-arkgraphics2d-text-fontwidth-e.md) | Enumerates the font widths. |
| [LineHeightStyle](arkts-arkgraphics2d-text-lineheightstyle-e.md) | Enumerates the line height scaling base. |
| [PlaceholderAlignment](arkts-arkgraphics2d-text-placeholderalignment-e.md) | Enumerates the vertical alignment modes of a placeholder relative to the surrounding text.  &gt; **NOTE：**&gt; &gt; The figure shows the last three alignment modes. The first three alignment modes are similar in text baseline &gt; alignment, with the comparison reference being the text baseline, indicated by the green line. &gt; &gt;  |
| [RectHeightStyle](arkts-arkgraphics2d-text-rectheightstyle-e.md) | Enumerates the rectangle height styles. |
| [RectWidthStyle](arkts-arkgraphics2d-text-rectwidthstyle-e.md) | Enumerates the rectangle width styles. |
| [SystemFontType](arkts-arkgraphics2d-text-systemfonttype-e.md) | Enumerates the font types, which can be combined through bitwise OR operations. |
| [TextAlign](arkts-arkgraphics2d-text-textalign-e.md) | Enumerates the text alignment modes. |
| [TextBadgeType](arkts-arkgraphics2d-text-textbadgetype-e.md) | Enumerates the text badges. |
| [TextBaseline](arkts-arkgraphics2d-text-textbaseline-e.md) | Enumerates the text baseline types. |
| [TextDecorationStyle](arkts-arkgraphics2d-text-textdecorationstyle-e.md) | Enumerates the text decoration styles. |
| [TextDecorationType](arkts-arkgraphics2d-text-textdecorationtype-e.md) | Enumerates the text decoration types. |
| [TextDirection](arkts-arkgraphics2d-text-textdirection-e.md) | Enumerates the text directions. |
| [TextDisplayState](arkts-arkgraphics2d-text-textdisplaystate-e.md) | Enumerates text display states. Native result after text typesetting, which is irrelevant to external display factors such as external canvas cropping and screen overflow. |
| [TextHeightBehavior](arkts-arkgraphics2d-text-textheightbehavior-e.md) | Enumerates the text height modifier patterns. |
| [TextHighContrast](arkts-arkgraphics2d-text-texthighcontrast-e.md) | Enumerates the high contrast types for text rendering. |
| [TextProcessState](arkts-arkgraphics2d-text-textprocessstate-e.md) | Enumerates text processing states. |
| [TextUndefinedGlyphDisplay](arkts-arkgraphics2d-text-textundefinedglyphdisplay-e.md) | Enumerates the modes for displaying undefined text glyphs. |
| [TextVerticalAlign](arkts-arkgraphics2d-text-textverticalalign-e.md) | Enumerates the vertical alignment modes of text. |
| [WordBreak](arkts-arkgraphics2d-text-wordbreak-e.md) | Enumerates the word break types. |

### Types

| Name | Description |
| --- | --- |
| [CaretOffsetsCallback](arkts-arkgraphics2d-text-caretoffsetscallback-t.md) | Defines the callback used to receive the offset and index of each character in a text line object as its parameters. |

