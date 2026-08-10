# Paragraph

保存文本内容及样式的载体，支持排版与绘制操作。

下列API示例中都需先使用[ParagraphBuilder](arkts-arkgraphics2d-text-paragraphbuilder-c.md)类的[build()](arkts-arkgraphics2d-text-paragraphbuilder-c.md#build)接口获取到Paragraph对象实例，再通过此实例调用对应方法。

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

返回段落是否超过最大行数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-didExceedMaxLines(): boolean--><!--Device-Paragraph-didExceedMaxLines(): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true表示段落超出了最大行限制，false则表示没有超出最大行限制。 |

## Examples

```TypeScript
let didExceed = paragraph.didExceedMaxLines();
```

## forceReuseRasterResult

```TypeScript
forceReuseRasterResult(isForce: boolean): void
```

设置是否强制复用光栅化结果。不调用此接口时，系统默认允许更新光栅化结果。

适用于文本内容未发生变化但需要多次调用[paint](arkts-arkgraphics2d-text-paragraph-c.md#paint)绘制的场景，通过复用光栅化结果可避免重复光栅化计算以提升绘制性能。设置后，在下次调用  
[paint](arkts-arkgraphics2d-text-paragraph-c.md#paint)绘制时生效。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Paragraph-forceReuseRasterResult(isForce: boolean): void--><!--Device-Paragraph-forceReuseRasterResult(isForce: boolean): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isForce | boolean | Yes | 是否强制复用光栅化结果。true表示强制复用光栅化结果，false表示允许更新光栅化结果。 |

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

ArkTS-Dyn:
```TypeScript
getActualTextRange(lineNumber: number, includeSpaces: boolean): Range
```

ArkTS-Sta:
```TypeScript
getActualTextRange(lineNumber: int, includeSpaces: boolean): Range
```

获取指定行的实际可见文本范围，不包括溢出的省略号。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getActualTextRange(lineNumber: int, includeSpaces: boolean): Range--><!--Device-Paragraph-getActualTextRange(lineNumber: int, includeSpaces: boolean): Range-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lineNumber | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 要获取文本范围的行索引，行索引从0开始。该接口只能获取已有行的边界，即输入行索引从0开始。最大行索引为文本行数量-1，文本行数量可通过 [getLineCount](arkts-arkgraphics2d-text-paragraph-c.md#getlinecount)接口获取。 |
| includeSpaces | boolean | Yes | 表示是否应包含空白字符。true表示包含空白字符，false表示不包含空白字符。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | 返回对应行数的实际文本范围。如果行索引非法，返回的start和end均为0。 |

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

获取拉丁字母基线位置。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getAlphabeticBaseline(): double--><!--Device-Paragraph-getAlphabeticBaseline(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | 拉丁字母下的基线位置，浮点数，单位为物理像素px。 |

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

获取与给定坐标最接近的字符位置信息。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-Paragraph-getCharacterPositionAtCoordinate(x: double, y: double, encoding: drawing.TextEncoding): PositionWithAffinity--><!--Device-Paragraph-getCharacterPositionAtCoordinate(x: double, y: double, encoding: drawing.TextEncoding): PositionWithAffinity-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 文本排版区域内的水平坐标，单位为物理像素（px）。相对于文本排版区域左上角的x偏移量，向右为正方向。支持浮点数，可取负值（表示在文本区域左侧）。坐标超出文本区域范围时，将返回最近的字 符位置。可通过触摸事件或点击事件获取。 |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 文本排版区域内的垂直坐标，单位为物理像素（px）。相对于文本排版区域左上角的y偏移量，向下为正方向。支持浮点数，可取负值（表示在文本区域上方）。坐标超出文本区域范围时，将返回最近的字 符位置。可通过触摸事件或点击事件获取。 |
| encoding | drawing.TextEncoding | Yes | 文本编码类型。目前仅支持UTF-8和UTF-16编码类型。对于UTF-8编码，返回的字符位置表示字节偏移量。对于UTF-16编码，返回的字符 位置表示UTF-16编码单元偏移量。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PositionWithAffinity](../../apis-arkui/arkts-apis/arkts-arkui-positionwithaffinity-i.md) | 字符位置信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 25900001 | Parameter error. Possible causes: Incorrect parameter range. |

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

获取指定字形范围对应的字符范围。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-Paragraph-getCharacterRangeForGlyphRange(glyphRange: Range, encoding: drawing.TextEncoding): Array<Range>--><!--Device-Paragraph-getCharacterRangeForGlyphRange(glyphRange: Range, encoding: drawing.TextEncoding): Array<Range>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| glyphRange | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes | 字形范围。 |
| encoding | drawing.TextEncoding | Yes | 文本编码类型。目前仅支持UTF-8和UTF-16编码类型。对于UTF-8编码，返回的字符范围表示字节范围。对于UTF-16编码，返回的字符范 围表示UTF-16编码单元范围。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;Range&gt; | 字符范围。如果数组包含一个元素，它表示字符范围。如果包含两个元素，第一个是字符范围，第二个是实际的字形范围。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 25900001 | Parameter error. Possible causes: Incorrect parameter range. |

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

ArkTS-Dyn:
```TypeScript
getGlyphPositionAtCoordinate(x: number, y: number): PositionWithAffinity
```

ArkTS-Sta:
```TypeScript
getGlyphPositionAtCoordinate(x: double, y: double): PositionWithAffinity
```

获取与给定坐标最接近的字形位置信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getGlyphPositionAtCoordinate(x: double, y: double): PositionWithAffinity--><!--Device-Paragraph-getGlyphPositionAtCoordinate(x: double, y: double): PositionWithAffinity-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 横坐标，浮点数，单位为物理像素px。 |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 纵坐标，浮点数，单位为物理像素px。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PositionWithAffinity](../../apis-arkui/arkts-apis/arkts-arkui-positionwithaffinity-i.md) | 字形位置信息。 |

## Examples

```TypeScript
let positionWithAffinity = paragraph.getGlyphPositionAtCoordinate(0, 0);
```

## getGlyphRangeForCharacterRange

```TypeScript
getGlyphRangeForCharacterRange(characterRange: Range, encoding: drawing.TextEncoding): Array<Range>
```

获取指定字符范围对应的字形范围。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-Paragraph-getGlyphRangeForCharacterRange(characterRange: Range, encoding: drawing.TextEncoding): Array<Range>--><!--Device-Paragraph-getGlyphRangeForCharacterRange(characterRange: Range, encoding: drawing.TextEncoding): Array<Range>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| characterRange | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes | 字符范围。 |
| encoding | drawing.TextEncoding | Yes | 文本编码类型。目前仅支持UTF-8和UTF-16编码类型。对于UTF-8编码，返回的实际字符范围表示字节范围。对于UTF-16编码，返回的实 际字符范围表示UTF-16编码单元范围。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;Range&gt; | 字形范围。数组包含两个元素，第一个是字形范围，第二个是实际的字符范围。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 25900001 | Parameter error. Possible causes: Incorrect parameter range. |

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

ArkTS-Dyn:
```TypeScript
getHeight(): number
```

ArkTS-Sta:
```TypeScript
getHeight(): double
```

获取文本总高度。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getHeight(): double--><!--Device-Paragraph-getHeight(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | 总高度，浮点数，单位为物理像素px。 |

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

获取表意字（如CJK（中文，日文，韩文））下的基线位置。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getIdeographicBaseline(): double--><!--Device-Paragraph-getIdeographicBaseline(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | 表意字下的基线位置，浮点数，单位为物理像素px。 |

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

返回文本行数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getLineCount(): int--><!--Device-Paragraph-getLineCount(): int-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 文本行数量，整数。 |

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

返回指定行的行高。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getLineHeight(line: int): double--><!--Device-Paragraph-getLineHeight(line: int): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| line | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 文本行索引，整数，范围为0~[getLineCount](arkts-arkgraphics2d-text-paragraph-c.md#getlinecount)-1。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | 行高，单位为物理像素px。 |

## Examples

```TypeScript
let lineHeight = paragraph.getLineHeight(0);
```

## getLineMetrics

```TypeScript
getLineMetrics(): Array<LineMetrics>
```

获取文本行的行度量数组。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getLineMetrics(): Array<LineMetrics>--><!--Device-Paragraph-getLineMetrics(): Array<LineMetrics>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;LineMetrics&gt; | 文本行的行度量数组。 |

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

获取特定行号的行度量信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getLineMetrics(lineNumber: int): LineMetrics | undefined--><!--Device-Paragraph-getLineMetrics(lineNumber: int): LineMetrics | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lineNumber | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 要查询度量信息的行的编号，行号从0开始，最大行索引为文本行数量-1，文本行数量可通过 [getLineCount](arkts-arkgraphics2d-text-paragraph-c.md#getlinecount)接口获取。 |

**Return value:**

| Type | Description |
| --- | --- |
| [LineMetrics](../../apis-arkui/arkts-apis/arkts-arkui-linemetrics-t.md) | 如果指定的行号有效且度量信息存在，则返回一个包含该行度量数据的LineMetrics对象；如果行号无效或无法获取度量信息，则返回undefined。 |

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

返回指定行的行宽。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getLineWidth(line: int): double--><!--Device-Paragraph-getLineWidth(line: int): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| line | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 文本行索引，整数，范围为0~[getLineCount](arkts-arkgraphics2d-text-paragraph-c.md#getlinecount)-1。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | 行宽，单位为物理像素px。 |

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

获取文本最长行宽。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getLongestLine(): double--><!--Device-Paragraph-getLongestLine(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | 最长一行的宽度，浮点数，单位为物理像素px。 |

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

获取文本最长一行的宽度（包含缩进），建议向上取整。文本内容为空时返回0。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getLongestLineWithIndent(): double--><!--Device-Paragraph-getLongestLineWithIndent(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | 最长一行的宽度（该宽度包含当前行缩进的宽度），浮点数，单位为物理像素px。 |

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

获取段落最大固有宽度。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getMaxIntrinsicWidth(): double--><!--Device-Paragraph-getMaxIntrinsicWidth(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | 该段落所占水平空间的最大固有宽度，浮点数，单位为物理像素px。 |

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

获取文本最大行宽。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getMaxWidth(): double--><!--Device-Paragraph-getMaxWidth(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | 最大的行宽，浮点数，单位为物理像素px。 |

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

获取段落最小固有宽度。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getMinIntrinsicWidth(): double--><!--Device-Paragraph-getMinIntrinsicWidth(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | 该段落所占水平空间的最小固有宽度，浮点数，单位为物理像素px。 |

## Examples

```TypeScript
let minIntrinsicWidth = paragraph.getMinIntrinsicWidth();
```

## getParagraphStyle

```TypeScript
getParagraphStyle(): ParagraphStyle
```

获取段落的样式配置。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Paragraph-getParagraphStyle(): ParagraphStyle--><!--Device-Paragraph-getParagraphStyle(): ParagraphStyle-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md) | 段落的样式配置。 &lt;br&gt;其中`textStyle.color`、`textStyle.textShadows.color`、`textStyle.backgroundRect.color`、 `textStyle.decoration.color`属性：返回32位无符号整型颜色数值。示例：返回值`4278190080`，对应纯黑色十六进制颜色值`0xFF000000`，等价于 [common2D.Color]{ |

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

获取段落的文本处理状态。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Paragraph-getProcessState(): TextProcessState--><!--Device-Paragraph-getProcessState(): TextProcessState-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [TextProcessState](arkts-arkgraphics2d-text-textprocessstate-e.md) | 段落的文本处理状态。 |

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

获取文本中所有占位符所占的矩形区域。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getRectsForPlaceholders(): Array<TextBox>--><!--Device-Paragraph-getRectsForPlaceholders(): Array<TextBox>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;TextBox&gt; | 矩形区域数组。 |

## Examples

```TypeScript
let placeholderRects = paragraph.getRectsForPlaceholders();
```

## getRectsForRange

```TypeScript
getRectsForRange(range: Range, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>
```

获取给定的矩形区域宽度以及矩形区域高度的规格下，文本中该区间范围内的字符所占的矩形区域。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getRectsForRange(range: Range, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>--><!--Device-Paragraph-getRectsForRange(range: Range, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes | 需要获取的区域的文本区间。 |
| widthStyle | [RectWidthStyle](../../apis-arkui/arkts-apis/arkts-arkui-rectwidthstyle-t.md) | Yes | 返回的矩形区域的宽度的规格。 |
| heightStyle | [RectHeightStyle](arkts-arkgraphics2d-text-rectheightstyle-e.md) | Yes | 返回的矩形区域的高度的规格。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;TextBox&gt; | 矩形区域数组。 |

## Examples

```TypeScript
let range: text.Range = { start: 0, end: 1};
let rects = paragraph.getRectsForRange(range, text.RectWidthStyle.TIGHT, text.RectHeightStyle.TIGHT);
```

## getTextDisplayState

```TypeScript
getTextDisplayState(): TextDisplayState
```

获取段落的文本显示状态。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Paragraph-getTextDisplayState(): TextDisplayState--><!--Device-Paragraph-getTextDisplayState(): TextDisplayState-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [TextDisplayState](arkts-arkgraphics2d-text-textdisplaystate-e.md) | 段落的文本显示状态。 |

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

返回所有的文本行。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getTextLines(): Array<TextLine>--><!--Device-Paragraph-getTextLines(): Array<TextLine>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;TextLine&gt; | 文本行载体数组。 |

## Examples

```TypeScript
let lines = paragraph.getTextLines();
```

## getVisibleTextRanges

```TypeScript
getVisibleTextRanges(): Array<Range>
```

获取段落中在屏幕上可见的文本范围。不包含因最大行数（[ParagraphStyle](arkts-arkgraphics2d-text-paragraphstyle-i.md)的maxLines属性）截断或省略号模式（  
[EllipsisMode](arkts-arkgraphics2d-text-ellipsismode-e.md)）替换而未显示的文本。

**说明：**

返回的范围取决于段落的具体截断情况（如是否设置最大行数或省略号等）：  
| 场景 | 说明 |  
|---|---|  
| 文本未被截断 | 范围包含全部已排版文本 |  
| 仅设置maxLines截断（未设置省略号） | 范围为实际显示的文本，即第一行至第maxLines行末尾的文本。 |  
| 尾部省略（EllipsisMode.END） | 范围为省略号之前的文本。 |  
| 头部省略（EllipsisMode.START） | 范围为省略号之后的文本。 |  
| 中部省略（EllipsisMode.MIDDLE） | 第一个范围为省略号之前的文本，第二个范围为省略号之后的文本。 |  
| 多行头部省略（EllipsisMode.MULTILINE_START） | 同中部省略，返回省略号前后的文本范围。 |  
| 多行中部省略（EllipsisMode.MULTILINE_MIDDLE） | 同中部省略，返回省略号前后的文本范围。 |

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Paragraph-getVisibleTextRanges(): Array<Range>--><!--Device-Paragraph-getVisibleTextRanges(): Array<Range>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;Range&gt; | 段落可见文本范围数组，范围为UTF-16编码单元索引。 |

## Examples

```TypeScript
let visibleRanges = paragraph.getVisibleTextRanges();
```

## getWordBoundary

ArkTS-Dyn:
```TypeScript
getWordBoundary(offset: number): Range
```

ArkTS-Sta:
```TypeScript
getWordBoundary(offset: int): Range
```

返回给定offset的字形所在单词的索引区间。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-getWordBoundary(offset: int): Range--><!--Device-Paragraph-getWordBoundary(offset: int): Range-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 字形的偏移量，整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | 单词的索引区间。 |

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

进行排版并计算所有字形位置，使用Promise异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-layout(width: double): Promise<void>--><!--Device-Paragraph-layout(width: double): Promise<void>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 单行的最大宽度，浮点数，单位为物理像素px。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

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

ArkTS-Dyn:
```TypeScript
layoutSync(width: number): void
```

ArkTS-Sta:
```TypeScript
layoutSync(width: double): void
```

进行排版并计算所有字形位置。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-layoutSync(width: double): void--><!--Device-Paragraph-layoutSync(width: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 单行的最大宽度，浮点数，单位为物理像素px。 |

## Examples

```TypeScript
paragraph.layoutSync(100);
```

## layoutWithConstraints

```TypeScript
layoutWithConstraints(size: TextRectSize): TextLayoutResult
```

使用给定的高度和宽度进行排版并计算所有字形的位置。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-Paragraph-layoutWithConstraints(size: TextRectSize): TextLayoutResult--><!--Device-Paragraph-layoutWithConstraints(size: TextRectSize): TextLayoutResult-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | [TextRectSize](arkts-arkgraphics2d-text-textrectsize-i.md) | Yes | 约束的高度和宽度，单位为物理像素px。 |

**Return value:**

| Type | Description |
| --- | --- |
| [TextLayoutResult](arkts-arkgraphics2d-text-textlayoutresult-i.md) | 布局后的实际尺寸和排版后容下的字符范围。 |

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

ArkTS-Dyn:
```TypeScript
paint(canvas: drawing.Canvas, x: number, y: number): void
```

ArkTS-Sta:
```TypeScript
paint(canvas: drawing.Canvas, x: double, y: double): void
```

在画布上以 (x, y) 为左上角绘制文本。调用前必须先调用[layout()](arkts-arkgraphics2d-text-paragraph-c.md#layout)接口进行排版，否则无法正确显示文本内容。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-paint(canvas: drawing.Canvas, x: double, y: double): void--><!--Device-Paragraph-paint(canvas: drawing.Canvas, x: double, y: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| canvas | drawing.Canvas | Yes | 绘制的目标画布。 |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 绘制的左上角位置的横坐标，浮点数，单位为物理像素px。 |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 绘制的左上角位置的纵坐标，浮点数，单位为物理像素px。 |

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

在画布上沿路径绘制文本。调用前必须先调用[layout()](arkts-arkgraphics2d-text-paragraph-c.md#layout)接口进行排版，否则无法正确显示文本内容。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-paintOnPath(canvas: drawing.Canvas, path: drawing.Path, hOffset: double, vOffset: double): void--><!--Device-Paragraph-paintOnPath(canvas: drawing.Canvas, path: drawing.Path, hOffset: double, vOffset: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| canvas | drawing.Canvas | Yes | 绘制的目标画布。 |
| path | drawing.Path | Yes | 确认文字位置的路径。 |
| hOffset | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 沿路径方向偏置，从路径起点向前为正，向后为负，单位为物理像素px。 |
| vOffset | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 沿路径垂直方向偏置，沿路径方向左侧为负，右侧为正，单位为物理像素px。 |

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

更新整个文本段落的颜色。如果当前装饰线未设置颜色，使用该接口也会同时更新装饰线的颜色。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-updateColor(color: common2D.Color): void--><!--Device-Paragraph-updateColor(color: common2D.Color): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | common2D.Color | Yes | 更新后的字体色。 |

## Examples

```TypeScript
paragraph.updateColor({ alpha: 255, red: 255, green: 0, blue: 0 });
```

## updateDecoration

```TypeScript
updateDecoration(decoration: Decoration): void
```

更新整个文本段落的装饰线。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Paragraph-updateDecoration(decoration: Decoration): void--><!--Device-Paragraph-updateDecoration(decoration: Decoration): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| decoration | [Decoration](arkts-arkgraphics2d-text-decoration-i.md) | Yes | 更新后的装饰线。 |

## Examples

```TypeScript
paragraph.updateDecoration({
  textDecoration: text.TextDecorationType.OVERLINE,
  color: { alpha: 255, red: 255, green: 0, blue: 0 },
  decorationStyle: text.TextDecorationStyle.WAVY,
  decorationThicknessScale: 2.0,
});
```

