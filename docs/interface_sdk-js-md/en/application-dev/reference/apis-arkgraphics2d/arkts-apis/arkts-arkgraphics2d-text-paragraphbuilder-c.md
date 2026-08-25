# ParagraphBuilder

Implements a paragraph builder that uses the builder pattern to construct paragraph objects. Developers initialize ParagraphBuilder by passing [ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md) and [FontCollection](arkts-arkgraphics2d-text-fontcollection-c.md) to the constructor, then set the text style through [pushStyle](#pushstyle), add text content through [addText](#addtext), and finally call [build()](#build) to generate a [Paragraph](arkts-arkgraphics2d-text-paragraph-c.md) object for typesetting and drawing.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## addPlaceholder

```TypeScript
addPlaceholder(placeholderSpan: PlaceholderSpan): void
```

Inserts a placeholder when building a text paragraph. After insertion, the placeholder occupies the corresponding space in paragraph typesetting according to the specified width, height, and alignment, and affects text line breaking and layout.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| placeholderSpan | [PlaceholderSpan](arkts-arkgraphics2d-text-placeholderspan-i.md) | Yes |

## addSymbol

```TypeScript
addSymbol(symbolId: number): void
```

Inserts a symbol into the paragraph being built.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| symbolId | number | Yes |

## addText

```TypeScript
addText(text: string): void
```

Inserts a text string into the paragraph being built.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [text](arkts-graphics-text.md) | string | Yes |

## build

```TypeScript
build(): Paragraph
```

Builds a paragraph and generates a paragraph object that can be used for subsequent typesetting and rendering. After build() is called, a new ParagraphBuilder instance must be created to build text again.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Paragraph](../../apis-arkui/arkts-apis/arkts-arkui-paragraph-t.md) |

## buildLineTypeset

```TypeScript
buildLineTypeset(): LineTypeset
```

Builds a line typesetter and generates a LineTypeset object that can be used for line-by-line typesetting calculation.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [LineTypeset](arkts-arkgraphics2d-text-linetypeset-c.md) |

## constructor

```TypeScript
constructor(paragraphStyle: ParagraphStyle, fontCollection: FontCollection)
```

A constructor used to create a **ParagraphBuilder** object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| paragraphStyle | [ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md) | Yes |
| fontCollection | [FontCollection](arkts-arkgraphics2d-text-fontcollection-c.md) | Yes |

## popStyle

```TypeScript
popStyle(): void
```

Restores the previous text style.

> **NOTE：**&gt;
> This method must be called after [pushStyle()](#pushstyle). After it is called,
> subsequently added text will use the text style before the pop operation. If the style stack is empty, the
> textStyle in [ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md) will be used as the default style.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

## pushStyle

```TypeScript
pushStyle(textStyle: TextStyle): void
```

Applies a new style to the current text blob.

> **NOTE：**&gt;
> When you update the style of the current text blob, all text added afterward will use this new style.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| textStyle | [TextStyle](arkts-arkgraphics2d-text-textstyle-i.md) | Yes |
