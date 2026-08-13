# Paragraph

Implements a carrier that stores the text content and style. You can perform operations such as layout and drawing. Before calling any of the following APIs, you must use [build()](arkts-arkgraphics2d-text-paragraphbuilder-c.md#build) of the [ParagraphBuilder](arkts-arkgraphics2d-text-paragraphbuilder-c.md#ParagraphBuilder) class to create a **Paragraph** object.

**Since:** 23

**Deprecated since:** -1

<!--Device-text-class Paragraph--><!--Device-text-class Paragraph-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { text } from '@kit.ArkGraphics2D';
```

## didExceedMaxLines

```TypeScript
didExceedMaxLines(): boolean
```

Checks whether the number of lines in the paragraph exceeds the maximum.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-didExceedMaxLines(): boolean--><!--Device-Paragraph-didExceedMaxLines(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
let didExceed = paragraph.didExceedMaxLines();
```

## forceReuseRasterResult

```TypeScript
forceReuseRasterResult(isForce: boolean): void
```

Sets whether to force reuse of the rasterization result. If this API is not called, the system allows updating the rasterization result by default. This API is suitable for scenarios where the text content remains unchanged but [paint](#paint) needs to be called multiple times for drawing. By reusing the rasterization result, repeated rasterization calculations can be avoided to improve drawing performance. After this setting is applied, it takes effect the next time [paint](#paint) is called for drawing.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Paragraph-forceReuseRasterResult(isForce: boolean): void--><!--Device-Paragraph-forceReuseRasterResult(isForce: boolean): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isForce | boolean | Yes |

## Examples

```TypeScript
// Index.ets
import { text, drawing } from '@kit.ArkGraphics2D'
import { image } from '@kit.ImageKit'
 
function textFunc(pixelmap: PixelMap) {
  let canvas = new drawing.Canvas(pixelmap);
  let textData = "Hello World";
  let myTextStyle: text.TextStyle = {
    color: { alpha: 255, red: 255, green: 0, blue: 0 },
    fontSize: 33,
  };
  let myParagraphStyle: text.ParagraphStyle = {
    textStyle: myTextStyle
  };
  let fontCollection = new text.FontCollection();
  let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
  paragraphBuilder.addText(textData);
  let paragraph = paragraphBuilder.build();
  paragraph.layoutSync(200);
  paragraph.forceReuseRasterResult(true);
  paragraph.paint(canvas, 0, 0);
}

@Entry
@Component
struct Index {
  @State pixelmap?: PixelMap = undefined;
  fun: Function = textFunc;
  build() {
    Column() {
      Image(this.pixelmap).width(200).height(200);
      Button("Click").onClick(() => {
        if (this.pixelmap == undefined) {
          const color: ArrayBuffer = new ArrayBuffer(160000);
          let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 200, width: 200 } }
          this.pixelmap = image.createPixelMapSync(color, opts);
        }
        this.fun(this.pixelmap);
      })
    }
  }
}
```

## getActualTextRange

```TypeScript
getActualTextRange(lineNumber: number, includeSpaces: boolean): Range
```

Obtains the actually visible text range in the specified line, excluding any overflow ellipsis.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getActualTextRange(lineNumber: int, includeSpaces: boolean): Range--><!--Device-Paragraph-getActualTextRange(lineNumber: int, includeSpaces: boolean): Range-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [lineNumber](arkts-arkgraphics2d-text-linemetrics-i.md) | number | Yes |
| includeSpaces | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) |

## Examples

```TypeScript
let rang = paragraph.getActualTextRange(0, true);
```

## getAlphabeticBaseline

```TypeScript
getAlphabeticBaseline(): number
```

Obtains the alphabetic baseline.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getAlphabeticBaseline(): double--><!--Device-Paragraph-getAlphabeticBaseline(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let alphabeticBaseline = paragraph.getAlphabeticBaseline();
```

## getCharacterPositionAtCoordinate

```TypeScript
getCharacterPositionAtCoordinate(x: number, y: number, encoding: drawing.TextEncoding): PositionWithAffinity
```

Obtains the character position information closest to the given coordinates.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-Paragraph-getCharacterPositionAtCoordinate(x: double, y: double, encoding: drawing.TextEncoding): PositionWithAffinity--><!--Device-Paragraph-getCharacterPositionAtCoordinate(x: double, y: double, encoding: drawing.TextEncoding): PositionWithAffinity-End-->

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

## Examples

```TypeScript
import { drawing, text } from '@kit.ArkGraphics2D'

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button("get character position")
        .onClick(() => {
          let encoding: drawing.TextEncoding = drawing.TextEncoding.TEXT_ENCODING_UTF8;
          let textData = "Heน้ำl👨‍👩‍👧lo1️⃣World";
          let myTextStyle: text.TextStyle = {
            color: { alpha: 255, red: 255, green: 0, blue: 0 },
            fontSize: 33,
          };
          let myParagraphStyle: text.ParagraphStyle = {
            textStyle: myTextStyle,
            align: text.TextAlign.END,
          };
          let fontCollection = new text.FontCollection();
          let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
          paragraphBuilder.addText(textData);
          let paragraph = paragraphBuilder.build();
          paragraph.layoutSync(200);
          let x = 10;
          let y = 5;
          let position = paragraph.getCharacterPositionAtCoordinate(x, y, encoding);
        })
    }
  }
}
```

## getCharacterRangeForGlyphRange

```TypeScript
getCharacterRangeForGlyphRange(glyphRange: Range, encoding: drawing.TextEncoding): Array<Range>
```

Obtains the character range corresponding to the specified glyph range.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-Paragraph-getCharacterRangeForGlyphRange(glyphRange: Range, encoding: drawing.TextEncoding): Array<Range>--><!--Device-Paragraph-getCharacterRangeForGlyphRange(glyphRange: Range, encoding: drawing.TextEncoding): Array<Range>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| glyphRange | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes |
| encoding | drawing.TextEncoding | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;Range & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) |

## Examples

```TypeScript
import { drawing, text } from '@kit.ArkGraphics2D'

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button("get character range")
        .onClick(() => {
          let glyphRange: text.Range = { start: 0, end: 5 };
          let encoding: drawing.TextEncoding = drawing.TextEncoding.TEXT_ENCODING_UTF8;
          let textData = "Heน้ำl👨‍👩‍👧lo1️⃣World";
          let myTextStyle: text.TextStyle = {
            color: { alpha: 255, red: 255, green: 0, blue: 0 },
            fontSize: 33,
          };
          let myParagraphStyle: text.ParagraphStyle = {
            textStyle: myTextStyle,
            align: text.TextAlign.END,
          };
          let fontCollection = new text.FontCollection();
          let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
          paragraphBuilder.addText(textData);
          let paragraph = paragraphBuilder.build();
          paragraph.layoutSync(200);
          let ranges = paragraph.getCharacterRangeForGlyphRange(glyphRange, encoding);
        })
    }
  }
}
```

## getGlyphPositionAtCoordinate

```TypeScript
getGlyphPositionAtCoordinate(x: number, y: number): PositionWithAffinity
```

Obtains the position of a glyph closest to the given coordinates.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getGlyphPositionAtCoordinate(x: double, y: double): PositionWithAffinity--><!--Device-Paragraph-getGlyphPositionAtCoordinate(x: double, y: double): PositionWithAffinity-End-->

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

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-Paragraph-getGlyphRangeForCharacterRange(characterRange: Range, encoding: drawing.TextEncoding): Array<Range>--><!--Device-Paragraph-getGlyphRangeForCharacterRange(characterRange: Range, encoding: drawing.TextEncoding): Array<Range>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| characterRange | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes |
| encoding | drawing.TextEncoding | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;Range & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-abnormal-parameter-value) |

## Examples

```TypeScript
import { drawing, text } from '@kit.ArkGraphics2D'

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button("get glyph range")
        .onClick(() => {
          let characterRange: text.Range = { start: 0, end: 5 };
          let encoding: drawing.TextEncoding = drawing.TextEncoding.TEXT_ENCODING_UTF8;
          let textData = "Heน้ำl👨‍👩‍👧lo1️⃣World";
          let myTextStyle: text.TextStyle = {
            color: { alpha: 255, red: 255, green: 0, blue: 0 },
            fontSize: 33,
          };
          let myParagraphStyle: text.ParagraphStyle = {
            textStyle: myTextStyle,
            align: text.TextAlign.END,
          };
          let fontCollection = new text.FontCollection();
          let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
          paragraphBuilder.addText(textData);
          let paragraph = paragraphBuilder.build();
          paragraph.layoutSync(200);
          let ranges = paragraph.getGlyphRangeForCharacterRange(characterRange, encoding);
        })
    }
  }
}
```

## getHeight

```TypeScript
getHeight(): number
```

Obtains the total height of the text.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getHeight(): double--><!--Device-Paragraph-getHeight(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let height = paragraph.getHeight();
```

## getIdeographicBaseline

```TypeScript
getIdeographicBaseline(): number
```

Obtains the ideographic baseline.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getIdeographicBaseline(): double--><!--Device-Paragraph-getIdeographicBaseline(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let ideographicBaseline = paragraph.getIdeographicBaseline();
```

## getLineCount

```TypeScript
getLineCount(): number
```

Obtains the number of text lines.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getLineCount(): int--><!--Device-Paragraph-getLineCount(): int-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let lineCount = paragraph.getLineCount();
```

## getLineHeight

```TypeScript
getLineHeight(line: number): number
```

Obtains the height of a given line.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getLineHeight(line: int): double--><!--Device-Paragraph-getLineHeight(line: int): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| line | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let lineHeight = paragraph.getLineHeight(0);
```

## getLineMetrics

```TypeScript
getLineMetrics(): Array<LineMetrics>
```

Obtains an array of line measurement information.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getLineMetrics(): Array<LineMetrics>--><!--Device-Paragraph-getLineMetrics(): Array<LineMetrics>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;LineMetrics & gt; |

## Examples

```TypeScript
let arrLineMetric =  paragraph.getLineMetrics();
```

## getLineMetrics

```TypeScript
getLineMetrics(lineNumber: number): LineMetrics | undefined
```

Obtains the line measurement information of a line.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getLineMetrics(lineNumber: int): LineMetrics | undefined--><!--Device-Paragraph-getLineMetrics(lineNumber: int): LineMetrics | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [lineNumber](arkts-arkgraphics2d-text-linemetrics-i.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [LineMetrics](../../apis-arkui/arkts-apis/arkts-arkui-linemetrics-t.md) |

## Examples

```TypeScript
let lineMetrics =  paragraph.getLineMetrics(0);
```

## getLineWidth

```TypeScript
getLineWidth(line: number): number
```

Obtains the width of a given line.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getLineWidth(line: int): double--><!--Device-Paragraph-getLineWidth(line: int): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| line | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let lineWidth = paragraph.getLineWidth(0);
```

## getLongestLine

```TypeScript
getLongestLine(): number
```

Obtains the longest line in the text.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getLongestLine(): double--><!--Device-Paragraph-getLongestLine(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let longestLine = paragraph.getLongestLine();
```

## getLongestLineWithIndent

```TypeScript
getLongestLineWithIndent(): number
```

Obtains the width of the longest line, including its indentation, in the text. You are advised to round up the return value. If the text content is empty, **0** is returned.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getLongestLineWithIndent(): double--><!--Device-Paragraph-getLongestLineWithIndent(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let longestLineWithIndent = paragraph.getLongestLineWithIndent();
```

## getMaxIntrinsicWidth

```TypeScript
getMaxIntrinsicWidth(): number
```

Obtains the maximum intrinsic width of the paragraph.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getMaxIntrinsicWidth(): double--><!--Device-Paragraph-getMaxIntrinsicWidth(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let maxIntrinsicWidth = paragraph.getMaxIntrinsicWidth();
```

## getMaxWidth

```TypeScript
getMaxWidth(): number
```

Obtains the maximum width of the line in the text.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getMaxWidth(): double--><!--Device-Paragraph-getMaxWidth(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let maxWidth = paragraph.getMaxWidth();
```

## getMinIntrinsicWidth

```TypeScript
getMinIntrinsicWidth(): number
```

Obtains the minimum intrinsic width of the paragraph.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getMinIntrinsicWidth(): double--><!--Device-Paragraph-getMinIntrinsicWidth(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

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

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Paragraph-getParagraphStyle(): ParagraphStyle--><!--Device-Paragraph-getParagraphStyle(): ParagraphStyle-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md) |

## Examples

```TypeScript
import { text } from '@kit.ArkGraphics2D'
import { common2D } from '@kit.ArkGraphics2D'

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button("Click")
        .onClick(() => {
          let textData = "Hello World";
          let myTextStyle: text.TextStyle = {
            color: { alpha: 255, red: 255, green: 0, blue: 0 },
            fontSize: 33,
          };
          let myParagraphStyle: text.ParagraphStyle = {
            textStyle: myTextStyle
          };
          let fontCollection = new text.FontCollection();
          let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
          paragraphBuilder.addText(textData);
          let paragraph = paragraphBuilder.build();
          paragraph.layoutSync(200);
          let paragraphStyle = paragraph.getParagraphStyle();
          if (paragraphStyle.textStyle != undefined) {
            console.info("Print fontSize: " + paragraphStyle.textStyle?.fontSize);
            if (paragraphStyle.textStyle?.color != undefined && typeof paragraphStyle.textStyle?.color == 'number') {
              let textColor: common2D.Color = numberToRGBA(paragraphStyle.textStyle?.color);
              console.info(`Print text color ARGB: ${textColor.alpha}, ${textColor.red}, ${textColor.green}, ${textColor.blue}`);
            }
          }
        })
    }
  }
}

function numberToRGBA(colorNum: number): common2D.Color {
  const a = (colorNum >>> 24) & 0xFF;
  const r = (colorNum >>> 16) & 0xFF;
  const g = (colorNum >>> 8) & 0xFF;
  const b = colorNum & 0xFF;
  return { alpha: a, red: r, green: g, blue: b };
}
```

## getProcessState

```TypeScript
getProcessState(): TextProcessState
```

Obtains the text processing status of a paragraph.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Paragraph-getProcessState(): TextProcessState--><!--Device-Paragraph-getProcessState(): TextProcessState-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextProcessState](arkts-arkgraphics2d-text-textprocessstate-e.md) |

## Examples

```TypeScript
import { text } from '@kit.ArkGraphics2D'

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button("Click")
        .onClick(() => {
          let textData = "Hello World";
          let myTextStyle: text.TextStyle = {
            color: { alpha: 255, red: 255, green: 0, blue: 0 },
            fontSize: 33,
          };
          let myParagraphStyle: text.ParagraphStyle = {
            textStyle: myTextStyle
          };
          let fontCollection = new text.FontCollection();
          let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
          paragraphBuilder.addText(textData);
          let paragraph = paragraphBuilder.build();
          let processState = paragraph.getProcessState(); // Now it is INIT
          console.info("Print state: " + processState);
          paragraph.layoutSync(200);
          processState = paragraph.getProcessState(); // Now it is FORMATTED
          console.info("Print state: " + processState);
        })
    }
  }
}
```

## getRectsForPlaceholders

```TypeScript
getRectsForPlaceholders(): Array<TextBox>
```

Obtains the rectangles occupied by all placeholders in the text.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getRectsForPlaceholders(): Array<TextBox>--><!--Device-Paragraph-getRectsForPlaceholders(): Array<TextBox>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;TextBox & gt; |

## Examples

```TypeScript
let placeholderRects = paragraph.getRectsForPlaceholders();
```

## getRectsForRange

```TypeScript
getRectsForRange(range: Range, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>
```

Obtains the rectangles occupied by the characters in the range of the text under the given rectangle width and height.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getRectsForRange(range: Range, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>--><!--Device-Paragraph-getRectsForRange(range: Range, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes |
| widthStyle | [RectWidthStyle](../../apis-arkui/arkts-apis/arkts-arkui-rectwidthstyle-t.md) | Yes |
| heightStyle | [RectHeightStyle](arkts-arkgraphics2d-text-rectheightstyle-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;TextBox & gt; |

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

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Paragraph-getTextDisplayState(): TextDisplayState--><!--Device-Paragraph-getTextDisplayState(): TextDisplayState-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextDisplayState](arkts-arkgraphics2d-text-textdisplaystate-e.md) |

## Examples

```TypeScript
import { text } from '@kit.ArkGraphics2D'

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button("Click")
        .onClick(() => {
          let textData = "Hello World";
          let myTextStyle: text.TextStyle = {
            color: { alpha: 255, red: 255, green: 0, blue: 0 },
            fontSize: 33,
          };
          let myParagraphStyle: text.ParagraphStyle = {
            textStyle: myTextStyle
          };
          let fontCollection = new text.FontCollection();
          let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
          paragraphBuilder.addText(textData);
          let paragraph = paragraphBuilder.build();
          let displayState = paragraph.getTextDisplayState(); // Now it is UNKNOWN
          console.info("Print state: " + displayState);
          paragraph.layoutSync(200);
          displayState = paragraph.getTextDisplayState(); // Now it is CLIP
          console.info("Print state: " + displayState);
        })
    }
  }
}
```

## getTextLines

```TypeScript
getTextLines(): Array<TextLine>
```

Obtains all the text lines.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getTextLines(): Array<TextLine>--><!--Device-Paragraph-getTextLines(): Array<TextLine>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[TextLine](arkts-arkgraphics2d-text-textline-c.md)&gt; |

## Examples

```TypeScript
let lines = paragraph.getTextLines();
```

## getVisibleTextRanges

```TypeScript
getVisibleTextRanges(): Array<Range>
```

Obtains the range of text that is visible on the screen in a paragraph. Excludes text that is not displayed due to truncation by the maximum line count (the maxLines attribute of [ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md#ParagraphStyle)) or replacement in ellipsis mode ([EllipsisMode](arkts-arkgraphics2d-text-ellipsismode-e.md#EllipsisMode)). **NOTE：**The returned range depends on the specific truncation of the paragraph (for example, whether the maximum number of lines or ellipsis is set): | Scenario| Description| |---|---| | Text is not truncated.| The range includes all typeset text.| | Only maxLines truncation is set (no ellipsis).| the text from the first line to the end of the maxLines line.| | EllipsisMode.END| The range is the text before the ellipsis.| | EllipsisMode.START| The value is the text after the ellipsis.| | EllipsisMode.MIDDLE| the text range before and after the ellipsis is returned.| | EllipsisMode.MULTILINE_START| the text range before and after the ellipsis is returned.| | EllipsisMode.MULTILINE_MIDDLE| the text range before and after the ellipsis is returned.|

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Paragraph-getVisibleTextRanges(): Array<Range>--><!--Device-Paragraph-getVisibleTextRanges(): Array<Range>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;Range & gt; |

## Examples

```TypeScript
let visibleRanges = paragraph.getVisibleTextRanges();
```

## getWordBoundary

```TypeScript
getWordBoundary(offset: number): Range
```

Obtains the range of the word where the glyph with a given offset is located.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getWordBoundary(offset: int): Range--><!--Device-Paragraph-getWordBoundary(offset: int): Range-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) |

## Examples

```TypeScript
let wordRange = paragraph.getWordBoundary(0);
```

## layout

```TypeScript
layout(width: number): Promise<void>
```

Performs layout and calculates the positions of all glyphs. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-layout(width: double): Promise<void>--><!--Device-Paragraph-layout(width: double): Promise<void>-End-->

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
    try {
      await paragraph.layout(200);
      console.info('Succeeded in doing layout');
    } catch (error) {
      let e: Error = error as Error;
      console.error(`Failed to do layout, error: ${JSON.stringify(e)} message: ${e.message}`);
    }
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

```TypeScript
layoutSync(width: number): void
```

Performs layout and calculates the positions of all glyphs.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-layoutSync(width: double): void--><!--Device-Paragraph-layoutSync(width: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| width | number | Yes |

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

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-Paragraph-layoutWithConstraints(size: TextRectSize): TextLayoutResult--><!--Device-Paragraph-layoutWithConstraints(size: TextRectSize): TextLayoutResult-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | [TextRectSize](arkts-arkgraphics2d-text-textrectsize-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextLayoutResult](arkts-arkgraphics2d-text-textlayoutresult-i.md) |

## Examples

```TypeScript
let size: text.TextRectSize = { width: 200, height: 100 };
let result = paragraph.layoutWithConstraints(size); // Enhanced layoutSync
console.info('Width: ' + result.correctRect.width + ', Height: ' + result.correctRect.height);
for (let i = 0; i < result.fitStrRange.length; ++i) {
  console.info('fitRange: [' + result.fitStrRange[i].start + ', ' + result.fitStrRange[i].end + ']');
}
```

## paint

```TypeScript
paint(canvas: drawing.Canvas, x: number, y: number): void
```

Draws text on the canvas with (x, y) as the upper-left corner. You must call [layout()](#layout) for typesetting before calling this API; otherwise, the text content cannot be displayed correctly.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-paint(canvas: drawing.Canvas, x: double, y: double): void--><!--Device-Paragraph-paint(canvas: drawing.Canvas, x: double, y: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| canvas | drawing.Canvas | Yes |
| x | number | Yes |
| y | number | Yes |

## Examples

```TypeScript
const color: ArrayBuffer = new ArrayBuffer(160000);
let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 200, width: 200 } }
let pixelMap: image.PixelMap = image.createPixelMapSync(color, opts);
let canvas = new drawing.Canvas(pixelMap);
paragraph.paint(canvas, 0, 0);
```

## paintOnPath

```TypeScript
paintOnPath(canvas: drawing.Canvas, path: drawing.Path, hOffset: number, vOffset: number): void
```

Draws text along a path on the canvas. You must call [layout()](#layout) for typesetting before calling this API; otherwise, the text content cannot be displayed correctly.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-paintOnPath(canvas: drawing.Canvas, path: drawing.Path, hOffset: double, vOffset: double): void--><!--Device-Paragraph-paintOnPath(canvas: drawing.Canvas, path: drawing.Path, hOffset: double, vOffset: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| canvas | drawing.Canvas | Yes |
| path | drawing.Path | Yes |
| hOffset | number | Yes |
| vOffset | number | Yes |

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

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-updateColor(color: common2D.Color): void--><!--Device-Paragraph-updateColor(color: common2D.Color): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | common2D.Color | Yes |

## Examples

```TypeScript
paragraph.updateColor({ alpha: 255, red: 255, green: 0, blue: 0 });
```

## updateDecoration

```TypeScript
updateDecoration(decoration: Decoration): void
```

Updates the decoration line of the entire text span.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-updateDecoration(decoration: Decoration): void--><!--Device-Paragraph-updateDecoration(decoration: Decoration): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| decoration | [Decoration](arkts-arkgraphics2d-text-decoration-i.md) | Yes |

## Examples

```TypeScript
paragraph.updateDecoration({
  textDecoration: text.TextDecorationType.OVERLINE,
  color: { alpha: 255, red: 255, green: 0, blue: 0 },
  decorationStyle: text.TextDecorationStyle.WAVY,
  decorationThicknessScale: 2.0,
});
```
