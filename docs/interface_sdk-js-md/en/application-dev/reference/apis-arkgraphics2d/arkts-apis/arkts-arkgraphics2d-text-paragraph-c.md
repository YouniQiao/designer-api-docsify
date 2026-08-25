# Paragraph

Implements a carrier that stores the text content and style. You can perform operations such as layout and drawing.Before calling any of the following APIs, you must use [build()](arkts-arkgraphics2d-text-paragraphbuilder-c.md#build) of the [ParagraphBuilder](arkts-arkgraphics2d-text-paragraphbuilder-c.md) class to create a **Paragraph** object.

**Since:** 12

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## didExceedMaxLines

```TypeScript
didExceedMaxLines(): boolean
```

Checks whether the number of lines in the paragraph exceeds the maximum.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## forceReuseRasterResult

```TypeScript
forceReuseRasterResult(isForce: boolean): void
```

Sets whether to force reuse of the rasterization result. If this API is not called, the system allows updating the rasterization result by default.This API is suitable for scenarios where the text content remains unchanged but [paint](#paint) needs to be called multiple times for drawing. By reusing the rasterization result, repeated rasterization calculations can be avoided to improve drawing performance. After this setting is applied, it takes effect the next time [paint](#paint) is called for drawing.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isForce | boolean | Yes |

## getActualTextRange

```TypeScript
getActualTextRange(lineNumber: number, includeSpaces: boolean): Range
```

Obtains the actually visible text range in the specified line, excluding any overflow ellipsis.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [lineNumber](arkts-arkgraphics2d-text-linemetrics-i.md) | number | Yes |
| includeSpaces | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) |

## getAlphabeticBaseline

```TypeScript
getAlphabeticBaseline(): number
```

Obtains the alphabetic baseline.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getCharacterPositionAtCoordinate

```TypeScript
getCharacterPositionAtCoordinate(x: number, y: number, encoding: drawing.TextEncoding): PositionWithAffinity
```

Obtains the character position information closest to the given coordinates.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |
| encoding | drawing.TextEncoding | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PositionWithAffinity](../../apis-arkui/arkts-apis/arkts-arkui-positionwithaffinity-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) |

## getCharacterRangeForGlyphRange

```TypeScript
getCharacterRangeForGlyphRange(glyphRange: Range, encoding: drawing.TextEncoding): Array<Range>
```

Obtains the character range corresponding to the specified glyph range.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| glyphRange | [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes |
| encoding | drawing.TextEncoding | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;Range & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) |

## getGlyphPositionAtCoordinate

```TypeScript
getGlyphPositionAtCoordinate(x: number, y: number): PositionWithAffinity
```

Obtains the position of a glyph closest to the given coordinates.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PositionWithAffinity](../../apis-arkui/arkts-apis/arkts-arkui-positionwithaffinity-i.md) |

## getGlyphRangeForCharacterRange

```TypeScript
getGlyphRangeForCharacterRange(characterRange: Range, encoding: drawing.TextEncoding): Array<Range>
```

Obtains the glyph range corresponding to the specified character range.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| characterRange | [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes |
| encoding | drawing.TextEncoding | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;Range & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) |

## getHeight

```TypeScript
getHeight(): number
```

Obtains the total height of the text.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getIdeographicBaseline

```TypeScript
getIdeographicBaseline(): number
```

Obtains the ideographic baseline.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getLineCount

```TypeScript
getLineCount(): number
```

Obtains the number of text lines.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getLineHeight

```TypeScript
getLineHeight(line: number): number
```

Obtains the height of a given line.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| line | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getLineMetrics

```TypeScript
getLineMetrics(): Array<LineMetrics>
```

Obtains an array of line measurement information.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;LineMetrics & gt; |

## getLineMetrics

```TypeScript
getLineMetrics(lineNumber: number): LineMetrics | undefined
```

Obtains the line measurement information of a line.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [lineNumber](arkts-arkgraphics2d-text-linemetrics-i.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| LineMetrics \| undefined |

## getLineWidth

```TypeScript
getLineWidth(line: number): number
```

Obtains the width of a given line.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| line | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getLongestLine

```TypeScript
getLongestLine(): number
```

Obtains the longest line in the text.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getLongestLineWithIndent

```TypeScript
getLongestLineWithIndent(): number
```

Obtains the width of the longest line, including its indentation, in the text. You are advised to round up the return value. If the text content is empty, **0** is returned.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getMaxIntrinsicWidth

```TypeScript
getMaxIntrinsicWidth(): number
```

Obtains the maximum intrinsic width of the paragraph.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getMaxWidth

```TypeScript
getMaxWidth(): number
```

Obtains the maximum width of the line in the text.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getMinIntrinsicWidth

```TypeScript
getMinIntrinsicWidth(): number
```

Obtains the minimum intrinsic width of the paragraph.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## getParagraphStyle

```TypeScript
getParagraphStyle(): ParagraphStyle
```

Obtains the style configuration of a paragraph.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md) |

## getProcessState

```TypeScript
getProcessState(): TextProcessState
```

Obtains the text processing status of a paragraph.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextProcessState](arkts-arkgraphics2d-text-textprocessstate-e.md) |

## getRectsForPlaceholders

```TypeScript
getRectsForPlaceholders(): Array<TextBox>
```

Obtains the rectangles occupied by all placeholders in the text.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;TextBox & gt; |

## getRectsForRange

```TypeScript
getRectsForRange(range: Range, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>
```

Obtains the rectangles occupied by the characters in the range of the text under the given rectangle width and height.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes |
| widthStyle | [RectWidthStyle](arkts-arkgraphics2d-text-rectwidthstyle-e.md) | Yes |
| heightStyle | [RectHeightStyle](arkts-arkgraphics2d-text-rectheightstyle-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;TextBox & gt; |

## getTextDisplayState

```TypeScript
getTextDisplayState(): TextDisplayState
```

Obtains the text display status of a paragraph.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextDisplayState](arkts-arkgraphics2d-text-textdisplaystate-e.md) |

## getTextLines

```TypeScript
getTextLines(): Array<TextLine>
```

Obtains all the text lines.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[TextLine](arkts-arkgraphics2d-text-textline-c.md)&gt; |

## getVisibleTextRanges

```TypeScript
getVisibleTextRanges(): Array<Range>
```

Obtains the range of text that is visible on the screen in a paragraph. Excludes text that is not displayed due to truncation by the maximum line count (the maxLines attribute of [ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md)) or replacement in ellipsis mode ([EllipsisMode](arkts-arkgraphics2d-text-ellipsismode-e.md)).  
**NOTE：**The returned range depends on the specific truncation of the paragraph (for example, whether the maximum number of lines or ellipsis is set):
| [Scenario](../../apis-multimodal-awareness-kit/arkts-apis/arkts-multimodalawareness-onscreen-scenario-e-sys.md) | Description| |---|---| | Text is not truncated.| The range includes all typeset text.| | Only maxLines truncation is set (no ellipsis).| the text from the first line to the end of the maxLines line.| | EllipsisMode.END| The range is the text before the ellipsis.| | EllipsisMode.START| The value is the text after the ellipsis.| | EllipsisMode.MIDDLE| the text range before and after the ellipsis is returned.| | EllipsisMode.MULTILINE_START| the text range before and after the ellipsis is returned.| | EllipsisMode.MULTILINE_MIDDLE|

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;Range & gt; |

## getWordBoundary

```TypeScript
getWordBoundary(offset: number): Range
```

Obtains the range of the word where the glyph with a given offset is located.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) |

## layout

```TypeScript
layout(width: number): Promise<void>
```

Performs layout and calculates the positions of all glyphs. This API uses a promise to return the result.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| width | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## layoutSync

```TypeScript
layoutSync(width: number): void
```

Performs layout and calculates the positions of all glyphs.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| width | number | Yes |

## layoutWithConstraints

```TypeScript
layoutWithConstraints(size: TextRectSize): TextLayoutResult
```

Performs layout with the given height and width and calculates the positions of all glyphs.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | [TextRectSize](arkts-arkgraphics2d-text-textrectsize-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextLayoutResult](arkts-arkgraphics2d-text-textlayoutresult-i.md) |

## paint

```TypeScript
paint(canvas: drawing.Canvas, x: number, y: number): void
```

Draws text on the canvas with (x, y) as the upper-left corner. You must call [layout()](#layout) for typesetting before calling this API; otherwise, the text content cannot be displayed correctly.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| canvas | drawing.Canvas | Yes |
| x | number | Yes |
| y | number | Yes |

## paintOnPath

```TypeScript
paintOnPath(canvas: drawing.Canvas, path: drawing.Path, hOffset: number, vOffset: number): void
```

Draws text along a path on the canvas. You must call [layout()](#layout) for typesetting before calling this API; otherwise, the text content cannot be displayed correctly.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| canvas | drawing.Canvas | Yes |
| path | drawing.Path | Yes |
| hOffset | number | Yes |
| vOffset | number | Yes |

## updateColor

```TypeScript
updateColor(color: common2D.Color): void
```

Updates the color of the entire text span. This API call also updates the decoration color if it hasn't been set yet.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | common2D.Color | Yes |

## updateDecoration

```TypeScript
updateDecoration(decoration: Decoration): void
```

Updates the decoration line of the entire text span.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| decoration | [Decoration](arkts-arkgraphics2d-text-decoration-i.md) | Yes |
