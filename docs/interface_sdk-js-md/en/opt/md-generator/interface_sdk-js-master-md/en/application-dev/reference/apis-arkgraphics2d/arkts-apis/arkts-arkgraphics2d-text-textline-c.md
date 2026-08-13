# TextLine

Implements a carrier that describes the basic text line structure of a paragraph. Before calling any of the following APIs, you must use [getTextLines()](arkts-arkgraphics2d-text-paragraph-c.md#getTextLines) of the [Paragraph](arkts-arkgraphics2d-text-paragraph-c.md#Paragraph) class or [createLine()](arkts-arkgraphics2d-text-linetypeset-c.md#createLine) of the [LineTypeset](arkts-arkgraphics2d-text-linetypeset-c.md#LineTypeset) class to create a **TextLine** object.

**Since:** 23

**Deprecated since:** -1

<!--Device-text-class TextLine--><!--Device-text-class TextLine-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { text } from '@kit.ArkGraphics2D';
```

## createTruncatedLine

```TypeScript
createTruncatedLine(width: number, ellipsisMode: EllipsisMode, ellipsis: string): TextLine
```

Creates a truncated text line object.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TextLine-createTruncatedLine(width: double, ellipsisMode: EllipsisMode, ellipsis: string): TextLine--><!--Device-TextLine-createTruncatedLine(width: double, ellipsisMode: EllipsisMode, ellipsis: string): TextLine-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| width | number | Yes |
| ellipsisMode | [EllipsisMode](../../apis-na/arkts-apis/arkts-na-enums-ellipsismode-e.md) | Yes |
| [ellipsis](arkts-arkgraphics2d-text-textstyle-i.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextLine](arkts-arkgraphics2d-text-textline-c.md) |

## Examples

```TypeScript
import { drawing, text } from '@kit.ArkGraphics2D'
import { image } from '@kit.ImageKit'

function textFunc(pixelmap: PixelMap) {
  let canvas = new drawing.Canvas(pixelmap);
  let truncatedTextLine = lines[0].createTruncatedLine(100, text.EllipsisMode.START, "...");
  truncatedTextLine.paint(canvas, 0, 100);
}

@Entry
@Component
struct Index {
  @State pixelmap?: PixelMap = undefined;
  fun: Function = textFunc;
  build() {
    Column() {
      Image(this.pixelmap).width(200).height(200);
      Button().onClick(() => {
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

## createTruncatedLine

```TypeScript
createTruncatedLine(width: number, ellipsisMode: EllipsisMode, ellipsis: string): TextLine | undefined
```

Creates a truncated text line object.

**Since:** 23

**Deprecated since:** -1

<!--Device-TextLine-createTruncatedLine(width: double, ellipsisMode: EllipsisMode, ellipsis: string): TextLine | undefined--><!--Device-TextLine-createTruncatedLine(width: double, ellipsisMode: EllipsisMode, ellipsis: string): TextLine | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| width | number | Yes |
| ellipsisMode | [EllipsisMode](../../apis-na/arkts-apis/arkts-na-enums-ellipsismode-e.md) | Yes |
| [ellipsis](arkts-arkgraphics2d-text-textstyle-i.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextLine](arkts-arkgraphics2d-text-textline-c.md) |

## enumerateCaretOffsets

```TypeScript
enumerateCaretOffsets(callback: CaretOffsetsCallback): void
```

Enumerates the offset and index of each character in a text line.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TextLine-enumerateCaretOffsets(callback: CaretOffsetsCallback): void--><!--Device-TextLine-enumerateCaretOffsets(callback: CaretOffsetsCallback): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [CaretOffsetsCallback](arkts-arkgraphics2d-text-caretoffsetscallback-t.md) | Yes |

## Examples

```TypeScript
lines[0].enumerateCaretOffsets((offset: number, index: number, leadingEdge: boolean): boolean => {
  console.info('textLine: offset: ' + offset + ', index: ' + index + ', leadingEdge: ' + leadingEdge);
  return index > 50;
});
```

## getAlignmentOffset

```TypeScript
getAlignmentOffset(alignmentFactor: number, alignmentWidth: number): number
```

Obtains the offset of this text line after alignment based on the alignment factor and alignment width.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TextLine-getAlignmentOffset(alignmentFactor: double, alignmentWidth: double): double--><!--Device-TextLine-getAlignmentOffset(alignmentFactor: double, alignmentWidth: double): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| alignmentFactor | number | Yes |
| alignmentWidth | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let alignmentOffset = lines[0].getAlignmentOffset(0.5, 500);
```

## getGlyphCount

```TypeScript
getGlyphCount(): number
```

Obtains the number of glyphs in this text line.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TextLine-getGlyphCount(): int--><!--Device-TextLine-getGlyphCount(): int-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let glyphCount = lines[0].getGlyphCount();
```

## getGlyphRuns

```TypeScript
getGlyphRuns(): Array<Run>
```

Obtains the array of glyph runs in the text line.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TextLine-getGlyphRuns(): Array<Run>--><!--Device-TextLine-getGlyphRuns(): Array<Run>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[Run](arkts-arkgraphics2d-text-run-c.md)&gt; |

## Examples

```TypeScript
let runs = lines[0].getGlyphRuns();
```

## getImageBounds

```TypeScript
getImageBounds(): common2D.Rect
```

Obtains the image boundaries of this text line. The image boundaries, equivalent to visual boundaries, depend on the font, font size, and characters. For example, for the string " a b " (which has a space before "a" and a space after "b"), only "a b" is visible to users, and therefore the image boundaries do not include these spaces at the beginning and end of the line. For the strings "j" and "E", their image boundaries are different. Specifically, the width of the boundary for "j" is narrower than that for "E", and the height of the boundary for "j" is taller than that for "E". > **NOTE：**> > The figure shows the image boundaries for the string " a b ". > >  > > The figure shows the image boundaries for the string "j" or "E". > > 

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TextLine-getImageBounds(): common2D.Rect--><!--Device-TextLine-getImageBounds(): common2D.Rect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| common2D.Rect |

## Examples

```TypeScript
let imageBounds = lines[0].getImageBounds();
```

## getOffsetForStringIndex

```TypeScript
getOffsetForStringIndex(index: number): number
```

Obtains the offset of a character with the specified index in this text line.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TextLine-getOffsetForStringIndex(index: int): double--><!--Device-TextLine-getOffsetForStringIndex(index: int): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let offset = lines[0].getOffsetForStringIndex(3);
```

## getStringIndexForPosition

```TypeScript
getStringIndexForPosition(point: common2D.Point): number
```

Obtains the index of a character at the specified position in the original string.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TextLine-getStringIndexForPosition(point: common2D.Point): int--><!--Device-TextLine-getStringIndexForPosition(point: common2D.Point): int-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| point | common2D.Point | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let point : common2D.Point = { x: 15.0, y: 2.0 };
let index = lines[0].getStringIndexForPosition(point);
```

## getTextRange

```TypeScript
getTextRange(): Range
```

Obtains the range of the text in this text line in the entire paragraph.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TextLine-getTextRange(): Range--><!--Device-TextLine-getTextRange(): Range-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) |

## Examples

```TypeScript
let textRange = lines[0].getTextRange();
```

## getTrailingSpaceWidth

```TypeScript
getTrailingSpaceWidth(): number
```

Obtains the width of the spaces at the end of this text line.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TextLine-getTrailingSpaceWidth(): double--><!--Device-TextLine-getTrailingSpaceWidth(): double-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let trailingSpaceWidth = lines[0].getTrailingSpaceWidth();
```

## getTypographicBounds

```TypeScript
getTypographicBounds(): TypographicBounds
```

Obtains the typographic boundaries of the text line. These boundaries depend on the typographic font and font size, but not on the characters themselves. For example, for the string " a b " (which has a space before "a" and a space after "b"), the typographic boundaries include the spaces at the beginning and end of the line. Similarly, the strings "j" and "E" have identical typographic boundaries, independent of the characters themselves. > **NOTE：**> > The figure shows the typesetting boundaries for the string " a b ". > >  > > The figure shows the typesetting boundaries for the string "j" or "E". > > ! > [TypographicBounds-Character.png](../../../reference/apis-arkgraphics2d/figures/TypographicBounds-Character.png)

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TextLine-getTypographicBounds(): TypographicBounds--><!--Device-TextLine-getTypographicBounds(): TypographicBounds-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TypographicBounds](arkts-arkgraphics2d-text-typographicbounds-i.md) |

## Examples

```TypeScript
let bounds = lines[0].getTypographicBounds();
console.info('textLine ascent:' + bounds.ascent + ', descent:' + bounds.descent + ', leading:' + bounds.leading + ', width:' + bounds.width);
```

## paint

```TypeScript
paint(canvas: drawing.Canvas, x: number, y: number): void
```

Paints this text line on the canvas with the coordinate point (x, y) as the upper left corner.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-TextLine-paint(canvas: drawing.Canvas, x: double, y: double): void--><!--Device-TextLine-paint(canvas: drawing.Canvas, x: double, y: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| canvas | drawing.Canvas | Yes |
| x | number | Yes |
| y | number | Yes |

## Examples

```TypeScript
import { drawing } from '@kit.ArkGraphics2D'
import { image } from '@kit.ImageKit'

function textFunc(pixelmap: PixelMap) {
  let canvas = new drawing.Canvas(pixelmap);
  lines[0].paint(canvas, 0, 0);
}

@Entry
@Component
struct Index {
  @State pixelmap?: PixelMap = undefined;
  fun: Function = textFunc;
  build() {
    Column() {
      Image(this.pixelmap).width(200).height(200);
      Button().onClick(() => {
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
