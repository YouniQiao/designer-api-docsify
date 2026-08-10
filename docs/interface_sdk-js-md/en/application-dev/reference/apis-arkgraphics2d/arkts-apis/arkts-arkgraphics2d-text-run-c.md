# Run

文本排版单元，表示一段具有相同样式属性的连续文本片段。Run由[TextLine](arkts-arkgraphics2d-text-textline-c.md)类的[getGlyphRuns()](arkts-arkgraphics2d-text-textline-c.md#getglyphruns)接口获取。

下列API示例中都需先使用[TextLine](arkts-arkgraphics2d-text-textline-c.md)类的[getGlyphRuns()](arkts-arkgraphics2d-text-textline-c.md#getglyphruns)接口获取Run对象实例，再通过此实例调用对应方法。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-text-class Run--><!--Device-text-class Run-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## getAdvances

```TypeScript
getAdvances(range: Range): Array<common2D.Point>
```

获取该排版单元指定范围内每个字形的字形宽度数组。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-getAdvances(range: Range): Array<common2D.Point>--><!--Device-Run-getAdvances(range: Range): Array<common2D.Point>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes | 要获取的字形位置范围。range.start表示范围开始的位置，range.end表示范围的长度。如果长度是0表示从range.start开始获取到渲染块结束。当 range.end、range.start为负数，或者传入null、undefined时，该方法将返回undefined。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;common2D.Point&gt; | 返回该排版单元中每个字形相对于水平方向的字形宽度数组。其中， [common2D.Point]{ |

## Examples

```TypeScript
let advancesRange = runs[0].getAdvances({start:1, end:2}); // Obtain the widths of glyphs in the range starting from position 1, with a length of 2.
advancesRange = runs[0].getAdvances({start:-1, end:2}); // -1 is an invalid value, and undefined is returned.
advancesRange = runs[0].getAdvances({start:0, end:-10}); // -10 is an invalid value, and undefined is returned.
let advancesNull = runs[0].getAdvances(null); // null is an invalid value, and undefined is returned.
```

## getAdvances

```TypeScript
getAdvances(range: Range): Array<common2D.Point> | undefined
```

获取该排版单元指定范围内每个字形的字形宽度数组。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Run-getAdvances(range: Range): Array<common2D.Point> | undefined--><!--Device-Run-getAdvances(range: Range): Array<common2D.Point> | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes | 要获取的字形位置范围。range.start表示范围开始的位置，range.end表示范围的长度。如果长度是0表示从range.start开始获取到渲染块结束。当 range.end、range.start为负数，或者传入null、undefined时，该方法将返回undefined。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;common2D.Point&gt; | 返回该排版单元中每个字形相对于水平方向的字形宽度数组。其中， [common2D.Point]{ |

## getFont

```TypeScript
getFont(): drawing.Font
```

获取排版单元的字体属性对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-getFont(): drawing.Font--><!--Device-Run-getFont(): drawing.Font-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| drawing.Font | 该排版单元的字体属性对象实例。 |

## Examples

```TypeScript
let font = runs[0].getFont();
```

## getGlyphCount

ArkTS-Dyn:
```TypeScript
getGlyphCount(): number
```

ArkTS-Sta:
```TypeScript
getGlyphCount(): int
```

获取该排版单元中字形的数量。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-getGlyphCount(): int--><!--Device-Run-getGlyphCount(): int-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | 该排版单元中字形数量，整数。 |

## Examples

```TypeScript
let glyphs = runs[0].getGlyphCount();
```

## getGlyphs

ArkTS-Dyn:
```TypeScript
getGlyphs(): Array<number>
```

ArkTS-Sta:
```TypeScript
getGlyphs(): Array<int>
```

获取该排版单元中每个字符的字形序号。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-getGlyphs(): Array<int>--><!--Device-Run-getGlyphs(): Array<int>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt; | 该排版单元中每个字符对应的字形序号。 |

## Examples

```TypeScript
let glyph = runs[0].getGlyphs();
```

## getGlyphs

```TypeScript
getGlyphs(range: Range): Array<int>
```

获取该排版单元指定范围内每个字符的字形序号。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-getGlyphs(range: Range): Array<int>--><!--Device-Run-getGlyphs(range: Range): Array<int>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes | 要获取的字形序号范围，range.start表示范围开始的位置，range.end表示范围的长度，当range.end为0时表示从range.start开始获取到渲染块结束。当 range.end、range.start为负数，或者传入null、undefined时，该方法将返回undefined。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;int&gt; | 该排版单元中每个字符对应的字形序号。 |

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

## getGlyphs

```TypeScript
getGlyphs(range: Range): Array<int> | undefined
```

获取该排版单元指定范围内每个字符的字形序号。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Run-getGlyphs(range: Range): Array<int> | undefined--><!--Device-Run-getGlyphs(range: Range): Array<int> | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes | 要获取的字形序号范围，range.start表示范围开始的位置，range.end表示范围的长度，当range.end为0时表示从range.start开始获取到渲染块结束。当 range.end、range.start为负数，或者传入null、undefined时，该方法将返回undefined。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;int&gt; | 该排版单元中每个字符对应的字形序号。 |

## getImageBounds

```TypeScript
getImageBounds(): common2D.Rect
```

获取该排版单元的图像边界，图像边界与排版字体、排版字号、字符本身都有关，相当于视觉边界，例如字符串为" a b "，'a'字符前面有1个空格，'b'字符后面有1个空格，用户在界面上只能看到"a b"，图像边界即为不包括带行首和末尾空格的边界。

> **说明：**
> 
> 示意图展示了字符串为" a b "的图像边界。
> 
> ![ImageBounds.png](../../../reference/apis-arkgraphics2d/figures/ImageBounds.png)
> 
> 示意图展示了字符串为"j"或"E"的图像边界。
> 
> ![ImageBounds-Character.png](../../../reference/apis-arkgraphics2d/figures/ImageBounds-Character.png)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-getImageBounds(): common2D.Rect--><!--Device-Run-getImageBounds(): common2D.Rect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| common2D.Rect | 该排版单元的图像边界，单位为物理像素px。 |

## Examples

```TypeScript
let bounds = runs[0].getImageBounds();
```

## getOffsets

```TypeScript
getOffsets(): Array<common2D.Point>
```

获取该排版单元中每个字形的索引偏移量。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-getOffsets(): Array<common2D.Point>--><!--Device-Run-getOffsets(): Array<common2D.Point>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;common2D.Point&gt; | 该排版单元中每个字形相对于其索引的偏移量。 |

## Examples

```TypeScript
let offsets = runs[0].getOffsets();
```

## getPositions

```TypeScript
getPositions(): Array<common2D.Point>
```

获取该排版单元中每个字形相对于每行的字形位置。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-getPositions(): Array<common2D.Point>--><!--Device-Run-getPositions(): Array<common2D.Point>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;common2D.Point&gt; | 该排版单元中每个字形相对于每行的字形位置。 |

## Examples

```TypeScript
let positions = runs[0].getPositions();
```

## getPositions

```TypeScript
getPositions(range: Range): Array<common2D.Point>
```

获取该排版单元指定范围内每个字形相对于每行的字形位置数组。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-getPositions(range: Range): Array<common2D.Point>--><!--Device-Run-getPositions(range: Range): Array<common2D.Point>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes | 要获取的字形位置范围，range.start表示范围开始的位置，range.end表示范围的长度，如果长度是0表示从范围range.start开始获取到渲染块结束。当 range.end、range.start为负数，或者传入null、undefined时，该方法将返回undefined。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;common2D.Point&gt; | 该排版单元中每个字形相对于每行的字形位置。 |

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

## getPositions

```TypeScript
getPositions(range: Range): Array<common2D.Point> | undefined
```

获取该排版单元指定范围内每个字形相对于每行的字形位置数组。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Run-getPositions(range: Range): Array<common2D.Point> | undefined--><!--Device-Run-getPositions(range: Range): Array<common2D.Point> | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes | 要获取的字形位置范围，range.start表示范围开始的位置，range.end表示范围的长度，如果长度是0表示从范围range.start开始获取到渲染块结束。当 range.end、range.start为负数，或者传入null、undefined时，该方法将返回undefined。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;common2D.Point&gt; | 该排版单元中每个字形相对于每行的字形位置。 |

## getStringIndices

```TypeScript
getStringIndices(range?: Range): Array<int>
```

获取排版单元指定范围内字形的字符索引，该索引是相对于整个段落的偏移。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-getStringIndices(range?: Range): Array<int>--><!--Device-Run-getStringIndices(range?: Range): Array<int>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | No | 要获取的字符索引范围，range.start表示范围开始的位置，range.end表示范围的长度，如果长度是0表示从范围range.start开始获取到渲染块结束。当 range.end、range.start为负数，或者传入null、undefined时，该方法将返回undefined。不传该参数时，默认获取整个渲染块。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;int&gt; | 返回每个字符的索引。 |

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

## getStringIndices

```TypeScript
getStringIndices(range?: Range): Array<int> | undefined
```

获取排版单元指定范围内字形的字符索引，该索引是相对于整个段落的偏移。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-Run-getStringIndices(range?: Range): Array<int> | undefined--><!--Device-Run-getStringIndices(range?: Range): Array<int> | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | No | 要获取的字符索引范围，range.start表示范围开始的位置，range.end表示范围的长度，如果长度是0表示从范围range.start开始获取到渲染块结束。当 range.end、range.start为负数，或者传入null、undefined时，该方法将返回undefined。不传该参数时，默认获取整个渲染块。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;int&gt; | 返回每个字符的索引。 |

## getStringRange

```TypeScript
getStringRange(): Range
```

获取排版单元生成字形的字符范围。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-getStringRange(): Range--><!--Device-Run-getStringRange(): Range-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | 排版单元生成字形的字符范围，Range类型中的start表示字符范围的开始位置，该位置是相对于整个段落的索引，Range类型中的end表示字符范围的长度。 |

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

获取该排版单元的文本方向。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-getTextDirection(): TextDirection--><!--Device-Run-getTextDirection(): TextDirection-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [TextDirection](arkts-arkgraphics2d-text-textdirection-e.md) | 返回该排版单元的文本方向。 |

## Examples

```TypeScript
let textDirection = runs[0].getTextDirection();
```

## getTextStyle

```TypeScript
getTextStyle(): TextStyle
```

获取该排版单元的文本样式。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Run-getTextStyle(): TextStyle--><!--Device-Run-getTextStyle(): TextStyle-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [TextStyle](../../apis-arkui/arkts-apis/arkts-arkui-styledstring-textstyle-c.md) | 该排版单元的文本样式。 &lt;br&gt;**说明：** &lt;br&gt;1.`textStyle.color`、`textStyle.textShadows.color`、`textStyle.backgroundRect.color`、 `textStyle.decoration.color`属性：返回32位无符号整型颜色数值。示例：返回值`4278190080`，对应纯黑色十六进制颜色值`0xFF000000`，等价于 [common2D.Color]{ |

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

获取该排版单元的排版边界，排版边界与排版字体、排版字号有关，与字符本身无关，例如字符串为" a b "，'a'字符前面有1个空格，'b'字符后面有1个空格，排版边界就包括行首和末尾空格的边界。

> **说明：**
> 
> 示意图展示了字符串为" a b "的排版边界。
> 
> ![TypographicBounds.png](../../../reference/apis-arkgraphics2d/figures/TypographicBounds.png)
> 
> 示意图展示了字符串为"j"或"E"的排版边界。
> 
> !
> [TypographicBounds-Character.png](../../../reference/apis-arkgraphics2d/figures/TypographicBounds-Character.png)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-getTypographicBounds(): TypographicBounds--><!--Device-Run-getTypographicBounds(): TypographicBounds-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [TypographicBounds](arkts-arkgraphics2d-text-typographicbounds-i.md) | 该排版单元的排版边界。 |

## Examples

```TypeScript
let typographicBounds = runs[0].getTypographicBounds();
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

在画布上以(x, y)为左上角位置绘制排版单元。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Run-paint(canvas: drawing.Canvas, x: double, y: double): void--><!--Device-Run-paint(canvas: drawing.Canvas, x: double, y: double): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| canvas | drawing.Canvas | Yes | 绘制的目标 canvas。 |
| x | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 绘制的左上角位置的横坐标，浮点数，单位为物理像素px。 |
| y | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 绘制的左上角位置的纵坐标，浮点数，单位为物理像素px。 |

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

