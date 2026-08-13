# TextLine

描述段落基础文本行结构的载体。 下列API示例中都需先使用[Paragraph](arkts-arkgraphics2d-text-paragraph-c.md#Paragraph)类的[getTextLines()](arkts-arkgraphics2d-text-paragraph-c.md#getTextLines)接口或者 [LineTypeset](arkts-arkgraphics2d-text-linetypeset-c.md#LineTypeset)类的[createLine()](arkts-arkgraphics2d-text-linetypeset-c.md#createLine)接口获取到TextLine对象实例，再通过此实例调用对 应方法。

**起始版本：** 23

**废弃版本：** -1

<!--Device-text-class TextLine--><!--Device-text-class TextLine-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## createTruncatedLine

```TypeScript
createTruncatedLine(width: number, ellipsisMode: EllipsisMode, ellipsis: string): TextLine
```

创建一个截断的文本行对象。

**起始版本：** 18

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-TextLine-createTruncatedLine(width: double, ellipsisMode: EllipsisMode, ellipsis: string): TextLine--><!--Device-TextLine-createTruncatedLine(width: double, ellipsisMode: EllipsisMode, ellipsis: string): TextLine-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| width | number | 是 |
| ellipsisMode | [EllipsisMode](arkts-arkgraphics2d-text-ellipsismode-e.md) | 是 |
| [ellipsis](arkts-arkgraphics2d-text-textstyle-i.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| [TextLine](arkts-arkgraphics2d-text-textline-c.md) |

## 示例

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

创建一个截断的文本行对象。

**起始版本：** 23

**废弃版本：** -1

<!--Device-TextLine-createTruncatedLine(width: double, ellipsisMode: EllipsisMode, ellipsis: string): TextLine | undefined--><!--Device-TextLine-createTruncatedLine(width: double, ellipsisMode: EllipsisMode, ellipsis: string): TextLine | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| width | number | 是 |
| ellipsisMode | [EllipsisMode](arkts-arkgraphics2d-text-ellipsismode-e.md) | 是 |
| [ellipsis](arkts-arkgraphics2d-text-textstyle-i.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| [TextLine](arkts-arkgraphics2d-text-textline-c.md) |

## enumerateCaretOffsets

```TypeScript
enumerateCaretOffsets(callback: CaretOffsetsCallback): void
```

枚举文本行中每个字符的偏移量和索引值。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-TextLine-enumerateCaretOffsets(callback: CaretOffsetsCallback): void--><!--Device-TextLine-enumerateCaretOffsets(callback: CaretOffsetsCallback): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [CaretOffsetsCallback](arkts-arkgraphics2d-text-caretoffsetscallback-t.md) | 是 |

## 示例

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

获取文本行根据对齐因子和对齐宽度计算的对齐所需偏移量。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-TextLine-getAlignmentOffset(alignmentFactor: double, alignmentWidth: double): double--><!--Device-TextLine-getAlignmentOffset(alignmentFactor: double, alignmentWidth: double): double-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| alignmentFactor | number | 是 |
| alignmentWidth | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## 示例

```TypeScript
let alignmentOffset = lines[0].getAlignmentOffset(0.5, 500);
```

## getGlyphCount

```TypeScript
getGlyphCount(): number
```

获取文本行中字形的数量。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-TextLine-getGlyphCount(): int--><!--Device-TextLine-getGlyphCount(): int-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## 示例

```TypeScript
let glyphCount = lines[0].getGlyphCount();
```

## getGlyphRuns

```TypeScript
getGlyphRuns(): Array<Run>
```

获取文本行的排版单元数组。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-TextLine-getGlyphRuns(): Array<Run>--><!--Device-TextLine-getGlyphRuns(): Array<Run>-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| Array&lt;[Run](arkts-arkgraphics2d-text-run-c.md)&gt; |

## 示例

```TypeScript
let runs = lines[0].getGlyphRuns();
```

## getImageBounds

```TypeScript
getImageBounds(): common2D.Rect
```

获取文本行的图像边界。文本行图像边界与排版字体、排版字号、字符本身都有关，相当于视觉边界。例如字符串为" a b "，'a'字符前面有1个空格，'b'字符后面有1个空格，用户在界面上只能看到"a b"，图像边界即为不包括带行首 和末尾空格的边界。例如字符串为"j"或"E"，视觉边界不同，即与字符本身有关，"j"字符串的视觉边界宽度小于"E"字符串的视觉边界宽度，"j"字符串的视觉边界高度大于"E"字符串的视觉边界高度。 > **说明：** > > 示意图展示了字符串为" a b "的图像边界。 > >  > > 示意图展示了字符串为"j"或"E"的图像边界。 > > 

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-TextLine-getImageBounds(): common2D.Rect--><!--Device-TextLine-getImageBounds(): common2D.Rect-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| common2D.Rect |

## 示例

```TypeScript
let imageBounds = lines[0].getImageBounds();
```

## getOffsetForStringIndex

```TypeScript
getOffsetForStringIndex(index: number): number
```

获取文本行中给定字符串索引处的偏移量。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-TextLine-getOffsetForStringIndex(index: int): double--><!--Device-TextLine-getOffsetForStringIndex(index: int): double-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## 示例

```TypeScript
let offset = lines[0].getOffsetForStringIndex(3);
```

## getStringIndexForPosition

```TypeScript
getStringIndexForPosition(point: common2D.Point): number
```

获取给定位置在原始字符串中的字符索引。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-TextLine-getStringIndexForPosition(point: common2D.Point): int--><!--Device-TextLine-getStringIndexForPosition(point: common2D.Point): int-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| point | common2D.Point | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## 示例

```TypeScript
let point : common2D.Point = { x: 15.0, y: 2.0 };
let index = lines[0].getStringIndexForPosition(point);
```

## getTextRange

```TypeScript
getTextRange(): Range
```

获取该行文本在整个段落文本中的索引区间。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-TextLine-getTextRange(): Range--><!--Device-TextLine-getTextRange(): Range-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) |

## 示例

```TypeScript
let textRange = lines[0].getTextRange();
```

## getTrailingSpaceWidth

```TypeScript
getTrailingSpaceWidth(): number
```

获取文本行尾部空白字符的宽度。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-TextLine-getTrailingSpaceWidth(): double--><!--Device-TextLine-getTrailingSpaceWidth(): double-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| number |

## 示例

```TypeScript
let trailingSpaceWidth = lines[0].getTrailingSpaceWidth();
```

## getTypographicBounds

```TypeScript
getTypographicBounds(): TypographicBounds
```

获取文本行的排版边界。文本行排版边界与排版字体、排版字号有关，与字符本身无关。例如字符串为" a b "，'a'字符前面有1个空格，'b'字符后面有1个空格，排版边界就包括行首和末尾空格的边界。例如字符串为"j"或"E"，排版 边界相同，即与字符本身无关。 > **说明：** > > 示意图展示了字符串为" a b "的排版边界。 > >  > > 示意图展示了字符串为"j"或"E"的排版边界。 > > ! > [TypographicBounds-Character.png](../../../reference/apis-arkgraphics2d/figures/TypographicBounds-Character.png)

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-TextLine-getTypographicBounds(): TypographicBounds--><!--Device-TextLine-getTypographicBounds(): TypographicBounds-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [TypographicBounds](arkts-arkgraphics2d-text-typographicbounds-i.md) |

## 示例

```TypeScript
let bounds = lines[0].getTypographicBounds();
console.info('textLine ascent:' + bounds.ascent + ', descent:' + bounds.descent + ', leading:' + bounds.leading + ', width:' + bounds.width);
```

## paint

```TypeScript
paint(canvas: drawing.Canvas, x: number, y: number): void
```

在画布上以坐标点(x, y)为左上角位置绘制该文本行。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-TextLine-paint(canvas: drawing.Canvas, x: double, y: double): void--><!--Device-TextLine-paint(canvas: drawing.Canvas, x: double, y: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [canvas](../../apis-arkui/arkts-apis/arkts-arkui-canvasrenderingcontext2d-c.md) | drawing.Canvas | 是 |
| x | number | 是 |
| y | number | 是 |

## 示例

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
