# Run

Represents a text typesetting unit, which is a continuous text segment with the same style attributes. Run is obtained through the [getGlyphRuns()](arkts-arkgraphics2d-text-textline-c.md#getGlyphRuns) API of the [TextLine](arkts-arkgraphics2d-text-textline-c.md#TextLine)class.

Before calling any of the following APIs, you must use [getGlyphRuns()](arkts-arkgraphics2d-text-textline-c.md#getGlyphRuns) of the  
[TextLine](arkts-arkgraphics2d-text-textline-c.md#TextLine) class to create a **Run** object.

**Since:** 12

<!--Device-text-class Run--><!--Device-text-class Run-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { text } from '@kit.ArkGraphics2D';
```

## getAdvances

```TypeScript
getAdvances(range: Range): Array<common2D.Point>
```

Obtains the glyph width array of each glyph within the specified range of the run.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-getAdvances(range: Range): Array<common2D.Point>--><!--Device-Run-getAdvances(range: Range): Array<common2D.Point>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;common2D.Point & gt; |

## Examples

```TypeScript
let advancesRange = runs[0].getAdvances({start:1, end:2}); // Obtain the widths of glyphs in the range starting from position 1, with a length of 2.
advancesRange = runs[0].getAdvances({start:-1, end:2}); // -1 is an invalid value, and undefined is returned.
advancesRange = runs[0].getAdvances({start:0, end:-10}); // -10 is an invalid value, and undefined is returned.
let advancesNull = runs[0].getAdvances(null); // null is an invalid value, and undefined is returned.
```

## getFont

```TypeScript
getFont(): drawing.Font
```

Obtains the **Font** object of this run.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-getFont(): drawing.Font--><!--Device-Run-getFont(): drawing.Font-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| drawing.Font |

## Examples

```TypeScript
let font = runs[0].getFont();
```

## getGlyphCount

```TypeScript
getGlyphCount(): number
```

Obtains the number of glyphs in this run.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-getGlyphCount(): int--><!--Device-Run-getGlyphCount(): int-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## Examples

```TypeScript
let glyphs = runs[0].getGlyphCount();
```

## getGlyphs

```TypeScript
getGlyphs(): Array<number>
```

Obtains the index of each glyph in this run.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-getGlyphs(): Array<int>--><!--Device-Run-getGlyphs(): Array<int>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;number & gt; |

## Examples

```TypeScript
let glyph = runs[0].getGlyphs();
```

## getGlyphs

```TypeScript
getGlyphs(range: Range): Array<number>
```

Obtains the index of each glyph in the specified range of this run.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-getGlyphs(range: Range): Array<int>--><!--Device-Run-getGlyphs(range: Range): Array<int>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;number & gt; |

## Examples

```TypeScript
import { text } from '@kit.ArkGraphics2D'

function textFunc() {
  let glyphs = runs[0].getGlyphs(); // Obtain the index of all glyphs of the run.
  let glyphsRange = runs[0].getGlyphs({start:1, end:2}); // Obtain the glyph indices within the range starting at position 1 with a length of 2 from the rendered block.
  glyphsRange = runs[0].getGlyphs({start:-1, end:2}); // -1 is an invalid value, and undefined is returned.
  glyphsRange = runs[0].getGlyphs({start:0, end:-10}); // -10 is an invalid value, and undefined is returned.
  let glyphsNull = runs[0].getGlyphs(null); // null is an invalid value, and undefined is returned.
  let glyphsUndefined = runs[0].getGlyphs(undefined); // undefined is an invalid value, and undefined is returned.
}

@Entry
@Component
struct Index {
  fun: Function = textFunc;
  build() {
    Column() {
      Button().onClick(() => {
        this.fun();
      })
    }
  }
}
```

## getImageBounds

```TypeScript
getImageBounds(): common2D.Rect
```

Obtains the image boundaries of the typographic unit. Equivalent to visual boundaries, these boundaries are associated with the typographic font, font size, and characters. For example, for the string " a b " (which has a space before "a" and a space after "b"), only "a b" is visible to users, and therefore the image boundaries do not include these spaces at the beginning and end of the line.

> **NOTE：**
> 
> The figure shows the image boundaries for the string " a b ".
> 
> ![ImageBounds.png](../../../reference/apis-arkgraphics2d/figures/ImageBounds.png)
> 
> The figure shows the image boundaries for the string "j" or "E".
> 
> ![ImageBounds-Character.png](../../../reference/apis-arkgraphics2d/figures/ImageBounds-Character.png)

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-getImageBounds(): common2D.Rect--><!--Device-Run-getImageBounds(): common2D.Rect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| common2D.Rect |

## Examples

```TypeScript
let bounds = runs[0].getImageBounds();
```

## getOffsets

```TypeScript
getOffsets(): Array<common2D.Point>
```

Obtains the offset of each glyph in this run relative to its index.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-getOffsets(): Array<common2D.Point>--><!--Device-Run-getOffsets(): Array<common2D.Point>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;common2D.Point & gt; |

## Examples

```TypeScript
let offsets = runs[0].getOffsets();
```

## getPositions

```TypeScript
getPositions(): Array<common2D.Point>
```

Obtains the position of each glyph relative to the respective line in this run.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-getPositions(): Array<common2D.Point>--><!--Device-Run-getPositions(): Array<common2D.Point>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;common2D.Point & gt; |

## Examples

```TypeScript
let positions = runs[0].getPositions();
```

## getPositions

```TypeScript
getPositions(range: Range): Array<common2D.Point>
```

Obtains the position array of each glyph relative to the respective line within the specified range of this run.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-getPositions(range: Range): Array<common2D.Point>--><!--Device-Run-getPositions(range: Range): Array<common2D.Point>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;common2D.Point & gt; |

## Examples

```TypeScript
import { text } from '@kit.ArkGraphics2D'

function textFunc() {
  let positions = runs[0].getPositions(); // Obtain the positions of all glyphs in the run.
  let positionsRange = runs[0].getPositions({start:1, end:2}); // Obtain the positions of glyphs in the range starting from position 1, with a length of 2.
  positionsRange = runs[0].getPositions({start:-1, end:2}); // -1 is an invalid value, and undefined is returned.
  positionsRange = runs[0].getPositions({start:0, end:-10}); // -10 is an invalid value, and undefined is returned.
  let positionsNull = runs[0].getPositions(null); // null is an invalid value, and undefined is returned.
  let positionsUndefined = runs[0].getPositions(undefined); // undefined is an invalid value, and undefined is returned.
}

@Entry
@Component
struct Index {
  fun: Function = textFunc;
  build() {
    Column() {
      Button().onClick(() => {
        this.fun();
      })
    }
  }
}
```

## getStringIndices

```TypeScript
getStringIndices(range?: Range): Array<number>
```

Obtains an array of character indices for glyphs within a specified range of this run, where the indices are offsets relative to the entire paragraph.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-getStringIndices(range?: Range): Array<int>--><!--Device-Run-getStringIndices(range?: Range): Array<int>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;number & gt; |

## Examples

```TypeScript
import { text } from '@kit.ArkGraphics2D'

function textFunc() {
  let indices = runs[0].getStringIndices(); // Obtain the indices of all characters in the run.
  let indicesRange = runs[0].getStringIndices({start:1, end:2}); // Obtain the indices of characters in the range starting from position 1, with a length of 2.
  indicesRange = runs[0].getStringIndices({start:-1, end:2}); // -1 is an invalid value, and undefined is returned.
  indicesRange = runs[0].getStringIndices({start:0, end:-10}); // -10 is an invalid value, and undefined is returned.
  let indicesNull = runs[0].getStringIndices(null); // null is an invalid value, and undefined is returned.
  let indicesUndefined = runs[0].getStringIndices(undefined); // undefined is an invalid value, and undefined is returned.
}

@Entry
@Component
struct Index {
  fun: Function = textFunc;
  build() {
    Column() {
      Button().onClick(() => {
        this.fun();
      })
    }
  }
}
```

## getStringRange

```TypeScript
getStringRange(): Range
```

Obtains the range of glyphs generated by this run.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-getStringRange(): Range--><!--Device-Run-getStringRange(): Range-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) |

## Examples

```TypeScript
let runStringRange = runs[0].getStringRange();
let location = runStringRange.start;
let length = runStringRange.end;
```

## getTextDirection

```TypeScript
getTextDirection(): TextDirection
```

Obtains the text direction of the run.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-getTextDirection(): TextDirection--><!--Device-Run-getTextDirection(): TextDirection-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextDirection](arkts-arkgraphics2d-text-textdirection-e.md) |

## Examples

```TypeScript
let textDirection = runs[0].getTextDirection();
```

## getTextStyle

```TypeScript
getTextStyle(): TextStyle
```

Obtains the text style of this typesetting unit.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Run-getTextStyle(): TextStyle--><!--Device-Run-getTextStyle(): TextStyle-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TextStyle](../../apis-arkui/arkts-apis/arkts-arkui-styledstring-textstyle-c.md) |

## Examples

```TypeScript
// Index.ets
import { text } from "@kit.ArkGraphics2D"
import { common2D } from '@kit.ArkGraphics2D'
import { JSON } from "@kit.ArkTS";

function textFunc() {
  let textStyle: text.TextStyle = {
    color: { alpha: 255, red: 255, green: 0, blue: 0 },
    fontSize: 33,
  };
  let paragraphStyle: text.ParagraphStyle = {
    textStyle: textStyle,
    align: text.TextAlign.END,
  };
  let fontCollection = new text.FontCollection();
  let paragraphBuilder = new text.ParagraphBuilder(paragraphStyle, fontCollection);
  paragraphBuilder.addText("Hello World");
  let paragraph = paragraphBuilder.build();
  paragraph.layoutSync(50);
  let lines = paragraph.getTextLines();
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    let runs = line.getGlyphRuns();
    for (let j = 0; j < runs.length; j++) {
      const run = runs[j];
      const runStyle = run.getTextStyle();
      console.info(`print line [${i}] run [${j}] textStyle: ${JSON.stringify(runStyle)}`);
      if (runStyle?.color != undefined && typeof runStyle?.color == 'number') {
        let textColor: common2D.Color = numberToRGBA(runStyle?.color);
        console.info(`Print text color ARGB: ${textColor.alpha}, ${textColor.red}, ${textColor.green}, ${textColor.blue}`);
      }
    }
  }
}

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button("Click").onClick((e: ClickEvent) => {
        textFunc();
      })
    }
  }
}

function numberToRGBA(colorNum: number): common2D.Color {
  const alpha = (colorNum >>> 24) & 0xFF;
  const red = (colorNum >>> 16) & 0xFF;
  const green = (colorNum >>> 8) & 0xFF;
  const blue = colorNum & 0xFF;
  return { alpha: alpha, red: red, green: green, blue: blue };
}
```

## getTypographicBounds

```TypeScript
getTypographicBounds(): TypographicBounds
```

Obtains the typographic boundaries of the typographic unit. These boundaries are associated with the typographic font and font size, but not with the characters. For example, for the string " a b " (which has a space before "a" and a space after "b"), the typographic boundaries include the spaces at the beginning and end of the line.

> **NOTE：**
> 
> The figure shows the typesetting boundaries for the string " a b ".
> 
> ![TypographicBounds.png](../../../reference/apis-arkgraphics2d/figures/TypographicBounds.png)
> 
> The figure shows the typesetting boundaries for the string "j" or "E".
> 
> !
> [TypographicBounds-Character.png](../../../reference/apis-arkgraphics2d/figures/TypographicBounds-Character.png)

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-getTypographicBounds(): TypographicBounds--><!--Device-Run-getTypographicBounds(): TypographicBounds-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TypographicBounds](arkts-arkgraphics2d-text-typographicbounds-i.md) |

## Examples

```TypeScript
let typographicBounds = runs[0].getTypographicBounds();
```

## paint

```TypeScript
paint(canvas: drawing.Canvas, x: number, y: number): void
```

Paints this run on the canvas with the coordinate point (x, y) as the upper left corner.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-paint(canvas: drawing.Canvas, x: double, y: double): void--><!--Device-Run-paint(canvas: drawing.Canvas, x: double, y: double): void-End-->

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
import { text } from '@kit.ArkGraphics2D'
import { image } from '@kit.ImageKit'

function textFunc(pixelmap: PixelMap) {
  let canvas = new drawing.Canvas(pixelmap);
  runs[0].paint(canvas, 0, 0);
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
