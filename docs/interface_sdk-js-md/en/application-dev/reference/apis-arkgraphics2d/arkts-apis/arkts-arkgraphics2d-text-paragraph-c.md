# Paragraph

Implements a carrier that stores the text content and style. You can perform operations such as layout and drawing.

Before calling any of the following APIs, you must use [build()](arkts-arkgraphics2d-text-paragraphbuilder-c.md#build) of the  
[ParagraphBuilder](arkts-arkgraphics2d-text-paragraphbuilder-c.md) class to create a **Paragraph** object.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-text-class Paragraph--><!--Device-text-class Paragraph-End-->

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

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-didExceedMaxLines(): boolean--><!--Device-Paragraph-didExceedMaxLines(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. The value **true** means that the number of lines exceeds the maximum, and **false** means the opposite. |

## Examples

```TypeScript
let didExceed = paragraph.didExceedMaxLines();
```

## forceReuseRasterResult

```TypeScript
forceReuseRasterResult(isForce: boolean): void
```

Sets whether to force reuse of the rasterization result. If this API is not called, the system allows updating the rasterization result by default.

This API is suitable for scenarios where the text content remains unchanged but  
[paint](arkts-arkgraphics2d-text-paragraph-c.md#paint) needs to be called multiple times for drawing. By reusing the rasterization result, repeated rasterization calculations can be avoided to improve drawing performance. After this setting is applied, it takes effect the next time [paint](arkts-arkgraphics2d-text-paragraph-c.md#paint) is called for drawing.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Paragraph-forceReuseRasterResult(isForce: boolean): void--><!--Device-Paragraph-forceReuseRasterResult(isForce: boolean): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isForce | boolean | Yes | Whether to force reuse of the rasterization result. The value **true** means to force reuse of the rasterization result, and **false** means to allow updating the rasterization result. |

## getActualTextRange

ArkTS-Dyn:
```TypeScript
getActualTextRange(lineNumber: number, includeSpaces: boolean): Range
```

ArkTS-Sta:
```TypeScript
getActualTextRange(lineNumber: int, includeSpaces: boolean): Range
```

Obtains the actually visible text range in the specified line, excluding any overflow ellipsis.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getActualTextRange(lineNumber: int, includeSpaces: boolean): Range--><!--Device-Paragraph-getActualTextRange(lineNumber: int, includeSpaces: boolean): Range-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lineNumber | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Line number of the text range, starting from 0. This API can only be used to obtain the bounds of existing lines. That is, the line number must start from 0, and the maximum line index is the number of text lines – 1. The number of text lines can be obtained via the [getLineCount](arkts-arkgraphics2d-text-paragraph-c.md#getlinecount) API. |
| includeSpaces | boolean | Yes | Whether spaces are included. The value **true** means that spaces are contained, and **false** means the opposite. |

**Return value:**

| Type | Description |
| --- | --- |
| [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Text range obtained. If the line index is invalid, **start** and **end** are both **0**. |

## Examples

```TypeScript
let rang = paragraph.getActualTextRange(0, true);
```

## getAlphabeticBaseline

ArkTS-Dyn:
```TypeScript
getAlphabeticBaseline(): number
```

ArkTS-Sta:
```TypeScript
getAlphabeticBaseline(): double
```

Obtains the alphabetic baseline.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getAlphabeticBaseline(): double--><!--Device-Paragraph-getAlphabeticBaseline(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | Alphabetic baseline, in units of px. The value is a floating point number. |

## Examples

```TypeScript
let alphabeticBaseline = paragraph.getAlphabeticBaseline();
```

## getCharacterPositionAtCoordinate

ArkTS-Dyn:
```TypeScript
getCharacterPositionAtCoordinate(x: number, y: number, encoding: drawing.TextEncoding): PositionWithAffinity
```

ArkTS-Sta:
```TypeScript
getCharacterPositionAtCoordinate(x: double, y: double, encoding: drawing.TextEncoding): PositionWithAffinity
```

Obtains the character position information closest to the given coordinates.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-Paragraph-getCharacterPositionAtCoordinate(x: double, y: double, encoding: drawing.TextEncoding): PositionWithAffinity--><!--Device-Paragraph-getCharacterPositionAtCoordinate(x: double, y: double, encoding: drawing.TextEncoding): PositionWithAffinity-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Horizontal coordinate in the text layout area, in physical pixels (px). X offset relative to the top-left corner of the text layout area, with the right direction as positive. Supports floating-point values and accepts negative values, which indicate positions to the left of the text layout area. If the coordinates are beyond the text layout area, the nearest character position is returned. It can be obtained through a touch event or click event. |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Vertical coordinate in the text layout area, in physical pixels (px). Y offset relative to the top-left corner of the text layout area, with the downward direction as positive. Supports floating-point values and accepts negative values, which indicate positions above the text layout area. If the coordinates are beyond the text layout area, the nearest character position is returned. It can be obtained through a touch event or click event. |
| encoding | drawing.TextEncoding | Yes | Text encoding type. Currently, only UTF-8 and UTF-16 encoding types are supported. For UTF-8 encoding, the returned character position indicates the byte offset. For UTF-16 encoding, the returned character position indicates the UTF-16 encoding unit offset. |

**Return value:**

| Type | Description |
| --- | --- |
| [PositionWithAffinity](../../apis-arkui/arkts-apis/arkts-arkui-positionwithaffinity-i.md) | Character position. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) | Parameter error. Possible causes: Incorrect parameter range. |

## getCharacterRangeForGlyphRange

```TypeScript
getCharacterRangeForGlyphRange(glyphRange: Range, encoding: drawing.TextEncoding): Array<Range>
```

Obtains the character range corresponding to the specified glyph range.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-Paragraph-getCharacterRangeForGlyphRange(glyphRange: Range, encoding: drawing.TextEncoding): Array<Range>--><!--Device-Paragraph-getCharacterRangeForGlyphRange(glyphRange: Range, encoding: drawing.TextEncoding): Array<Range>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| glyphRange | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes | Glyph range. |
| encoding | drawing.TextEncoding | Yes | Text encoding type. Currently, only UTF-8 and UTF-16 encoding types are supported. For UTF-8 encoding, the returned character range indicates the byte range. For UTF-16 encoding, the returned character range indicates the UTF-16 encoding unit range. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;Range&gt; | Character range. If the array contains one element, it indicates the character range. If the array contains two elements, the first element indicates the character range, and the second element indicates the actual glyph range. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) | Parameter error. Possible causes: Incorrect parameter range. |

## getGlyphPositionAtCoordinate

ArkTS-Dyn:
```TypeScript
getGlyphPositionAtCoordinate(x: number, y: number): PositionWithAffinity
```

ArkTS-Sta:
```TypeScript
getGlyphPositionAtCoordinate(x: double, y: double): PositionWithAffinity
```

Obtains the position of a glyph closest to the given coordinates.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getGlyphPositionAtCoordinate(x: double, y: double): PositionWithAffinity--><!--Device-Paragraph-getGlyphPositionAtCoordinate(x: double, y: double): PositionWithAffinity-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Horizontal coordinate, which is a floating-point value in physical pixels (px). |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Vertical coordinate, which is a floating-point value in physical pixels (px). |

**Return value:**

| Type | Description |
| --- | --- |
| [PositionWithAffinity](../../apis-arkui/arkts-apis/arkts-arkui-positionwithaffinity-i.md) | Position of the glyph. |

## Examples

```TypeScript
let positionWithAffinity = paragraph.getGlyphPositionAtCoordinate(0, 0);
```

## getGlyphRangeForCharacterRange

```TypeScript
getGlyphRangeForCharacterRange(characterRange: Range, encoding: drawing.TextEncoding): Array<Range>
```

Obtains the glyph range corresponding to the specified character range.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-Paragraph-getGlyphRangeForCharacterRange(characterRange: Range, encoding: drawing.TextEncoding): Array<Range>--><!--Device-Paragraph-getGlyphRangeForCharacterRange(characterRange: Range, encoding: drawing.TextEncoding): Array<Range>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| characterRange | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes | Character range. |
| encoding | drawing.TextEncoding | Yes | Text encoding type. Currently, only UTF-8 and UTF-16 encoding types are supported. For UTF-8 encoding, the returned actual character range indicates the byte range. For UTF-16 encoding, the returned actual character range indicates the UTF-16 encoding unit range. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;Range&gt; | Glyph range. The array contains two elements. The first element indicates the glyph range, and the second element indicates the actual character range. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) | Parameter error. Possible causes: Incorrect parameter range. |

## getHeight

ArkTS-Dyn:
```TypeScript
getHeight(): number
```

ArkTS-Sta:
```TypeScript
getHeight(): double
```

Obtains the total height of the text.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getHeight(): double--><!--Device-Paragraph-getHeight(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | Total height, in units of px. The value is a floating point number. |

## Examples

```TypeScript
let height = paragraph.getHeight();
```

## getIdeographicBaseline

ArkTS-Dyn:
```TypeScript
getIdeographicBaseline(): number
```

ArkTS-Sta:
```TypeScript
getIdeographicBaseline(): double
```

Obtains the ideographic baseline.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getIdeographicBaseline(): double--><!--Device-Paragraph-getIdeographicBaseline(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | Baseline position under ideographic characters, a floating point number in physical pixels ( px). |

## Examples

```TypeScript
let ideographicBaseline = paragraph.getIdeographicBaseline();
```

## getLineCount

ArkTS-Dyn:
```TypeScript
getLineCount(): number
```

ArkTS-Sta:
```TypeScript
getLineCount(): int
```

Obtains the number of text lines.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getLineCount(): int--><!--Device-Paragraph-getLineCount(): int-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | Number of text lines. The value is an integer. |

## Examples

```TypeScript
let lineCount = paragraph.getLineCount();
```

## getLineHeight

ArkTS-Dyn:
```TypeScript
getLineHeight(line: number): number
```

ArkTS-Sta:
```TypeScript
getLineHeight(line: int): double
```

Obtains the height of a given line.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getLineHeight(line: int): double--><!--Device-Paragraph-getLineHeight(line: int): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| line | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Index of the text line, which is an integer ranging from 0 to [getLineCount](arkts-arkgraphics2d-text-paragraph-c.md#getlinecount)-1. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | Line height, in physical pixels (px). |

## Examples

```TypeScript
let lineHeight = paragraph.getLineHeight(0);
```

## getLineMetrics

```TypeScript
getLineMetrics(): Array<LineMetrics>
```

Obtains an array of line measurement information.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getLineMetrics(): Array<LineMetrics>--><!--Device-Paragraph-getLineMetrics(): Array<LineMetrics>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;LineMetrics&gt; | Array of line measurement information. |

## Examples

```TypeScript
let arrLineMetric =  paragraph.getLineMetrics();
```

## getLineMetrics

ArkTS-Dyn:
```TypeScript
getLineMetrics(lineNumber: number): LineMetrics | undefined
```

ArkTS-Sta:
```TypeScript
getLineMetrics(lineNumber: int): LineMetrics | undefined
```

Obtains the line measurement information of a line.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getLineMetrics(lineNumber: int): LineMetrics | undefined--><!--Device-Paragraph-getLineMetrics(lineNumber: int): LineMetrics | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lineNumber | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Number of the line for which metric information is to be queried. Line numbers start from 0, and the maximum line index is the number of text lines minus 1. The number of text lines can be obtained through the [getLineCount](arkts-arkgraphics2d-text-paragraph-c.md#getlinecount) API. |

**Return value:**

| Type | Description |
| --- | --- |
| [LineMetrics](../../apis-arkui/arkts-apis/arkts-arkui-linemetrics-t.md) | LineMetrics** object containing the measurement information if the specified line number is valid and the measurement information exists. If the line number is invalid or the measurement information cannot be obtained, **undefined** is returned. |

## Examples

```TypeScript
let lineMetrics =  paragraph.getLineMetrics(0);
```

## getLineWidth

ArkTS-Dyn:
```TypeScript
getLineWidth(line: number): number
```

ArkTS-Sta:
```TypeScript
getLineWidth(line: int): double
```

Obtains the width of a given line.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getLineWidth(line: int): double--><!--Device-Paragraph-getLineWidth(line: int): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| line | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Text line index, which is an integer ranging from 0 to [getLineCount](arkts-arkgraphics2d-text-paragraph-c.md#getlinecount)-1. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | Line width, in physical pixels (px). |

## Examples

```TypeScript
let lineWidth = paragraph.getLineWidth(0);
```

## getLongestLine

ArkTS-Dyn:
```TypeScript
getLongestLine(): number
```

ArkTS-Sta:
```TypeScript
getLongestLine(): double
```

Obtains the longest line in the text.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getLongestLine(): double--><!--Device-Paragraph-getLongestLine(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | Longest line, in units of px. The value is a floating point number. |

## Examples

```TypeScript
let longestLine = paragraph.getLongestLine();
```

## getLongestLineWithIndent

ArkTS-Dyn:
```TypeScript
getLongestLineWithIndent(): number
```

ArkTS-Sta:
```TypeScript
getLongestLineWithIndent(): double
```

Obtains the width of the longest line, including its indentation, in the text. You are advised to round up the return value. If the text content is empty, **0** is returned.

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getLongestLineWithIndent(): double--><!--Device-Paragraph-getLongestLineWithIndent(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | Width of the longest line, including its indentation. The value is a floating point number, in px. |

## Examples

```TypeScript
let longestLineWithIndent = paragraph.getLongestLineWithIndent();
```

## getMaxIntrinsicWidth

ArkTS-Dyn:
```TypeScript
getMaxIntrinsicWidth(): number
```

ArkTS-Sta:
```TypeScript
getMaxIntrinsicWidth(): double
```

Obtains the maximum intrinsic width of the paragraph.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getMaxIntrinsicWidth(): double--><!--Device-Paragraph-getMaxIntrinsicWidth(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | Maximum intrinsic width, in units of px. The value is a floating point number. |

## Examples

```TypeScript
let maxIntrinsicWidth = paragraph.getMaxIntrinsicWidth();
```

## getMaxWidth

ArkTS-Dyn:
```TypeScript
getMaxWidth(): number
```

ArkTS-Sta:
```TypeScript
getMaxWidth(): double
```

Obtains the maximum width of the line in the text.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getMaxWidth(): double--><!--Device-Paragraph-getMaxWidth(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | Maximum line width, in units of px. The value is a floating point number. |

## Examples

```TypeScript
let maxWidth = paragraph.getMaxWidth();
```

## getMinIntrinsicWidth

ArkTS-Dyn:
```TypeScript
getMinIntrinsicWidth(): number
```

ArkTS-Sta:
```TypeScript
getMinIntrinsicWidth(): double
```

Obtains the minimum intrinsic width of the paragraph.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getMinIntrinsicWidth(): double--><!--Device-Paragraph-getMinIntrinsicWidth(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | Minimum intrinsic width, in units of px. The value is a floating point number. |

## Examples

```TypeScript
let minIntrinsicWidth = paragraph.getMinIntrinsicWidth();
```

## getParagraphStyle

```TypeScript
getParagraphStyle(): ParagraphStyle
```

Obtains the style configuration of a paragraph.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Paragraph-getParagraphStyle(): ParagraphStyle--><!--Device-Paragraph-getParagraphStyle(): ParagraphStyle-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md) | Style configuration of the paragraph. &lt;br&gt;The `textStyle.color`, `textStyle.textShadows.color`, `textStyle.backgroundRect.color`, and `textStyle.decoration.color` properties return a 32-bit unsigned integer color value. Example: The return value `4278190080` corresponds to the pure black hexadecimal color value `0xFF000000`, which is equivalent to the [common2D.Color]{ |

## getProcessState

```TypeScript
getProcessState(): TextProcessState
```

Obtains the text processing status of a paragraph.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Paragraph-getProcessState(): TextProcessState--><!--Device-Paragraph-getProcessState(): TextProcessState-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [TextProcessState](arkts-arkgraphics2d-text-textprocessstate-e.md) | Text processing status of a paragraph. |

## getRectsForPlaceholders

```TypeScript
getRectsForPlaceholders(): Array<TextBox>
```

Obtains the rectangles occupied by all placeholders in the text.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getRectsForPlaceholders(): Array<TextBox>--><!--Device-Paragraph-getRectsForPlaceholders(): Array<TextBox>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;TextBox&gt; | Array holding the rectangles obtained. |

## Examples

```TypeScript
let placeholderRects = paragraph.getRectsForPlaceholders();
```

## getRectsForRange

```TypeScript
getRectsForRange(range: Range, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>
```

Obtains the rectangles occupied by the characters in the range of the text under the given rectangle width and height.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getRectsForRange(range: Range, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>--><!--Device-Paragraph-getRectsForRange(range: Range, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes | Range of the text. |
| widthStyle | [RectWidthStyle](../../apis-arkui/arkts-apis/arkts-arkui-rectwidthstyle-t.md) | Yes | Width of the rectangle. |
| heightStyle | [RectHeightStyle](arkts-arkgraphics2d-text-rectheightstyle-e.md) | Yes | Height of the rectangle. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;TextBox&gt; | Array holding the rectangles obtained. |

## Examples

```TypeScript
let range: text.Range = { start: 0, end: 1};
let rects = paragraph.getRectsForRange(range, text.RectWidthStyle.TIGHT, text.RectHeightStyle.TIGHT);
```

## getTextDisplayState

```TypeScript
getTextDisplayState(): TextDisplayState
```

Obtains the text display status of a paragraph.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Paragraph-getTextDisplayState(): TextDisplayState--><!--Device-Paragraph-getTextDisplayState(): TextDisplayState-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [TextDisplayState](arkts-arkgraphics2d-text-textdisplaystate-e.md) | Text display status of a paragraph. |

## getTextLines

```TypeScript
getTextLines(): Array<TextLine>
```

Obtains all the text lines.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getTextLines(): Array<TextLine>--><!--Device-Paragraph-getTextLines(): Array<TextLine>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;TextLine&gt; | Array of text lines. |

## Examples

```TypeScript
let lines = paragraph.getTextLines();
```

## getVisibleTextRanges

```TypeScript
getVisibleTextRanges(): Array<Range>
```

Obtains the range of text that is visible on the screen in a paragraph. Excludes text that is not displayed due to truncation by the maximum line count (the maxLines attribute of [ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md))or replacement in ellipsis mode ([EllipsisMode](arkts-arkgraphics2d-text-ellipsismode-e.md)).

**NOTE：**

The returned range depends on the specific truncation of the paragraph(for example, whether the maximum number of lines or ellipsis is set):

| Scenario| Description|  
|---|---|  
| Text is not truncated.| The range includes all typeset text.|  
| Only maxLines truncation is set (no ellipsis).| the text from the first line to the end of the maxLines line.|  
| EllipsisMode.END| The range is the text before the ellipsis.|  
| EllipsisMode.START| The value is the text after the ellipsis.|  
| EllipsisMode.MIDDLE| the text range before and after the ellipsis is returned.|  
| EllipsisMode.MULTILINE_START| the text range before and after the ellipsis is returned.|  
| EllipsisMode.MULTILINE_MIDDLE| the text range before and after the ellipsis is returned.|

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Paragraph-getVisibleTextRanges(): Array<Range>--><!--Device-Paragraph-getVisibleTextRanges(): Array<Range>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;Range&gt; | Array of the visible text range of a paragraph. The range is the index of the UTF-16 encoding unit. |

## getWordBoundary

ArkTS-Dyn:
```TypeScript
getWordBoundary(offset: number): Range
```

ArkTS-Sta:
```TypeScript
getWordBoundary(offset: int): Range
```

Obtains the range of the word where the glyph with a given offset is located.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getWordBoundary(offset: int): Range--><!--Device-Paragraph-getWordBoundary(offset: int): Range-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Offset of the glyph. The value is an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Range of the word. |

## Examples

```TypeScript
let wordRange = paragraph.getWordBoundary(0);
```

## layout

ArkTS-Dyn:
```TypeScript
layout(width: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
layout(width: double): Promise<void>
```

Performs layout and calculates the positions of all glyphs. This API uses a promise to return the result.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-layout(width: double): Promise<void>--><!--Device-Paragraph-layout(width: double): Promise<void>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Maximum width of a single line, in units of px. The value is a floating point number. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
import { drawing, text } from '@kit.ArkGraphics2D'
import { image } from '@kit.ImageKit'

let textStyle: text.TextStyle = {
  color: {
    alpha: 255,
    red: 255,
    green: 0,
    blue: 0
  },
  fontSize: 30,
};
let paragraphStyle: text.ParagraphStyle = {
  textStyle: textStyle,
};
let fontCollection: text.FontCollection = new text.FontCollection();
let paragraphBuilder = new text.ParagraphBuilder(paragraphStyle, fontCollection);
// Add a text string.
paragraphBuilder.addText("test");
// Create a paragraph object.
let paragraph = paragraphBuilder.build();

function textFunc(pixelmap: PixelMap) {
  // Construct a canvas using an image object.
  let canvas = new drawing.Canvas(pixelmap);
  // Draw a text string.
  paragraph.paint(canvas, 100, 10);
}

@Entry
@Component
struct Index {
  @State pixelmap?: PixelMap = undefined;
  fun: Function = textFunc;

  async prepareLayoutPromise() {
    // Calculate the layout of the paragraph object.
    paragraph.layout(200).then((data) => {
      console.info(`Succeeded in doing layout,  ${JSON.stringify(data)}`);
    }).catch((error: Error) => {
      console.error(`Failed to do layout, error: ${JSON.stringify(error)} message: ${error.message}`);
    });
  }

  aboutToAppear() {
    this.prepareLayoutPromise();
  }

  build() {
    Column() {
      Image(this.pixelmap).width(200).height(200);
      Button("layout")
        .width(100)
        .height(50)
        .onClick(() => {
          const color: ArrayBuffer = new ArrayBuffer(160000);
          let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 200, width: 200 } }
          if (this.pixelmap == undefined) {
            // Construct an image object.
            this.pixelmap = image.createPixelMapSync(color, opts);
          }
          // Draw the text.
          this.fun(this.pixelmap);
        })
    }
  }
}
```

## layoutSync

ArkTS-Dyn:
```TypeScript
layoutSync(width: number): void
```

ArkTS-Sta:
```TypeScript
layoutSync(width: double): void
```

Performs layout and calculates the positions of all glyphs.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-layoutSync(width: double): void--><!--Device-Paragraph-layoutSync(width: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Maximum width of a single line, in units of px. The value is a floating point number. |

## Examples

```TypeScript
paragraph.layoutSync(100);
```

## layoutWithConstraints

```TypeScript
layoutWithConstraints(size: TextRectSize): TextLayoutResult
```

Performs layout with the given height and width and calculates the positions of all glyphs.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-Paragraph-layoutWithConstraints(size: TextRectSize): TextLayoutResult--><!--Device-Paragraph-layoutWithConstraints(size: TextRectSize): TextLayoutResult-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | [TextRectSize](arkts-arkgraphics2d-text-textrectsize-i.md) | Yes | Constrained height and width, in physical pixels (px). |

**Return value:**

| Type | Description |
| --- | --- |
| [TextLayoutResult](arkts-arkgraphics2d-text-textlayoutresult-i.md) | Actual size after layout and character range after typesetting. |

## paint

ArkTS-Dyn:
```TypeScript
paint(canvas: drawing.Canvas, x: number, y: number): void
```

ArkTS-Sta:
```TypeScript
paint(canvas: drawing.Canvas, x: double, y: double): void
```

Draws text on the canvas with (x, y) as the upper-left corner. You must call  
[layout()](arkts-arkgraphics2d-text-paragraph-c.md#layout) for typesetting before calling this API; otherwise, the text content cannot be displayed correctly.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-paint(canvas: drawing.Canvas, x: double, y: double): void--><!--Device-Paragraph-paint(canvas: drawing.Canvas, x: double, y: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| canvas | drawing.Canvas | Yes | Target canvas. |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Horizontal coordinate of the upper left corner, which is a floating-point value, in physical pixels (px). |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Vertical coordinate of the upper left corner, which is a floating-point value, in physical pixels (px). |

## Examples

```TypeScript
const color: ArrayBuffer = new ArrayBuffer(160000);
let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 200, width: 200 } }
let pixelMap: image.PixelMap = image.createPixelMapSync(color, opts);
let canvas = new drawing.Canvas(pixelMap);
paragraph.paint(canvas, 0, 0);
```

## paintOnPath

ArkTS-Dyn:
```TypeScript
paintOnPath(canvas: drawing.Canvas, path: drawing.Path, hOffset: number, vOffset: number): void
```

ArkTS-Sta:
```TypeScript
paintOnPath(canvas: drawing.Canvas, path: drawing.Path, hOffset: double, vOffset: double): void
```

Draws text along a path on the canvas. You must call [layout()](arkts-arkgraphics2d-text-paragraph-c.md#layout) for typesetting before calling this API; otherwise, the text content cannot be displayed correctly.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-paintOnPath(canvas: drawing.Canvas, path: drawing.Path, hOffset: double, vOffset: double): void--><!--Device-Paragraph-paintOnPath(canvas: drawing.Canvas, path: drawing.Path, hOffset: double, vOffset: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| canvas | drawing.Canvas | Yes | Target canvas. |
| path | drawing.Path | Yes | Path along which the text is drawn. |
| hOffset | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Offset along the path direction. Positive values extend forward from the path start point, and negative values extend backward. Unit: physical pixels (px). |
| vOffset | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Offset along the vertical direction of the path. Positive values extend to the right along the path, and negative values extend to the left. Unit: physical pixels (px). |

## Examples

```TypeScript
const color: ArrayBuffer = new ArrayBuffer(160000);
let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 200, width: 200 } }
let pixelMap: image.PixelMap = image.createPixelMapSync(color, opts);
let canvas = new drawing.Canvas(pixelMap);
let path = new drawing.Path();
path.arcTo(20, 20, 180, 180, 180, 90);
paragraph.paintOnPath(canvas, path, 0, 0);
```

## updateColor

```TypeScript
updateColor(color: common2D.Color): void
```

Updates the color of the entire text span. This API call also updates the decoration color if it hasn't been set yet.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-updateColor(color: common2D.Color): void--><!--Device-Paragraph-updateColor(color: common2D.Color): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | common2D.Color | Yes | Updated font color. |

## Examples

```TypeScript
paragraph.updateColor({ alpha: 255, red: 255, green: 0, blue: 0 });
```

## updateDecoration

```TypeScript
updateDecoration(decoration: Decoration): void
```

Updates the decoration line of the entire text span.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-updateDecoration(decoration: Decoration): void--><!--Device-Paragraph-updateDecoration(decoration: Decoration): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| decoration | [Decoration](arkts-arkgraphics2d-text-decoration-i.md) | Yes | Updated decoration line. |

## Examples

```TypeScript
paragraph.updateDecoration({
  textDecoration: text.TextDecorationType.OVERLINE,
  color: { alpha: 255, red: 255, green: 0, blue: 0 },
  decorationStyle: text.TextDecorationStyle.WAVY,
  decorationThicknessScale: 2.0,
});
```

